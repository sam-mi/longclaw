# Generated by Django 3.1.8 on 2021-04-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0003_auto_20190322_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingProcessor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('shipping.shippingrateprocessor',),
        ),
        migrations.AlterModelOptions(
            name='shippingrateprocessor',
            options={},
        ),
        migrations.RemoveField(
            model_name='shippingrateprocessor',
            name='polymorphic_ctype',
        ),
        migrations.AddField(
            model_name='shippingrateprocessor',
            name='type',
            field=models.CharField(choices=[('shipping.shippingprocessor', 'shipping processor')], db_index=True, default='shipping.shippingprocessor', max_length=255),
            preserve_default=False,
        ),
    ]
