from odoo import fields, models, _

class Mahasiswa(models.Model):
    _name = "mahasiswa"
    _description = "Mahasiswa"

    image = fields.Binary()
    name = fields.Char(string="Nama")
    nim = fields.Char(string="NIM")
    tgl_sidang = fields.Date(string="Tgl Sidang")
    state = fields.Selection([('waiting','Waiting'),('success','Success'),('fail','Fail'),],default='waiting',string='Status')

    def button_success(self):
        self.state="success"

    def button_fail(self):
        self.state="fail"
