# Generated by Django 2.2.9 on 2021-04-05 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='publicacao',
            new_name='criacao',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='publicacao',
            new_name='criacao',
        ),
        migrations.RemoveField(
            model_name='avaliacao',
            name='cometario',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='comentario',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='curso',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
