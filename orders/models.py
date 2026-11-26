from django.db import models
from services.models import Service
# Create your models here.
class Order(models.Model):
    """Заявка на аренду спецтехники."""
    class StatusChoices(models.TextChoices):
        NEW = 'new', 'Новая'
        PROCESSED = 'processed', 'В обработке'
        DONE = 'done', 'Выполнена'
        CANCELLED = 'cancelled', 'Отменена'

    name = models.CharField(max_length=200, verbose_name="ФИО / Наименование компании")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Вид услуги"
    )
    purpose = models.TextField(blank=True, verbose_name="Цель предоставления спецтехники")
    duration = models.CharField(max_length=200, blank=True, verbose_name="Срок оказания услуги")
    location = models.CharField(max_length=300, blank=True, verbose_name="Объект / район оказания услуг")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.NEW,
        verbose_name="Статус"
    )
    consent = models.BooleanField(default=False, verbose_name="Согласие с политикой конфиденциальности")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка №{self.pk} от {self.name} ({self.created_at:%d.%m.%Y})"