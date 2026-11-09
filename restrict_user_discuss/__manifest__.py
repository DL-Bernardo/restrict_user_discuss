# -*- coding: utf-8 -*-
{
    'name': 'Restrict User Applications & Menu Access Control',
    'version': '18.0.2.1.1',
    'summary': 'Role-Based & User-Specific Application Visibility, Menu Restriction & Instant Cache Refresh',
    'description': """
        Enterprise-Grade Application & Root Menu Visibility Control for Odoo Community & Enterprise.
        - Role-Based Application Whitelisting per Security Group (visible_app_ids).
        - Strict Individual User Override (specific_visible_app_ids) with top priority.
        - Dedicated Technical Support Profile (grant Settings access while hiding the Apps Store menu).
        - Built-in Superuser (ID 1) anti-lockout protection.
        - Instant ORM menu cache invalidation (ir.ui.menu.clear_caches) with zero server restart.
    """,
    'author': 'DIGITALUB ANGOLA, LDA',
    'website': 'https://www.digitalub.ao',
    'support': 'suporte@digitalub.ao',
    'category': 'Extra Tools',
    'license': 'OPL-1',

    # Commercial Pricing for Odoo Apps Store
    'price': 29.0,
    'currency': 'USD',

    # Module Dependencies
    'depends': [
        'base',
        'mail',
    ],

    # Data & Views loaded on installation
    'data': [
        'security/user_groups.xml',
        'views/res_groups_views.xml',
        'views/res_users_views.xml',
        'views/hide_menus.xml',
    ],

    'images': [
        'static/description/banner.png',
        'static/description/step1_group_apps.png',
        'static/description/step2_user_override.png',
        'static/description/step3_clean_menu.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'post_init_hook': 'post_init_hook',
}
