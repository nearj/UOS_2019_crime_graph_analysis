# Generated by Django 2.0.13 on 2019-10-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0002_auto_20191025_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='law_cat_cd',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trial',
            name='pd_cd',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trial',
            name='s_age',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trial',
            name='s_race',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trial',
            name='s_sex',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trial',
            name='v_age',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trial',
            name='v_race',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trial',
            name='v_sex',
            field=models.FloatField(),
        ),
    ]