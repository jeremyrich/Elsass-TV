from django.db import models
from django.contrib.auth.models import User


class UserCustom(models.Model):  
    """As the User model is not changeable, this model, connected to User by a one to one relationship
    allows to create custom user objects, that can be connected to themselves through the
    Friendship table
    """
    friends = models.ManyToManyField("self", 
                through="Friendship",
                through_fields=("source_user","target_user"),
                symmetrical=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Friendship(models.Model): 
    """Connects custom users through a many to many relationship. The status of the friendship
    describes if this is a not-yet-accepted request (status = 0), an accepted request (status = 1),
    or a refused request/deleted friend (status = 2)
    """
    source_user = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    target_user = models.ForeignKey(UserCustom, on_delete=models.CASCADE, related_name='target_user')
    status = models.IntegerField(null=True)
        

