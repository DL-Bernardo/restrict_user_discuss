# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResGroups(models.Model):
    _inherit = 'res.groups'

    visible_app_ids = fields.Many2many(
        'ir.ui.menu',
        string='Aplicações Visíveis',
        domain=[('parent_id', '=', False)],
        help="Selecione quais as aplicações principais que devem ficar visíveis para os utilizadores deste grupo. "
             "Se alguma aplicação for selecionada, todas as outras aplicações principais ficarão ocultas para este grupo."
    )

    @api.model_create_multi
    def create(self, vals_list):
        groups = super(ResGroups, self).create(vals_list)
        if any('visible_app_ids' in vals or 'users' in vals for vals in vals_list):
            self.env['ir.ui.menu'].clear_caches()
            self.env.registry.clear_cache()
        return groups

    def write(self, vals):
        res = super(ResGroups, self).write(vals)
        if 'visible_app_ids' in vals or 'users' in vals:
            self.env['ir.ui.menu'].clear_caches()
            self.env.registry.clear_cache()
        return res

