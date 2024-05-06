#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:12:24 2024

@author: avodopivec
"""
from Bioreactor import Bioreactor
from PerfusionFilter import PerfusionFilter
from Input import Input

input_handler = Input.fromFile('input.json')
bioreactor = input_handler.instances.get('Bioreactor')
perfusionFilter = input_handler.instances.get('PerfusionFilter')


# bioreactor = Bioreactor(prodDays, titer, brxVol, vvd, bleedPercent)
# perfusionFilter = PerfusionFilter(innerDiam, length, surfaceArea, targetShearRate, brxProdOutFlow)
