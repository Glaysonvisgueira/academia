# Generated by Django 2.2.5 on 2019-10-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20191027_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='uf',
            field=models.CharField(choices=[('PI', 'PI'), ('MA', 'MA'), ('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('ES', 'ES'), ('CE', 'CE'), ('GO', 'GO'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2, verbose_name='UF:'),
        ),
    ]
