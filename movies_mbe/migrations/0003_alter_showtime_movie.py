# Generated by Django 3.2.9 on 2021-12-02 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_mbe', '0002_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='show_times', to='movies_mbe.movie'),
        ),
    ]
