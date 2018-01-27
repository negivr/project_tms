# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accidents(models.Model):
    accident_id = models.AutoField(primary_key=True)
    nature = models.CharField(max_length=50)
    injured = models.CharField(max_length=50)
    dead = models.CharField(max_length=50)
    note = models.CharField(max_length=150, blank=True, null=True)
    driver = models.ForeignKey('People', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accidents'


class AccountsUser(models.Model):
    user_ptr = models.ForeignKey('AuthUser', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'accounts_user'


class Addresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip = models.PositiveIntegerField()
    note = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


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
    username = models.CharField(unique=True, max_length=150)
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


class Corporations(models.Model):
    corp_id = models.AutoField(primary_key=True)
    corp_name = models.CharField(max_length=30)
    fein = models.CharField(unique=True, max_length=10)
    owner = models.ForeignKey('People', models.DO_NOTHING)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corporations'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Employers(models.Model):
    employer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, blank=True, null=True)
    fax = models.CharField(max_length=12, blank=True, null=True)
    contact_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employers'


class Employments(models.Model):
    employment_id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(Employers, models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    position = models.CharField(max_length=30, blank=True, null=True)
    reason_for_leaving = models.CharField(max_length=30)
    dot_regulated = models.IntegerField()
    part_of = models.IntegerField()
    driver = models.ForeignKey('People', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employments'


class Endorsments(models.Model):
    endorsment_id = models.AutoField(primary_key=True)
    endorsment = models.CharField(max_length=20, blank=True, null=True)
    lic = models.ForeignKey('Licenses', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endorsments'


class Licenses(models.Model):
    license_id = models.AutoField(primary_key=True)
    l_num = models.CharField(max_length=20)
    l_type = models.CharField(max_length=30, blank=True, null=True)
    l_state = models.CharField(max_length=2)
    l_class = models.CharField(max_length=2)
    expiration_date = models.DateField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'licenses'
        unique_together = (('l_num', 'l_state'),)


class People(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField()
    ssn = models.CharField(unique=True, max_length=11)

    class Meta:
        managed = False
        db_table = 'people'


class PeopleAddresses(models.Model):
    pa_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(People, models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people_addresses'


class PeopleLicenses(models.Model):
    pl_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(People, models.DO_NOTHING, blank=True, null=True)
    license = models.ForeignKey(Licenses, models.DO_NOTHING, blank=True, null=True)
    expiration_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'people_licenses'


class VehicleOwnerships(models.Model):
    ownership_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(People, models.DO_NOTHING, blank=True, null=True)
    corporation = models.ForeignKey(Corporations, models.DO_NOTHING, blank=True, null=True)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    vehicle_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_ownerships'


class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vin_number = models.CharField(max_length=17, blank=True, null=True)
    make = models.CharField(max_length=15, blank=True, null=True)
    model = models.CharField(max_length=15, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    vehicle_type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'vehicles'


class Violations(models.Model):
    violation_id = models.AutoField(primary_key=True)
    charge = models.CharField(max_length=100)
    v_date = models.DateField()
    state = models.CharField(max_length=2)
    note = models.CharField(max_length=150, blank=True, null=True)
    driver = models.ForeignKey(People, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'violations'
