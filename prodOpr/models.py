from django.db import models
from django.contrib.auth import get_user_model
from prodOpr.validations import validate_img

# Create your models here.


class ProductModel(models.Model):
    User=get_user_model()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pname=models.CharField(max_length=80)
    img=models.ImageField(upload_to='product/',validators=(validate_img,))
    price=models.FloatField(default=0.0,null=True)
    quantity=models.IntegerField(default=0,null=True)

    def __str__(self):
        return  self.pname

