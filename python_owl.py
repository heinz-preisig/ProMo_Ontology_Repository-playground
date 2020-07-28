

#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 Ontology design facility
===============================================================================

This program is part of the ProcessModelling suite

"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "16.09.2019"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "5.04"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"


import sys
import os

ProMo_path = os.path.join("../../","ProcessModeller_v7_04")



root = os.path.abspath(ProMo_path)      #os.path.join("../../"{{ProMo}}) #ProcessModeller_v7_04"))

ext = [root, os.path.join(root, 'packages'), \
             os.path.join(root, 'tasks'), \
             os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration')
       ]
# print(os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration'))

# emmo = "/home/heinz/1_Gits/ProcessModeller/ProcessModeller_v7_04/packages/OntologyBuilder/EMMO_Integration/"

sys.path.extend(ext)
from emmo_attach import ProMoOwlOntology
from Common.ontology_container import OntologyContainer

from owlready2 import *

ontology = OntologyContainer("flash_03") #'flash_03')


variables = ontology.vars

name = "play"
owlfile = name+".owl"

# onto  = O.setup_ontology(name)
o = ProMoOwlOntology()
onto = o.setupOnto()

V_1 = onto.VAR( "V_1" )
units = variables[1]["units"].asList()
V_1.time = [ units[0] ]
V_1.length = [ units[1] ]
V_1.amount = [ units[2] ]
V_1.mass = [ units[3] ]
V_1.temperature = [ units[4] ]
V_1.current = [ units[5] ]
V_1.light = [ units[6] ]

V_2 = onto.VAR( "V_2" )
units = variables[2]["units"].asList()
V_2.time = [ units[0] ]
V_2.length = [ units[1] ]
V_2.amount = [ units[2] ]
V_2.mass = [ units[3] ]
V_2.temperature = [ units[4] ]
V_2.current = [ units[5] ]
V_2.light = [ units[6] ]

V_5 = onto.VAR( "V_5" )
units = variables[5]["units"].asList()
V_5.time = [ units[0] ]
V_5.length = [ units[1] ]
V_5.amount = [ units[2] ]
V_5.mass = [ units[3] ]
V_5.temperature = [ units[4] ]
V_5.current = [ units[5] ]
V_5.light = [ units[6] ]

V_6 = onto.VAR( "V_6" )
units = variables[6]["units"].asList()
V_6.time = [ units[0] ]
V_6.length = [ units[1] ]
V_6.amount = [ units[2] ]
V_6.mass = [ units[3] ]
V_6.temperature = [ units[4] ]
V_6.current = [ units[5] ]
V_6.light = [ units[6] ]

V_7 = onto.VAR( "V_7" )
units = variables[7]["units"].asList()
V_7.time = [ units[0] ]
V_7.length = [ units[1] ]
V_7.amount = [ units[2] ]
V_7.mass = [ units[3] ]
V_7.temperature = [ units[4] ]
V_7.current = [ units[5] ]
V_7.light = [ units[6] ]

V_8 = onto.VAR( "V_8" )
units = variables[8]["units"].asList()
V_8.time = [ units[0] ]
V_8.length = [ units[1] ]
V_8.amount = [ units[2] ]
V_8.mass = [ units[3] ]
V_8.temperature = [ units[4] ]
V_8.current = [ units[5] ]
V_8.light = [ units[6] ]

V_9 = onto.VAR( "V_9" )
units = variables[9]["units"].asList()
V_9.time = [ units[0] ]
V_9.length = [ units[1] ]
V_9.amount = [ units[2] ]
V_9.mass = [ units[3] ]
V_9.temperature = [ units[4] ]
V_9.current = [ units[5] ]
V_9.light = [ units[6] ]

V_10 = onto.VAR( "V_10" )
units = variables[10]["units"].asList()
V_10.time = [ units[0] ]
V_10.length = [ units[1] ]
V_10.amount = [ units[2] ]
V_10.mass = [ units[3] ]
V_10.temperature = [ units[4] ]
V_10.current = [ units[5] ]
V_10.light = [ units[6] ]

V_11 = onto.VAR( "V_11" )
units = variables[11]["units"].asList()
V_11.time = [ units[0] ]
V_11.length = [ units[1] ]
V_11.amount = [ units[2] ]
V_11.mass = [ units[3] ]
V_11.temperature = [ units[4] ]
V_11.current = [ units[5] ]
V_11.light = [ units[6] ]

