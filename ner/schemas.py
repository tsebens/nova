from ninja import ModelSchema

from ner.models import Text, Mention, Entity


class TextSchema(ModelSchema):
    class Meta:
        model = Text
        fields = "__all__"


class ModelSchema(ModelSchema):
    class Meta:
        model = Mention
        fields = "__all__"


class EntitySchema(ModelSchema):
    class Meta:
        model = Entity
        fields = "__all__"

