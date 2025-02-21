from rest_framework import serializers
from .models import WatchList,StreamPlatform

# ---------------- Model Serializable ------------------

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'




# ---------------- Class Serializable ------------------
# class StreamPlatformSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(max_length=50) 
#     about = serializers.CharField(max_length=150)
#     website = serializers.URLField(max_length=50)

#     def create(self, validated_data):
#         return StreamPlatform.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.about = validated_data.get('about', instance.about)
#         instance.website = validated_data.get('website', instance.website)
#         instance.save()
#         return instance



# ---------------- Model Serializable ------------------

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'


# ---------------- Class Serializable ------------------
# class WatchlistSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(max_length=50)
#     storyline = serializers.CharField(max_length=150)
#     # platform = serializers.ForeignKey(StreamPlatform,on_delete=models.CASCADE)
#     active = serializers.BooleanField(default=True)
#     created= serializers.DateTimeField()

#     def create(self, validated_data):
#         return WatchList.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.storyline = validated_data.get('storyline', instance.storyline)
#         instance.active = validated_data.get('active', instance.active)
#         instance.created = validated_data.get('created', instance.created)
#         instance.save()
#         return instance
