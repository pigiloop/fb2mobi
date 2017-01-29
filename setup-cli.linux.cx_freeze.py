from cx_Freeze import setup, Executable

import sys
import os
import shutil
import version
import PIL, glob

base_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.argv.append('build_exe')

try:
    shutil.rmtree(os.path.join(base_dir, 'build'))
except:
    pass

try:
    shutil.rmtree(os.path.join(base_dir, 'dist'))
except:
    pass

includes = [
    'PIL._imaging',
    'modules.default_css'
]

excludes = [
    'pywin',
    'Tkconstants',
    'Tkinter',
    'tcl'
]

data_files = [
    (os.path.join(base_dir, 'modules', 'dictionaries'), 'dictionaries'),
    (os.path.join(base_dir, 'profiles'), 'profiles'),
    (os.path.join(base_dir, 'fb2mobi.config'), 'fb2mobi.config'),
    (os.path.join(base_dir, 'spaces.xsl'), 'spaces.xsl'),
    (os.path.join(base_dir, 'kindlegen'), 'kindlegen')
]

pil_libs = glob.glob(os.path.join(PIL.__path__[0], '.libs/*'))
if len(pil_libs) > 0:
    data_files = pil_libs + data_files

setup(
    name = "fb2mobi",
    version = version.VERSION,
    options={
        'build_exe': {
#            'silent': 1,
            'build_exe': 'dist',
            'zip_exclude_packages': '',
            'zip_include_packages': '*',
            'packages': 'lxml,PIL',
            'include_files': data_files,
            'includes': includes,
            'excludes': excludes,
        }
    },
    executables = [
        Executable('fb2mobi.py'),
        Executable('synccovers.py')
    ]
)
