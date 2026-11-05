# -*- coding: utf-8 -*-

def post_init_hook(env):
    """
    This hook sets the default visible application for the example group.
    It runs after the module is installed, ensuring that all dependencies
    and their data (like menu items) are already loaded.
    """
    # Find the example restricted group
    group = env.ref('restrict_user_discuss.group_hide_modules_user', raise_if_not_found=False)

    if group:
        # Find the Discuss app's root menu
        discuss_menu = env.ref('mail.menu_root', raise_if_not_found=False)
        if discuss_menu:
            # Set the visible_app_ids for the example group
            group.write({'visible_app_ids': [(4, discuss_menu.id)]})
