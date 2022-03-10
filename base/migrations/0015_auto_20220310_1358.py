# Generated by Django 3.2.7 on 2022-03-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_blogpost_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='topic',
            field=models.ManyToManyField(blank=True, to='base.SkillAndCategoryRelation'),
        ),
        migrations.RemoveField(
            model_name='project',
            name='skills_used',
        ),
        migrations.AddField(
            model_name='project',
            name='skills_used',
            field=models.ManyToManyField(blank=True, to='base.SkillAndCategoryRelation'),
        ),
    ]