# Generated by Django 3.2.5 on 2021-07-04 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'notes', 'verbose_name_plural': 'notes'},
        ),
        migrations.RenameField(
            model_name='notes',
            old_name='User',
            new_name='Username',
        ),
    ]
