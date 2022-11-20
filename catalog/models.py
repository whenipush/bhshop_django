from django.db import models

# Create your models here.


class Store(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=1)
    photo = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    created_at = models.DateField(auto_now_add=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']