from django.db import models
from django.utils.translation import gettext_lazy as _


class Ad(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=2000)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ad_images/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Ad")
        verbose_name_plural = _("Ads")
        ordering = ["-created_at"]


class Comment(models.Model):
    text = models.CharField(max_length=2000)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}, {self.created_at}"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
