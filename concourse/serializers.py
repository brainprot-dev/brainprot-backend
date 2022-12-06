from rest_framework import serializers 
from concourse.models import Post, TeamMember
 
# Create your Serializers here
# Post Serializer for Post Model
class PostSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'author',
                  'updated_on',
                  'created_on',
                  'status',
                  'content',
                  'slug',
                 )

# TeamMember Serializer for TeamMember Model
class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        fields = ('id',
                  'name',
                  'designation',
                  'affiliation',
                  'email',
                 )