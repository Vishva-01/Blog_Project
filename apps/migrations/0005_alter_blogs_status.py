# Generated by Django 4.2.2 on 2023-10-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_remove_blogs_tags_blogs_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Approved', max_length=10),
        ),
    ]