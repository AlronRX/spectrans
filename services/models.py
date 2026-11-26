from django.db import models

# Create your models here.
class Service(models.Model):
    """Услуга, которую оказывает компания."""
    title = models.CharField(max_length=200, verbose_name="Название услуги")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-идентификатор")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['sort_order', 'title']

    def __str__(self):
        return self.title


        