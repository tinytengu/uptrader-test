import re

from django.db import models
from django.urls import reverse


class MenuCategory(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (#{self.id})"

    class Meta:
        verbose_name_plural = "categories"


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    text = models.CharField(max_length=100)
    url = models.CharField(max_length=500)

    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.text} (#{self.id})"

    def is_url(self):
        return re.match(r"(?:^http[s]?:\/\/|^/)", self.url) is not None

    def is_url_match(self, url: str):
        if self.is_url():
            return url == self.url
        return url == reverse(self.url)
