from __future__ import absolute_import
from setuptools import setup

from sp_api.__version__ import __version__

setup(
    name=u'python-amazon-sp-api',
    version=__version__,
    install_requires=[
        u"requests",
        u"six>=1.15,<2",
        u"boto3>=1.16.39,<2",
        u"cachetools==3.1.1",
        u"pytz",
        u"confuse>=1.4,<1.8"
        u"enum==0.4.7"
    ],
    packages=[u'tests', u'tests.api', u'tests.api.orders', u'tests.api.sellers', u'tests.api.finances',
              u'tests.api.product_fees', u'tests.api.notifications', u'tests.api.reports', u'tests.client',
              u'sp_api',
              u'sp_api.api',
              u'sp_api.api.orders',
              u'sp_api.api.sellers',
              u'sp_api.api.finances',
              u'sp_api.api.product_fees',
              u'sp_api.api.products',
              u'sp_api.api.feeds',
              u'sp_api.api.sales',
              u'sp_api.api.catalog',
              u'sp_api.api.notifications',
              u'sp_api.api.reports',
              u'sp_api.api.inventories',
              u'sp_api.api.messaging',
              u'sp_api.api.upload',
              u'sp_api.api.merchant_fulfillment',
              u'sp_api.api.fulfillment_inbound',
              u'sp_api.auth',
              u'sp_api.base',
              u'sp_api.util',
                ##### DO NOT DELETE ########## INSERT PACKAGE HERE #######
              u'sp_api.api.listings_restrictions',
    

              u'sp_api.api.catalog_items',
              u'sp_api.api.product_type_definitions',
              u'sp_api.api.listings_items',
              u'sp_api.api.vendor_transaction_status',
              u'sp_api.api.vendor_shipments',
              u'sp_api.api.vendor_orders',
              u'sp_api.api.vendor_invoices',
              u'sp_api.api.vendor_direct_fulfillment_transactions',
              u'sp_api.api.vendor_direct_fulfillment_shipping',
              u'sp_api.api.vendor_direct_fulfillment_payments',
              u'sp_api.api.vendor_direct_fulfillment_orders',
              u'sp_api.api.vendor_direct_fulfillment_inventory',
              u'sp_api.api.tokens',
              u'sp_api.api.solicitations',
              u'sp_api.api.shipping',
              u'sp_api.api.services',
              u'sp_api.api.fba_small_and_light',
              u'sp_api.api.fba_inbound_eligibility',
              u'sp_api.api.authorization',
              u'sp_api.api.aplus_content',
              u'sp_api.api.fulfillment_outbound',
              ],
    scripts=[u'make_endpoint/make_endpoint'],
    url=u'https://github.com/saleweaver/python-amazon-sp-api',
    license=u'MIT',
    author=u'Michael',
    author_email=u'info@saleweaver.com',
    description=u'Python wrapper for the Amazon Selling-Partner API'
)

