import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikaa_ottaminen_palauttaa_kaiken_mita_on(self):
        self.varasto.lisaa_varastoon(2)
        saatu = self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(saatu, 2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liikaa_laittaminen_laittaa_tilavuuden_verran(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_saldo_teksti_on_oikein(self):
        saatu = self.varasto.__str__()
        self.assertEqual(saatu, "saldo = 0, vielä tilaa 10")

    def test_negatiivinen_lisäys_ei_onnistu(self):
        varasto = Varasto(10, -5)
        self.assertEqual(varasto.saldo, 0)

        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_negatiivinen_ottaminen_ei_onnistu(self):
        saatu = self.varasto.ota_varastosta(-10)
        self.assertEqual(saatu, 0)

    def test_negatiivinen_tilavuus_ei_onnistu(self):
        varasto = Varasto(-10)
        self.assertEqual(varasto.tilavuus, 0)
