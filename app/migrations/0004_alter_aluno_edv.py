# Generated by Django 5.2.2 on 2025-06-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_data_aluno_data_aniversario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='edv',
            field=models.CharField(max_length=8),
        ),
    ]
