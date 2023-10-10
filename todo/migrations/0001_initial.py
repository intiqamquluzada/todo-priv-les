# Generated by Django 4.2.6 on 2023-10-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ediləcək iş')),
                ('status', models.BooleanField(default=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ediləcək iş',
                'verbose_name_plural': 'Ediləcək işlər',
                'ordering': ('add_date',),
            },
        ),
    ]