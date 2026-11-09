# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID


def post_init_hook(env_or_cr, registry=None):
    """
    Sets the default visible application for the example restricted group.
    Supports both Odoo 15.0/16.0 (cr, registry) and Odoo 17.0+ (env) hook signatures.
    """
    env = env_or_cr if hasattr(env_or_cr, 'ref') else api.Environment(env_or_cr, SUPERUSER_ID, {})

    group = env.ref('restrict_user_discuss.group_hide_modules_user', raise_if_not_found=False)
    if group:
        discuss_menu = env.ref('mail.menu_root', raise_if_not_found=False)
        if discuss_menu:
            group.write({'visible_app_ids': [(4, discuss_menu.id)]})
