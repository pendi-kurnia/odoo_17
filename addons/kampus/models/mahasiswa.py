from odoo import fields, models, _

class Mahasiswa(models.Model):
    _name = "mahasiswa"
    _description = "Mahasiswa"

    name = fields.Char(string="Nama")
    nim = fields.Char(string="NIM")
    tgl_sidang = fields.Date(string="Tgl Sidang")
