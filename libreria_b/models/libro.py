from odoo import models, fields, api

class libro(models.Model):
     _name = 'libreria_b.libro'
     _description = 'libreria_b.libro'
     autores_id = fields.Many2many("libreria_b.autor",string="Autores")
     
     portada=fields.Image(max_width=100, max_height=100)
     # Campo tipo string (obligatorio)
     title = fields.Char(string='Titulo del Libro')
     # Campo tipo entero
     pages = fields.Integer(string='Número de Páginas',required=True)
     # Campo tipo float
     price = fields.Float(String='Precio',digits=(10,2),help='Precio del libro en euros')
     # Campo tipo booleano
     is_available = fields.Boolean(string='¿Disponible?',default=True)
     # Campo tipo fecha
     publicacion_date = fields.Date(String='Fecha de Publicacion')
     # Campo tipo fecha y hora
     created_datetime = fields.Date(string='Fecha y hora de registro',default=fields.Datetime.now)
     
     days_since_publication = fields.Integer(
          string="Días desde publicación",
          compute="_compute_days_since_publication",
          store=False
     )
     #depende del campo publicacion_date
     @api.depends('publicacion_date')
     def _compute_days_since_publication(self):
          for record in self:
               if record.publicacion_date:
                    delta = date.today() - record.publicacion_date
                    record.days_since_publication = delta.days
               else:
                    record.days_since_publication = 0
     
     #autores_ids = fields.Many2many

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text(string='Descripcion del libro',required=Trues)

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

