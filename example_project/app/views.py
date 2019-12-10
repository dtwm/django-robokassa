from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from robokassa.forms import RobokassaForm

from .models import Order


@login_required
def pay_with_robokassa(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    form = RobokassaForm(
        initial={
            "OutSum": order.total,
            "InvId": order.id,
            "Desc": order.name,
            "Email": request.user.email,
            # 'IncCurrLabel': '',
            # 'Culture': 'ru'
        }
    )

    return render(request, "app/pay_with_robokassa.html", {"form": form})
