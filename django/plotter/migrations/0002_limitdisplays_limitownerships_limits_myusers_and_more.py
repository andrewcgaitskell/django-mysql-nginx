# Generated by Django 4.0.5 on 2022-07-01 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LimitDisplays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit_id', models.IntegerField(blank=True, null=True)),
                ('plot_id', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('style', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'limit_displays',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LimitOwnerships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('limit_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'limit_ownerships',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Limits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spin_dependency', models.CharField(blank=True, max_length=255, null=True)),
                ('result_type', models.CharField(blank=True, max_length=255, null=True)),
                ('measurement_type', models.CharField(blank=True, max_length=60, null=True)),
                ('nomhash', models.TextField(blank=True, null=True)),
                ('x_units', models.CharField(blank=True, max_length=255, null=True)),
                ('y_units', models.CharField(blank=True, max_length=255, null=True)),
                ('x_rescale', models.CharField(blank=True, max_length=255, null=True)),
                ('y_rescale', models.CharField(blank=True, max_length=255, null=True)),
                ('default_color', models.CharField(blank=True, max_length=255, null=True)),
                ('default_style', models.CharField(blank=True, max_length=255, null=True)),
                ('data_values', models.TextField(blank=True, null=True)),
                ('data_label', models.CharField(blank=True, max_length=255, null=True)),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('data_comment', models.CharField(blank=True, max_length=255, null=True)),
                ('data_reference', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('creator_id', models.IntegerField(blank=True, null=True)),
                ('experiment', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('date_of_announcement', models.DateField(blank=True, null=True)),
                ('public', models.IntegerField(blank=True, null=True)),
                ('official', models.IntegerField(blank=True, null=True)),
                ('date_official', models.DateField(blank=True, null=True)),
                ('greatest_hit', models.IntegerField(blank=True, null=True)),
                ('date_of_run_start', models.DateField(blank=True, null=True)),
                ('date_of_run_end', models.DateField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'limits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('crypted_password', models.CharField(blank=True, max_length=40, null=True)),
                ('password', models.CharField(blank=True, max_length=40, null=True)),
                ('salt', models.CharField(blank=True, max_length=40, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('remember_token', models.CharField(blank=True, max_length=255, null=True)),
                ('remember_token_expires_at', models.DateTimeField(blank=True, null=True)),
                ('reset_password_code', models.CharField(blank=True, max_length=255, null=True)),
                ('reset_password_code_until', models.DateTimeField(blank=True, null=True)),
                ('activation_code', models.CharField(blank=True, max_length=255, null=True)),
                ('activated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'my_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlotOwnerships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('plot_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'plot_ownerships',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('x_min', models.CharField(blank=True, max_length=255, null=True)),
                ('x_max', models.CharField(blank=True, max_length=255, null=True)),
                ('y_min', models.CharField(blank=True, max_length=255, null=True)),
                ('y_max', models.CharField(blank=True, max_length=255, null=True)),
                ('x_units', models.CharField(blank=True, max_length=255, null=True)),
                ('y_units', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('plot_png', models.TextField(blank=True, null=True)),
                ('legend_png', models.TextField(blank=True, null=True)),
                ('plot_eps', models.TextField(blank=True, null=True)),
                ('legend_eps', models.TextField(blank=True, null=True)),
                ('no_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'plots',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('crypted_password', models.CharField(blank=True, max_length=40, null=True)),
                ('salt', models.CharField(blank=True, max_length=40, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('remember_token', models.CharField(blank=True, max_length=255, null=True)),
                ('remember_token_expires_at', models.DateTimeField(blank=True, null=True)),
                ('reset_password_code', models.CharField(blank=True, max_length=255, null=True)),
                ('reset_password_code_until', models.DateTimeField(blank=True, null=True)),
                ('activation_code', models.CharField(blank=True, max_length=255, null=True)),
                ('activated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
