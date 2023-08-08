# -*- coding: utf-8 -*-
"""
Cria pastas para armazenar posteriormente os dados.
"""
from os import path, mkdir
from pathlib import Path


DIR_DADOS = str(Path('../src/dados'))
if not path.exists(DIR_DADOS):
    mkdir(DIR_DADOS)
    mkdir(DIR_DADOS + '/csv')
    mkdir(DIR_DADOS + '/excel')