V_12 = onto.VAR( "V_12" )
units = variables[12]["units"].asList()
V_12.time = [ units[0] ]
V_12.length = [ units[1] ]
V_12.amount = [ units[2] ]
V_12.mass = [ units[3] ]
V_12.temperature = [ units[4] ]
V_12.current = [ units[5] ]
V_12.light = [ units[6] ]

V_13 = onto.VAR( "V_13" )
units = variables[13]["units"].asList()
V_13.time = [ units[0] ]
V_13.length = [ units[1] ]
V_13.amount = [ units[2] ]
V_13.mass = [ units[3] ]
V_13.temperature = [ units[4] ]
V_13.current = [ units[5] ]
V_13.light = [ units[6] ]

V_14 = onto.VAR( "V_14" )
units = variables[14]["units"].asList()
V_14.time = [ units[0] ]
V_14.length = [ units[1] ]
V_14.amount = [ units[2] ]
V_14.mass = [ units[3] ]
V_14.temperature = [ units[4] ]
V_14.current = [ units[5] ]
V_14.light = [ units[6] ]

V_15 = onto.VAR( "V_15" )
units = variables[15]["units"].asList()
V_15.time = [ units[0] ]
V_15.length = [ units[1] ]
V_15.amount = [ units[2] ]
V_15.mass = [ units[3] ]
V_15.temperature = [ units[4] ]
V_15.current = [ units[5] ]
V_15.light = [ units[6] ]

V_17 = onto.VAR( "V_17" )
units = variables[17]["units"].asList()
V_17.time = [ units[0] ]
V_17.length = [ units[1] ]
V_17.amount = [ units[2] ]
V_17.mass = [ units[3] ]
V_17.temperature = [ units[4] ]
V_17.current = [ units[5] ]
V_17.light = [ units[6] ]

V_18 = onto.VAR( "V_18" )
units = variables[18]["units"].asList()
V_18.time = [ units[0] ]
V_18.length = [ units[1] ]
V_18.amount = [ units[2] ]
V_18.mass = [ units[3] ]
V_18.temperature = [ units[4] ]
V_18.current = [ units[5] ]
V_18.light = [ units[6] ]

V_20 = onto.VAR( "V_20" )
units = variables[20]["units"].asList()
V_20.time = [ units[0] ]
V_20.length = [ units[1] ]
V_20.amount = [ units[2] ]
V_20.mass = [ units[3] ]
V_20.temperature = [ units[4] ]
V_20.current = [ units[5] ]
V_20.light = [ units[6] ]

V_21 = onto.VAR( "V_21" )
units = variables[21]["units"].asList()
V_21.time = [ units[0] ]
V_21.length = [ units[1] ]
V_21.amount = [ units[2] ]
V_21.mass = [ units[3] ]
V_21.temperature = [ units[4] ]
V_21.current = [ units[5] ]
V_21.light = [ units[6] ]

V_22 = onto.VAR( "V_22" )
units = variables[22]["units"].asList()
V_22.time = [ units[0] ]
V_22.length = [ units[1] ]
V_22.amount = [ units[2] ]
V_22.mass = [ units[3] ]
V_22.temperature = [ units[4] ]
V_22.current = [ units[5] ]
V_22.light = [ units[6] ]

V_26 = onto.VAR( "V_26" )
units = variables[26]["units"].asList()
V_26.time = [ units[0] ]
V_26.length = [ units[1] ]
V_26.amount = [ units[2] ]
V_26.mass = [ units[3] ]
V_26.temperature = [ units[4] ]
V_26.current = [ units[5] ]
V_26.light = [ units[6] ]

V_30 = onto.VAR( "V_30" )
units = variables[30]["units"].asList()
V_30.time = [ units[0] ]
V_30.length = [ units[1] ]
V_30.amount = [ units[2] ]
V_30.mass = [ units[3] ]
V_30.temperature = [ units[4] ]
V_30.current = [ units[5] ]
V_30.light = [ units[6] ]

V_31 = onto.VAR( "V_31" )
units = variables[31]["units"].asList()
V_31.time = [ units[0] ]
V_31.length = [ units[1] ]
V_31.amount = [ units[2] ]
V_31.mass = [ units[3] ]
V_31.temperature = [ units[4] ]
V_31.current = [ units[5] ]
V_31.light = [ units[6] ]

V_41 = onto.VAR( "V_41" )
units = variables[41]["units"].asList()
V_41.time = [ units[0] ]
V_41.length = [ units[1] ]
V_41.amount = [ units[2] ]
V_41.mass = [ units[3] ]
V_41.temperature = [ units[4] ]
V_41.current = [ units[5] ]
V_41.light = [ units[6] ]

