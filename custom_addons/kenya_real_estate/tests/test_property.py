from odoo.tests.common import TransactionCase

class TestEstateProperty(TransactionCase):
    def setUp(self):
        super().setUp()
        self.partner = self.env['res.partner'].create({'name': 'Test Landlord'})

    def test_create_property(self):
        prop = self.env['estate.property'].create({
            'name': 'Kilimani Apartment',
            'property_type': 'residential',
            'landlord_id': self.partner.id,
            'monthly_rent': 50000,
            'county': 'Nairobi',
        })
        self.assertEqual(prop.status, 'available')
        self.assertTrue(prop.ref.startswith('PROP/'))

    def test_lease_activates_property(self):
        prop = self.env['estate.property'].create({
            'name': 'Westlands Office',
            'property_type': 'commercial',
            'landlord_id': self.partner.id,
        })
        tenant = self.env['res.partner'].create({'name': 'Test Tenant'})
        lease = self.env['estate.lease'].create({
            'property_id': prop.id,
            'tenant_id': tenant.id,
            'date_start': '2026-01-01',
            'date_end': '2026-12-31',
        })
        lease.action_activate()
        self.assertEqual(lease.status, 'active')
        self.assertEqual(prop.status, 'leased')
