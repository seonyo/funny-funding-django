# Generated by Django 4.2.11 on 2024-06-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funfun', '0005_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='target_num',
        ),
        migrations.AddField(
            model_name='item',
            name='current_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='participant_num',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]