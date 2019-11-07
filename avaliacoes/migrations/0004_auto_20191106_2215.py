# Generated by Django 2.2.5 on 2019-11-07 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0003_auto_20191106_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='avaliador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]