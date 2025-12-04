from odoo import models, fields, api


class proyecto(models.Model):
    _name = 'gestor_proyectos.proyecto'
    _description = 'Clase para definir proyectos'

    nombre=fields.Char(string = 'nombre del proyecto', required=True)
    descripcion=fields.Char(string = 'descripcion del proyecto')
    
    fechaInicio=fields.Date(string = 'inicio del proyecto')
    fechaFin=fields.Date(string = 'fin del proyecto')

    responsable=fields.Char(string = 'responsable del proyecto')
    porcentajeAvance=fields.Float(string= 'porcentaje de progreso')

