#!/usr/bin/env python3

'''
#####---------------------------------------------------------
#####---------------------------------------------------------
#    Credit	: 	Asif Iqbal BHATTI
#    CODE to: 	convert Cell Matrix to Cell Parameters
#    VERSION: 	This script runs with python3 or later
#    FORMAT	:	POSCAR VASP5 format
#    DATE	: 	28/12/2019
#    USAGE	: 	python3 sys.argv[0]
#####---------------------------------------------------------
#####---------------------------------------------------------
'''

def Introduction():
	global message
	message = "              ____| Python script to process various properties |____"
	print(message)
	
if __name__ == "__main__":

	from elastic_constants 	import *
	from energy 			import *
	from contcar_poscar 	import *
	from poscar 			import *
	from fit_energy_vs_vol 	import *
	from strain 			import *
	from create_phonon_directories import *
	from evaluate_manually_Elastic_constants import *
	
	from colorama 			import Fore, Back, Style, init
	from termcolor 			import colored	
	from pylab 				import *
	import multiprocessing as mp
	import compileall
	
	print ("This may take a while!")
	compileall.compile_dir(".", force=1)
	
	Introduction()
	init(autoreset=True)
	print(colored('@'*80,'red'), end = '\n', flush=True)
	print("Number of processors Detected: ", mp.cpu_count())
	print(Back.MAGENTA + ' NB: POSCAR should be in VASP 5 format & without selective dynamics', end = '\n', flush=True)
	print(Style.RESET_ALL)	
	print(colored('-'*80,'red'), end = '\n', flush=True)
	print('>>> USAGE: execute by typing python3 sys.argv[0]')
	print(colored('~'*80,'red'), end = '\n', flush=True)
	print("**** Following are the options: ")
	print(colored('-'*80,'red'), end = '\n', flush=True)

	print("(01) To execute only POSCAR file (Convert Lattice Matrix to Lattice parameter)")
	print("(02) To execute POSCAR CELL VOLUME DIFFERENCE with final CONTCAR file")
	print("(03) To extract ENERGY from directories")
	print("(04) To extract ELASTIC CONSTANTS from OUTCAR file (IBRION=6,ISIF=3)")
	print("(05) To Fit energy vs volume curve to extract Elastic Moduli: B0")
	print("(06) CONVERT POSCAR file from VASP4 to VASP5 format")
	print("(07) Extract 'ELASTIC' constants (Cij) by deforming a crystal")
	print("(08) Create directories for PHONON calculations generated by PHONOPY code")
	print("(09) Calculate manually Elastic constants by inputting Cij values")
	print("(10) Calculate local lattice distortion for High Entropy Alloys: DEF1")
	print("(11) Calculate local lattice distortion for High Entropy Alloys: DEF2")

	print (colored('~'*80,'red'), end = '\n', flush=True)
	print (colored('*'*80,'red'), end = '\n', flush=True)

	while True:
		option = input("Enter the option as listed above: ")
		option = int(option)
		
		if (option == 1):
			poscar()
			
		elif (option == 2):
			VOL_P = main_poscar()
			VOL_C = main_contcar()
			volume_diff(VOL_P, VOL_C)
			
		elif (option == 3):
			energy_vs_volume()
			
		elif (option == 4):
			print("OUTCAR should be in the same directory from which this script is run ")		
			pool = mp.Pool(mp.cpu_count())
			elastic_matrix_VASP_STRESS()
			pool.close()
			
		elif (option == 5):
			fitting_energy_vs_volume_curve()
			
		elif (option == 6):
			poscar_VASP42VASP5()	
	
		elif (option == 7):
			Elastic_strain()
	
		elif (option == 8):
			create_phonon_directories()

		elif (option == 9):
			mechanical_properties()

		elif (option == 10):
			local_lattice_distortion_DEF1()
			
		elif (option == 11):		
			local_lattice_distortion_DEF2()
			
		else:
			print ("INVALID OPTION")
	
	
	
	
	
	
