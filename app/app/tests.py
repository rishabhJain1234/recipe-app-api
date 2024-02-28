from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numebers(self):
        res=calc.add(3,8)
        self.assertEqual(res,11)