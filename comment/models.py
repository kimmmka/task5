from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=200, db_index=True)
    rate = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    content = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    replies = models.CharField(max_length=200, db_index=True, default=None)
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.content)
    class Meta:
        ordering = ('created',)

