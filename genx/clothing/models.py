from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    CATEGORY_CHOICES = (
        ('m', 'Mens'),
        ('f', 'Womens'),
        ('k', 'Kids'),
    )

    prod_code = models.IntegerField(default=100)
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=300)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://media.istockphoto.com/id/1273109788/vector/coming-soon-isolated-vector-icon-paper-style-promotion-sign-start-a-new-business-design.jpg?s=612x612&w=0&k=20&c=0APH6QCc371SuCEYLspgp6oh-tE5-rvbK0dzLMRmJGA=")
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default="('m', 'Mens')")

    def __str__(self):
        return self.item_name

    
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
    quantity = models.PositiveIntegerField(default=1)
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

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} x {self.item.item_name} (Size: {self.size}) in {self.user.username}'s cart"