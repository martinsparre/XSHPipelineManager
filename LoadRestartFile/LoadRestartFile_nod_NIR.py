#!/usr/bin/python
#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, March 2011
#version 5.9.0

from PipelineManager import *

SciFiles = ['/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_NIR_098_0015.fits','/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_NIR_098_0016.fits','/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_NIR_098_0017.fits','/home/ms/Desktop/tmp_xsh/XSHOOTER_SLT_OBJ_NIR_098_0018.fits']#,



NIR = LoadRestartFile('Output/xsh_2dmap_NIR.restart')
NIR.ResetAllRecipes()



EsorexName='xsh_scired_slit_nod'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_NOD_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName,"RESPONSE_SLIT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")
NIR.EnableRecipe(SOFFileName)
NIR.SetFiles('OBJECT_SLIT_NOD_NIR',SciFiles)

NIR.RunPipeline()
