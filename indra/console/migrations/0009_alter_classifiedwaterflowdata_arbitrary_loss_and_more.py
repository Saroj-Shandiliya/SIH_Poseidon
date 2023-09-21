# Generated by Django 4.0.4 on 2023-09-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0008_classifiedwaterflowdata_arbitrary_loss_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifiedwaterflowdata',
            name='arbitrary_loss',
            field=models.FloatField(default=300),
        ),
        migrations.AlterField(
            model_name='classifiedwaterflowdata',
            name='unauthorised_consumption',
            field=models.FloatField(default=400),
        ),
    ]