# Generated by Django 2.2.27 on 2022-08-04 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamesessions', '0003_auto_20220804_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionplayer',
            name='savefile',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='SessionHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isMainHost', models.BooleanField(default=False)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamesessions.Session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['session', 'isMainHost', 'user'],
            },
        ),
        migrations.CreateModel(
            name='PlayedNation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamenation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gamesessions.GameNation')),
                ('sessionplayer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gamesessions.SessionPlayer')),
            ],
            options={
                'ordering': ['sessionplayer', 'gamenation'],
            },
        ),
    ]
