from django.db import models
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class List(models.Model):
    description = models.TextField(max_length=200, null=False, blank=False)
    detailed_description = models.TextField(max_length=3000, null=True, blank=True)
    status = models.CharField(max_length=120, null=False, blank=False, choices=status_choices)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Lists'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.status}: {self.description}'