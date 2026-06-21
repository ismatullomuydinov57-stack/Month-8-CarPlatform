from rest_framework import serializers

from .models import CarBrand, Car, Comment


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    my_brand=serializers.ChoiceField(choices=CarBrand.objects.all(), write_only=True)
    class Meta:
        model = Car
        fields = '__all__'
        depth=1

    def create(self, validated_data):
        brand=validated_data.pop("my_brand")
        car=Car.objects.create(**validated_data, brand=brand)
        return car

    def update(self, instance, validated_data):
        instance.brand=validated_data.pop("my_brand") if validated_data.get("my_brand") else instance.brand
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text']

