from django.contrib import admin
from .models import PragatishilModel,PepTalksUserModel,AriettaUserModel,DebateUserModel,LiterarryUserModel,PratibimbaUserModel,RongmilantiUserModel,TechonicsUserModel

class PragatishilAdmin(admin.ModelAdmin):
    fields = ('name','email','admission_year','your_department','contact_number','description')
admin.site.register(PragatishilModel, PragatishilAdmin)

class PEPAdmin(admin.ModelAdmin):
    fields = ('name','email','admission_year','your_department','contact_number','description')
admin.site.register(PepTalksUserModel, PEPAdmin)

class AriettaAdmin(admin.ModelAdmin):
    fields = ('name','email','admission_year','your_department','contact_number','description')
admin.site.register(AriettaUserModel, AriettaAdmin)

class DebateAdmin(admin.ModelAdmin):
    fields = ('name','email','admission_year','your_department','contact_number','description')
admin.site.register(DebateUserModel, DebateAdmin)

class LiterarryAdmin(admin.ModelAdmin):
    fields = ('name','email','admission_year','your_department','contact_number','description')
admin.site.register(LiterarryUserModel, LiterarryAdmin)

class PratibimbaAdmin(admin.ModelAdmin):
    fields = ('name','email','admission_year','your_department','contact_number','description')
admin.site.register(PratibimbaUserModel, PratibimbaAdmin)

class RongmilantiAdmin(admin.ModelAdmin):
    fields = ('name','email','admission_year','your_department','contact_number','description')
admin.site.register(RongmilantiUserModel, RongmilantiAdmin)

class TechonicsAdmin(admin.ModelAdmin):
    fields = ('name','email','admission_year','your_department','contact_number','description')
admin.site.register(TechonicsUserModel, TechonicsAdmin)