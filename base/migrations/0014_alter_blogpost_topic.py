# Generated by Django 3.2.7 on 2022-03-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_blogpost_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='topic',
            field=models.ManyToManyField(to='base.SkillAndCategoryRelation'),
        ),
    ]
