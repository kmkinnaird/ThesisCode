import os
import numpy

directory_name = '/Users/katiek/Desktop/CurrentCode/'
out_subdir = 'FileKeys/'


in_filename_list = []
key_list = []
color_list = []

temp_name_lst = [];

sub_dir_list = ['1/', '2/', '3/', '4/']
key_add_list = ['1', '2', '3', '4']
color_save = ['1', '2', '3', '4']
shingle_num_vec = ['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']



for i in range(len(sub_dir_list)):
	sub_dir_name = 'mazurka06-' + sub_dir_list[i]
	key_add = key_add_list[i]
	color_add = color_save[i]

	for filename in os.listdir(directory_name + 'MusicFiles/' + sub_dir_name):
		new_filename = filename.split('_')
		new_filename = new_filename[0]

		if len(new_filename) > 0:
			temp_name = sub_dir_name + new_filename
			temp_name_lst.append(temp_name)

			in_process_filename = directory_name + 'MusicFiles/' + sub_dir_name + filename
			in_filename_list.append(in_process_filename)

			key_list.append(key_add)
			color_list.append(color_add)

for s in range(len(shingle_num_vec)):
	shingle_num = shingle_num_vec[s]
	out_filename_list = []

	for j in range(len(temp_name_lst)):
		subdir_filename = temp_name_lst[j]

		out_process_filename = directory_name + 'MusicFiles/MATfiles/ShingleNumber' + shingle_num + '/' + subdir_filename  + '.mat'
		out_filename_list.append(out_process_filename)

	b = numpy.asarray(out_filename_list)
	output_MATfilename = directory_name + out_subdir + 'filenameAUDIO_list_ShingleNumber' + shingle_num + '.csv'
	numpy.savetxt(output_MATfilename, b, fmt="%s", delimiter=",")	



f = numpy.asarray(in_filename_list)
output_CSVfilename = directory_name + out_subdir + 'filenameAUDIO_list.csv'
numpy.savetxt(output_CSVfilename, f, fmt="%s", delimiter=",")	

k = numpy.asarray(key_list)
output_keyfilename = directory_name + out_subdir + 'keynameAUDIO_list.csv'
numpy.savetxt(output_keyfilename, k, fmt="%s", delimiter=",")

c = numpy.asarray(color_list)
output_keycolorname = directory_name + out_subdir + 'keycolorAUDIO_list.csv'
numpy.savetxt(output_keycolorname, c, fmt="%s", delimiter=",")