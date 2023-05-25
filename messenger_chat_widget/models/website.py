
from odoo import fields, models


class Website(models.Model):

    _inherit = "website"

    enable_messenger = fields.Boolean("Enable Messenger",
                                      help="Enable for show page id")
    fb_id_page = fields.Char(
        "Page Id", help="To add facebook")
