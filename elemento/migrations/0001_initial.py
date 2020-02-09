# Generated by Django 2.2.4 on 2020-02-08 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grupo', '0001_initial'),
        ('clasificacion', '0001_initial'),
        ('periodo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('masa_atomica', models.FloatField(default=None)),
                ('simbolo', models.CharField(default=None, max_length=10)),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clasificacion.Clasificacion')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupo.Grupo')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='periodo.Periodo')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
