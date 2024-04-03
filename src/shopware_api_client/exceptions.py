from typing import Any

from httpx import Response


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

    def __str__(self) -> str:
        return f"Status: {self.status} {self.title} - {self.detail}"

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
    def from_errors(cls, errors: list[dict[str, Any]]) -> "SWAPIErrorList":
        errlist = []

        for error in errors:
            exception_class = cls.get_exception_class(int(error["status"]))
            errlist.append(exception_class(**error))

        return SWAPIErrorList(errlist)

    @classmethod
    def from_response(cls, response: Response) -> "SWAPIError":
        exception_class = cls.get_exception_class(response.status_code)
        return exception_class(status=response.status_code, title=response.reason_phrase, detail=response.text)


class SWAPIErrorList(SWAPIException):
    def __init__(self, errors: list[SWAPIError]) -> None:
        self.errors = errors


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
