# Generated by Django 3.2.4 on 2021-06-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0005_auto_20210619_1211"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="number",
            field=models.IntegerField(max_length=11, null=True),
        ),
    ]
