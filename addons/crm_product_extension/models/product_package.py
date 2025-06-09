from odoo import models, fields

class ProductPackage(models.Model):
    _name = 'product.package'
    _description = "Пакети продуктів"

    name = fields.Char(string="Назва пакету", required=True)
    product_ids = fields.Many2many('product.product', string="Продукти в пакеті")