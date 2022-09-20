#!/usr/bin/env python3

from gettext import install
from multiprocessing.sharedctypes import Value
import sys
import subprocess


def	check_env() -> bool:
	return sys.prefix != sys.base_prefix

def	install_package(packages: list, requirements='requirements.txt') -> None:
	
	if not check_env():
		raise RuntimeError('Error: ENV')
	
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', *packages])
		
	installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
	installed_packages = installed_packages.decode('utf-8')
	print(installed_packages)
	with open(requirements, 'w', encoding='utf-8') as file:
		file.write(installed_packages)


def	main():
	
	install_package(['beautifulsoup4', 'PyTest'])
	

if __name__ == '__main__':
	try:
		main()
	
	except RuntimeError as err:
		print(f'Runtime error: {err.args[0]}')