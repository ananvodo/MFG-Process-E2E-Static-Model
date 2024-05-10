#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:12:24 2024

@author: avodopivec
"""

from equipment.chrom.Proa import Proa
from equipment.guard_filter.ProaGuardFilter import ProaGuardFilter
from equipment.perfusion_filter.PerfusionFilter import PerfusionFilter
from equipment.susv.ContinuousSusv import ContinuousSusv
from shared.UserInput import UserInput
from equipment.bioreactor.Bioreactor import Bioreactor


data = UserInput('input.json').data

bioreactor = Bioreactor.from_dictfile(data, 'Bioreactor')

perfusionFilter = PerfusionFilter.from_dictfile(data, 'PerfusionFilter')
perfusionFilter.provide_flows(bioreactor.outFlow)

susv1 = ContinuousSusv.from_dictfile(data, 'Susv1')
susv1.provide_flows(perfusionFilter.outFlow)

proaGuardFilter = ProaGuardFilter.from_dictfile(data, 'ProaGuardFilter')
proaGuardFilter.provide_flows(susv1.outFlow)

proa = Proa.from_dictfile(data, 'Proa')
proa.provide_flows(susv1.outFlow)
proa.calculate_steps(bioreactor.titer, susv1.flowPercentCompensation)
steps = proa.steps
