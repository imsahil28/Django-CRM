# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User



# class Profile(models.Model):
#     user = models.OneToOneField(User , on_delete=models.CASCADE)
#     auth_token = models.CharField(max_length=100 )
#     is_verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)  # Set default value to current time

def __str__(self):
         return self.user.username