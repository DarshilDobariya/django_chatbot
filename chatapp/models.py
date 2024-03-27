from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
    # ForeignKey relationship with the User model, indicating which user sent the message
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # TextField to store the user's msg and AI's rsponse
    message = models.TextField()
    response = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    # Customizes the string representation of the object
    def __str__(self):
        # Returns a string containing the username of the user who sent the message and the message itself
        return f'{self.user.username}: {self.message}'