# Generated by Django 3.0.2 on 2020-01-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20200114_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=20)),
                ('academic_year', models.CharField(max_length=10)),
            ],
        ),
    ]