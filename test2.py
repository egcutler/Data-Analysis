import data_analysis as da

path = (r'/root/workspace/github.com/egcutler/Data-Analysis/data archive')
filename = 'business data'
partial_name = 'business'
filetype = '.csv'
field_list = ['Account','Branch','External ID']
da.data_analysis_closed_date_flags(path, filename, partial_name, filetype , field_list, 'Closed Date', 'Creation Date', 'Modified Date')
