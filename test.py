import data_integrity_support as dis

path = (r'/root/workspace/github.com/egcutler/Data-Analysis/data archive')
filename = 'business data'
filetype = '.csv'

field_list = ['Account','Branch','External ID']

precheck = dis.FilePreCheck(path, filename, filetype)
precheck.file_exist_precheck()
precheck.fields_exist_precheck(field_list)