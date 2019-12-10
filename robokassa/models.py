from django.db import models


class SuccessNotification(models.Model):
    InvId = models.IntegerField("Номер заказа", db_index=True)
    OutSum = models.CharField("Сумма", max_length=15)

    created_at = models.DateTimeField(
        "Дата и время получения уведомления", auto_now_add=True
    )

    class Meta:
        verbose_name = "Уведомление об успешном платеже"
        verbose_name_plural = "Уведомления об успешных платежах (ROBOKASSA)"

    def __str__(self):
        return "#{}: {} ({})".format(self.InvId, self.OutSum, self.created_at)