V_45 = onto.VAR( "V_45" )
units = variables[45]["units"].asList()
V_45.time = [ units[0] ]
V_45.length = [ units[1] ]
V_45.amount = [ units[2] ]
V_45.mass = [ units[3] ]
V_45.temperature = [ units[4] ]
V_45.current = [ units[5] ]
V_45.light = [ units[6] ]

V_46 = onto.VAR( "V_46" )
units = variables[46]["units"].asList()
V_46.time = [ units[0] ]
V_46.length = [ units[1] ]
V_46.amount = [ units[2] ]
V_46.mass = [ units[3] ]
V_46.temperature = [ units[4] ]
V_46.current = [ units[5] ]
V_46.light = [ units[6] ]

V_49 = onto.VAR( "V_49" )
units = variables[49]["units"].asList()
V_49.time = [ units[0] ]
V_49.length = [ units[1] ]
V_49.amount = [ units[2] ]
V_49.mass = [ units[3] ]
V_49.temperature = [ units[4] ]
V_49.current = [ units[5] ]
V_49.light = [ units[6] ]

V_54 = onto.VAR( "V_54" )
units = variables[54]["units"].asList()
V_54.time = [ units[0] ]
V_54.length = [ units[1] ]
V_54.amount = [ units[2] ]
V_54.mass = [ units[3] ]
V_54.temperature = [ units[4] ]
V_54.current = [ units[5] ]
V_54.light = [ units[6] ]

V_56 = onto.VAR( "V_56" )
units = variables[56]["units"].asList()
V_56.time = [ units[0] ]
V_56.length = [ units[1] ]
V_56.amount = [ units[2] ]
V_56.mass = [ units[3] ]
V_56.temperature = [ units[4] ]
V_56.current = [ units[5] ]
V_56.light = [ units[6] ]

V_57 = onto.VAR( "V_57" )
units = variables[57]["units"].asList()
V_57.time = [ units[0] ]
V_57.length = [ units[1] ]
V_57.amount = [ units[2] ]
V_57.mass = [ units[3] ]
V_57.temperature = [ units[4] ]
V_57.current = [ units[5] ]
V_57.light = [ units[6] ]

V_58 = onto.VAR( "V_58" )
units = variables[58]["units"].asList()
V_58.time = [ units[0] ]
V_58.length = [ units[1] ]
V_58.amount = [ units[2] ]
V_58.mass = [ units[3] ]
V_58.temperature = [ units[4] ]
V_58.current = [ units[5] ]
V_58.light = [ units[6] ]

V_59 = onto.VAR( "V_59" )
units = variables[59]["units"].asList()
V_59.time = [ units[0] ]
V_59.length = [ units[1] ]
V_59.amount = [ units[2] ]
V_59.mass = [ units[3] ]
V_59.temperature = [ units[4] ]
V_59.current = [ units[5] ]
V_59.light = [ units[6] ]

V_60 = onto.VAR( "V_60" )
units = variables[60]["units"].asList()
V_60.time = [ units[0] ]
V_60.length = [ units[1] ]
V_60.amount = [ units[2] ]
V_60.mass = [ units[3] ]
V_60.temperature = [ units[4] ]
V_60.current = [ units[5] ]
V_60.light = [ units[6] ]

V_61 = onto.VAR( "V_61" )
units = variables[61]["units"].asList()
V_61.time = [ units[0] ]
V_61.length = [ units[1] ]
V_61.amount = [ units[2] ]
V_61.mass = [ units[3] ]
V_61.temperature = [ units[4] ]
V_61.current = [ units[5] ]
V_61.light = [ units[6] ]

V_62 = onto.VAR( "V_62" )
units = variables[62]["units"].asList()
V_62.time = [ units[0] ]
V_62.length = [ units[1] ]
V_62.amount = [ units[2] ]
V_62.mass = [ units[3] ]
V_62.temperature = [ units[4] ]
V_62.current = [ units[5] ]
V_62.light = [ units[6] ]

V_63 = onto.VAR( "V_63" )
units = variables[63]["units"].asList()
V_63.time = [ units[0] ]
V_63.length = [ units[1] ]
V_63.amount = [ units[2] ]
V_63.mass = [ units[3] ]
V_63.temperature = [ units[4] ]
V_63.current = [ units[5] ]
V_63.light = [ units[6] ]

V_64 = onto.VAR( "V_64" )
units = variables[64]["units"].asList()
V_64.time = [ units[0] ]
V_64.length = [ units[1] ]
V_64.amount = [ units[2] ]
V_64.mass = [ units[3] ]
V_64.temperature = [ units[4] ]
V_64.current = [ units[5] ]
V_64.light = [ units[6] ]

