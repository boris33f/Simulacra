from datetime import datetime

from Utilities import compile_module
from settings import *

root = os.path.dirname(__file__)
compile_module(creator_name, root, mods_folder)
print(datetime.now())
