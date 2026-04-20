import logging

from django.db.models.signals import (
    post_delete,
    post_init,
    post_save,
    pre_delete,
    pre_init,
    pre_save,
)
from django.dispatch import receiver

from apps.accounts.models import User
from apps.notifications.models import Notification

logger = logging.getLogger(__name__)


@receiver(pre_init, sender=User)
def user_pre_init(sender, args, kwargs, **extra):
    logger.info(f"[pre_init] User() chaqirilmoqda kwargs={kwargs}")



@receiver(post_init, sender=User)
def user_post_init(sender, instance, **kwargs):
    logger.info(f"[post_init] User instance yaratildi: {instance.phone}")



@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, raw, using, update_fields, **kwargs):
    if not instance.pk:
        logger.info(f"[pre_save] Yangi user yaratilmoqda: {instance.phone}")
    else:
        # Eski qiymatni DB dan o'qib solishtiramiz
        try:
            old = User.objects.get(pk=instance.pk)
            if old.phone != instance.phone:
                logger.info(f"[pre_save] Phone o'zgardi: {old.phone} -> {instance.phone}")
        except User.DoesNotExist:
            pass



@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, raw, using, update_fields, **kwargs):
    if created:
        logger.info(f"[post_save] Yangi user yaratildi: {instance.phone}")
        Notification.objects.create(
            user=instance,
            title="Welcome",
            message="Welcome to our platform",
        )
    else:
        logger.info(f"[post_save] User yangilandi: {instance.phone}")



@receiver(pre_delete, sender=User)
def user_pre_delete(sender, instance, using, origin, **kwargs):
    logger.info(f"[pre_delete] User o'chirilmoqda: {instance.phone}")



@receiver(post_delete, sender=User)
def user_post_delete(sender, instance, using, origin, **kwargs):
    logger.info(f"[post_delete] User o'chirildi: {instance.phone} (pk={instance.pk})")


#