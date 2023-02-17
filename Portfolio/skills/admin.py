from django.contrib import admin
from skills.models import Skills
# Register your models here.
class SkillsAdmin(admin.ModelAdmin):
    list_display=('skillName','onSite','skillExp')

admin.site.register(Skills,SkillsAdmin)