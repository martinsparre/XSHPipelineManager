#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, March 2011
#version 5.9.0

from PipelineManager import *

SciFiles = ['/home/ms/KU/Observations/GRB101219B/110125/Data/XSHOOTER_SLT_OBJ_UVB_025_0001.fits','/home/ms/KU/Observations/GRB101219B/110125/Data/XSHOOTER_SLT_OBJ_UVB_025_0002.fits','/home/ms/KU/Observations/GRB101219B/110125/Data/XSHOOTER_SLT_OBJ_UVB_026_0001.fits','/home/ms/KU/Observations/GRB101219B/110125/Data/XSHOOTER_SLT_OBJ_UVB_026_0002.fits']


for i in range(len(SciFiles)):
    UVB = LoadRestartFile('Output/xsh_2dmap_UVB.restart')
    UVB.ResetAllRecipes()

    EsorexName='xsh_scired_slit_stare'
    SOFFileName = EsorexName + '_' + str(i)
    
    UVB.DeclareNewRecipe(EsorexName, SOFFileName)
    UVB.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_STARE_UVB", "1..n", "any", "100k")
    UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
    UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "match", "match")
    UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
    UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")
    UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
    UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
    UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")
    UVB.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_UVB", "?", "-" ,"-")
    UVB.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_UVB", "?", "-" , "-")
    UVB.EnableRecipe(SOFFileName)

    UVB.SetFiles('OBJECT_SLIT_STARE_UVB',[SciFiles[i]])

    UVB.RunPipeline()
