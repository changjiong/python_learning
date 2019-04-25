from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Dbear'
    site_title = '小熊的宝宝站'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')