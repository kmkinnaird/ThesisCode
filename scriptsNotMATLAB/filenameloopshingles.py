import os
import numpy

directory_name = '/Users/katiek/Desktop/CurrentCode/'
out_subdir = 'FileKeys/'


full_filenameCSV_list = []
key_list = []
color_list = []

temp_name_lst = [];

sub_dir_list = ['Expanded/', 'NotExpanded/']
key_add_list = ['e', 'n']
color_save = ['1','2']
shingle_num_vec = ['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']



for i in range(len(sub_dir_list)):
	sub_dir_name = sub_dir_list[i]
	key_add = key_add_list[i]
	color_add = color_save[i]

	for filename in os.listdir(directory_name + 'CSVfiles/' + sub_dir_name):
		new_filename = filename.split('.')
		new_filename = new_filename[0]

		if len(new_filename) > 0:
			temp_name = sub_dir_name + new_filename
			temp_name_lst.append(temp_name)

			in_process_filename = directory_name + 'CSVfiles/' + sub_dir_name + new_filename + '.csv'
			full_filenameCSV_list.append(in_process_filename)

			first_cut = filename.split('ka')

			second_cut = first_cut[1].split('-')
			op_num = second_cut[0]
			if len(op_num) == 0:
				op_num = '00'

			third_cut = second_cut[1].split('.')
			no_num = third_cut[0]
			if len(no_num) == 1:
				no_num = '0' + no_num

			key_marker = key_add + op_num + no_num
			key_list.append(key_marker)

			color_list.append(color_add)

for s in range(len(shingle_num_vec)):
	shingle_num = shingle_num_vec[s]
	full_filenameMAT_list = []

	for j in range(len(temp_name_lst)):
		subdir_filename = temp_name_lst[j]

		out_process_filename = directory_name + 'MATfiles/ShingleNumber' + shingle_num + '/' + subdir_filename  + '.mat'
		full_filenameMAT_list.append(out_process_filename)

	b = numpy.asarray(full_filenameMAT_list)
	output_MATfilename = directory_name + out_subdir + 'filenameMAT_list_ShingleNumber' + shingle_num + '.csv'
	numpy.savetxt(output_MATfilename, b, fmt="%s", delimiter=",")	



f = numpy.asarray(full_filenameCSV_list)
output_CSVfilename = directory_name + out_subdir + 'filenameCSV_list.csv'
numpy.savetxt(output_CSVfilename, f, fmt="%s", delimiter=",")	

k = numpy.asarray(key_list)
output_keyfilename = directory_name + out_subdir + 'keyname_list.csv'
numpy.savetxt(output_keyfilename, k, fmt="%s", delimiter=",")

c = numpy.asarray(color_list)
output_keycolorname = directory_name + out_subdir + 'keycolor_list.csv'
numpy.savetxt(output_keycolorname, c, fmt="%s", delimiter=",")