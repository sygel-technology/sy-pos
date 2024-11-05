import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-pos",
    description="Meta package for sygel-technology-sy-pos Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-pos_discount_per_line>=15.0dev,<15.1dev',
        'odoo-addon-pos_partner_vat_required>=15.0dev,<15.1dev',
        'odoo-addon-pos_receipt_employee_name>=15.0dev,<15.1dev',
        'odoo-addon-pos_refund_order_pricelist>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