V_65 = onto.VAR( "V_65" )
units = variables[65]["units"].asList()
V_65.time = [ units[0] ]
V_65.length = [ units[1] ]
V_65.amount = [ units[2] ]
V_65.mass = [ units[3] ]
V_65.temperature = [ units[4] ]
V_65.current = [ units[5] ]
V_65.light = [ units[6] ]

V_66 = onto.VAR( "V_66" )
units = variables[66]["units"].asList()
V_66.time = [ units[0] ]
V_66.length = [ units[1] ]
V_66.amount = [ units[2] ]
V_66.mass = [ units[3] ]
V_66.temperature = [ units[4] ]
V_66.current = [ units[5] ]
V_66.light = [ units[6] ]

V_67 = onto.VAR( "V_67" )
units = variables[67]["units"].asList()
V_67.time = [ units[0] ]
V_67.length = [ units[1] ]
V_67.amount = [ units[2] ]
V_67.mass = [ units[3] ]
V_67.temperature = [ units[4] ]
V_67.current = [ units[5] ]
V_67.light = [ units[6] ]

V_68 = onto.VAR( "V_68" )
units = variables[68]["units"].asList()
V_68.time = [ units[0] ]
V_68.length = [ units[1] ]
V_68.amount = [ units[2] ]
V_68.mass = [ units[3] ]
V_68.temperature = [ units[4] ]
V_68.current = [ units[5] ]
V_68.light = [ units[6] ]

V_69 = onto.VAR( "V_69" )
units = variables[69]["units"].asList()
V_69.time = [ units[0] ]
V_69.length = [ units[1] ]
V_69.amount = [ units[2] ]
V_69.mass = [ units[3] ]
V_69.temperature = [ units[4] ]
V_69.current = [ units[5] ]
V_69.light = [ units[6] ]

V_71 = onto.VAR( "V_71" )
units = variables[71]["units"].asList()
V_71.time = [ units[0] ]
V_71.length = [ units[1] ]
V_71.amount = [ units[2] ]
V_71.mass = [ units[3] ]
V_71.temperature = [ units[4] ]
V_71.current = [ units[5] ]
V_71.light = [ units[6] ]

V_74 = onto.VAR( "V_74" )
units = variables[74]["units"].asList()
V_74.time = [ units[0] ]
V_74.length = [ units[1] ]
V_74.amount = [ units[2] ]
V_74.mass = [ units[3] ]
V_74.temperature = [ units[4] ]
V_74.current = [ units[5] ]
V_74.light = [ units[6] ]

V_75 = onto.VAR( "V_75" )
units = variables[75]["units"].asList()
V_75.time = [ units[0] ]
V_75.length = [ units[1] ]
V_75.amount = [ units[2] ]
V_75.mass = [ units[3] ]
V_75.temperature = [ units[4] ]
V_75.current = [ units[5] ]
V_75.light = [ units[6] ]

V_76 = onto.VAR( "V_76" )
units = variables[76]["units"].asList()
V_76.time = [ units[0] ]
V_76.length = [ units[1] ]
V_76.amount = [ units[2] ]
V_76.mass = [ units[3] ]
V_76.temperature = [ units[4] ]
V_76.current = [ units[5] ]
V_76.light = [ units[6] ]

V_77 = onto.VAR( "V_77" )
units = variables[77]["units"].asList()
V_77.time = [ units[0] ]
V_77.length = [ units[1] ]
V_77.amount = [ units[2] ]
V_77.mass = [ units[3] ]
V_77.temperature = [ units[4] ]
V_77.current = [ units[5] ]
V_77.light = [ units[6] ]

V_81 = onto.VAR( "V_81" )
units = variables[81]["units"].asList()
V_81.time = [ units[0] ]
V_81.length = [ units[1] ]
V_81.amount = [ units[2] ]
V_81.mass = [ units[3] ]
V_81.temperature = [ units[4] ]
V_81.current = [ units[5] ]
V_81.light = [ units[6] ]

V_82 = onto.VAR( "V_82" )
units = variables[82]["units"].asList()
V_82.time = [ units[0] ]
V_82.length = [ units[1] ]
V_82.amount = [ units[2] ]
V_82.mass = [ units[3] ]
V_82.temperature = [ units[4] ]
V_82.current = [ units[5] ]
V_82.light = [ units[6] ]

