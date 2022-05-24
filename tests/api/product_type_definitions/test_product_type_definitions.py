from __future__ import absolute_import
from sp_api.api import ProductTypeDefinitions


def test_get_product_type_definitions():
    r = ProductTypeDefinitions().get_definitions_product_type(u'LEGUME')
    assert r is not None
