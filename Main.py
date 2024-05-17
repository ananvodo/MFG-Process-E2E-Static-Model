#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:12:24 2024

@author: avodopivec
"""

from equipment.DepthFilterDiscr import DepthFilterDiscr
from equipment.PolishStep1 import PolishStep1
from equipment.Vi import Vi
from equipment.Bioreactor import Bioreactor
from equipment.GuardFilterDiscr import GuardFilterDiscr
from equipment.PerfusionFilter import PerfusionFilter
from equipment.Proa import Proa
from equipment.SusvDiscr import SusvDiscr
from process_params.ChromParams import ChromParams
from process_params.DepthFilterParams import DepthFilterParams
from process_params.ViParams import ViParams
from process_params.BioreactorParams import BioreactorParams
from process_params.GuardFilterParams import GuardFilterParams
from process_params.PerfusionFilterParams import PerfusionFilterParams
from process_params.SusvDiscrParams import SusvDiscrParams
from shared.UserInput import UserInput


data = UserInput('input.json').data

# -------------------------------------------------------------------------------------------------
# Getting all the parameters from the input file
# -------------------------------------------------------------------------------------------------

bioreactorParams = BioreactorParams.from_dictfile(data, 'Bioreactor')

perfusionFilterParams = PerfusionFilterParams.from_dictfile(
    data, 'PerfusionFilter')

susv1Params = SusvDiscrParams.from_dictfile(data, 'Susv1')

proaGuardFilterParams = GuardFilterParams.from_dictfile(
    data, 'ProaGuardFilter')

proaParams = ChromParams.from_dictfile(data, 'Proa')

viParams = ViParams.from_dictfile(data, 'VI')

susv2Params = SusvDiscrParams.from_dictfile(data, 'Susv2')

df1Params = DepthFilterParams.from_dictfile(data, 'DF1')

df1GuardFilterParams = GuardFilterParams.from_dictfile(
    data, 'Df1GuardFilter')

susv3Params = SusvDiscrParams.from_dictfile(data, 'Susv3')

ps1Params = ChromParams.from_dictfile(data, 'Ps1')

# -------------------------------------------------------------------------------------------------
# Getting the data from the parameters
# -------------------------------------------------------------------------------------------------

bioreactor = Bioreactor.from_params(
    bioreactorParams=bioreactorParams
)

perfusionFilter = PerfusionFilter.from_params(
    bioreactor=bioreactor,
    perfusionFilterParams=perfusionFilterParams
)

susv1 = SusvDiscr.from_params(
    susvDiscrParams=susv1Params,
    prevEquipment=perfusionFilter,
)

proaGuardFilter = GuardFilterDiscr.from_params(
    guardFilterDiscrParams=proaGuardFilterParams,
    prevEquipment=susv1
)

proa = Proa.from_params(
    chromParams=proaParams
)

proa.calculate_loading(
    chromParams=proaParams,
    prevEquipment=susv1,
)

vi = Vi.from_params(
    viParams=viParams,
    proa=proa,
    bioreactorParams=bioreactorParams
)

susv2 = SusvDiscr.from_params(
    susvDiscrParams=susv2Params,
    prevEquipment=vi,
)

df1 = DepthFilterDiscr.from_params(
    depthFilterParams=df1Params,
    bioreactorParams=bioreactorParams,
    susvDiscr=susv2
)

df1GuardFilter = GuardFilterDiscr.from_params(
    guardFilterDiscrParams=df1GuardFilterParams,
    prevEquipment=df1
)

ps1 = PolishStep1.from_params(
    chromParams=ps1Params
)

ps1.calculate_loading(
    chromParams=ps1Params,
    prevEquipment=df1GuardFilter
)

print(ps1)
