# Restrict User Applications & Menu Access Control (`restrict_user_discuss`)

![Version](https://img.shields.io/badge/Odoo-15.0%20%7C%2016.0%20%7C%2017.0%20%7C%2018.0%20%7C%2019.0%20%7C%2020.0-875A7B.svg?style=flat-square)
![License](https://img.shields.io/badge/License-OPL--1-blue.svg?style=flat-square)
![Author](https://img.shields.io/badge/Author-DIGITALUB%20ANGOLA-1259C3.svg?style=flat-square)

Enterprise-grade application and root menu visibility control for **Odoo 15.0, 16.0, 17.0, 18.0, 19.0 & 20.0 (Community & Enterprise)**. Eliminate menu clutter and enforce strict workspace boundaries per security group or individual user without restarting the Odoo server.

---

## Key Features

1. **Role-Based Security Group Whitelisting (`visible_app_ids`)**
   - Configure which root applications are visible directly inside any Odoo Security Group (`Settings -> Users & Companies -> Groups`).
   - Users belonging to multiple restricted groups automatically receive the combined union of allowed applications.
2. **Strict Individual User Override (`specific_visible_app_ids`)**
   - Assign specific applications directly on the User Form (`Settings -> Users & Companies -> Users`) to strictly override group-level visibility rules.
   - Real-time computed summary (`allowed_app_ids`) displays the exact effective applications for each user.
3. **Dedicated Technical Support Profile**
   - Grant support technicians access to **Settings** while keeping the **Apps Store** (`base.menu_management`) menu hidden.
4. **Superuser Anti-Lockout Protection**
   - Odoo Superuser (`ID 1`) and system administrators automatically retain full access to prevent accidental lockouts.
5. **Instant Menu Cache Invalidation**
   - Automatically triggers `ir.ui.menu.clear_caches()` on save so menu changes take effect on the user's very next page refresh.

---

## Priority Hierarchy

1. **Priority 0 (Bypass):** Superuser (`ID 1`) -> Always sees 100% of installed applications.
2. **Priority 1 (Strict Override):** If `specific_visible_app_ids` is filled on the User profile -> User sees **only** those selected applications.
3. **Priority 2 (Group Restriction):** If the user belongs to restricted Security Groups -> User sees the combined union of `visible_app_ids` across their groups.

---

## Technical Information

- **Technical Name:** `restrict_user_discuss`
- **Supported Versions:** `15.0` • `16.0` • `17.0` • `18.0` • `19.0` • `20.0`
- **Price:** `$29.00 USD`
- **Support:** `suporte@digitalub.ao` | [https://www.digitalub.ao](https://www.digitalub.ao)
