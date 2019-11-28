from django.db import models
from django.db import models


class AppJunior(models.Model):
    junior_id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.ForeignKey('Gendermaster', models.DO_NOTHING)
    sub = models.ForeignKey('AppUsermaster', models.DO_NOTHING)
    profile_pic_url = models.CharField(max_length=200, blank=True, null=True)
    overall_rating = models.DecimalField(
        max_digits=65535, decimal_places=65535)
    is_active = models.BooleanField()
    is_reco_created = models.BooleanField(blank=True, null=True)
    reco_created_at = models.DateTimeField(blank=True, null=True)
    is_reco_updated = models.BooleanField(blank=True, null=True)
    reco_updated_at = models.DateTimeField(blank=True, null=True)
    is_reco_deleted = models.BooleanField(blank=True, null=True)
    reco_deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_junior'


class AppJuniorSportPref(models.Model):
    junior = models.ForeignKey(AppJunior, models.DO_NOTHING, primary_key=True)
    sport = models.ForeignKey('Sportsmaster', models.DO_NOTHING)
    level = models.ForeignKey(
        'Levelsmaster', models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_junior_sport_pref'
        unique_together = (('junior', 'sport'),)


class AppJuniorTargetPref(models.Model):
    junior = models.ForeignKey(AppJunior, models.DO_NOTHING, primary_key=True)
    target = models.ForeignKey('Targetsmaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_junior_target_pref'
        unique_together = (('junior', 'target'),)


class AppUserSportPref(models.Model):
    sub = models.ForeignKey(
        'AppUsermaster', models.DO_NOTHING, primary_key=True)
    sport = models.ForeignKey('Sportsmaster', models.DO_NOTHING)
    level = models.ForeignKey(
        'Levelsmaster', models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_user_sport_pref'
        unique_together = (('sub', 'sport'),)


class AppUserTargetPref(models.Model):
    sub = models.ForeignKey(
        'AppUsermaster', models.DO_NOTHING, primary_key=True)
    target = models.ForeignKey('Targetsmaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_user_target_pref'
        unique_together = (('sub', 'target'),)


class AppUsermaster(models.Model):
    app_user_id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    bio = models.CharField(max_length=400, blank=True, null=True)
    user_title = models.CharField(max_length=100, blank=True, null=True)
    sub_id = models.UUIDField(unique=True)
    org = models.ForeignKey('Organizations', models.DO_NOTHING)
    gender = models.ForeignKey('Gendermaster', models.DO_NOTHING)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    profile_pic_url = models.CharField(max_length=200, blank=True, null=True)
    overall_rating = models.DecimalField(
        max_digits=65535, decimal_places=65535)
    is_event_creator = models.BooleanField()
    is_active = models.BooleanField()
    skip_user = models.ForeignKey(
        'SkipUserLogin', models.DO_NOTHING, blank=True, null=True)
    is_reco_created = models.BooleanField(blank=True, null=True)
    reco_created_at = models.DateTimeField(blank=True, null=True)
    is_reco_updated = models.BooleanField(blank=True, null=True)
    reco_updated_at = models.DateTimeField(blank=True, null=True)
    dob_reco = models.DateField(blank=True, null=True)
    pincode_reco = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_usermaster'


class AppsVersion(models.Model):
    version_id = models.UUIDField(primary_key=True)
    os = models.CharField(max_length=15)
    app_version = models.CharField(max_length=50)
    is_force_upgrade = models.BooleanField()
    version_code = models.CharField(max_length=50, blank=True, null=True)
    min_version_code = models.CharField(max_length=50, blank=True, null=True)
    min_app_version = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'apps_version'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
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


class ErrorLogTable(models.Model):
    error_id = models.UUIDField(primary_key=True)
    function_name = models.CharField(max_length=200, blank=True, null=True)
    error_code = models.CharField(max_length=200, blank=True, null=True)
    error_msg = models.CharField(max_length=500, blank=True, null=True)
    sub_id = models.UUIDField(blank=True, null=True)
    other_info = models.CharField(max_length=3000, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'error_log_table'


class EventLikes(models.Model):
    event = models.ForeignKey(
        'OmnifyEvent', models.DO_NOTHING, primary_key=True)
    sub = models.ForeignKey(AppUsermaster, models.DO_NOTHING)
    is_liked = models.BooleanField()
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'event_likes'
        unique_together = (('event', 'sub'),)


class Gendermaster(models.Model):
    gender_id = models.UUIDField(primary_key=True)
    gender_name = models.CharField(unique=True, max_length=50)
    country = models.CharField(max_length=10)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gendermaster'


class Levelsmaster(models.Model):
    level_id = models.UUIDField(primary_key=True)
    level_name = models.CharField(unique=True, max_length=30)
    country = models.CharField(max_length=10)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'levelsmaster'


class OmnifyClasses(models.Model):
    class_id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=2056)
    start_time = models.TimeField()
    end_time = models.TimeField()
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_classes'


class OmnifyClassesDaysOfWeek(models.Model):
    # Field renamed because it was a Python reserved word.
    class_field = models.ForeignKey(
        OmnifyClasses, models.DO_NOTHING, db_column='class_id', primary_key=True)
    day_of_week = models.CharField(max_length=50)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_classes_days_of_week'
        unique_together = (('class_field', 'day_of_week'),)


class OmnifyClasspack(models.Model):
    classpack_id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=2056)
    service_type = models.CharField(max_length=50)
    service_type_id = models.UUIDField()
    business_id = models.UUIDField()
    image_url = models.CharField(max_length=700, blank=True, null=True)
    timezone = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_published = models.BooleanField()
    is_disabled = models.BooleanField()
    is_deleted = models.BooleanField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    classpack_type = models.CharField(max_length=50)
    term_length = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    term_type = models.CharField(max_length=50, blank=True, null=True)
    is_autobook = models.BooleanField()
    credits = models.IntegerField(blank=True, null=True)
    is_reco_created_updated = models.BooleanField(blank=True, null=True)
    reco_created_updated_at = models.DateTimeField(blank=True, null=True)
    is_reco_deleted = models.BooleanField(blank=True, null=True)
    reco_deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_classpack'


class OmnifyClasspackAgeGroup(models.Model):
    classpack = models.ForeignKey(
        OmnifyClasspack, models.DO_NOTHING, primary_key=True)
    age_group = models.CharField(max_length=50)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_classpack_age_group'
        unique_together = (('classpack', 'age_group'),)


class OmnifyClasspackClassesMapping(models.Model):
    classpack = models.ForeignKey(
        OmnifyClasspack, models.DO_NOTHING, primary_key=True)
    # Field renamed because it was a Python reserved word.
    class_field = models.ForeignKey(
        OmnifyClasses, models.DO_NOTHING, db_column='class_id')
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_classpack_classes_mapping'
        unique_together = (('classpack', 'class_field'),)


class OmnifyClasspackLevels(models.Model):
    classpack = models.ForeignKey(
        OmnifyClasspack, models.DO_NOTHING, primary_key=True)
    level = models.ForeignKey(Levelsmaster, models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_classpack_levels'
        unique_together = (('classpack', 'level'),)


class OmnifyClasspackSports(models.Model):
    classpack = models.ForeignKey(
        OmnifyClasspack, models.DO_NOTHING, primary_key=True)
    sport = models.ForeignKey('Sportsmaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_classpack_sports'
        unique_together = (('classpack', 'sport'),)


class OmnifyClasspackTargets(models.Model):
    classpack = models.ForeignKey(
        OmnifyClasspack, models.DO_NOTHING, primary_key=True)
    target = models.ForeignKey('Targetsmaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_classpack_targets'
        unique_together = (('classpack', 'target'),)


class OmnifyEvent(models.Model):
    event_id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=2056)
    service_type = models.CharField(max_length=50)
    service_type_id = models.UUIDField()
    business_id = models.UUIDField()
    image_url = models.CharField(max_length=700, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    currency = models.CharField(max_length=20)
    min_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    max_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    timezone = models.CharField(max_length=20)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    is_published = models.BooleanField()
    is_disabled = models.BooleanField()
    is_deleted = models.BooleanField()
    total_likes = models.IntegerField()
    is_reco_created_updated = models.BooleanField(blank=True, null=True)
    reco_created_updated_at = models.DateTimeField(blank=True, null=True)
    is_reco_deleted = models.BooleanField(blank=True, null=True)
    reco_deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_event'


class OmnifyEventAgeGroup(models.Model):
    event = models.ForeignKey(OmnifyEvent, models.DO_NOTHING, primary_key=True)
    age_group = models.CharField(max_length=50)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_event_age_group'
        unique_together = (('event', 'age_group'),)


class OmnifyEventLevels(models.Model):
    event = models.ForeignKey(OmnifyEvent, models.DO_NOTHING, primary_key=True)
    level = models.ForeignKey(Levelsmaster, models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_event_levels'
        unique_together = (('event', 'level'),)


class OmnifyEventSports(models.Model):
    event = models.ForeignKey(OmnifyEvent, models.DO_NOTHING, primary_key=True)
    sport = models.ForeignKey('Sportsmaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_event_sports'
        unique_together = (('event', 'sport'),)


class OmnifyEventTargets(models.Model):
    event = models.ForeignKey(OmnifyEvent, models.DO_NOTHING, primary_key=True)
    target = models.ForeignKey('Targetsmaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_event_targets'
        unique_together = (('event', 'target'),)


class OmnifyFacility(models.Model):
    facility_category = models.ForeignKey(
        'OmnifyFacilityCategory', models.DO_NOTHING, primary_key=True)
    facility_id = models.UUIDField()
    title = models.CharField(max_length=2056)
    is_published = models.BooleanField()
    is_disabled = models.BooleanField()
    is_deleted = models.BooleanField()
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_facility'
        unique_together = (('facility_category', 'facility_id'),)


class OmnifyFacilityAgeGroup(models.Model):
    facility_category = models.ForeignKey(
        'OmnifyFacilityCategory', models.DO_NOTHING, primary_key=True)
    age_group = models.CharField(max_length=50)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_facility_age_group'
        unique_together = (('facility_category', 'age_group'),)


class OmnifyFacilityCategory(models.Model):
    facility_category_id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=2056)
    service_type = models.CharField(max_length=50)
    service_type_id = models.UUIDField()
    business_id = models.UUIDField()
    image_url = models.CharField(max_length=700, blank=True, null=True)
    timezone = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    min_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    max_price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    is_deleted = models.BooleanField()
    is_reco_created_updated = models.BooleanField(blank=True, null=True)
    reco_created_updated_at = models.DateTimeField(blank=True, null=True)
    is_reco_deleted = models.BooleanField(blank=True, null=True)
    reco_deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_facility_category'


class OmnifyFacilityLevels(models.Model):
    facility_category = models.ForeignKey(
        OmnifyFacilityCategory, models.DO_NOTHING, primary_key=True)
    level = models.ForeignKey(Levelsmaster, models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_facility_levels'
        unique_together = (('facility_category', 'level'),)


class OmnifyFacilitySports(models.Model):
    facility_category = models.ForeignKey(
        OmnifyFacilityCategory, models.DO_NOTHING, primary_key=True)
    sport = models.ForeignKey('Sportsmaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_facility_sports'
        unique_together = (('facility_category', 'sport'),)


class OmnifyFacilityTargets(models.Model):
    facility_category = models.ForeignKey(
        OmnifyFacilityCategory, models.DO_NOTHING, primary_key=True)
    target = models.ForeignKey('Targetsmaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'omnify_facility_targets'
        unique_together = (('facility_category', 'target'),)


class Organizations(models.Model):
    org_id = models.UUIDField(primary_key=True)
    status = models.ForeignKey('VerificationStatusMaster', models.DO_NOTHING)
    org_name = models.CharField(max_length=250)
    org_email = models.CharField(max_length=150)
    org_contact = models.CharField(max_length=20)
    pan_no = models.CharField(max_length=40)
    account_number = models.CharField(max_length=40)
    ifsc_code = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=200)
    territory = models.CharField(max_length=200)
    pincode = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'organizations'
        unique_together = (('org_name', 'org_email'),)


class Rolesmaster(models.Model):
    role_id = models.UUIDField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=50)
    country = models.CharField(max_length=10)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rolesmaster'


class SkipUserLogin(models.Model):
    skip_user_id = models.UUIDField(primary_key=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'skip_user_login'


class SportsAdvice(models.Model):
    sport_advice_id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    overall_rating = models.DecimalField(
        max_digits=65535, decimal_places=65535)
    img_url = models.CharField(max_length=500, blank=True, null=True)
    blog_url = models.CharField(max_length=500)
    video_url = models.CharField(max_length=500, blank=True, null=True)
    audio_url = models.CharField(max_length=500, blank=True, null=True)
    reading_time = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(
        'SportsAdviceCategoryMaster', models.DO_NOTHING)
    gender = models.ForeignKey(Gendermaster, models.DO_NOTHING)
    source_type = models.ForeignKey(
        'SportsAdviceSourceTypeMaster', models.DO_NOTHING)
    seasonality = models.ForeignKey(
        'SportsAdviceSeasonalityMaster', models.DO_NOTHING)
    total_bookmarks = models.IntegerField()
    total_likes = models.IntegerField()
    total_comments = models.IntegerField()
    bounce_rate = models.DecimalField(max_digits=65535, decimal_places=65535)
    avg_time_spent = models.IntegerField(blank=True, null=True)
    page_view = models.IntegerField(blank=True, null=True)
    sphere_id = models.UUIDField(blank=True, null=True)
    sphere_created_date = models.DateTimeField(blank=True, null=True)
    sphere_updated_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sports_advice'


class SportsAdviceCategoryMaster(models.Model):
    category_id = models.UUIDField(primary_key=True)
    category_name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sports_advice_category_master'


class SportsAdviceLikesBookmarks(models.Model):
    sport_advice = models.ForeignKey(
        SportsAdvice, models.DO_NOTHING, primary_key=True)
    sub = models.ForeignKey(AppUsermaster, models.DO_NOTHING)
    is_liked = models.BooleanField(blank=True, null=True)
    is_bookmarked = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sports_advice_likes_bookmarks'
        unique_together = (('sport_advice', 'sub'),)


class SportsAdviceSeasonalityMaster(models.Model):
    seasonality_id = models.UUIDField(primary_key=True)
    seasonality_name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sports_advice_seasonality_master'


class SportsAdviceSourceTypeMaster(models.Model):
    source_type_id = models.UUIDField(primary_key=True)
    source_type_name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sports_advice_source_type_master'


class SportsAdviceSportLevelAssociation(models.Model):
    sport_advice = models.ForeignKey(
        SportsAdvice, models.DO_NOTHING, primary_key=True)
    sport = models.ForeignKey('Sportsmaster', models.DO_NOTHING)
    level = models.ForeignKey(Levelsmaster, models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sports_advice_sport_level_association'
        unique_together = (('sport_advice', 'sport'),)


class SportsAdviceTarget(models.Model):
    sport_advice = models.ForeignKey(
        SportsAdvice, models.DO_NOTHING, primary_key=True)
    target = models.ForeignKey('Targetsmaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sports_advice_target'
        unique_together = (('sport_advice', 'target'),)


class SportsAdviceTopic(models.Model):
    sport_advice = models.ForeignKey(
        SportsAdvice, models.DO_NOTHING, primary_key=True)
    topic = models.ForeignKey('SportsAdviceTopicMaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sports_advice_topic'
        unique_together = (('sport_advice', 'topic'),)


class SportsAdviceTopicMaster(models.Model):
    topic_id = models.UUIDField(primary_key=True)
    topic_name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sports_advice_topic_master'


class Sportsmaster(models.Model):
    sport_id = models.UUIDField(primary_key=True)
    master_sport_id = models.IntegerField(blank=True, null=True)
    sport_name = models.CharField(max_length=150)
    sport_group_name = models.CharField(max_length=50, blank=True, null=True)
    sport_category = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.CharField(max_length=400)
    country = models.CharField(max_length=10)
    is_system_created = models.BooleanField()
    status = models.ForeignKey('VerificationStatusMaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sportsmaster'


class Targetsmaster(models.Model):
    target_id = models.UUIDField(primary_key=True)
    target_name = models.CharField(max_length=50)
    country = models.CharField(max_length=10)
    is_system_created = models.BooleanField()
    status = models.ForeignKey('VerificationStatusMaster', models.DO_NOTHING)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'targetsmaster'


class Taxmaster(models.Model):
    tax_id = models.UUIDField(primary_key=True)
    tax_name = models.CharField(unique=True, max_length=50)
    tax_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    country = models.CharField(max_length=10)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'taxmaster'

class VerificationStatusMaster(models.Model):
    status_id = models.UUIDField(primary_key=True)
    status_name = models.CharField(unique=True, max_length=60)
    country = models.CharField(max_length=10)
    is_active = models.BooleanField()
    created_by = models.UUIDField()
    created_at = models.DateTimeField()
    updated_by = models.UUIDField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'verification_status_master'

# Create your models here.
class contentId(models.Model):
    typeId = models.IntegerField(primary_key=True)
    classtype = models.CharField(max_length=100,default="")
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    key = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name
    
class Templates(models.Model):
    id = models.IntegerField(primary_key=True)
    typeof = models.CharField(max_length=20)
    sportbtn = models.TextField()
    location = models.TextField()
    userid = models.TextField()
    check = models.TextField(default="")
    submit = models.TextField()

class Selection(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    keyId = models.CharField(max_length=100)
    location = models.BooleanField()
    check = models.BooleanField(default=False)
    url = models.TextField()
    endpoint = models.CharField(max_length=200,default="")
    notAvailable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    