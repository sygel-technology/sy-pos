import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-sygel-technology-sy-pos",
    description="Meta package for sygel-technology-sy-pos Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-pos_lot_selection',
        'odoo14-addon-pos_refund',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
