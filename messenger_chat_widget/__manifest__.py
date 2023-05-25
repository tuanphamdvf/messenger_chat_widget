# -*- coding: utf-8 -*-
{
    'name': "Messenger Chat Widget",
    "summary": "An application that allows you to connect with Messenger and easily configure it so that your customers can chat directly on your website.",
    'description': """An application that allows you to connect with Messenger and easily configure it so that your customers can chat directly on your website.!!
    """,
    "price": "0",
    "currency": "EUR",
    'license': 'GPL-3',
    'author': "TTN SOFTWARE",
    'website': "TTNSOFTWARE.STORE",
    'version': '15.1.1',
    'category': 'App',
    'depends': ['base', 'website', 'website_sale'],

    'data': [
        'views/custome_template.xml',
        'views/floating_chat_widget.xml',
        # 'views/custome_template.xml',
        #  'views/floating_chat_widget.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'messenger_chat_widget/static/src/xml/*',
        ],
        'web.assets_backend': [
            'messenger_chat_widget/static/src/components/**/*',
            'messenger_chat_widget/static/src/scss/**/*',
            'messenger_chat_widget/static/lib/*',
            'messenger_chat_widget/static/src/js/**/*',
        ],

    },
    'images': ['static/img/main_screenshot.gif']
}
