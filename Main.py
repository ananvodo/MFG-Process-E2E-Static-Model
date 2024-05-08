#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:12:24 2024

@author: avodopivec
"""

from Input import FileInput
from Reader import Reader
from Bioreactor import Bioreactor
from PerfusionFilter import PerfusionFilter

data = FileInput('input.json').data

bioreactor = Reader.read_no_nested_dict(data, 'Bioreactor', Bioreactor)
perfusionFilter = Reader.read_no_nested_dict(data, 'PerfusionFilter', PerfusionFilter)


# input_handler = FileInput('input.json')

# bioreactor = input_handler.instances.get('Bioreactor')

# perfusionFilter = input_handler.instances.get('PerfusionFilter')
# perfusionFilter.provide_flows(bioreactor.outFlow)

# susv1 = input_handler.instances.get('Susv1')
# susv1.provide_flows(perfusionFilter.outFlow)

# proaGuardFilter = input_handler.instances.get('ProaGuardFilter')
# proaGuardFilter.provide_flows(susv1.normalOutFlow)

# proa = input_handler.instances.get('Proa')
