from dataclasses import field
from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

# Define Class of models and fields


class koordinator_renstra(models.Model):
    # define the name of model and the descrption
    _name = 'renstra.koordinator'
    _inherit = ['mail.thread']
    _description = 'Data Model koordinator renstra FT'

    # define fields for name
    name = fields.Char('Nama Lengkap', required=True)

    # define field for NIP
    nip = fields.Char('NIP', required=True)

    # define Fields for email
    email = fields.Char('E-mail', help='Masukan Email Univeritas Valid')

    # define fields for user Id using many 2 one relation
    user_id = fields.Many2one(
        comodel_name='renstra.koordinator', string='user_ID', track_visibility='onchange')
    id_number = fields.Char(string='ID Number', track_visibility='onchange')
    id_user = fields.Many2one(comodel_name='res.users', string='User ID')

    # define key and value of jabatan koordinator for selection fields
    list_jabatan = [('koor_penalaranFT', 'Koordinator Kemahasiswaan Bidang Penalaran Fakultas Teknik'), ('koor_kemahasiswaanFT', 'Koordinator Bidang Kemahasiswaan FT'),
                    ('koor_TA_industri', 'Koordinator Tugas Akhir Teknik Industri'), (
                        'koor_TA_elektro', 'Koordinator Tugas Akhir Teknik Elektro'),
                    ('koor_biro_radio_FT', 'Koordinator Biro Radio FT'), ('koor_kerjasama_FT',
                                                                          'Koordinator Kerjasama FT'), ('koor_penelitian', 'Koordinator Bidang Penelitian dan Pengabdian FT'),
                    ('koor_jurnal_FT', 'Koordinator Bidang Penerbitan Jurnal FT'), ('koor_student_service_FT',
                                                                                    'Koordinator Bidang Student Service Center FT'), ('koor_data_info_FT', 'Koordinator Bidang Data dan Informasi FT'),
                    ('koor_TA_biomedis', 'Koordinator Tugas Akhir Biomedis'), ('koor_tim_kreatif',
                                                                               'Koordinator Tim Kreatif'), ('koor_angka_kredit', 'Koordinator Penilai Angka Kredit'),
                    ('koor_KP_FT', 'Koordinator Kerja Praktek FT'), ('koor_lab_biomedis',
                                                                     'Koordinator Lab Keilmuan Teknik Biomedis'), ('koor_lab_industri', 'Koordinator Lab Keilmuan Teknik Industri'),
                    ('koor_lab_elektro', 'Koordinator Lab Keilmuan Teknik Elektro'), ('koor_lab_kerjasama', 'Koordinator Lab Kerjasama Industri'), ('koor_lab_riset', 'Koordinator Lab Riset')]

    # create fields selection of koordinator from list_jabatan
    jabatan = fields.Selection(
        string='Jabatan', selection=list_jabatan, required=True)

    # Define key and value of progdi for selection fields of progdi
    list_progdi = [('industri', 'Teknik Industri'), 
                   ('biomedis', 'Teknik Biomedis'), 
                   ('elektro', 'Teknik Elektro')]

    program_studi = fields.Selection(
        string='Program Studi', selection=list_progdi, required=False)

    # create  user_id  and id number using sequence_id
    @api.model
    def create(self, vals):
        vals['id_number'] = self.env['ir.sequence'].next_by_code(
            'renstra.koordinator')
        groups = self.env['res.groups'].search(
            [('name', '=', vals['jabatan'])], limit=1)
        groups_id = groups.id
        new_user = {
            'password': 'DinusPolke',
            'login': vals['nip'],
            'name': vals['name'],
            'email': vals['email'],
            'groups_id': [(6, 0, [groups_id])]
        }
        user = self.env['res.users'].search([('login', '=', vals['nip'])])
        if user:
            raise UserError(("Pengguna dengan NIP ini sudah ada"))
        else:
            new_user = self.env['res.users'].create(new_user)
            vals.update({'id_user': new_user.id})
        res = super(koordinator_renstra, self).create(vals)
        return res

    # @api.model
    # def create(self, vals):
    #     vals['id_number'] = self.env['ir.sequence'].next_by_code(
    #         'renstra.koordinator')
    #     groups = self.env['res.groups'].search(
    #         [('name', '=', vals['jabatan'])], limit=1)
    #     groups_id = groups,
    #     new_user = {
    #         'password': 'DinusPolke',
    #         'login': vals['nip'],
    #         'name': vals['name'],
    #         'email': vals['email'],
    #         'groups': groups_id
    #     }
    #     user = self.env['res.users'].search([('login', '=', vals['nip'])])
    #     if user:
    #         raise UserError(("Pengguna dengan NIP ini sudah ada"))
    #     else:
    #         new_user = self.env['res.users'].create(new_user)
    #         vals.update({'id_user': new_user.id})
    #     res = super(koordinator_renstra, self).create(vals)
    #     return super(koordinator_renstra, self).create(vals)