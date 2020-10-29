import compileall

compileall.compile_dir('Dragon_Game/', force=True)

# Perform same compilation, excluding files in .svn directories.
import re
compileall.compile_dir('Dragon_Game/', rx=re.compile(r'[/\\][.]svn'), force=True)

# pathlib.Path objects can also be used.
import pathlib
compileall.compile_dir(pathlib.Path('Dragon_Game/'), force=True)