V_83 = onto.VAR( "V_83" )
units = variables[83]["units"].asList()
V_83.time = [ units[0] ]
V_83.length = [ units[1] ]
V_83.amount = [ units[2] ]
V_83.mass = [ units[3] ]
V_83.temperature = [ units[4] ]
V_83.current = [ units[5] ]
V_83.light = [ units[6] ]

V_84 = onto.VAR( "V_84" )
units = variables[84]["units"].asList()
V_84.time = [ units[0] ]
V_84.length = [ units[1] ]
V_84.amount = [ units[2] ]
V_84.mass = [ units[3] ]
V_84.temperature = [ units[4] ]
V_84.current = [ units[5] ]
V_84.light = [ units[6] ]

V_85 = onto.VAR( "V_85" )
units = variables[85]["units"].asList()
V_85.time = [ units[0] ]
V_85.length = [ units[1] ]
V_85.amount = [ units[2] ]
V_85.mass = [ units[3] ]
V_85.temperature = [ units[4] ]
V_85.current = [ units[5] ]
V_85.light = [ units[6] ]

V_86 = onto.VAR( "V_86" )
units = variables[86]["units"].asList()
V_86.time = [ units[0] ]
V_86.length = [ units[1] ]
V_86.amount = [ units[2] ]
V_86.mass = [ units[3] ]
V_86.temperature = [ units[4] ]
V_86.current = [ units[5] ]
V_86.light = [ units[6] ]

V_87 = onto.VAR( "V_87" )
units = variables[87]["units"].asList()
V_87.time = [ units[0] ]
V_87.length = [ units[1] ]
V_87.amount = [ units[2] ]
V_87.mass = [ units[3] ]
V_87.temperature = [ units[4] ]
V_87.current = [ units[5] ]
V_87.light = [ units[6] ]

V_88 = onto.VAR( "V_88" )
units = variables[88]["units"].asList()
V_88.time = [ units[0] ]
V_88.length = [ units[1] ]
V_88.amount = [ units[2] ]
V_88.mass = [ units[3] ]
V_88.temperature = [ units[4] ]
V_88.current = [ units[5] ]
V_88.light = [ units[6] ]

V_89 = onto.VAR( "V_89" )
units = variables[89]["units"].asList()
V_89.time = [ units[0] ]
V_89.length = [ units[1] ]
V_89.amount = [ units[2] ]
V_89.mass = [ units[3] ]
V_89.temperature = [ units[4] ]
V_89.current = [ units[5] ]
V_89.light = [ units[6] ]

V_92 = onto.VAR( "V_92" )
units = variables[92]["units"].asList()
V_92.time = [ units[0] ]
V_92.length = [ units[1] ]
V_92.amount = [ units[2] ]
V_92.mass = [ units[3] ]
V_92.temperature = [ units[4] ]
V_92.current = [ units[5] ]
V_92.light = [ units[6] ]

V_93 = onto.VAR( "V_93" )
units = variables[93]["units"].asList()
V_93.time = [ units[0] ]
V_93.length = [ units[1] ]
V_93.amount = [ units[2] ]
V_93.mass = [ units[3] ]
V_93.temperature = [ units[4] ]
V_93.current = [ units[5] ]
V_93.light = [ units[6] ]

V_94 = onto.VAR( "V_94" )
units = variables[94]["units"].asList()
V_94.time = [ units[0] ]
V_94.length = [ units[1] ]
V_94.amount = [ units[2] ]
V_94.mass = [ units[3] ]
V_94.temperature = [ units[4] ]
V_94.current = [ units[5] ]
V_94.light = [ units[6] ]

V_95 = onto.VAR( "V_95" )
units = variables[95]["units"].asList()
V_95.time = [ units[0] ]
V_95.length = [ units[1] ]
V_95.amount = [ units[2] ]
V_95.mass = [ units[3] ]
V_95.temperature = [ units[4] ]
V_95.current = [ units[5] ]
V_95.light = [ units[6] ]

V_96 = onto.VAR( "V_96" )
units = variables[96]["units"].asList()
V_96.time = [ units[0] ]
V_96.length = [ units[1] ]
V_96.amount = [ units[2] ]
V_96.mass = [ units[3] ]
V_96.temperature = [ units[4] ]
V_96.current = [ units[5] ]
V_96.light = [ units[6] ]

V_98 = onto.VAR( "V_98" )
units = variables[98]["units"].asList()
V_98.time = [ units[0] ]
V_98.length = [ units[1] ]
V_98.amount = [ units[2] ]
V_98.mass = [ units[3] ]
V_98.temperature = [ units[4] ]
V_98.current = [ units[5] ]
V_98.light = [ units[6] ]

