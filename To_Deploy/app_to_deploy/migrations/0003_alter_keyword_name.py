# Generated by Django 4.2.3 on 2023-07-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_to_deploy', '0002_alter_keyword_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
