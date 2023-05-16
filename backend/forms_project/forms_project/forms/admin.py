
from django.contrib import admin
from django.db import models
from forms_project.utils.inspector import Inspector

all_models = Inspector.get_classes('forms_project.forms.models', base_class=models.Model)
all_models = [c for c in all_models if 'django.' not in c.__module__]
for cls in all_models:
    admin.site.register(cls)
    
