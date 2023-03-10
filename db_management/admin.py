from django.contrib import admin
from django.apps import apps

post_models = apps.get_app_config('db_management').get_models()

for model in post_models:
    admin.site.register(model)
