#!/usr/bin/env python
"""
setup.py file for smc600 module
"""

import glob
import os
import shutil

from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py


def copy_ext_modules():
    ext_module_paths = glob.glob("*.pyd")
    for ext_module_path in ext_module_paths:
        if os.path.exists(ext_module_path):
            dst_file_path = 'SMC600'
            print(f"Copy {ext_module_path} to {dst_file_path}")
            shutil.copy(ext_module_path, dst_file_path)
            return
    print('Failed to found compiled pyd file')
    exit(-1)


MOTION_EXT = Extension(
    name='_smc600',
    sources=[
        'SMC600/smc600.i',
    ],
    library_dirs=['SMC600'],
    libraries=['LTSMC'],
    swig_opts=['-c++'],
)


# Build extensions before python modules,
# or the generated SWIG python files will be missing.
class BuildPy(build_py):
    def run(self):
        build_ext_cmd = self.get_finalized_command('build_ext')
        build_ext_cmd.inplace = 1
        self.run_command('build_ext')
        copy_ext_modules()
        super(build_py, self).run()


setup(name='SMC600',
      version='0.0.11',
      author="WingC",
      author_email="1018957763@qq.com",
      description="""Python module for SMC600""",
      license='GPL',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',

          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Programming Language :: Python :: 3',
      ],
      cmdclass={
          'build_py': BuildPy,
      },
      packages=find_packages(),
      package_dir={'SMC600': 'SMC600'},
      ext_modules=[MOTION_EXT],
      package_data={'SMC600': ['*.h', '*.dll', '*.lib', '*.pyd']},
      include_package_data=True,
      python_requires='>=3.4',
      )
