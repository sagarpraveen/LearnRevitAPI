# -*- coding: utf-8 -*-
__title__ = "Rename Views"
__doc__ = """Version = 1.0
Date    = 08.10.2024
_____________________________________________________________________
Description:
Rename views in Revit by using Find/Replace Logic.
_____________________________________________________________________
How-to:
-> Click on the button
-> Select Views
-> Define Renaming Rules
-> Rename Views
_____________________________________________________________________
Last update:
- [08.10.2024] - 1.0 RELEASE
_____________________________________________________________________
To-Do:
- Describe Next Features
_____________________________________________________________________
Author: Erik Frits"""

from compiler.ast import Print

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
#==================================================
# Regular + Autodesk
from Autodesk.Revit.DB import *

# pyRevit
from pyrevit import revit, forms

from Autodesk.Revit.DB import *

# pyRevit
from pyrevit import revit, forms

# .NET Imports (You often need List import)
import clr
from rpw import uidoc

clr.AddReference("System")
from System.Collections.Generic import List

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
#==================================================
doc   = __revit__.ActiveUIDocument.Document #type: Document
from Autodesk.Revit.UI import UIDocument
from Autodesk.Revit.ApplicationServices import Application

uidoc = __revit__.ActiveUIDocument          #type: UIDocument
app   = __revit__.Application               #type: Application

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝
#==================================================

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# START CODE HERE
#==================================================

#1️⃣ Select Views
sel_el_ids  = uidoc.Selection.GetElementIds()
sel_elem    = [doc.GetElement(e_id) for e_id in sel_el_ids]
sel_views   = [el for el in sel_elem if issubclass(type(el), View)]

# If None Selected - Prompt SelectViews from pyrevit.forms.select_views()
if not sel_views:
    sel_elem = forms.select_views()

# Ensure Views Selected
if not sel_views:
    forms.alert('No Views Selected. Please Try Again', exitscript=True )

print('Done!')

