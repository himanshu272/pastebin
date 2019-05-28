# Generated by Django 2.2.1 on 2019-05-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0003_auto_20190528_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpaste',
            name='language',
            field=models.CharField(choices=[('Python', 'PYTHON'), ('CPP', 'C/C++'), ('Java', 'Java'), ('JS', 'JavaScript'), ('GEN', 'TextFile')], default='GEN', max_length=10),
        ),
    ]