# Generated by Django 4.0.3 on 2022-08-14 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_tool_fooball'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MyPerson',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('demo.person',),
        ),
    ]
