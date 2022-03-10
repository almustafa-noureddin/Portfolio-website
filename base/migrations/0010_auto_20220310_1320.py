# Generated by Django 3.2.7 on 2022-03-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20220310_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='topic',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='topic',
            field=models.ManyToManyField(blank=True, null=True, to='base.SkillAndCategoryRelation'),
        ),
    ]
