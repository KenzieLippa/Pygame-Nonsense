from os import walk
import pygame
#allows to walk thru

def import_folder(path):
	surface_list = []

	#can unpack
	#returns list with all elements in th folder
	#dont care about folder name or sub folder
	for folder_name, sub_folder, img_files in walk(path):
		#for what ever reason was reading out of order so u need to sort
		img_files.sort()
		for image in img_files:
			full_path = path+"/"+ image
			# print(img_files)
			# print(full_path)
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)
			#print(full_path)

	return surface_list