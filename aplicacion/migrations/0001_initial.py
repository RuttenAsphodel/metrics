# Generated by Django 4.0.6 on 2024-12-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('team_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_accuracy', models.FloatField()),
                ('shooting_accuracy', models.FloatField()),
                ('ball_control', models.FloatField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.player')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.FloatField()),
                ('agility', models.FloatField()),
                ('strength', models.FloatField()),
                ('endurance', models.FloatField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.player')),
            ],
        ),
    ]