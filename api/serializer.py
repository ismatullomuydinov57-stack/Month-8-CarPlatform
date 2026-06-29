from rest_framework import serializers

from .models import CarBrand, Car, Comment

class CarSerializerForBrand(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class BrandSerializerForCar(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarBrandSerializer(serializers.ModelSerializer):
    # cars=serializers.StringRelatedField(many=True, read_only=True)
    # cars=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # cars=serializers.SlugRelatedField(many=True, read_only=True, slug_field='model_name'),
    # cars=serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='car-detail')

    cars=CarSerializerForBrand(many=True, read_only=True)


    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'country', 'cars']

class CarSerializer(serializers.ModelSerializer):
    brand_name=serializers.CharField(source="brand")
    class Meta:
        model = Car
        exclude=['color']


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

