# Generated by Django 5.0.6 on 2024-06-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_rate', models.IntegerField(default=1)),
            ],
        ),
    ]
