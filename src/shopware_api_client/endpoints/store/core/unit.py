from ....endpoints.admin.core.unit import UnitBase


class Unit(UnitBase):
    short_code: str | None
    name: str | None