V_99 = onto.VAR( "V_99" )
units = variables[99]["units"].asList()
V_99.time = [ units[0] ]
V_99.length = [ units[1] ]
V_99.amount = [ units[2] ]
V_99.mass = [ units[3] ]
V_99.temperature = [ units[4] ]
V_99.current = [ units[5] ]
V_99.light = [ units[6] ]

V_100 = onto.VAR( "V_100" )
units = variables[100]["units"].asList()
V_100.time = [ units[0] ]
V_100.length = [ units[1] ]
V_100.amount = [ units[2] ]
V_100.mass = [ units[3] ]
V_100.temperature = [ units[4] ]
V_100.current = [ units[5] ]
V_100.light = [ units[6] ]

V_101 = onto.VAR( "V_101" )
units = variables[101]["units"].asList()
V_101.time = [ units[0] ]
V_101.length = [ units[1] ]
V_101.amount = [ units[2] ]
V_101.mass = [ units[3] ]
V_101.temperature = [ units[4] ]
V_101.current = [ units[5] ]
V_101.light = [ units[6] ]

V_104 = onto.VAR( "V_104" )
units = variables[104]["units"].asList()
V_104.time = [ units[0] ]
V_104.length = [ units[1] ]
V_104.amount = [ units[2] ]
V_104.mass = [ units[3] ]
V_104.temperature = [ units[4] ]
V_104.current = [ units[5] ]
V_104.light = [ units[6] ]

V_106 = onto.VAR( "V_106" )
units = variables[106]["units"].asList()
V_106.time = [ units[0] ]
V_106.length = [ units[1] ]
V_106.amount = [ units[2] ]
V_106.mass = [ units[3] ]
V_106.temperature = [ units[4] ]
V_106.current = [ units[5] ]
V_106.light = [ units[6] ]

V_107 = onto.VAR( "V_107" )
units = variables[107]["units"].asList()
V_107.time = [ units[0] ]
V_107.length = [ units[1] ]
V_107.amount = [ units[2] ]
V_107.mass = [ units[3] ]
V_107.temperature = [ units[4] ]
V_107.current = [ units[5] ]
V_107.light = [ units[6] ]

V_108 = onto.VAR( "V_108" )
units = variables[108]["units"].asList()
V_108.time = [ units[0] ]
V_108.length = [ units[1] ]
V_108.amount = [ units[2] ]
V_108.mass = [ units[3] ]
V_108.temperature = [ units[4] ]
V_108.current = [ units[5] ]
V_108.light = [ units[6] ]

V_110 = onto.VAR( "V_110" )
units = variables[110]["units"].asList()
V_110.time = [ units[0] ]
V_110.length = [ units[1] ]
V_110.amount = [ units[2] ]
V_110.mass = [ units[3] ]
V_110.temperature = [ units[4] ]
V_110.current = [ units[5] ]
V_110.light = [ units[6] ]

V_111 = onto.VAR( "V_111" )
units = variables[111]["units"].asList()
V_111.time = [ units[0] ]
V_111.length = [ units[1] ]
V_111.amount = [ units[2] ]
V_111.mass = [ units[3] ]
V_111.temperature = [ units[4] ]
V_111.current = [ units[5] ]
V_111.light = [ units[6] ]

V_112 = onto.VAR( "V_112" )
units = variables[112]["units"].asList()
V_112.time = [ units[0] ]
V_112.length = [ units[1] ]
V_112.amount = [ units[2] ]
V_112.mass = [ units[3] ]
V_112.temperature = [ units[4] ]
V_112.current = [ units[5] ]
V_112.light = [ units[6] ]

V_113 = onto.VAR( "V_113" )
units = variables[113]["units"].asList()
V_113.time = [ units[0] ]
V_113.length = [ units[1] ]
V_113.amount = [ units[2] ]
V_113.mass = [ units[3] ]
V_113.temperature = [ units[4] ]
V_113.current = [ units[5] ]
V_113.light = [ units[6] ]

V_114 = onto.VAR( "V_114" )
units = variables[114]["units"].asList()
V_114.time = [ units[0] ]
V_114.length = [ units[1] ]
V_114.amount = [ units[2] ]
V_114.mass = [ units[3] ]
V_114.temperature = [ units[4] ]
V_114.current = [ units[5] ]
V_114.light = [ units[6] ]

