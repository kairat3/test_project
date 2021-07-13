from django.db import models

import user.models


class Category(models.Model):
    category = models.SlugField(max_length=100, primary_key=True, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        if not self.parent:
            return f"Category: {self.category}"
        else:
            return f"{self.parent} --> {self.category}"


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', blank=True)
    owner = models.ForeignKey(user.models.CustomUser, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return f"{self.title}"


class ArticleImages(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    @staticmethod
    def generate_name():
        import random
        return "Image" + str(random.randint(1, 99999))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(ArticleImages, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} --> {self.post.id}"