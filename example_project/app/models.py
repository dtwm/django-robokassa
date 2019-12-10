from django.db import models
from django.dispatch import receiver
from robokassa.signals import result_received


class Order(models.Model):
    name = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=255, blank=True, null=True)
    paid_sum = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    extra_param = models.CharField(max_length=255, blank=True, null=True)


@receiver(result_received)
def payment_received(sender, **kwargs):
    order = Order.objects.get(pk=kwargs["InvId"])
    order.status = "paid"
    order.paid_sum = kwargs["OutSum"]
    order.extra_param = kwargs["extra"]["my_param"]
    order.save()
