from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    subject = models.CharField(verbose_name="Subject",max_length=200)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'
    
class SkillCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Skill Categories'
        verbose_name = 'Skill Category'
    
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skill_category")
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    skill_category = models.ForeignKey(SkillCategory,null=True,on_delete=models.SET_NULL, blank=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    
    def __str__(self):
        return self.name

class SkillAndCategoryRelation(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='mtm', blank=True, null=True)
    skill_category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='mtm', blank=True, null=True)
    
    def __str__(self):
        return f'{self.skill}, {self.skill_category}'

class Social(models.Model):
    
    class Meta:
        verbose_name_plural = 'Socials'
        verbose_name = 'Social'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    icon_html = models.CharField(max_length=200, blank=True, null=True)
    link= models.URLField(max_length = 100, null=True, blank=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skill_categories = models.ManyToManyField(SkillCategory, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")
    socials= models.ManyToManyField(Social, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Project(models.Model):

    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="projects")
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    skills_used = models.ManyToManyField(Skill, blank=True)
    github_link = models.URLField(max_length=200)
    live_link = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/projects/{self.slug}"


class BlogPost(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Posts'
        verbose_name = 'Blog Post'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="blog_posts")
    name = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    topic = models.ForeignKey(SkillAndCategoryRelation,on_delete=models.SET_NULL, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

