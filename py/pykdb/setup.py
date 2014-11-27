from distutils.core import setup
from distutils.extension import Extension
import platform
import os.path as path

if platform.system() == 'Windows':
	if platform.architecture()[0] == '64bit':
		c_dot_o = path.abspath('../../../../cookbook_code/r/w64_qserver/c.o')
	else:
		c_dot_o = path.abspath('../../../../cookbook_code/r/w32_qserver/c.o')
		
	libs = ['ws2_32']
	extra_compile_args = ['/O2', '/Zi']
	
if platform.system() == 'Linux':
	if platform.architecture()[0] == '64bit':
		c_dot_o = path.abspath('../../../../cookbook_code/r/l64_qserver/c.o')
	else:
		c_dot_o = path.abspath('../../../../cookbook_code/r/l32_qserver/c.o')
		
	libs = ['']
	extra_compile_args = ['']

k_dot_h_loc = path.abspath('../../../../kx/kdb+/c/c' )

kdbmodule =  Extension('pykdb.kdb', 
			['src/qserver1.c', 'src/common1.c', 'src/dtm.c'], 
			define_macros = [('KXVER', '3'), ('HAVE_ROUND', None)],
			include_dirs = [k_dot_h_loc],
			extra_compile_args = extra_compile_args,
			libraries = libs,
			extra_objects = [c_dot_o],
			extra_link_args = ['']
			)

setup (name = 'pykdb', 
	version = '0.99-0',
	packages = ['pykdb'],
	description = 'Utilities for Python kdb+ interaction',
	author = 'G O Brown',
	author_email = 'gb9801@gmail.com',
	ext_modules = [kdbmodule]
	)
