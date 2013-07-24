#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, March 2011
#version 5.9.0

from PipelineManager import *


SciFiles = ['/home/ms/KU/Observations/GRB101219B/110125/Data/XSHOOTER_SLT_OBJ_VIS_025_0001.fits','/home/ms/KU/Observations/GRB101219B/110125/Data/XSHOOTER_SLT_OBJ_VIS_025_0002.fits','/home/ms/KU/Observations/GRB101219B/110125/Data/XSHOOTER_SLT_OBJ_VIS_026_0001.fits','/home/ms/KU/Observations/GRB101219B/110125/Data/XSHOOTER_SLT_OBJ_VIS_026_0002.fits']
#slit = ['-2.0','3.0','-2.0','3.0']

for i in range(len(SciFiles)):
    VIS = LoadRestartFile('Output/xsh_2dmap_VIS.restart')
    VIS.ResetAllRecipes()

    EsorexName='xsh_scired_slit_stare'
    SOFFileName = EsorexName + '_'+str(i)
    
    VIS.DeclareNewRecipe(EsorexName, SOFFileName)
    VIS.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_STARE_VIS", "1..n", "any", "100k")
    VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
    VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
    VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
    VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
    VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
    VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
    VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
    VIS.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
    VIS.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_VIS", "?", "-" , "-")
    VIS.EnableRecipe(SOFFileName)

    #VIS.SetRecipeOptions(SOFFileName, '--sky-subtract=FALSE --localize-slit-position='+slit[i])

    VIS.SetFiles('OBJECT_SLIT_STARE_VIS',[SciFiles[i]])

    VIS.RunPipeline()
