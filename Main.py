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
from Proa import Proa
from ChromStep import ProaBufferStep
from Column import ProaSbmColumn
from ChromResin import ProaChromResin
from Susv import ContinuousSusv
from GuardFilter import GuardFilter


data = FileInput('input.json').data

bioreactor = Reader.read_no_nested_dict(data, 'Bioreactor', Bioreactor)

perfusionFilter = Reader.read_no_nested_dict(data, 'PerfusionFilter', PerfusionFilter)
perfusionFilter.provide_flows(bioreactor.outFlow)

susv1 = Reader.read_no_nested_dict(data, 'Susv1', ContinuousSusv)
susv1.provide_flows(perfusionFilter.outFlow)

proaGuardFilter = Reader.read_no_nested_dict(data, 'ProaGuardFilter', GuardFilter)
proaGuardFilter.provide_flows(susv1.outFlow)

proa = Reader.read_proa(data, 'Proa')
proa.provide_flows(susv1.outFlow, susv1.flowPercentCompensation)
proa.calculate_steps(bioreactor.titer)
steps = proa.steps[1]
resin = proa.resin
column = proa.column
print(steps)