V_115 = onto.VAR( "V_115" )
units = variables[115]["units"].asList()
V_115.time = [ units[0] ]
V_115.length = [ units[1] ]
V_115.amount = [ units[2] ]
V_115.mass = [ units[3] ]
V_115.temperature = [ units[4] ]
V_115.current = [ units[5] ]
V_115.light = [ units[6] ]

V_116 = onto.VAR( "V_116" )
units = variables[116]["units"].asList()
V_116.time = [ units[0] ]
V_116.length = [ units[1] ]
V_116.amount = [ units[2] ]
V_116.mass = [ units[3] ]
V_116.temperature = [ units[4] ]
V_116.current = [ units[5] ]
V_116.light = [ units[6] ]

V_117 = onto.VAR( "V_117" )
units = variables[117]["units"].asList()
V_117.time = [ units[0] ]
V_117.length = [ units[1] ]
V_117.amount = [ units[2] ]
V_117.mass = [ units[3] ]
V_117.temperature = [ units[4] ]
V_117.current = [ units[5] ]
V_117.light = [ units[6] ]

V_118 = onto.VAR( "V_118" )
units = variables[118]["units"].asList()
V_118.time = [ units[0] ]
V_118.length = [ units[1] ]
V_118.amount = [ units[2] ]
V_118.mass = [ units[3] ]
V_118.temperature = [ units[4] ]
V_118.current = [ units[5] ]
V_118.light = [ units[6] ]

V_120 = onto.VAR( "V_120" )
units = variables[120]["units"].asList()
V_120.time = [ units[0] ]
V_120.length = [ units[1] ]
V_120.amount = [ units[2] ]
V_120.mass = [ units[3] ]
V_120.temperature = [ units[4] ]
V_120.current = [ units[5] ]
V_120.light = [ units[6] ]

V_121 = onto.VAR( "V_121" )
units = variables[121]["units"].asList()
V_121.time = [ units[0] ]
V_121.length = [ units[1] ]
V_121.amount = [ units[2] ]
V_121.mass = [ units[3] ]
V_121.temperature = [ units[4] ]
V_121.current = [ units[5] ]
V_121.light = [ units[6] ]

V_122 = onto.VAR( "V_122" )
units = variables[122]["units"].asList()
V_122.time = [ units[0] ]
V_122.length = [ units[1] ]
V_122.amount = [ units[2] ]
V_122.mass = [ units[3] ]
V_122.temperature = [ units[4] ]
V_122.current = [ units[5] ]
V_122.light = [ units[6] ]

V_123 = onto.VAR( "V_123" )
units = variables[123]["units"].asList()
V_123.time = [ units[0] ]
V_123.length = [ units[1] ]
V_123.amount = [ units[2] ]
V_123.mass = [ units[3] ]
V_123.temperature = [ units[4] ]
V_123.current = [ units[5] ]
V_123.light = [ units[6] ]





V_6.is_function_of = [ V_5 ]

V_7.is_function_of = [ V_5 ]

V_8.is_function_of = [ V_1 ]


V_10.is_function_of = [ V_87 ]
V_10.is_function_of = [ V_1 ]
V_10.is_function_of = [ V_88 ]
V_10.is_function_of = [ V_89 ]




V_14.is_function_of = [ V_11 ]
V_14.is_function_of = [ V_12 ]

V_15.is_function_of = [ V_11 ]
V_15.is_function_of = [ V_13 ]

V_17.is_function_of = [ V_11 ]
V_17.is_function_of = [ V_15 ]
V_17.is_function_of = [ V_13 ]

V_18.is_function_of = [ V_9 ]
V_18.is_function_of = [ V_1 ]



V_22.is_function_of = [ V_20 ]
V_22.is_function_of = [ V_21 ]

V_26.is_function_of = [ V_17 ]
V_26.is_function_of = [ V_14 ]


V_31.is_function_of = [ V_11 ]
V_31.is_function_of = [ V_10 ]
V_31.is_function_of = [ V_112 ]
V_31.is_function_of = [ V_10 ]


V_45.is_function_of = [ V_41 ]
V_45.is_function_of = [ V_13 ]
V_45.is_function_of = [ V_11 ]
V_45.is_function_of = [ V_14 ]
V_45.is_function_of = [ V_18 ]

V_46.is_function_of = [ V_45 ]


V_54.is_function_of = [ V_2 ]
V_54.is_function_of = [ V_46 ]
V_54.is_function_of = [ V_22 ]
V_54.is_function_of = [ V_2 ]
V_54.is_function_of = [ V_14 ]

V_56.is_function_of = [ V_10 ]




V_60.is_function_of = [ V_13 ]
V_60.is_function_of = [ V_10 ]

