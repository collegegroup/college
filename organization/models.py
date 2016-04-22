# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BasicCoachingCourses(models.Model):
    course_id = models.AutoField(db_column='COURSE_ID', primary_key=True)  # Field name made lowercase.
    course_name = models.CharField(db_column='COURSE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='CATEGORY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BASIC_COACHING_COURSES'


class BasicCollegeCourses(models.Model):
    course_id = models.AutoField(db_column='COURSE_ID', primary_key=True)  # Field name made lowercase.
    course_name = models.CharField(db_column='COURSE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='CATEGORY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BASIC_COLLEGE_COURSES'


class City(models.Model):
    city_id = models.AutoField(db_column='CITY_ID', primary_key=True)  # Field name made lowercase.
    city_name = models.CharField(db_column='CITY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state_name = models.CharField(db_column='STATE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CITY'


class CoachingCategory(models.Model):
    category_id = models.AutoField(db_column='CATEGORY_ID', primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='CATEGORY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COACHING_CATEGORY'


class CoachingFacilities(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    coaching_id = models.IntegerField(db_column='COACHING_ID', blank=True, null=True)  # Field name made lowercase.
    facility_name = models.CharField(db_column='FACILITY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    facility_status = models.CharField(db_column='FACILITY_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COACHING_FACILITIES'


class CoachingReview(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    institute_id = models.IntegerField(db_column='INSTITUTE_ID', blank=True, null=True)  # Field name made lowercase.
    institute_name = models.CharField(db_column='INSTITUTE_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='COURSE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fee = models.DecimalField(db_column='FEE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    year_of_batch = models.CharField(db_column='YEAR_OF_BATCH', max_length=45, blank=True, null=True)  # Field name made lowercase.
    review = models.CharField(db_column='REVIEW', max_length=250, blank=True, null=True)  # Field name made lowercase.
    faculties = models.IntegerField(db_column='FACULTIES', blank=True, null=True)  # Field name made lowercase.
    administration = models.IntegerField(db_column='ADMINISTRATION', blank=True, null=True)  # Field name made lowercase.
    alumni = models.IntegerField(db_column='ALUMNI', blank=True, null=True)  # Field name made lowercase.
    atmosphere = models.IntegerField(db_column='ATMOSPHERE', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COACHING_REVIEW'


class CollegeCategory(models.Model):
    category_id = models.AutoField(db_column='CATEGORY_ID', primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='CATEGORY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COLLEGE_CATEGORY'


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


class CollegeFacilities(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    college_id = models.IntegerField(db_column='COLLEGE_ID', blank=True, null=True)  # Field name made lowercase.
    facility_name = models.CharField(db_column='FACILITY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    facility_status = models.CharField(db_column='FACILITY_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COLLEGE_FACILITIES'


class CollegeMain(models.Model):
    college_id = models.AutoField(db_column='COLLEGE_ID', primary_key=True)  # Field name made lowercase.
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
    profile_image = models.CharField(db_column='PROFILE_IMAGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    highest_package = models.DecimalField(db_column='HIGHEST_PACKAGE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    average_package = models.DecimalField(db_column='AVERAGE_PACKAGE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COLLEGE_MAIN'


class CollegeReview(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    college_id = models.IntegerField(db_column='COLLEGE_ID', blank=True, null=True)  # Field name made lowercase.
    college_name = models.CharField(db_column='COLLEGE_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='COURSE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    entrance = models.CharField(db_column='ENTRANCE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rank = models.CharField(db_column='RANK', max_length=45, blank=True, null=True)  # Field name made lowercase.
    passout_year = models.CharField(db_column='PASSOUT_YEAR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fee = models.DecimalField(db_column='FEE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    review = models.CharField(db_column='REVIEW', max_length=250, blank=True, null=True)  # Field name made lowercase.
    faculties = models.IntegerField(db_column='FACULTIES', blank=True, null=True)  # Field name made lowercase.
    infrastructure = models.IntegerField(db_column='INFRASTRUCTURE', blank=True, null=True)  # Field name made lowercase.
    accommodation = models.IntegerField(db_column='ACCOMMODATION', blank=True, null=True)  # Field name made lowercase.
    placement = models.IntegerField(db_column='PLACEMENT', blank=True, null=True)  # Field name made lowercase.
    social_life = models.IntegerField(db_column='SOCIAL_LIFE', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COLLEGE_REVIEW'


class InstituteCourses(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    institute_id = models.IntegerField(db_column='INSTITUTE_ID', blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='COURSE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='DURATION', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fee = models.DecimalField(db_column='FEE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INSTITUTE_COURSES'


class InstituteMain(models.Model):
    institute_id = models.AutoField(db_column='INSTITUTE_ID', primary_key=True)  # Field name made lowercase.
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
    profile_image = models.CharField(db_column='PROFILE_IMAGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
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


class SchoolCurriculum(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    school_id = models.IntegerField(db_column='SCHOOL_ID', blank=True, null=True)  # Field name made lowercase.
    curriculum_name = models.CharField(db_column='CURRICULUM_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    curriculum_status = models.CharField(db_column='CURRICULUM_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCHOOL_CURRICULUM'


class SchoolFacilities(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    school_id = models.IntegerField(db_column='SCHOOL_ID', blank=True, null=True)  # Field name made lowercase.
    facility_name = models.CharField(db_column='FACILITY_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    facility_status = models.CharField(db_column='FACILITY_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCHOOL_FACILITIES'


class SchoolMain(models.Model):
    school_id = models.AutoField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
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
    profile_image = models.CharField(db_column='PROFILE_IMAGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCHOOL_MAIN'


class SchoolReview(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    school_id = models.IntegerField(db_column='SCHOOL_ID', blank=True, null=True)  # Field name made lowercase.
    state_name = models.CharField(db_column='STATE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    school_name = models.CharField(db_column='SCHOOL_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    stream = models.CharField(db_column='STREAM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    board = models.CharField(db_column='BOARD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fee = models.DecimalField(db_column='FEE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    review = models.CharField(db_column='REVIEW', max_length=250, blank=True, null=True)  # Field name made lowercase.
    faculties = models.IntegerField(db_column='FACULTIES', blank=True, null=True)  # Field name made lowercase.
    facilities = models.IntegerField(db_column='FACILITIES', blank=True, null=True)  # Field name made lowercase.
    infrastructure = models.IntegerField(db_column='INFRASTRUCTURE', blank=True, null=True)  # Field name made lowercase.
    extra_curriculum = models.IntegerField(db_column='EXTRA_CURRICULUM', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCHOOL_REVIEW'


class State(models.Model):
    state_id = models.AutoField(db_column='STATE_ID', primary_key=True)  # Field name made lowercase.
    state_name = models.CharField(db_column='STATE_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATE'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
