from django.db import models

class list(models.Model):
    description = models.CharField(max_length=120, null=False, blank=False)
    status = models.TextField(max_length=3000, null=False, blank=False)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        db_table = 'Lists'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.status}: {self.description}'