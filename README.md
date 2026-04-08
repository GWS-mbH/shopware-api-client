# Shopware API Client

A Django-ORM like, Python 3.12, async Shopware 6 admin and store-front API client.

## Installation

```sh
pip install shopware-api-client

# If you want to use the redis cache
pip install shopware-api-client[redis]
```

## Usage

There are two kinds of clients provided by this library. The `client.AdminClient` for the Admin API and the
`client.StoreClient` for the Store API.

### client.AdminClient

To use the AdminClient you need to create a `config.AdminConfig`. The `AdminConfig` class supports two login methods
(grant-types):
- **client_credentials** (Default) Let's you log in with a `client_id` and `client_secret`
- **password** Let's you log in using a `username` and `password`

You also need to provide the Base-URL of your shop.

Example:

```python
from shopware_api_client.config import AdminConfig

CLIENT_ID = "MyClientID"
CLIENT_SECRET = "SuperSecretToken"
SHOP_URL = "https://pets24.shop"

config = AdminConfig(url=SHOP_URL, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, grant_type="client_credentials")

# or for "password"

ADMIN_USER = "admin"
ADMIN_PASSWORD = "!MeowMoewMoew~"

config = AdminConfig(url=SHOP_URL, username=ADMIN_USER, password=ADMIN_PASSWORD, grant_type="password")
```

Now you can create the Client. There are two output formats for the client, that can be selected by the `raw` parameter:
- **raw=True** Outputs the result as a plain dict or list of dicts
- **raw=False** (Default) Outputs the result as Pydantic-Models

```python
from shopware_api_client.client import AdminClient

# Model-Mode
client = AdminClient(config=config)

# raw-Mode
client = AdminClient(config=config, raw=True)
```

Client-Connections should be closed after usage: `await client.close()`. The client can also be used in an `async with`
block to be closed automatically.

```python
from shopware_api_client.client import AdminClient

async with AdminClient(config=config) as client:
    # do important stuff
    pass
```

All registered Endpoints are directly available from the client instance. For example if you want to query the Customer
Endpoint:

```python
customer = await client.customer.first()
```

