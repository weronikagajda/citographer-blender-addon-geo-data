import sys
import os
import bpy

# Add the relative path to the 'libs' folder
addon_path = os.path.dirname(os.path.abspath(__file__))
libs_path = os.path.join(addon_path, 'libs')

# Append the 'libs' folder to sys.path if it's not already there
if libs_path not in sys.path:
    sys.path.append(libs_path)

# Set any necessary environment variables (for pyproj, for example)
proj_path = os.path.join(libs_path, 'proj-3.4.1')  # Adjust the version of PROJ if needed
os.environ['PROJ_LIB'] = proj_path

# Import external libraries from the 'libs' folder
from pyproj import Transformer  # Import pyproj
import pandas as pd  # Import pandas
from PIL import Image  # Import Pillow

from .panels import *
from .operators import *
from .utilities import *

bl_info = {
    "name" : "Citography - Beta",
    "author" : "Wero",
    "version" : (3, 1),
    "blender" : (3, 6, 4),
    "locoation" : "View3d > Tool",
    "description": "Extended Mapping Tool",
    "warning" : "",
    "wiki_url" : "",
    "catregory" : "3D View",   
}
    
def register():
    panels.register()
    operators.register()

def unregister():
    panels.unregister()
    operators.unregister()
    
if __name__ == "__main__":
    register()