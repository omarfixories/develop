# -*- coding: utf-8 -*-

{
    'name'         : 'Odoo Academy',
    'summary'      : """Academy app to manage Training""",
    'description'  : """
        Academy app to manage Training
        -Courses
        -Sessions
        -Attendees
    """,
    'Author'       : 'Odoo',
    'website'      : 'https://www.fixories.com',
    'category'     : 'Training',
    'version'      : '0.1',
    'depends'      : ['base'],
    'data'         : [  
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'security/academy_security.xml',
        'security/ir.model.access.csv',
                     ],
    'demo'         : ['demo/academy_demo.xml'],

}