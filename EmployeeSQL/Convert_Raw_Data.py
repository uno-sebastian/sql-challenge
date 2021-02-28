import os
from csv import reader

def match_headers_with_type(headers, sample_row):
	matched = {}
	for i in range(len(headers)):
		data_type = 'VARCHAR'
		if sample_row[i].isdecimal():
			if '.' in sample_row[i]:
				data_type = 'DECIMAL'
			else:
				data_type = 'INT'
		elif '/' in sample_row[i]:
			data_type = 'DATE'
		elif sample_row[i].lower == 'true' or sample_row[i].lower == 'false':
			data_type = 'BOOLEAN'
		matched[headers[i]] = data_type
	return matched

def create_sql_table(table_name, headers, sample_row):
	matched = match_headers_with_type(headers, rows[0])
	table = []
	table.append('-- Drop table if exists\n')
	table.append(f'DROP TABLE IF EXISTS {table_name};\n\n')
	table.append('-- Create new table to import data\n')
	table.append(f'CREATE TABLE {table_name} (\n')
	length = len(headers)
	for i in range(length):
		line = f'\t{headers[i]} {matched[headers[i]]}'
		if i != (length - 1):
			line += ','
		table.append(line + '\n')
	table.append(');\n\n')
	return table

def with_quotes(data_type):
	if 'VARCHAR' in data_type:
		return True
	if 'DATE' in data_type:
		return True
	return False

def create_sql_add_data(table_name, headers, rows):
	matched = match_headers_with_type(headers, rows[0])
	add_data = []
	
	insert_line = '-- Import the data\n'
	insert_line += f'INSERT INTO {table_name} ('
	length = len(headers)
	for i in range(length):
		insert_line += headers[i]
		if i != (length - 1):
			insert_line += ', '
	insert_line += ')\nVALUES\n'
	add_data.append(insert_line)
	for row in rows:
		row_line = '\t('
		for i in range(length):
			if with_quotes(matched[headers[i]]):
				row_line += f"'{row[i]}'"
			else: row_line += row[i]
			if i != (length - 1):
				row_line += ', '
		row_line += '),\n'
		add_data.append(row_line)
	last_char_index = add_data[-1].rfind(',')
	add_data[-1] = f'{add_data[-1][:last_char_index]};{add_data[-1][last_char_index+1:]}\n'
	return add_data

def create_sql_file(table_name, headers, rows):
	file_name = table_name + '-schema-and-insert-data.sql'
	print('writing to file ' + file_name)
	try:
		sql_file = open(file_name, 'w+')
		sql_file.writelines(create_sql_table(table_name, headers, rows[0]))
		sql_file.writelines(create_sql_add_data(table_name, headers, rows))
		sql_file.write(f'SELECT * FROM {table_name};')
		sql_file.close()
		print('\tdone writing')
	except Exception as e:
		print('\tERROR\n')
		print(e)

for csv_name in os.listdir('Raw_Data/'):
	file_path = os.path.join('Raw_Data/', csv_name)
	print('opening file ' + file_path)
	with open(file_path, newline='', encoding='utf-8') as csv_file:
		csv_reader = reader(csv_file)
		headers = next(csv_reader)
		rows = []
		for row in csv_reader:
			rows.append(row)
		create_sql_file(csv_name.split('.')[0], headers, rows)

