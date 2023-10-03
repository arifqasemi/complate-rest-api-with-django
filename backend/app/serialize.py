from rest_framework import serializers
from .models import Movie, StreamPlateform,Review

class ReviewSerializer(serializers.ModelSerializer):
    user_review = serializers.StringRelatedField()
   

    class Meta:
        model = Review
        fields = '__all__'




class MovieSerializer(serializers.ModelSerializer):
    len_title = serializers.SerializerMethodField(read_only=True)
    reviews =  serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='app:review-detail',
    
    )
    movie_url = serializers.HyperlinkedIdentityField(read_only=True,
        view_name='app:movie-detail'  
    )

    class Meta:
        model = Movie
        fields = ('id','reviews','plateform','len_title','title', 'description', 'image','movie_url','avrg_rating','total_rating')

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("sorry the title and description are the same")
        return data
    
    def validate_title(self, attrs):
        if len(attrs) < 2:
            raise serializers.ValidationError("name is too short")
        else:
            return attrs
    def get_len_title(self, data):
        return len(data.title)

class StreamPlateformSerializer(serializers.ModelSerializer):
    # movie = MovieSerializer(many=True, read_only=True)
    movie = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='app:movie-detail'
    )
    stream_url = serializers.HyperlinkedIdentityField(read_only=True,
        view_name='app:stream-detail'  
    )

    class Meta:
        model = StreamPlateform
        fields = ['id','name','about','website','movie','stream_url']


       # different method for serializing

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     description = serializers.CharField()
#     image = serializers.CharField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.description = validated_data.get('description',instance.description)
#         instance.image = validated_data.get('image',instance.image)
#         instance.save()
#         return instance
    
    # def validate(self, data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError("sorry the title and description are the same")
    #     return data
    
    # def validate_title(self, attrs):
    #     if len(attrs) < 2:
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return attrs