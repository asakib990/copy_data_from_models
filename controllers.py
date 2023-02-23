# -*- coding: utf-8 -*-
from odoo import http


class ApiModule(http.Controller):
    @http.route('/api/new', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):

        contacts = http.request.env['res.partner'].sudo().search([]) # here res.partner is the model trageted model to copy data

        for contact in contacts:

            http.request.env['api.control'].sudo().create({         # here api.control is the model where data will be paste
                'name': contact.name,
                'email': contact.email,
                'phone': contact.phone,
                'website': contact.website
            })

        return kw

