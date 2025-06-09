{
    'name': "CRM Product Extension",
    'version': '1.0',
    'category': 'Sales',
    'summary': "Додавання продуктів у CRM",
    'author': "Максим",
    'depends': ['crm', 'product', 'base'],
    'data': [
        'views/crm_lead_views.xml',
        'views/product_package_views.xml',
    ],
    'installable': True,
    'application': False,
}