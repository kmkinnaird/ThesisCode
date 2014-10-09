import os
import music21 as m21
import numpy

def get_notes_and_durations_by_quarters(work_list, num_qtrs=2):
    notes = [[[(nn.midi,n.quarterLength) 
    for n in w.flat.notes.getElementsByOffset(i,i+num_qtrs,includeEndBoundary=False, mustBeginInSpan=False)
    for nn in n.pitches]
         for i in xrange(0,int(max([o['offset'] for o in w.flat.notes.offsetMap]))+num_qtrs,num_qtrs)] for w in work_list]
    return notes

directory_name = '/Users/katiek/Desktop/CurrentCode/'
sub_dir_list = ['Expanded', 'NotExpanded']


for i in range(len(sub_dir_list)):
	sub_dir_name = sub_dir_list[i]
	os.mkdir(directory_name + 'CSVfiles/' + sub_dir_name + '/')

	for filename in os.listdir(directory_name + '/KRNfiles/' + sub_dir_name + 'KRN/' ):
		process_filename = directory_name + 'KRNfiles/' + sub_dir_name + 'KRN/' + filename
		maz = m21.converter.parseFile(process_filename)
		notes = get_notes_and_durations_by_quarters([maz], num_qtrs=1)

		hist = []

		for beat in notes[0]:
			hist.append(numpy.zeros(12))
			for n in beat:
				hist[-1][n[0]%12]+=n[1]


		hist = numpy.array(hist).T
		a = numpy.asarray(hist)

		new_filename = filename.split('.')
		new_filename = new_filename[0] + '.csv'
		output_filename = directory_name + 'CSVfiles/' + sub_dir_name + '/' + new_filename

		numpy.savetxt(output_filename, a, delimiter=',')