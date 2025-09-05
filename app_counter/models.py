from django.db import models
from django.conf import settings


class Counter(models.Model):
    value = models.IntegerField(blank=False, null=False, default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    is_favorite = models.BooleanField(default=False)
    name = models.CharField(max_length=10, blank=True, default="")

    def save(self, *args, **kwargs):
        if not self.name and not self.pk:
            user_counters_count = Counter.objects.filter(user=self.user).count()
            self.name = f"Счетчик {user_counters_count + 1}"
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name} (id={self.id}, value={self.value})"
