# Generated by Django 3.2.8 on 2021-10-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
