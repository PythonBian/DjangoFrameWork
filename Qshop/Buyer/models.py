from django.db import models
from Seller.models import LoginUser

class PayOrder(models.Model):
    """
    订单表
    订单状态
    0 未支付
    1 已支付
    2 待收货
    3/4 完成/拒收
    """
    order_number = models.CharField(max_length=32)
    order_data = models.DateTimeField(auto_now=True)
    order_total = models.FloatField(blank=True,null=True)
    order_user = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)

class OrderInfo(models.Model):
    """
    订单详情表
    订单状态
    0 未支付
    1 已支付
    2 待收货
    3/4 完成/拒收
    """
    order_id = models.ForeignKey(to=PayOrder,on_delete=models.CASCADE)
    goods_id = models.IntegerField()
    goods_picture = models.CharField(max_length=32)
    goods_name = models.CharField(max_length=32)
    goods_count = models.IntegerField()
    goods_price = models.FloatField()
    goods_total_price = models.FloatField()
    order_status = models.IntegerField(default=0)
    store_id = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)

class Cart(models.Model):
    """
    商品名称
    商品数量（购买数量）
    商品价格
    商品图片
    商品总价（单个商品）
    商品id
    用户
    """
    goods_name = models.CharField(max_length=32)
    goods_number = models.IntegerField()
    goods_price = models.FloatField()
    goods_picture = models.CharField(max_length=32)
    goods_total = models.FloatField()
    goods_id = models.IntegerField()
    cart_user = models.IntegerField()

"""
一个订单，三件商品，假如一件商品确认发货，其他两件未发货
订单状态？
前端展示问题
后端修改问题
"""

# Create your models here.
