from rest_framework import serializers

from app.models import *

class EngagementPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=EngagementPost
        fields='__all__'
class EngagementPostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=EngagementPostContent
        fields='__all__'
class EngagementPostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=EngagementPostProduct
        fields='__all__'
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields='__all__'


class EngagementPostCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=EngagementPostCollection
        fields='__all__'


