from django.db import models

CHOICES = (
    ("Hələ başlanmayıb", "not"),
    ("Davam edir", "progress"),
    ("Bitib", "finish")
)


class Todo(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ediləcək iş")
    status = models.CharField(max_length=255, choices=CHOICES, verbose_name="Taskin statusu", null=True, blank=True, default="Hələ başlanmayıb")
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(null=True, blank=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("add_date",)
        verbose_name = "Ediləcək iş"
        verbose_name_plural = "Ediləcək işlər"
