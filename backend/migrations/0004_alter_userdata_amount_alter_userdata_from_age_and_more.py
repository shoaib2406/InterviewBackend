# Generated by Django 4.1 on 2022-08-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_income_grows_userdata_income_grows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='amount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='from_age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='income_grows',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='to_age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]