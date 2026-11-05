# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    specific_visible_app_ids = fields.Many2many(
        'ir.ui.menu',
        'res_users_visible_menus_rel',
        'user_id', 'menu_id',
        string='Aplicações Visíveis Específicas',
        domain=[('parent_id', '=', False)],
        help="Aplicações específicas permitidas para este utilizador. Se configurado, o utilizador terá acesso estrito APENAS às aplicações aqui selecionadas, sobrepondo restrições de grupos."
    )

    allowed_app_ids = fields.Many2many(
        'ir.ui.menu',
        string='Aplicações Permitidas (Resumo)',
        compute='_compute_allowed_apps',
        help="Lista consolidada de aplicações principais que o utilizador tem permissão para visualizar."
    )

    @api.depends('groups_id.visible_app_ids', 'groups_id', 'specific_visible_app_ids')
    def _compute_allowed_apps(self):
        # Busca todos os menus raiz com sudo()
        all_main_menus = self.env['ir.ui.menu'].sudo().search([('parent_id', '=', False)])
        
        for user in self:
            # 1. Superuser raiz (ID 1 - __system__) tem sempre acesso a tudo
            if user.id == 1:
                user.allowed_app_ids = all_main_menus
                continue

            # 2. Prioridade 1: Configuração Específica do Utilizador (Override Estrito)
            # Se o administrador definiu aplicações específicas para este utilizador, respeita estritamente essa lista
            if user.specific_visible_app_ids:
                user.allowed_app_ids = user.specific_visible_app_ids
                continue

            # 3. Prioridade 2: Restrições configuradas nos Grupos do utilizador
            restricted_groups = user.groups_id.filtered(lambda g: g.visible_app_ids)
            if restricted_groups:
                user.allowed_app_ids = restricted_groups.mapped('visible_app_ids')
                continue

            # 4. Sem restrições específicas ou de grupo: exibe todas as aplicações
            user.allowed_app_ids = all_main_menus

    @api.model_create_multi
    def create(self, vals_list):
        users = super(ResUsers, self).create(vals_list)
        if any('specific_visible_app_ids' in vals or 'groups_id' in vals for vals in vals_list):
            self.env['ir.ui.menu'].clear_caches()
            self.env.registry.clear_cache()
        return users

    def write(self, vals):
        res = super(ResUsers, self).write(vals)
        if 'specific_visible_app_ids' in vals or 'groups_id' in vals:
            self.env['ir.ui.menu'].clear_caches()
            self.env.registry.clear_cache()
        return res

