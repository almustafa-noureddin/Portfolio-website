# Generated by Django 3.2.7 on 2022-03-10 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_media_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='skills_used',
        ),
        migrations.AddField(
            model_name='project',
            name='skills_used',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.skillandcategoryrelation'),
        ),
    ]
