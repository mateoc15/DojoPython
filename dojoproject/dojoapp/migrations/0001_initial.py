# Generated by Django 2.1 on 2018-08-25 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('habilitado', models.BooleanField(default=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dojoapp.Estudiante'),
        ),
    ]
