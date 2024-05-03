# Generated by Django 5.0.4 on 2024-05-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
