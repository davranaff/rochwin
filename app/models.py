from django.db import models
from django.core.validators import MinValueValidator
from users.models import Employee, Client
from app.querysets.orderqueryset import OrderQueryset


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Order(BaseModel):
    client = models.ForeignKey(Client, models.CASCADE, related_name='order', related_query_name='order')
    product = models.ManyToManyField('Product', related_name='order', related_query_name='order')
    employee = models.ForeignKey(Employee, models.CASCADE, related_name='order', related_query_name='order')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = OrderQueryset.as_manager()

    def __str__(self) -> str:
        return 'order id #{}'.format(self.id)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'