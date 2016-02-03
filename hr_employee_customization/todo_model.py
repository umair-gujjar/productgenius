# -*- coding: utf-8 -*-

from openerp import models,fields

class Newform(models.Model):
	_name= 'new.form'
	name = fields.Char('Description',required=True)
	is_done = fields.Boolean('Done?')
	active = fields.Boolean('Active?',default=True)

