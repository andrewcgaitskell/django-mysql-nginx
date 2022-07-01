# Generated by Django 4.0.5 on 2022-07-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0002_limitdisplays_limitownerships_limits_myusers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamplePlotData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Age', models.IntegerField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'ExamplePlotData',
                'managed': True,
            },
        ),
    ]