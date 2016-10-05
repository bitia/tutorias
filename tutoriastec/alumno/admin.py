from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from alumno.models import AlumnoUser

class AlumnoUserResource(resources.ModelResource):

    class Meta:
        model = AlumnoUser
        exclude = ('user_ptr', 'password','last_login','is_superuser',"groups", "user_permissions","is_staff", "is_active", "date_joined")
        export_order= ("id","username","first_name","last_name","carrera",
        "semestre","sexo","telefono",)

class AlumnoUserAdmin(ImportExportModelAdmin):
    resource_class = AlumnoUserResource
    search_fields = ['username']
    #firtname es igual a nombre , last name apellido , username a numero de control 
    list_display =("id","first_name","last_name","username","carrera",
        "semestre","telefono","sexo",)


admin.site.register(AlumnoUser,AlumnoUserAdmin)