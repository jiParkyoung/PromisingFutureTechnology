# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Stopwords(models.Model):
    stopword = models.CharField(primary_key=True,max_length=20000)

    class Meta:
        managed = False
        db_table = 'stopwords'


class Table1(models.Model):
    column1 = models.CharField(max_length=20000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table1'


class Thesis(models.Model):
    title = models.CharField(primary_key=True, max_length=2000)
    searchq = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    word2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thesis'
    
class Total(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sentence = models.TextField( max_length=10000)
    title = models.CharField(max_length=10000)
    label = models.BigIntegerField()
    key = models.TextField()
    year = models.CharField(max_length=1000)    
    percentage = models.FloatField()
    class Meta:
        managed = False
        db_table = 'total'
        
class ThesisUse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=1280, blank=True, null=True)
    year = models.CharField(max_length=1000)   
    month = models.CharField(max_length=1000)   
    use =models.CharField(max_length=1000)   

    class Meta:
        managed = False
        db_table = 'thesis_use'
        

class link(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=2000, blank=True, null=True)
    URL= models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LINK'
        
        
class market(models.Model):
    key = models.CharField(max_length=200, blank=True, null=True,primary_key=True)
    contents= models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MARKETABILITY'

