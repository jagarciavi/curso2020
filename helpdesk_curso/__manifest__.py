# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "HelpDesk Curso",
    "summary":
        "Module to Support Teams",
    "version": "13.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "José Antonio García Vicente <jantonio.garcia@iriego.es>",
    "license": "AGPL-3",
    "depends": [
        'base',
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "wizards/helpdesk_set_responsable_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_team_views.xml",
        "views/helpdesk_ticket_stage_views.xml",
        "views/res_users_views.xml",
    ],
    "application": True,
    "installable": True,
}
