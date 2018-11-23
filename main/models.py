from django.db import models


class Decade(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_decade'


class Film(models.Model):
    fid = models.CharField(max_length=255)
    actor = models.CharField(max_length=255, blank=True, null=True)
    cate_log_name = models.CharField(max_length=255)
    cate_log_id = models.ForeignKey('CateLog', on_delete=models.CASCADE, related_name='films')
    evaluation = models.FloatField()
    image = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.IntegerField()
    loc_name = models.CharField(max_length=255, blank=True, null=True)
    loc_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    on_decade = models.CharField(max_length=255, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sub_class_name = models.CharField(max_length=255, blank=True, null=True)
    sub_class_id = models.CharField(max_length=255, blank=True, null=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    is_vip = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_film'


class Level(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_level'


class Loc(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_loc'


class Raty(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    en_time = models.CharField(max_length=255, blank=True, null=True)
    film_id = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_raty'


class Res(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    episodes = models.IntegerField()
    is_use = models.IntegerField()
    link = models.TextField(blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    film_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_res'


class ResCopy1(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    episodes = models.IntegerField()
    is_use = models.IntegerField()
    link = models.TextField(blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    film_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_res_copy1'


class SubClass(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_subclass'


class TType(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    subclass = models.ForeignKey(SubClass, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 't_type'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    is_vip = models.BigIntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    passwd = models.CharField(max_length=255, blank=True, null=True)
    is_manager = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_user'


class VipCode(models.Model):
    id = models.CharField(primary_key=True, max_length=225)
    code = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    expire_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 't_vipcode'


class VipCodeCopy1(models.Model):
    id = models.CharField(primary_key=True, max_length=225)
    code = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    expire_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 't_vipcode_copy1'


class CateLog(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_cate_log'
