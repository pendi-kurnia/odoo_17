{
    'name': 'Kampus',
    'version': '1.0',
    'summary': 'Modul uji coba untuk memastikan bisa terbaca di Odoo',
    'author': 'Pendi Kurnia',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
         'security/ir.model.access.csv',
         'views/mahasiswa_view.xml',
         'views/mahasiswa_menu.xml',

    ],
    'installable': True,
    'application': True,
}