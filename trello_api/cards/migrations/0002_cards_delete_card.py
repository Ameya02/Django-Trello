# Generated by Django 5.0.4 on 2024-05-03 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
        ('columns', '0002_alter_column_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('position', models.PositiveIntegerField(default=0)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='columns.column')),
            ],
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]
