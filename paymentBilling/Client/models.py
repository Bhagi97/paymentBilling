from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    gst_no = models.IntegerField()
    no_of_sales_users = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    # class Meta:
        # permissions = (
        #     ("view_blog", "Can view the blog"),
        #     ("can_publish_blog", "Can publish a blog"),
        # )


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='client_profile', on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username



