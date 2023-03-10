from rest_framework import serializers
from .models import myuser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=myuser
        fields="__all__"

class UserdetailSerializer(serializers.ModelSerializer):
    class  Meta:
       model=myuser
       fields=["id","username","roles"]