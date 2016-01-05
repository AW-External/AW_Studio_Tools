import os, subprocess
file_directory = os.path.dirname(__file__)
inherited_environment =  os.environ.copy()
MAYA_SCRIPT_PATH = []
inherited_environment["PYTHONPATH"] =  os.path.join(file_directory, "Maya")
Mel_Script_Folders =  ["ANIMATION", "ARRAYTOOLS", "BINDING", "CONVERSIONS", "D3DX", "DEBUGING", "DMLTOOLS", "ENVIORMENT", "GLOBALUSAGE", "GUI", "POLY", "SCENE", "STRINGTOOLS", "SYSTEM", "TEXTPROSSING", "TRANSFORMS", "HIERARCHY"]

for folder in Mel_Script_Folders:
	folder = os.path.join(file_directory, "Maya", "Scripts", "Mel", folder)
	MAYA_SCRIPT_PATH.append(folder)
	
inherited_environment["MAYA_SCRIPT_PATH"] =  ";".join(MAYA_SCRIPT_PATH)

subprocess.call(r"C:\Program Files\Autodesk\Maya2015\bin\maya.exe", shell=False, close_fds=True, cwd=file_directory, env=inherited_environment)
