import unittest
import json

from synsets_extraction import alt_gen

class SyncSetTest(unittest.TestCase):
    
    def test_sample(self):
        file = open('datatest/6.json')
        input = alt_gen('ahad', file)
        file.close()
        output = [['ahad', 'minggu'], ['ahad', 'esa', 'satu', 'tunggal']]
        self.assertEqual(input, output, '\nresult: {}\nexpected: {}'.format(input, output))

    def test_sample2(self):
        file = open('datatest/2.json')
        input = alt_gen('setanggi', file)
        file.close()
        output = [[]]
        self.assertEqual(input, output, '\nresult: {}\nexpected: {}'.format(input, output))

    def test_sample3(self):
        file = open('datatest/3.json')
        input = alt_gen('aborsi', file)
        file.close()
        output = [['aborsi', 'pengguguran']]
        self.assertEqual(input, output, '\nresult: {}\nexpected: {}'.format(input, output))

    def test_sample4(self):
        file = open('datatest/4.json')
        input = alt_gen('pekan', file)
        file.close()
        output = [['pasar','pekan', 'rekan'], ['minggu', 'pekan']]
        self.assertEqual(input, output, '\nresult: {}\nexpected: {}'.format(input, output))

    def test_sample5(self):
        file = open('datatest/5.json')
        input = alt_gen('lebu', file)
        file.close()
        output = [['peleraian','perbaikan', 'perdamaian']]
        self.assertEqual(input, output, '\nresult: {}\nexpected: {}'.format(input, output))

    def test_sample6(self):
        file = open('datatest/21.json')
        input = alt_gen('abu', file)
        file.close()
        output = [['abu', 'abuk']]
        self.assertEqual(input, output, '\nresult: {}\nexpected: {}'.format(input, output))

if __name__ == '__main__':
    unittest.main()
