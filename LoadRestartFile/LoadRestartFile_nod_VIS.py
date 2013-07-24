#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, March 2011
#version 5.9.0

from PipelineManager import *


VIS = LoadRestartFile('OutputBase/xsh_2dmap_VIS.restart')
VIS.ResetAllRecipes()

EsorexName='xsh_scired_slit_nod'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName,SOFFileName)
VIS.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_NOD_VIS", "1..n", "any", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_VIS", "1", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_VIS", "?", "-" , "-")
VIS.EnableRecipe(SOFFileName)

VIS.SetFiles('OBJECT_SLIT_NOD_VIS',['/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_VIS_098_0005.fits','/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_VIS_098_0006.fits','/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_VIS_098_0007.fits','/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_VIS_098_0008.fits'])


VIS.RunPipeline()
