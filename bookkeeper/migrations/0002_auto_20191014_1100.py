# Generated by Django 2.2.6 on 2019-10-14 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['category', '-payment_date'], 'verbose_name': 'Расход', 'verbose_name_plural': 'Расходы'},
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookkeeper.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='comments',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата оплаты'),
        ),
    ]
