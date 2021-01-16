from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subjet = f'Commande N°: {order.id}'
    message = f'Chére {order.first_name},\n\n' \
              f'vous avez passer une commande avec succés' \
              f'votre identifiant de commande est le: {order.id}'

    mail_sent = send_mail(subject, message, 'inter.taki@gmail.com',[order.email])
    return mail_sent