from typing import Any

from httpx import Response
from pydantic import ValidationError


class SWException(Exception):
    pass


class SWAPIException(SWException):
    pass


class SWModelException(SWException):
    pass


class SWFilterException(SWModelException):
    pass


class SWAPIConfigException(SWAPIException):
    pass


class SWAPIRetryException(SWAPIException):
    pass


class SWAPIMethodNotAvailable(SWAPIConfigException):
    def __init__(self, msg: str | None = None, *args: list[Any], **kwargs: dict[Any, Any]) -> None:
        if not msg:
            msg = "Method unsupported by this Endpoint"
        super().__init__(msg, *args, **kwargs)


class SWAPIError(SWAPIException):
    def __init__(self, **kwargs: Any) -> None:
        self.id = kwargs.get("id", "")
        self.links = kwargs.get("links", {})
        self.status = kwargs.get("status", "")
        self.code = kwargs.get("code", "")
        self.title = kwargs.get("title", "")
        self.detail = kwargs.get("detail", "")
        self.description = kwargs.get("description", "")
        self.source = kwargs.get("source", {})
        self.meta = kwargs.get("meta", {})
        self.headers = kwargs.get("headers", {})
        self.request = kwargs.get("request", None)
        self.response = kwargs.get("response", None)

    def __str__(self) -> str:
        return f"Status: {self.status} {self.title} - {self.detail} - {self.source}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self}>"

    @classmethod
    def get_exception_class(cls, status_code: int) -> type["SWAPIError"]:
        match status_code:
            case 400:
                return SWAPIBadRequest
            case 401:
                return SWAPIUnauthorized
            case 403:
                return SWAPIForbidden
            case 404:
                return SWAPINotFound
            case 405:
                return SWAPIMethodNotAllowed
            case 412:
                return SWAPIPreconditionFailed
            case 429:
                return SWAPITooManyRequests
            case 500:
                return SWAPIInternalServerError
            case 501:
                return SWAPINotImplemented
            case 502:
                return SWAPIBadGateway
            case 503:
                return SWAPIServiceUnavailable
            case 504:
                return SWAPIGatewayTimeout
            case 505:
                return SWAPIHTTPVersionNotSupported
            case _:
                return SWAPIError

    @classmethod
    def from_errors(cls, errors: list[dict[str, Any]], response: Response) -> "SWAPIErrorList":
        errlist = []

        for error in errors:
            error.update({"response": response, "request": response.request})
            exception_class = cls.get_exception_class(int(error["status"]))
            errlist.append(exception_class(**error))

        return SWAPIErrorList(errlist)

    @classmethod
    def from_response(cls, response: Response) -> "SWAPIError":
        exception_class = cls.get_exception_class(response.status_code)

        try:
            response.headers["requested-url"] = str(response.request.url)
        except RuntimeError:
            # If the request URL is not available, we can ignore it.
            pass

        return exception_class(
            status=response.status_code,
            title=response.reason_phrase,
            detail=response.text,
            headers=response.headers,
            request=response._request,
            response=response,
        )


class SWAPIErrorList(SWAPIException):
    def __init__(self, errors: list[SWAPIError]) -> None:
        self.errors = errors

    def __str__(self) -> str:
        return f"Errors: {self.errors}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self}>"


class SWAPIDataValidationError(SWAPIException):
    def __init__(self, errors: list[ValidationError] | None = None) -> None:
        self.errors = errors if isinstance(errors, (list, tuple)) else []

    def __str__(self) -> str:
        return f"Invalid Shopware data (pydantic). Errors:\n{'\n'.join([str(e) for e in self.errors])}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self}>"


class SWNoClientProvided(SWModelException):
    pass


class SWAPIBadRequest(SWAPIError):
    pass


class SWAPIUnauthorized(SWAPIError):
    pass


class SWAPIForbidden(SWAPIError):
    pass


class SWAPINotFound(SWAPIError):
    pass


class SWAPIMethodNotAllowed(SWAPIError):
    pass


class SWAPIPreconditionFailed(SWAPIError):
    pass


class SWAPITooManyRequests(SWAPIError):
    pass


class SWAPIInternalServerError(SWAPIError):
    pass


class SWAPINotImplemented(SWAPIError):
    pass


class SWAPIBadGateway(SWAPIError):
    pass


class SWAPIServiceUnavailable(SWAPIError):
    pass


class SWAPIGatewayTimeout(SWAPIError):
    pass


class SWAPIHTTPVersionNotSupported(SWAPIError):
    pass
