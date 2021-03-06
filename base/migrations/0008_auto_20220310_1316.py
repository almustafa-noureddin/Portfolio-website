# Generated by Django 3.2.7 on 2022-03-10 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20220310_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='skill_categories',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill_categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.skillcategory'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='skills',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.skill'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='socials',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='socials',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.social'),
        ),
    ]
