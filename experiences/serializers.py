from rest_framework.serializers import ModelSerializer
from .models import Perk, Experience
from categories.serializers import CategorySerializer


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class PerkDetailSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = (
            "name",
            "details",
            "explanation",
        )


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class ExperienceDetailSerializer(ModelSerializer):
    perks = PerkSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = (
            "country",
            "city",
            "name",
            "host",
            "price",
            "address",
            "start",
            "end",
            "description",
            "perks",
            "category",
        )
