# Generated by Django 3.2.7 on 2022-03-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20220310_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillandcategoryrelation',
            name='blog_topic',
            field=models.ManyToManyField(blank=True, null=True, to='base.BlogPost'),
        ),
    ]
