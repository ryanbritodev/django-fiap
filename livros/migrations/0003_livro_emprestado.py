# Generated by Django 5.1.6 on 2025-03-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_livro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
    ]
