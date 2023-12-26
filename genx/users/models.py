from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class CusOrders(models.Model):
    size = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )

    order_id = models.AutoField(primary_key=True)
    prod_code = models.IntegerField()
    quantity = models.IntegerField(default=1)
    user = models.CharField(max_length=200)
    size = models.CharField(max_length=2, choices=size, default='M')

    def __str__(self):
        return str(
            (
                str(self.order_id),
                str(self.prod_code),
                str(self.quantity),
                str(self.user),
                str(self.size),
            )
        )
        

class CusRatingFeedback(models.Model):
    prod_code = models.IntegerField(default=1)
    ratings = models.FloatField()
    feedback = models.CharField(max_length=200)
    username  = models.CharField(max_length=200, default='username')

    def __str__(self):
        return str(
            (
                str(self.prod_code),
                str(self.ratings),
                str(self.feedback),
                str(self.username)
            )
        )