from typing import Callable, TypeVar

from google.protobuf.json_format import MessageToDict
from pydantic import BaseModel

BaseModelT = TypeVar('BaseModelT', bound=BaseModel)


class CTSModel(BaseModel):
    @staticmethod
    def to_cts(constructor: Callable, pydantic_obj: BaseModelT):
        obj = constructor()
        for k, v in pydantic_obj.dict().items():
            setattr(obj, k, v)
        return obj

    def update_from_pydantic(self, o: BaseModelT):
        for field in o.__fields__:
            if (new_value := getattr(o, field)) != getattr(self, field):
                setattr(self, field, new_value)

    @staticmethod
    def proto_to_dict(proto_message, use_integers_for_enums=True):
        return MessageToDict(
                proto_message._meta.parent.pb(proto_message),
                including_default_value_fields=False,
                preserving_proto_field_name=True,
                use_integers_for_enums=use_integers_for_enums,
        )

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