All available Endpoint functions can be found in the [AdminEndpoint](#list-of-available-functions) section.

There are two additional ways how the client can be utilized by using it with the Endpoint-Class directly or the
associated Pydantic Model:

```python
from shopware_api_client.endpoints.admin.core.customer import Customer, CustomerEndpoint

# Endpoint
customer_endpoint = CustomerEndpoint(client=client)
customer = await customer_endpoint.first()

# Pydantic Model
customer = await Customer.using(client=client).first()
```

#### Related Objects

If you use the Pydantic-Model approach (`raw=False`) you can also use the returned object to access its related objects:

```python
from shopware_api_client.endpoints.admin import Customer

customer = await Customer.using(client=client).first()
customer_group = await customer.group  # Returns a CustomerGroup object
all_the_customers = await customer_group.customers  # Returns a list of Customer objects
```

**!! Be careful to not close the client before doing related objects calls, since they use the same Client instance !!**
```python
from shopware_api_client.client import AdminClient
from shopware_api_client.endpoints.admin import Customer

async with AdminClient(config=config) as client:
    customer = await Customer.using(client=client).first()

customer_group = await customer.group  # This will fail, because the client connection is already closed!
```

#### CustomEntities

Shopware allows to create custom entities. You can use the `load_custom_entities` function to load them into the client.

```python
from shopware_api_client.client import AdminClient

config = ...
client = AdminClient(config=config)
await client.load_custom_entities(client)

# Endpoint for the custom entity ce_blog
await client.ce_blog.all()

# Pydantic Model for the custom entity ce_blog
CeBlog = client.ce_blog.model_class
```
Since custom entities are completely dynamic no autocompletion in IDE is available. However there are some pydantic validations added for the field-types of the custom entity. Relations are currently not supported, but everything else should work as expected.

### client.StoreClient

To use the StoreClient you need to create a `config.StoreConfig`. The `StoreConfig` needs a store api access key.
You also need to provide the Base-URL of your shop.

Some Endpoints (that are somehow related to a user) require a context-token. This parameter is optional.

Example:

```python
from shopware_api_client.config import StoreConfig

ACCESS_KEY = "SJMSAKSOMEKEY"
CONTEXT_TOKEN = "ASKSKJNNMMS"
SHOP_URL = "https://pets24.shop"

config = StoreConfig(url=SHOP_URL, access_key=STORE_API_ACCESS_KEY, context_token=CONTEXT_TOKEN)
```

This config can be used with the `StoreClient`, ~~which works exactly like the `AdminClient`~~.
The `StoreClient` has far less endpoints and does mostly not support full updated of models, but uses
helper-functions.

### Redis Caching for Rate Limits

Both the AdminClient and the StoreClient use a built-in rate limiter. Shopware's rate limits differ based on the endpoints, both for the [SaaS-](https://docs.shopware.com/en/en/shopware-6-en/saas/rate-limits) and the [on-premise-solution](https://developer.shopware.com/docs/guides/hosting/infrastructure/rate-limiter.html).

To be able to respect the rate limit when sending requests from multiple clients, it is possible to use redis as a cache-backend for route-based rate-limit data. If redis is not used, each Client independently keeps track of the rate limit. Please note that the non-Redis cache is not thread-safe.

To use redis, simply hand over a redis-client to the client config:
```py
import redis
from shopware_api_client.config import AdminConfig, StoreConfig
from shopware_api_client.client import AdminClient, StoreClient

redis_client = redis.Redis()

admin_config = AdminConfig(
    url='',
    client_id='...',
    client_secre='...',
    redis_client=redis_client,
)
admin_client = AdminClient(config=config)  # <- This client uses the redis client now

store_config = StoreConfig(
    url='',
    access_key='',
    context_token=''
    redis_client=redis_client,
)
store_client = StoreClient(config=config)  # <- Works for store client as well (Only do this in safe environments)
```

__Note:__ Shopware currently enforces rate limits on a per–public‑IP basis. As a result, you should only share Redis‑backed rate‑limit caching among clients that originate from the same public IP address.

## AdminEndpoint
The `base.AdminEndpoint` class should be used for creating new Admin-Endpoints. It provides some usefull functions to call
the Shopware-API.

The base structure of an Endpoint is pretty simple:

```python
from shopware_api_client.base import EndpointMixin, AdminEndpoint


class CustomerGroup(EndpointMixin["CustomerGroupEndpoint"]):
    # Model definition
    pass


class CustomerGroupEndpoint(AdminEndpoint[CustomerGroup]):
    name = "customer_group"  # name of the Shopware-Endpoint (snaky)
    path = "/customer-group"  # path of the Shopware-Endpoint
    model_class = CustomerGroup  # Pydantic-Model of this Endpoint
```

### List of available Functions

- `all()` return all objects (GET /customer-group or POST /search/customer-group if filter or sort is set)
- `get(pk: str = id)` returns the object with the passed id (GET /customer-group/id)
- `update(pk: str = id, obj: ModelClass | dict[str: Any]` updates an object (PATCH /customer-group/id)
- `create(obj: ModelClass | dict[str: Any]` creates a new object (POST /customer-group)
- `delete(pk: str = id)` deletes an object (DELETE /customer-group/id)
- `filter(name="Cats")` adds a filter to the query. Needs to be called with .all(), .iter() or .first())) More Info: [Filter](#filter)
- `limit(count: int | None)` sets the limit parameter, to limit the amount of results. Needs to be called with .all() or .first()
- `first()` sets the limit to 1 and returns the result (calling .all())
- `order_by(fields: str | tuple[str]` sets the sort parameter. Needs to be called with .all(), .iter() or .first(). Syntax: "name" for ASC, "-name" for DESC
- `select_related(**kwargs: dict[str, Any])` sets the _associations parameter to define which related models to load in the request. Needs to be called with .all(), .iter() or .first().
- `only(**kwargs: list[str])` sets the _includes parameter to define which fields to request. Needs to be called with .all(), .iter() or .first().
- `iter(batch_size: int = 100)` sets the limit-parameter to batch_size and makes use of the pagination of the api. Should be used when requesting a big set of data (GET /customer-group or POST /search/customer-group if filter or sort is set)
- `bulk_upsert(objs: list[ModelClass] | list[dict[str, Any]` creates/updates multiple objects. Does always return dict of plain response. (POST /_action/sync)
- `bulk_delete(objs: list[ModelClass] | list[dict[str, Any]` deletes multiple objects. Does always return dict or plain response. (POST /_action/sync)

Not all functions are available for the StoreClient-Endpoints. But some of them have some additional functions.
StoreClient-Endpoints using the `base.StoreSearchEndpoint` can use most of the filter functions, but not create/update/delete.

### Filter

The `filter()` functions allows you to filter the result of an query. The parameters are basically the field names.
You can add an appendix to change the filter type. Without it looks for direct matches (equals). The following
appendices are available:

- `__in` expects a list of values, matches if the value is provided in this list (equalsAny)
- `__contains` matches values that contain this value (contains)
- `__gt` greater than (range)
- `__gte` greater than equal (range)
- `__lt` lower than (range)
- `__lte` lower than equal (range)
- `__range` expects a touple of two items, matches everything inbetween. inclusive. (range)
- `__startswith` matches if the value starts with this (prefix)
- `__endswith` matches if the value ends with this (suffix)

For some fields (that are returned as dict, like custom_fields) it's also possible to filter over the values of it's
keys. To do so you can append the key seperated by "__" For example if we have a custom field called "preferred_protein"
we can filter on it like this:
```python
customer = await Customer.using(client=client).filter(custom_field__preferred_protein="fish")

# or with filter-type-appendix
customer = await Customer.using(client=client).filter(custom_field__preferred_protein__in=["fish", "chicken"])
```

## ApiModelBase

The `base.ApiModelBase` class is basicly a `pydantic.BaseModel` which should be used to create Endpoint-Models.

The base structure of an Endpoint-Model looks like this. Field names are converted to snake_case. Aliases are autogenerated:

```python
from pydantic import Field
from typing import Any
from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class CustomerGroup(ApiModelBase, CustomFieldsMixin):
    _identifier = "customer_group"  # name of the Shopware-Endpoint (snaky)

    name: str  # Field with type
    display_gross: bool | None = None
    # other fields...
```

This Base-Models live in `shopware_api_client.models`

The `id`, `version_id`, `created_at`, `updated_at` and `translated` attributes are provided in the ApiModelBase and
must not be added. This are default fields of Shopwares `Entity` class, even they are not always used.

If an entity supports the `EntityCustomFieldsTrait` you can add the `CustomFieldsMixin` to add the custom_fields field.

### List of available Function

- `save()` executes `Endpoint.update()` if an id is set otherwise `Endpoint.create()`
- `delete()` executes `Endpoint.delete()`


### AdminModel + Relations

To make relations to other models work, we have to define them in the Model. There are two classes to make this work:
`endpoints.relations.ForeignRelation` and `endpoints.relations.ManyRelation`.

- `ForeignRelation[class]` is used when we get the id of the related object in the api response.
  - `class`: Class of the related model

- `ManyRelation[class]` is used for the reverse relation. We don't get ids in the api response, but it can be used through
relation links.
  - `class`: Class of the related model

Example (Customer):

```python
from pydantic import Field

from shopware_api_client.base import AdminModel
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.customer import Customer as CustomerBase

"""
// shopware_api_client.models.customer.Customer:
class Customer(ApiModelBase):
    # we have an id so we can create a ForeignRelation to it
    default_billing_address_id: IdField
"""

# final model containing relations for admin api. Must be AdminModel
class Customer(CustomerBase, AdminModel["CustomerEndpoint"]):
    default_billing_address: ForeignRelation["CustomerAddress"]

    # We don't have a field for all addresses of a customer, but there is a relation for it!
    addresses: ManyRelation["CustomerAddress"]

# model relation classes have to be imported at the end. pydantic needs the full import (not just TYPE_CHECKING)
# and this saves us from circular imports
from shopware_api_client.endpoints.admin import CustomerAddress  # noqa: E402

```

## Development

### Testing

You can use `poetry build` and `poetry run pip install -e .` to install the current src.

Then run `poetry run pytest .` to execute the tests.

### Model Creation

Shopware provides API-definitions for their whole API. You can download it from `<shopurl>/api/_info/openapi3.json`
Then you can use tools like `datamodel-code-generator`

```
datamodel-codegen --input openapi3.json --output model_openapi3.py --snake-case-field --use-double-quotes --output-model-type=pydantic_v2.BaseModel --use-standard-collections --use-union-operator
```

The file may look confusing at first, but you can search for Endpoint-Name + JsonApi (Example: class CustomerJsonApi)
to get all returned fields + relationships class as an overview over the available Relations. However, the Models will
need some modifications. But it's a good start.

Not all fields returned by the API are writeable and the API will throw an error when you try to set it. So this fields
must have an `exclude=True` in their definition. To find out which fields need to be excluded check the Shopware
Endpoint documentation at https://shopware.stoplight.io/. Go to the Endpoint your Model belongs to and check the
available POST fields.

The newly created Model and its Endpoint must than be imported to `admin/__init__.py` or `store/__init__.py`. The Model must be added to `__all__`
The Endpoint must be added to the Endpoints class. The `__all__` statement is necessary so they
don't get cleaned away as unused imports by code-formaters/cleaners.

We need to import all related models at the **end** of the file. If we don't add them, Pydantic fails to build the model. If we add them before
our model definition, we run into circular imports.

Every model has a base model that lives in `models/<model_file>.py`. This model only contains direct fields (no relations), which are used by
both endpoints (store & admin). This base models are extended in the endpoints to contain relations (`endpoints/admin/core/<model_file>.py` & `endpoints/store/core/<model_file>.py`).

### Structure

```
> endpoints  -- All endpoints live here
  > admin  -- AdminAPI endpoints
    > core  -- AdminAPI > Core
      customer_address.py  -- Every Endpoint has its own file. Model and Endpoint are defined here
    > commercial  -- AdminAPI > Commercial
    > digital_sales_rooms  -- AdminAPI > Digital Sales Rooms
  > store  -- StoreAPI
    > core  -- StoreAPI > Core
    > commercial  -- StoreAPI > Commercial
    > digital_sales_rooms  -- StoreAPI > Digital Sales Rooms
> models  -- base models to be extended in admin/store endpoints (shopware => Entity)
> structs  -- data structures that do not have a model (shopware => Struct)
base.py  -- All the Base Classes (nearly)
fieldsets.py  -- FieldSetBase has its own file to prevent pydantic problems
client.py  -- Clients & Registry
config.py  -- Configs
exceptions.py  -- Exceptions
logging.py  -- Logging
tests.py  -- tests
```
