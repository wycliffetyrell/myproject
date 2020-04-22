from django.db import models
from django.urls import reverse

# Create your models here.
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    last_name = models.CharField(max_length=150)
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


class DashDashboardentry(models.Model):
    layout_uid = models.CharField(max_length=25)
    placeholder_uid = models.CharField(max_length=255)
    plugin_uid = models.CharField(max_length=255)
    plugin_data = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    workspace = models.ForeignKey('DashDashboardworkspace', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dash_dashboardentry'


class DashDashboardplugin(models.Model):
    plugin_uid = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'dash_dashboardplugin'


class DashDashboardpluginGroups(models.Model):
    dashboardplugin = models.ForeignKey(DashDashboardplugin, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dash_dashboardplugin_groups'
        unique_together = (('dashboardplugin', 'group'),)


class DashDashboardpluginUsers(models.Model):
    dashboardplugin = models.ForeignKey(DashDashboardplugin, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dash_dashboardplugin_users'
        unique_together = (('dashboardplugin', 'user'),)


class DashDashboardsettings(models.Model):
    layout_uid = models.CharField(max_length=25)
    title = models.CharField(max_length=255)
    is_public = models.IntegerField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    allow_different_layouts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dash_dashboardsettings'


class DashDashboardworkspace(models.Model):
    layout_uid = models.CharField(max_length=25)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=50)
    position = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField()
    is_cloneable = models.IntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dash_dashboardworkspace'
        unique_together = (('user', 'slug'), ('user', 'name'),)


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



class PriceList(models.Model):
    product_name = models.CharField(max_length=255)
    product_size = models.CharField(max_length=100)
    product_price = models.DecimalField(decimal_places=2,max_digits=100)

    class Meta:
        
        db_table = 'price_list'

class Orders(models.Model):
    user_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=255)
    order_quantity = models.CharField(max_length=100)
    order_size = models.CharField(max_length=100)
    order_type = models.CharField(max_length=100)
    order_date = models.DateTimeField()
    status = models.IntegerField()
    order_number = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'orders'        

class OrderTotalPrice(models.Model):
    user_id = models.CharField(max_length=255)
    order_total = models.DecimalField(decimal_places=2,max_digits=100)
    order_status = models.IntegerField()
    order_date = models.DateTimeField()
    order_number = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'order_total_price'


class Users(models.Model):
    user_name = models.CharField(max_length=100)
    user_apartment = models.CharField(max_length=100)
    user_contact = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'users'


def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={ 'id':self.id } )

def get_update_url(self):
        return reverse('orders-detail', kwargs={ 'id':self.id } )    

def get_orders_url(self):
        return reverse('orders-update', kwargs={ 'id':self.id } ) 

def get_productupdate_url(self):
        return reverse('product-update', kwargs={ 'id':self.id } )            
