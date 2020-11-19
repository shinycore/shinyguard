from datetime import datetime
from typing import Any, Optional

from marshmallow import EXCLUDE, Schema, ValidationError, fields, post_load


class TimestampDateTime(fields.Field):
    def _deserialize(self, value: Any, attr: Optional[str], data: Optional[dict], **kwargs) -> datetime:
        try:
            value = int(value)
        except ValueError as e:  # pragma: no cover
            raise ValidationError("Timestamp must be a number") from e
        else:
            return datetime.utcfromtimestamp(value)


class OTAUpdateSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    datetime = TimestampDateTime()
    version = fields.Str()


class OTAUpdateListSchema(Schema):
    response = fields.Nested(OTAUpdateSchema, many=True)

    @post_load
    def flatten_response(self, data: dict, **kwargs: Any) -> list[dict]:
        return data.get("response")


class GerritChangeSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str()
    submitted = fields.DateTime()
