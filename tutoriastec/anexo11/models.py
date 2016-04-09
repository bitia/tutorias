from __future__ import unicode_literals

from django.db import models
class OrganizacionEstudio(models.Model):
    usuario = models.OneToOneField(User,blank=True, null= True, on_delete=models.CASCADE)

    opc_asertividad=(
        ('1','Si'),
        ('0','No'),
        )
    pregunta1=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta2=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta3=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta4=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas") 
    pregunta5=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta6=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta7=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta8=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas") 
    pregunta9=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta10=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta11=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta12=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta13=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta14=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas") 
    pregunta15=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta16=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta17=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta18=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas") 
    pregunta19=models.CharField(choices=opc_asertividad,default ='0',
            blank=False,max_length=2,verbose_name="preguntas")
    pregunta20=models.CharField(choices=opc_asertividad,default ='0',s
            blank=False,max_length=2,verbose_name="preguntas")

    DIAGNOSTICO_OPC=(
        ('0','Muy bajo'),
        ('1','bajo'),
        ('2','Por debajo del promedio'),
        ('3','Promedio bajo'),
        ('4','Promedio'),
        ('5','Promedio alto'),
        ('6','Por encima del promedio'),
        ('7','alto'),
        ('8','muy alto'),
        )
    diagnostico=models.CharField(choices=DIAGNOSTICO_OPC,
            blank=True,max_length=2)


    def __unicode__(self):
        return "%s "% (self.usuario.username)

# Create your models here.
