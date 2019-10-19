# Generated by Django 2.2.5 on 2019-10-18 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20191016_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='complemento',
            field=models.CharField(blank=True, max_length=150, verbose_name='Complemento do endereço:'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='status',
            field=models.CharField(choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')], max_length=7, verbose_name='Status:'),
        ),
    ]
