from odoo import models, fields

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    product_ids = fields.Many2many('product.product', string="Продукти")
    package_id = fields.Many2one('product.package', string="Пакет продуктів")

    def apply_package(self):
        if self.package_id:
            self.product_ids = self.package_id.product_ids