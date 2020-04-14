# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, fields, api, _


class sale_order_history(models.Model):
    """ sale order histroy """
    _name = 'sale.order.history'

    original_id = fields.Many2one('sale.order', string="Sale")
    order_id = fields.Many2one('sale.order', string="Name")
    user_id = fields.Many2one('res.users', string="Revision User")


class sale_order(models.Model):
    """ sale order """
    _inherit = 'sale.order'

    sale_history_id = fields.One2many('sale.order.history', 'original_id',
                                      string="Order History")
    sale_history_count = fields.Integer(compute='_find_len')

    def _find_len(self):
        sale_history_list = [data.id for data in self.sale_history_id]
        self.sale_history_count = len(sale_history_list)

    def action_sale_revision_validate(self):
        new_sale_id = self.copy()
        active_id = self._context.get('active_id')
        uid_id = self.env.user.id
        sale_history = self.env['sale.order.history'].create(
            {'order_id': new_sale_id.id, 'user_id': uid_id,
             'original_id': self.ids[0]})
        sale_history_list = [data.id for data in self.sale_history_id]
        new_sale_id.name = self.name + ' - R' + str(len(sale_history_list))
        new_sale_id.origin = self.name

        action = \
            self.env.ref('sale.action_quotations_with_onboarding').read()[0]
        if new_sale_id:
            action['views'] = [
                (self.env.ref('sale.view_order_form').id, 'form')]
            action['res_id'] = new_sale_id.ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action

    def action_view_sale_revision(self):
        action = \
            self.env.ref('sale.action_quotations_with_onboarding').read()[0]
        sale_history_id = self.mapped('sale_history_id.order_id')
        if len(sale_history_id) > 1:
            action['domain'] = [('id', 'in', sale_history_id.ids)]
        elif sale_history_id:
            action['views'] = [
                (self.env.ref('sale.view_order_form').id, 'form')]
            action['res_id'] = sale_history_id.id
        return action

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
