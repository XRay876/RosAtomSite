# Generated by Django 4.2.2 on 2023-07-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_productsveh'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsVnedr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uVnedrID', models.CharField(max_length=50, verbose_name='Код')),
                ('uVnedrComponentA', models.CharField(max_length=100, verbose_name='ComponentA')),
                ('uVnedrComponentB', models.CharField(max_length=100, verbose_name='ComponentB')),
                ('uVnedrLinkedProducts', models.CharField(max_length=100, verbose_name='LinkedProducts')),
                ('uVnedrName', models.TextField(verbose_name='Название')),
                ('uVnedrStatus', models.CharField(max_length=100, verbose_name='Статус')),
                ('uVnedrComand', models.CharField(max_length=100, verbose_name='Команда')),
                ('uVnedrRP', models.CharField(max_length=100, verbose_name='РП')),
                ('uVnedrStartTime', models.DateField(verbose_name='Дата начала')),
                ('uVnedrStopTime', models.DateField(verbose_name='Окончание')),
                ('uVnedrCustomer', models.CharField(max_length=100, verbose_name='Заказчик')),
                ('uVnedrNotes', models.TextField(verbose_name='Notes')),
                ('uVnedrDocumentation', models.URLField(verbose_name='Документация')),
                ('uVnedrPlantUML', models.CharField(max_length=300, verbose_name='PlantUML')),
                ('uVnedr_Status', models.CharField(max_length=100, verbose_name='_статус')),
                ('uVnedrConstruction', models.CharField(max_length=100, verbose_name='Construction')),
                ('uVnedrAncestor', models.CharField(max_length=50, verbose_name='Предшественник')),
                ('uVnedrLinkProject', models.URLField(verbose_name='LinkProject')),
            ],
        ),
    ]