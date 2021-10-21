import sys, os

sample_name = sys.argv[1]

order1 = ['ls','sample_name', '> id.txt']
#order2 = ['python','/data/Analysis/Project/EnfantGuard/bin/NameFind_js.py','id.txt', '> Samplesheet.txt']
order2 = ['python','/home/shinejh0528/NameFind_aofl_jh.py','id.txt']#, '> Samplesheet.txt']
#order3 = ['python', 'samplesheet.py', 'print_data']
order1[1] = '/data/Analysis/Project/EnfantGuard/Analysis_data/' + sample_name
#order3[2] = sample_name

final_order1 = ' '.join(order1)
os.system(final_order1)
final_order2 = ' '.join(order2)
os.system(final_order2)


