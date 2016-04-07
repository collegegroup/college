# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class City(models.Model):
    city_id = models.IntegerField(db_column='CITY_ID', primary_key=True)  # Field name made lowercase.
    city_name = models.CharField(db_column='CITY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state_id = models.IntegerField(db_column='STATE_ID', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CITY'


class CollegeCourses(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    college_id = models.IntegerField(db_column='COLLEGE_ID', blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='COURSE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='DURATION', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fee = models.DecimalField(db_column='FEE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    entrance = models.CharField(db_column='ENTRANCE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COLLEGE_COURSES'


class CollegeMain(models.Model):
    college_id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    college_name = models.CharField(db_column='COLLEGE_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    establishment = models.CharField(db_column='ESTABLISHMENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=256, blank=True, null=True)  # Field name made lowercase.
    affiliation = models.CharField(db_column='AFFILIATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='WEBSITE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=256, blank=True, null=True)  # Field name made lowercase.
    landline_num = models.CharField(db_column='LANDLINE_NUM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobile_num = models.CharField(db_column='MOBILE_NUM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    facilities = models.CharField(db_column='FACILITIES', max_length=2, blank=True, null=True)  # Field name made lowercase.
    profile_image = models.ImageField(db_column='PROFILE_IMAGE', upload_to="profiles/college/")  # Field name made lowercase.
    highest_package = models.DecimalField(db_column='HIGHEST_PACKAGE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    average_package = models.DecimalField(db_column='AVERAGE_PACKAGE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COLLEGE_MAIN'


class InstituteCourses(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    college_id = models.IntegerField(db_column='COLLEGE_ID', blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='COURSE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='DURATION', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fee = models.DecimalField(db_column='FEE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INSTITUTE_COURSES'


class InstituteMain(models.Model):
    institute_id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    institute_name = models.CharField(db_column='INSTITUTE_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    director_name = models.CharField(db_column='DIRECTOR_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    establishment = models.CharField(db_column='ESTABLISHMENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=256, blank=True, null=True)  # Field name made lowercase.
    affiliation = models.CharField(db_column='AFFILIATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='WEBSITE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=256, blank=True, null=True)  # Field name made lowercase.
    landline_num = models.CharField(db_column='LANDLINE_NUM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobile_num = models.CharField(db_column='MOBILE_NUM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    facilities = models.CharField(db_column='FACILITIES', max_length=2, blank=True, null=True)  # Field name made lowercase.
    profile_image = models.ImageField(db_column='PROFILE_IMAGE', upload_to="profiles/coaching/")  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INSTITUTE_MAIN'


class Location(models.Model):
    location_id = models.AutoField(db_column='LOCATION_ID', primary_key=True)  # Field name made lowercase.
    state_name = models.CharField(db_column='STATE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city_name = models.CharField(db_column='CITY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sub_city = models.CharField(db_column='SUB_CITY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pin_code = models.CharField(db_column='PIN_CODE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION'


class SchoolMain(models.Model):
    school_id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school_name = models.CharField(db_column='SCHOOL_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    establishment = models.CharField(db_column='ESTABLISHMENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=256, blank=True, null=True)  # Field name made lowercase.
    affiliation = models.CharField(db_column='AFFILIATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='WEBSITE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    school_start_time = models.TimeField(db_column='SCHOOL_START_TIME', blank=True, null=True)  # Field name made lowercase.
    school_end_time = models.TimeField(db_column='SCHOOL_END_TIME', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=256, blank=True, null=True)  # Field name made lowercase.
    landline_num = models.CharField(db_column='LANDLINE_NUM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobile_num = models.CharField(db_column='MOBILE_NUM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    facilities = models.CharField(db_column='FACILITIES', max_length=45, blank=True, null=True)  # Field name made lowercase.
    profile_image = models.ImageField(db_column='PROFILE_IMAGE', upload_to="profiles/coaching/")  # Field name made lowercase.
    extra_curriculum = models.CharField(db_column='EXTRA_CURRICULUM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCHOOL_MAIN'


class State(models.Model):
    state_id = models.AutoField(db_column='STATE_ID', primary_key=True)  # Field name made lowercase.
    state_name = models.CharField(db_column='STATE_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATE'




