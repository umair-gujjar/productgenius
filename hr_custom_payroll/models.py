# -*- coding: utf-8 -*-

from openerp import models, fields, api
class hr_custom_contract(models.Model):
	_inherit = 'hr.contract'
	bonus = fields.Float('Bonus')
	loan_and_advance = fields.Float('Loan & Advance')
	medical_opd = fields.Float('Bonus')
	mobile = fields.Float('Mobile')
	fuel_other = fields.Float('Fuel/others')
	overtime_food = fields.Float('Overtime/Food')
	sr_other = fields.Float('SR/other')
