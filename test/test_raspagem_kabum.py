import sys
import logging

sys.path.insert(0, '../src/criar_dados/')
from unittest import TestCase, main
from raspagem_kabum import Kabum

logging.basicConfig(
    level=logging.DEBUG,
    encoding='utf-8',
    filename='log.txt',
    filemode='w',
    format='%(asctime)s :: %(name)s :: %(levelname)s :: %(lineno)d :: %(message)s',
)


class TestsRaspagem(TestCase):
    def setUp(self):
        self.raspagem = Kabum()

    def test_get_placas(self):
        self.assertNotEqual(len(self.raspagem.get_placas()), 0)

    def test_get_links(self):
        self.assertNotEqual(len(self.raspagem.get_links_placas()), 0)

    def test_get_links_imagens(self):
        self.assertNotEqual(len(self.raspagem.get_links_imagens()), 0)

    def test_get_precos(self):
        self.assertNotEqual(len(self.raspagem.get_precos()), 0)


if __name__ == '__main__':
    main()
