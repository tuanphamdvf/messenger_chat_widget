
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """
    Inheriting fields into settings
    """
    _inherit = 'res.config.settings'

    enable_messenger = fields.Boolean("Enable Messenger",
                                      related="website_id.enable_messenger",
                                      help="Enable for show page id field",
                                      readonly=False)
    fb_id_page = fields.Char("Facebook Page Id",
                             related="website_id.fb_id_page",
                             help="To add facebook page id", readonly=False)
