from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    SkillCategory,
    SkillAndCategoryRelation,
    Skill,
    Media,
    Social,
    )
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','skill_category')

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(SkillAndCategoryRelation)
class SkillAndCategoryRelationAdmin(admin.ModelAdmin):
    list_display = ('id','skill','skill_category')