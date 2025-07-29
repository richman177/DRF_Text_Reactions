from django.db import models


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.text}"


class Reaction(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='reactions')
    emoji = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emoji} - {self.quote}"
