# Generated by Django 5.1.6 on 2025-03-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_livro_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, upload_to='capas/%d/%m/%Y'),
        ),
    ]
