# Generated by Django 4.0.5 on 2022-06-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cadastro_users',
        ),
        migrations.RemoveField(
            model_name='cadastro_livros',
            name='edicao',
        ),
        migrations.AddField(
            model_name='cadastro_livros',
            name='autor',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
