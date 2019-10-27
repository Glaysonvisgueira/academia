# Generated by Django 2.2.5 on 2019-10-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF:')),
                ('rg', models.CharField(max_length=7, verbose_name='RG:')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome:')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço:')),
                ('complemento', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento do endereço:')),
                ('bairro', models.CharField(max_length=40, verbose_name='Bairro:')),
                ('cidade', models.CharField(max_length=40, verbose_name='Cidade:')),
                ('uf', models.CharField(choices=[('PI', 'PI'), ('MA', 'MA'), ('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('ES', 'ES'), ('CE', 'CE'), ('GO', 'GO'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2, verbose_name='UF:')),
                ('nascimento', models.DateField(verbose_name='Data de nascimento:')),
                ('telefone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Telefone:')),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('dataInicio', models.DateField(verbose_name='Data de início:')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('status', models.CharField(choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')], max_length=7, verbose_name='Status:')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id', 'cpf', 'rg', 'nome', 'dataInicio', 'status'],
            },
        ),
    ]
