# Generated by Django 2.1 on 2018-09-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='question',
            name='weight',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterOrderWithRespectTo(
            name='answer',
            order_with_respect_to='questions',
        ),
    ]