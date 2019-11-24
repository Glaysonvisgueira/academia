# Generated by Django 2.2.5 on 2019-11-23 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frequencia',
            options={'ordering': ['id', 'usuario', 'data', 'is_presente'], 'verbose_name': 'Frequência', 'verbose_name_plural': 'Frequências'},
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='data',
            field=models.DateField(verbose_name='Data da presença'),
        ),
        migrations.AddConstraint(
            model_name='frequencia',
            constraint=models.UniqueConstraint(fields=('usuario', 'data'), name='presença do cliente'),
        ),
    ]