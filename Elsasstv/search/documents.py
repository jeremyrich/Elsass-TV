from django_elasticsearch_dsl import DocType, Index
from django.contrib.auth.models import User

from movies.models import Movie


# initiation of movie elasticsearch indexation 
movie = Index('movie')
movie.settings(
    number_of_shards=1,
    number_of_replicas=0
)

user = Index('user')
user.settings(
    number_of_shards=1,
    number_of_replicas=0
)

# selecting fields to index
@movie.doc_type
class MovieDocument(DocType):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'original_title',
            'overview',
            'poster_path',
            'vote_average',           
        ]

# selecting fields to index
@user.doc_type
class UserDocument(DocType):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]
