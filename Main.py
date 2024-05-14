#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:12:24 2024

@author: avodopivec
"""

from equipment.Bioreactor import Bioreactor
from equipment.GuardFilterDiscr import GuardFilterDiscr
from equipment.PerfusionFilter import PerfusionFilter
from equipment.Proa import Proa
from equipment.SusvDiscr import SusvDiscr
from process_params.BioreactorParams import BioreactorParams
from process_params.GuardFilterParams import GuardFilterParams
from process_params.PerfusionFilterParams import PerfusionFilterParams
from process_params.ProaParams import ProaParams
from process_params.SusvDiscrParams import SusvDiscrParams
from shared.UserInput import UserInput


data = UserInput('input.json').data

# Getting all the parameters from the input file
bioreactorParams = BioreactorParams.from_dictfile(data, 'Bioreactor')
perfusionFilterParams = PerfusionFilterParams.from_dictfile(
    data, 'PerfusionFilter')
susv1Params = SusvDiscrParams.from_dictfile(data, 'Susv1')
proaGuardFilterParams = GuardFilterParams.from_dictfile(
    data, 'ProaGuardFilter')
proaParams = ProaParams.from_dictfile(data, 'Proa')

# Getting the data from the parameters
bioreactor = Bioreactor.from_params(
    bioreactorParams=bioreactorParams
)
perfusionFilter = PerfusionFilter.from_params(
    bioreactor=bioreactor,
    perfusionFilterParams=perfusionFilterParams
)
susv1 = SusvDiscr.from_params(
    susvDiscrParams=susv1Params,
    perfusionFilter=perfusionFilter,
)

proaGuardFilter = GuardFilterDiscr.from_params(
    guardFilterDiscrParams=proaGuardFilterParams,
    susvDiscr=susv1
)

proa = Proa.from_params(
    proaParams=proaParams
)
proa.calculate_loading(
    proaParams=proaParams,
    susvDiscr=susv1,
    bioreactorParams=bioreactorParams
)
print(proa)
