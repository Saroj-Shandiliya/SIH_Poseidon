# Generated by Django 4.0.4 on 2023-09-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0005_classifiedwaterflowdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvdata',
            name='year',
            field=models.IntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='csvdata',
            name='flow_analysis_central',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='csvdata',
            name='flow_analysis_receive',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]