from odoo import models, fields, api

class autor(models.Model):
    _name = 'libreria_b.autor'
    _description = 'Descripcion del modulo del autor'
    # Define que el campo "nombre" será el que se muestre en visitas Many2one/Many2many
    _rec_name = 'nombre'

    nombre = fields.Char(string="Autor",required=True)

    libros_ids = fields.Many2many("libreria_b.libro",string="Libros")
