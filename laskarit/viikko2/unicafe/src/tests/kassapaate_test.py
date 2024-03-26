import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassaPaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_rahamaara_ja_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 0)

    def test_riittava_kateisella_maksu_toimii_oikein_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertAlmostEqual(self.kassapaate.edulliset, 1)
        self.assertAlmostEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_riittava_kateisella_maksu_toimii_oikein_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 1)
        self.assertAlmostEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kateismaksu_ei_ole_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_kateismaksu_ei_ole_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 0)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
   
    def test_edullinen_jos_kortilla_on_tarpeeksi_rahaa_veloitetaan_kortilta_ja_palautetaan_True_lounaiden_maara_kasvaa_kassan_rahamaara_ei_muutu(self):
        kortti = Maksukortti(500)
        kortti_maksu = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertAlmostEqual(kortti.saldo, 260)
        self.assertAlmostEqual(kortti_maksu, True)
        self.assertAlmostEqual(self.kassapaate.edulliset, 1)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_jos_kortilla_ei_ole_tarpeeksi_rahaa_ei_veloiteta_palautetaan_False_lounaiden_maara_ei_muutu(self):
        kortti = Maksukortti(100)
        kortti_maksu = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertAlmostEqual(kortti.saldo, 100)
        self.assertAlmostEqual(kortti_maksu, False)
        self.assertAlmostEqual(self.kassapaate.edulliset,0)

    def test_maukas_jos_kortilla_on_tarpeeksi_rahaa_veloitetaan_kortilta_ja_palautetaan_True_lounaiden_maara_kasvaakassan_rahamaara_ei_muutu(self):
        kortti = Maksukortti(500)
        kortti_maksu = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertAlmostEqual(kortti.saldo, 100)
        self.assertAlmostEqual(kortti_maksu, True)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 1)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_jos_kortilla_ei_ole_tarpeeksi_rahaa_ei_veloiteta_palautetaan_False_lounaiden_maara_ei_muutu(self):
        kortti = Maksukortti(100)
        kortti_maksu = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertAlmostEqual(kortti.saldo, 100)
        self.assertAlmostEqual(kortti_maksu, False)
        self.assertAlmostEqual(self.kassapaate.maukkaat,0)

    def test_rahan_lataaminen_korttiin(self):
        kortti= Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertAlmostEqual(kortti.saldo, 200)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_korttiin_lataaminen_negatiivisella_summalla(self):
        kortti= Maksukortti(100)
        lataus = self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertAlmostEqual(lataus, None)
        self.assertAlmostEqual(kortti.saldo, 100)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_saldo_euroina(self):
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
