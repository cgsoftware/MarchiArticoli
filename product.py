# -*- encoding: utf-8 -*-

import netsvc
import pooler, tools
import math

from tools.translate import _

from osv import fields, osv


class product_product(osv.osv):
    _inherit = 'product.product'
    
    _columns = {
                'marchio_ids':fields.many2one('marchio.marchio', 'Marchio'),
                }

product_product()
