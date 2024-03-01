#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:19:29 2024

@author: joaocastro
"""

import pandas as pd
dados = pd.read_csv("census-income.csv" ,delimiter ="," ,header=None) # ler dados sem header

# para obter detalhes de uma função da biblioteca padrão do Python, por exemplo
# help(list)
# para obter detalhes de uma função da biblioteca Pandas, por exemplo
# help(pd.read_csv)

firstFive = dados.head(n=10)

print(firstFive)