V_61.is_function_of = [ V_57 ]
V_61.is_function_of = [ V_60 ]


V_63.is_function_of = [ V_57 ]
V_63.is_function_of = [ V_62 ]
V_63.is_function_of = [ V_58 ]




V_67.is_function_of = [ V_59 ]
V_67.is_function_of = [ V_14 ]

V_68.is_function_of = [ V_64 ]
V_68.is_function_of = [ V_65 ]
V_68.is_function_of = [ V_66 ]
V_68.is_function_of = [ V_67 ]

V_69.is_function_of = [ V_61 ]

V_71.is_function_of = [ V_69 ]
V_71.is_function_of = [ V_61 ]


V_75.is_function_of = [ V_74 ]
V_75.is_function_of = [ V_71 ]
V_75.is_function_of = [ V_62 ]
V_75.is_function_of = [ V_62 ]

V_76.is_function_of = [ V_68 ]
V_76.is_function_of = [ V_75 ]

V_77.is_function_of = [ V_13 ]
V_77.is_function_of = [ V_63 ]
V_77.is_function_of = [ V_76 ]

V_81.is_function_of = [ V_2 ]
V_81.is_function_of = [ V_99 ]
V_81.is_function_of = [ V_22 ]
V_81.is_function_of = [ V_2 ]
V_81.is_function_of = [ V_15 ]

V_82.is_function_of = [ V_2 ]
V_82.is_function_of = [ V_15 ]

V_83.is_function_of = [ V_6 ]
V_83.is_function_of = [ V_30 ]
V_83.is_function_of = [ V_82 ]
V_83.is_function_of = [ V_30 ]

V_84.is_function_of = [ V_83 ]
V_84.is_function_of = [ V_60 ]

V_85.is_function_of = [ V_30 ]
V_85.is_function_of = [ V_81 ]
V_85.is_function_of = [ V_84 ]

V_86.is_function_of = [ V_22 ]
V_86.is_function_of = [ V_30 ]
V_86.is_function_of = [ V_100 ]
V_86.is_function_of = [ V_30 ]
V_86.is_function_of = [ V_31 ]

V_87.is_function_of = [ V_85 ]
V_87.is_function_of = [ V_86 ]
V_87.is_function_of = [ V_77 ]
V_87.is_function_of = [ V_87 ]
V_87.is_function_of = [ V_7 ]

V_88.is_function_of = [ V_1 ]

V_89.is_function_of = [ V_1 ]


V_93.is_function_of = [ V_49 ]
V_93.is_function_of = [ V_18 ]
V_93.is_function_of = [ V_13 ]
V_93.is_function_of = [ V_31 ]
V_93.is_function_of = [ V_11 ]
V_93.is_function_of = [ V_31 ]


V_95.is_function_of = [ V_41 ]
V_95.is_function_of = [ V_94 ]
V_95.is_function_of = [ V_31 ]
V_95.is_function_of = [ V_13 ]
V_95.is_function_of = [ V_11 ]
V_95.is_function_of = [ V_15 ]
V_95.is_function_of = [ V_18 ]

V_96.is_function_of = [ V_92 ]
V_96.is_function_of = [ V_13 ]

V_98.is_function_of = [ V_96 ]
V_98.is_function_of = [ V_95 ]

V_99.is_function_of = [ V_98 ]

V_100.is_function_of = [ V_93 ]




V_107.is_function_of = [ V_106 ]

V_108.is_function_of = [ V_107 ]
V_108.is_function_of = [ V_104 ]

V_110.is_function_of = [ V_108 ]
V_110.is_function_of = [ V_104 ]

V_111.is_function_of = [ V_11 ]
V_111.is_function_of = [ V_14 ]
V_111.is_function_of = [ V_12 ]

V_112.is_function_of = [ V_11 ]
V_112.is_function_of = [ V_15 ]
V_112.is_function_of = [ V_13 ]
V_112.is_function_of = [ V_14 ]
V_112.is_function_of = [ V_12 ]






V_118.is_function_of = [ V_117 ]
V_118.is_function_of = [ V_1 ]
V_118.is_function_of = [ V_116 ]

V_120.is_function_of = [ V_5 ]

V_121.is_function_of = [ V_113 ]

V_122.is_function_of = [ V_118 ]
V_122.is_function_of = [ V_115 ]
V_122.is_function_of = [ V_113 ]
V_122.is_function_of = [ V_114 ]
V_122.is_function_of = [ V_113 ]
V_122.is_function_of = [ V_121 ]

onto.save("variables.owl")