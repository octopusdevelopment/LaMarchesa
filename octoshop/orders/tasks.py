from celery import task
from io import BytesIO
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.conf import settings
from .models import Order
import weasyprint


def order_send_email(order):
    subject = f'La Marchesa - Commande N°: {order.id}'
    message = f'Cher/Chère {order.first_name},\n' \
              f'Vous avez passé une commande avec succès, veuillez trouver votre facture en piece jointe. \n' \
              f'Votre identifiant de commande est le: {order.id}' \

    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [order.email])
    html = render_to_string('pdf.html', {"order":order})
    out = BytesIO()
    weasyprint.HTML(string=html).write_pdf(out)
    # attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    email.send()
    return True

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Commande N°: {order.id}'
    message = f'Chère {order.first_name},\n\n' \
              f'Vous avez passé une commande avec succès' \
              f'Votre identifiant de commande est le: {order.id}'

    mail_sent = send_mail(subject, message, 'inter.taki@gmail.com',[order.email])
    return mail_sent

@task
def order_validated(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'OCTOSHOP - Commande ID° {order.id}'
    message = 'Merci de nous avoir fait confiance.\n Veuillez trouver votre facture en piece jointe'
    email = EmailMessage(subject, message,'admin@octoshop.com', [order.email])

    html = render_to_string('pdf.html', {"order":order})
    out = BytesIO()
    #stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out)
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    email.send()