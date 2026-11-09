# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    specific_visible_app_ids = fields.Many2many(
        'ir.ui.menu',
        'res_users_visible_menus_rel',
        'user_id', 'menu_id',
        string='Specific Visible Applications',
        domain=[('parent_id', '=', False)],
        help="Specific apps allowed for this user, in addition to those from their groups."
    )

    allowed_app_ids = fields.Many2many(
        'ir.ui.menu',
        string='Allowed Applications',
        compute='_compute_allowed_apps',
        help="Aggregated list of applications the user is allowed to see based on their groups and specific selection."
    )

    @api.depends('groups_id.visible_app_ids', 'groups_id', 'specific_visible_app_ids')
    def _compute_allowed_apps(self):
        all_main_menus = self.env['ir.ui.menu'].sudo().search([('parent_id', '=', False)])

        for user in self:
            # 1. Root Superuser (ID 1 - __system__) always retains full unrestricted access
            if user.id == 1:
                user.allowed_app_ids = all_main_menus
                continue

            # 2. Priority 1: Individual User Specific Configuration (Strict Override)
            if user.specific_visible_app_ids:
                user.allowed_app_ids = user.specific_visible_app_ids
                continue

            # 3. Priority 2: Restrictions configured on the user's Security Groups
            user_groups = getattr(user, 'groups_id', self.env['res.groups'])
            restricted_groups = user_groups.filtered(lambda g: g.visible_app_ids)
            if restricted_groups:
                user.allowed_app_ids = restricted_groups.mapped('visible_app_ids')
                continue

            # 4. No specific or group restrictions: display all root applications
            user.allowed_app_ids = all_main_menus

    @api.model_create_multi
    def create(self, vals_list):
        users = super(ResUsers, self).create(vals_list)
        if any(k in vals for vals in vals_list for k in ('specific_visible_app_ids', 'groups_id', 'group_ids')):
            if hasattr(self.env['ir.ui.menu'], 'clear_caches'):
                self.env['ir.ui.menu'].clear_caches()
            if hasattr(self.env.registry, 'clear_cache'):
                self.env.registry.clear_cache()
        return users

    def write(self, vals):
        res = super(ResUsers, self).write(vals)
        if any(k in vals for k in ('specific_visible_app_ids', 'groups_id', 'group_ids')):
            if hasattr(self.env['ir.ui.menu'], 'clear_caches'):
                self.env['ir.ui.menu'].clear_caches()
            if hasattr(self.env.registry, 'clear_cache'):
                self.env.registry.clear_cache()
        return res
