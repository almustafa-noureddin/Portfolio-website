# Generated by Django 3.2.7 on 2022-03-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_skillandcategoryrelation_blog_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='topic',
            field=models.ManyToManyField(blank=True, to='base.SkillAndCategoryRelation'),
        ),
    ]