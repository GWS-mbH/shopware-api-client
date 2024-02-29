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


class SWAPIMethodNotAvailable(SWAPIConfigException):
    pass


class SWAPIError(SWAPIException):
    pass


class SWNoClientProvided(SWModelException):
    pass
