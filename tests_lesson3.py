import unittest
from lesson3.lesson3_hw import Film, FilmSiyahisi


class Lesson3(unittest.TestCase):
    def test_setter(self):
        f = Film("Inception", 2010, 8.8)
        with self.assertRaises(ValueError):
            f.reyting = 12
        with self.assertRaises(ValueError):
            Film("X", 2020, 15)

    def test_str(self):
        self.assertEqual(str(Film("Inception", 2010, 8.8)), "Inception (2010) ⭐ 8.8")

    def test_from_string(self):
        f = Film.from_string("Interstellar|2014|8.6")
        self.assertEqual((f.ad, f.il, f.reyting), ("Interstellar", 2014, 8.6))

    def test_siyahi(self):
        s = FilmSiyahisi()
        self.assertIsNone(s.en_yaxsi())
        s.elave_et(Film.from_string("Inception|2010|8.8"))
        s.elave_et(Film.from_string("Interstellar|2014|8.6"))
        self.assertEqual(len(s), 2)
        self.assertEqual(s.en_yaxsi().ad, "Inception")
        self.assertEqual(FilmSiyahisi().filmler, [])

    def test_bonus(self):
        self.assertEqual(Film("A", 2000, 5), Film("A", 2000, 9))
        self.assertEqual(len({Film("A", 2000, 5), Film("A", 2000, 9)}), 1)


if __name__ == "__main__":
    unittest.main()
