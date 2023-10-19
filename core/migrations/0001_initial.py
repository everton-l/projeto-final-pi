# Generated by Django 4.2.6 on 2023-10-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='image')),
                ('descricao', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
