# Generated by Django 4.1.7 on 2023-03-03 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_alter_poll_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='Api.poll'),
        ),
    ]
