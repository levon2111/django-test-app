from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from help_gamblers.taskapp.celery import app


@app.task
def send_signup_email(user):
    callback_url = f'{settings.FRONT_URL}?token={user["token"]}'
    email = EmailMessage(
        subject='Welcome to HelpGamblers',
        body=render_to_string(
            template_name="email/account_confirmation.html",
            context={"name": user['name'], "callback_url": callback_url},
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user['email']],
    )
    email.send(fail_silently=False)


@app.task
def forgot_password_email(user):
    callback_url = f'{settings.FRONT_URL}?token={user["token"]}&reset=true'
    email = EmailMessage(
        subject='HelpGamblers: Reset your password',
        body=render_to_string(
            template_name="email/reset_password.html",
            context={"name": user['name'], "callback_url": callback_url},
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user['email']],
    )
    email.send(fail_silently=False)
