# -*- coding: utf-8 -*-
__title__ = "Button 4"
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

# ════════════════════════════════════════════════════════ IMPORTS
from Autodesk.Revit.DB import *
from pyrevit import revit, forms
import clr
from rpw import uidoc

clr.AddReference("System")
from System.Collections.Generic import List

# ════════════════════════════════════════════════════════ VARIABLES
doc = __revit__.ActiveUIDocument.Document  # type: Document
uidoc = __revit__.ActiveUIDocument          # type: UIDocument
app = __revit__.Application                 # type: Application

# ════════════════════════════════════════════════════════ MAIN
# 1️⃣ Select Views
try:
    sel_el_ids = uidoc.Selection.GetElementIds()
    sel_elem = [doc.GetElement(e_id) for e_id in sel_el_ids]
    sel_views = [el for el in sel_elem if isinstance(el, View)]

    # If None Selected - Prompt SelectViews from pyrevit.forms.select_views()
    if not sel_views:
        sel_views = forms.select_views()

    # Ensure Views Selected
    if not sel_views:
        forms.alert('No Views Selected. Please Try Again', exitscript=True)

    print('Done!')

except Exception as e:
    forms.alert('An error occurred: {str(e)}', exitscript=True)