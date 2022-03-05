# Generated by Django 3.2.7 on 2022-03-05 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20220305_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='topic',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.skillandcategoryrelation'),
        ),
    ]