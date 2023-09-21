# Generated by Django 4.0.4 on 2023-09-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0003_alter_customuser_groups_alter_customuser_secretkey_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('day', models.IntegerField()),
                ('real_losses', models.IntegerField()),
                ('flow_analysis_central', models.IntegerField()),
                ('flow_analysis_receive', models.IntegerField()),
                ('loss_analysis', models.CharField(max_length=10)),
                ('alert_analysis', models.CharField(max_length=10)),
            ],
        ),
    ]