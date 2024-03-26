import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')
        
    def test_laataminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 20.00 euroa')

    def test_saldo_vähenee_oikein_jos_rahaa_on_tarpeeksi_ottaa(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 9.00 euroa')

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi_ottaa(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')

    def test_ota_rahaa_palautusarvo_toimii_oikein(self):        
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)

    def test_saldo_euroina(self):
        self.assertAlmostEqual(self.maksukortti.saldo_euroina(), 10)
