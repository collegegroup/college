# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-28 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(db_column='CITY_ID', primary_key=True, serialize=False)),
                ('city_name', models.CharField(blank=True, db_column='CITY_NAME', max_length=100, null=True)),
                ('state_id', models.IntegerField(blank=True, db_column='STATE_ID', null=True)),
                ('lastupd_dttm', models.DateTimeField(blank=True, db_column='LASTUPD_DTTM', null=True)),
            ],
            options={
                'db_table': 'CITY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CollegeCourses',
            fields=[
                ('seq_id', models.AutoField(db_column='SEQ_ID', primary_key=True, serialize=False)),
                ('college_id', models.IntegerField(blank=True, db_column='COLLEGE_ID', null=True)),
                ('course', models.CharField(blank=True, db_column='COURSE', max_length=45, null=True)),
                ('duration', models.CharField(blank=True, db_column='DURATION', max_length=45, null=True)),
                ('fee', models.DecimalField(blank=True, db_column='FEE', decimal_places=2, max_digits=10, null=True)),
                ('entrance', models.CharField(blank=True, db_column='ENTRANCE', max_length=45, null=True)),
                ('lastupd_dttm', models.DateTimeField(blank=True, db_column='LASTUPD_DTTM', null=True)),
            ],
            options={
                'db_table': 'COLLEGE_COURSES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CollegeMain',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('college_name', models.CharField(blank=True, db_column='COLLEGE_NAME', max_length=200, null=True)),
                ('location', models.CharField(blank=True, db_column='LOCATION', max_length=200, null=True)),
                ('establishment', models.CharField(blank=True, db_column='ESTABLISHMENT', max_length=45, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=256, null=True)),
                ('affiliation', models.CharField(blank=True, db_column='AFFILIATION', max_length=200, null=True)),
                ('website', models.CharField(blank=True, db_column='WEBSITE', max_length=45, null=True)),
                ('address', models.CharField(blank=True, db_column='ADDRESS', max_length=256, null=True)),
                ('landline_num', models.CharField(blank=True, db_column='LANDLINE_NUM', max_length=45, null=True)),
                ('mobile_num', models.CharField(blank=True, db_column='MOBILE_NUM', max_length=45, null=True)),
                ('emailid', models.CharField(blank=True, db_column='EMAILID', max_length=45, null=True)),
                ('facilities', models.CharField(blank=True, db_column='FACILITIES', max_length=2, null=True)),
                ('profile_image', models.CharField(blank=True, db_column='PROFILE_IMAGE', max_length=100, null=True)),
                ('highest_package', models.DecimalField(blank=True, db_column='HIGHEST_PACKAGE', decimal_places=2, max_digits=10, null=True)),
                ('average_package', models.DecimalField(blank=True, db_column='AVERAGE_PACKAGE', decimal_places=2, max_digits=10, null=True)),
                ('lastupd_dttm', models.DateTimeField(blank=True, db_column='LASTUPD_DTTM', null=True)),
            ],
            options={
                'db_table': 'COLLEGE_MAIN',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InstituteCourses',
            fields=[
                ('seq_id', models.AutoField(db_column='SEQ_ID', primary_key=True, serialize=False)),
                ('college_id', models.IntegerField(blank=True, db_column='COLLEGE_ID', null=True)),
                ('course', models.CharField(blank=True, db_column='COURSE', max_length=45, null=True)),
                ('duration', models.CharField(blank=True, db_column='DURATION', max_length=45, null=True)),
                ('fee', models.DecimalField(blank=True, db_column='FEE', decimal_places=2, max_digits=10, null=True)),
                ('lastupd_dttm', models.DateTimeField(blank=True, db_column='LASTUPD_DTTM', null=True)),
            ],
            options={
                'db_table': 'INSTITUTE_COURSES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InstituteMain',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('institute_name', models.CharField(blank=True, db_column='INSTITUTE_NAME', max_length=200, null=True)),
                ('director_name', models.CharField(blank=True, db_column='DIRECTOR_NAME', max_length=45, null=True)),
                ('location', models.CharField(blank=True, db_column='LOCATION', max_length=200, null=True)),
                ('establishment', models.CharField(blank=True, db_column='ESTABLISHMENT', max_length=45, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=256, null=True)),
                ('affiliation', models.CharField(blank=True, db_column='AFFILIATION', max_length=200, null=True)),
                ('website', models.CharField(blank=True, db_column='WEBSITE', max_length=45, null=True)),
                ('address', models.CharField(blank=True, db_column='ADDRESS', max_length=256, null=True)),
                ('landline_num', models.CharField(blank=True, db_column='LANDLINE_NUM', max_length=45, null=True)),
                ('mobile_num', models.CharField(blank=True, db_column='MOBILE_NUM', max_length=45, null=True)),
                ('emailid', models.CharField(blank=True, db_column='EMAILID', max_length=45, null=True)),
                ('facilities', models.CharField(blank=True, db_column='FACILITIES', max_length=2, null=True)),
                ('profile_image', models.CharField(blank=True, db_column='PROFILE_IMAGE', max_length=100, null=True)),
                ('lastupd_dttm', models.DateTimeField(blank=True, db_column='LASTUPD_DTTM', null=True)),
            ],
            options={
                'db_table': 'INSTITUTE_MAIN',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(db_column='LOCATION_ID', primary_key=True, serialize=False)),
                ('state_name', models.CharField(blank=True, db_column='STATE_NAME', max_length=100, null=True)),
                ('city_name', models.CharField(blank=True, db_column='CITY_NAME', max_length=100, null=True)),
                ('sub_city', models.CharField(blank=True, db_column='SUB_CITY', max_length=100, null=True)),
                ('pin_code', models.CharField(blank=True, db_column='PIN_CODE', max_length=6, null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=2, null=True)),
                ('lastupd_dttm', models.DateTimeField(blank=True, db_column='LASTUPD_DTTM', null=True)),
            ],
            options={
                'db_table': 'LOCATION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolMain',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('school_name', models.CharField(blank=True, db_column='SCHOOL_NAME', max_length=200, null=True)),
                ('location', models.CharField(blank=True, db_column='LOCATION', max_length=200, null=True)),
                ('establishment', models.CharField(blank=True, db_column='ESTABLISHMENT', max_length=45, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=256, null=True)),
                ('affiliation', models.CharField(blank=True, db_column='AFFILIATION', max_length=200, null=True)),
                ('website', models.CharField(blank=True, db_column='WEBSITE', max_length=45, null=True)),
                ('school_start_time', models.TimeField(blank=True, db_column='SCHOOL_START_TIME', null=True)),
                ('school_end_time', models.TimeField(blank=True, db_column='SCHOOL_END_TIME', null=True)),
                ('address', models.CharField(blank=True, db_column='ADDRESS', max_length=256, null=True)),
                ('landline_num', models.CharField(blank=True, db_column='LANDLINE_NUM', max_length=45, null=True)),
                ('mobile_num', models.CharField(blank=True, db_column='MOBILE_NUM', max_length=45, null=True)),
                ('emailid', models.CharField(blank=True, db_column='EMAILID', max_length=45, null=True)),
                ('facilities', models.CharField(blank=True, db_column='FACILITIES', max_length=45, null=True)),
                ('profile_image', models.CharField(blank=True, db_column='PROFILE_IMAGE', max_length=100, null=True)),
                ('extra_curriculum', models.CharField(blank=True, db_column='EXTRA_CURRICULUM', max_length=45, null=True)),
                ('lastupd_dttm', models.DateTimeField(blank=True, db_column='LASTUPD_DTTM', null=True)),
            ],
            options={
                'db_table': 'SCHOOL_MAIN',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(db_column='STATE_ID', primary_key=True, serialize=False)),
                ('state_name', models.CharField(blank=True, db_column='STATE_NAME', max_length=45, null=True)),
                ('lastupd_dttm', models.DateTimeField(blank=True, db_column='LASTUPD_DTTM', null=True)),
            ],
            options={
                'db_table': 'STATE',
                'managed': False,
            },
        ),
    ]
