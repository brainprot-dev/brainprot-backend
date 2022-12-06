from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Post model
class Post(models.Model):
    STATUS = (
        (0,"Draft"),
        (1,"Published")
    )

    title = models.CharField(
        max_length=300,
        default='',
        help_text="Title of the News Article",
        verbose_name="Title of Article"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="Article slug",
        verbose_name="Slug"
    )
    author = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        related_name='blog_posts',
        help_text="Article authored by this user",
        verbose_name="Article Authored"
    )
    updated_on = models.DateTimeField(
        auto_now= True,
        help_text="Article updated on date",
        verbose_name="Updated on"
    )
    content = models.TextField(
        help_text="Content of the article",
        verbose_name="Article Content"
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Article creation date",
        verbose_name="Created on"
    )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# Team Member Model      
class TeamMember(models.Model):
    name = models.CharField(
        max_length=150,
        default='',
        help_text="Name of the Member",
        verbose_name="Member Name"
    )
    designation = models.CharField(
        max_length=250,
        default='',
        help_text="Designation/Title of the member",
        verbose_name="Member Designation"
    )
    affiliation = models.TextField(
        help_text="Affiliation of the Team Member",
        verbose_name="Member Affiliation"
    )
    email = models.CharField(
        max_length=150,
        default='',
        help_text="e-Mail address of the team member",
        verbose_name="Member e-mail"
    )
    
    def __str__(self):
        return self.name
