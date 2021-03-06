# Generated by Django 2.2.7 on 2019-11-21 10:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('fnac', models.DateField()),
                ('instrumento', models.CharField(choices=[('guitarra', 'guitarra'), ('bajo', 'bajo'), ('bateria', 'bateria'), ('violin', 'violin'), ('piano', 'piano')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoMusical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creacion', models.DateField()),
                ('estilo', models.CharField(choices=[('rock', 'rock'), ('pop', 'pop'), ('indie', 'indie'), ('metal', 'metal'), ('r&b', 'r&b'), ('alternativa', 'alternativa')], max_length=20)),
                ('miembros', models.ManyToManyField(to='práctica_05.Musico')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('lanzamiento', models.DateField()),
                ('estrellas', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='práctica_05.GrupoMusical')),
            ],
        ),
    ]
