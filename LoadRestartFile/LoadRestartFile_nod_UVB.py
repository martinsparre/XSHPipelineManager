#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, March 2011
#version 5.9.0

from PipelineManager import *


UVB = LoadRestartFile('Output/xsh_2dmap_UVB.restart')
UVB.ResetAllRecipes()

EsorexName='xsh_scired_slit_nod'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_NOD_UVB", "1..n", "any", "100k")
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

UVB.SetFiles('OBJECT_SLIT_NOD_UVB',['/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_UVB_098_0005.fits','/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_UVB_098_0006.fits','/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_UVB_098_0007.fits','/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_UVB_098_0008.fits'])


UVB.RunPipeline()
