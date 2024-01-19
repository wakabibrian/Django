# Generated by Django 5.0.1 on 2024-01-19 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_address_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Enteries'},
        ),
        migrations.AddField(
            model_name='book',
            name='publised_countries',
            field=models.ManyToManyField(to='book_outlet.country'),
        ),
    ]
