import sys
from os import chdir, getcwd, path
from pathlib import Path

local_dir = getcwd()
top_level = Path(__file__).parent.parent

# always use the same, absolute paths - which makes
# moving the notebooks around easier
chdir(top_level)

# allow easy access to packages defined in the root
sys.path.insert(1, path.join(sys.path[0], '..'))
