from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    This class represents a blog post model in Django.
    """

    class Status(models.TextChoices):
        """
        This inner class represents the choices for the status field.
        """
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    class Meta:
        """
        This inner class represents additional metadata for the Post model.
        """
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        """
        Returns a string representation of the Post object.

        :return: The title of the post.
        """
        return self.title