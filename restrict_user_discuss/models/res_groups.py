# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResGroups(models.Model):
    _inherit = 'res.groups'

    visible_app_ids = fields.Many2many(
        'ir.ui.menu',
        string='Visible Applications',
        domain=[('parent_id', '=', False)],
        help="Select which applications should remain visible for users in this group. "
             "If any apps are selected, all other main apps will be hidden."
    )

    @api.model_create_multi
    def create(self, vals_list):
        groups = super(ResGroups, self).create(vals_list)
        if any(k in vals for vals in vals_list for k in ('visible_app_ids', 'users', 'user_ids')):
            if hasattr(self.env['ir.ui.menu'], 'clear_caches'):
                self.env['ir.ui.menu'].clear_caches()
            if hasattr(self.env.registry, 'clear_cache'):
                self.env.registry.clear_cache()
        return groups

    def write(self, vals):
        res = super(ResGroups, self).write(vals)
        if any(k in vals for k in ('visible_app_ids', 'users', 'user_ids')):
            if hasattr(self.env['ir.ui.menu'], 'clear_caches'):
                self.env['ir.ui.menu'].clear_caches()
            if hasattr(self.env.registry, 'clear_cache'):
                self.env.registry.clear_cache()
        return res
