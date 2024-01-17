import data_integrity_support_files as disf

path = (r'/root/workspace/github.com/egcutler/Data-Analysis/data archive')
filename = 'business data'
partial_name = 'business'
filetype = '.csv'
field_list = ['Account','Branch','External ID']

precheck_folder = disf.FolderPreCheck(path)
if precheck_folder.check_files_with_partial_name(partial_name, filetype):
      precheck_file = disf.FilePreCheck(path, filename, filetype)
      precheck_file.file_exist_precheck()
      precheck_file.fields_exist_precheck(field_list)


precheck_file.check_fields_with_partialname("a")
  