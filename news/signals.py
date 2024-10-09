from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from .models import Post


@receiver(m2m_changed, sender=Post.subscribers.through)
def post_created(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':

        subscribers = instance.subscribers.all()
        emails = subscribers.values_list('email', flat=True)

        subject = f'Новый пост в категории {instance.categoryType}'

        text_content = (
            f'Пост: {instance.title}\n'
            f'Содержание: {instance.text}\n\n'
            f'Ссылка на пост: http://127.0.0.1:8000{instance.get_absolute_url()}'
        )
        html_content = (
            f'Пост: {instance.title}<br>'
            f'Содержание: {instance.text}<br><br>'
            f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
            f'Ссылка на пост</a>'
        )
        for email in emails:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()