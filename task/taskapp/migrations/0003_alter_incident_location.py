# Generated by Django 4.0.4 on 2022-05-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_alter_incident_initial_severity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='location',
            field=models.CharField(choices=[('corporate headoffice', 'CORPORATE HEADOFFICE'), ('operations department', 'OPERATIONS DEPARTMENT'), ('work station', 'WORK STATION'), ('orange', 'ORANGE'), ('marketing division', 'MARKETING DIVISION')], default='corporate headoffice', max_length=22),
        ),
    ]
