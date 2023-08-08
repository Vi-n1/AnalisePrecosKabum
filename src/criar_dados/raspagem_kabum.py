# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import logging


class Kabum:
    def __init__(self):
        self._log = logging.getLogger(__name__)
        self._log.debug('Raspagem inicializadaa')
        _link_placas = 'https://www.kabum.com.br/hardware/placa-de-video-vga? \
            facet_filters=&sort=most_searched&page_size=100&page_number=1'

        _cabecalho = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 \
                Safari/537.36 Edg/114.0.1823.58'
        }
        _resposta = requests.get(_link_placas, _cabecalho)
        self._pagina = BeautifulSoup(_resposta.content, features='html.parser')

    def get_placas(self) -> list:
        """
        Extrai os nomes das placas
        :return: lista contendo os nomes das placas
        """
        placas = self._pagina.find_all(
            name='span',
            class_='sc-d79c9c3f-0 hkwBHG sc-d55b419d-16 kaRfLk nameCard',
        )
        quantidade_placas = len(placas)
        if quantidade_placas == 0:
            self._log.debug('Classe de "span" não funcionando')
            self._log.debug('Falha na busca das placas')
            return []
        else:
            lista_placas = ['Placas']
            for index in range(0, quantidade_placas):
                lista_placas.append(placas[index].get_text().replace(',', ''))
            return lista_placas

    def get_links_placas(self) -> list:
        """
        Extrai os links das placas
        :return: lista contendo os links das placas
        """
        links_placas = self._pagina.find_all(
            name='a', class_='sc-d55b419d-10 bGNHzD productLink', href=True
        )
        quantidade_links = len(links_placas)
        if quantidade_links == 0:
            self._log.debug('Classe de "a" não funcionando')
            self._log.debug('Falha na busca de links')
            return []
        else:
            link_base = 'https://www.kabum.com.br'
            lista_links = ['Links placas']
            for i in range(0, quantidade_links):
                lista_links.append(link_base + links_placas[i].get('href'))
            return lista_links

    def get_links_imagens(self) -> list:
        """
        Extrai os nomes das placas
        :return: lista contendo os nomes das placas
        """
        links_imagens = self._pagina.find_all(name='img', class_='imageCard')
        quantidade_imagens = len(links_imagens)
        if quantidade_imagens == 0:
            self._log.debug('Classe de "img" não funcionando')
            self._log.debug('Falha na busca de imagens')
            return []
        else:
            lista_links_imagens = ['Links imagens']
            for index in range(0, quantidade_imagens):
                lista_links_imagens.append(links_imagens[index].get('src'))
            return lista_links_imagens

    def get_precos(self) -> list:
        """
        Extrai os preços das placas
        :return: lista contendo os preços das placas
        """
        precos = self._pagina.find_all(
            name='span', class_='sc-3b515ca1-2 gABrIj priceCard'
        )
        quantidade_precos = len(precos)
        if quantidade_precos == 0:
            self._log.debug('Classe de "span" não funcionando')
            self._log.debug('Falha na busca de preços')
            return []
        else:
            lista_precos = ['Preços']
            for index in range(0, quantidade_precos):
                lista_precos.append(precos[index].get_text().replace(' ', ' '))
            return lista_precos
