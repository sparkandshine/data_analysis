#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import operator
import re

def read_csv_into_lists(filename):
	"""read a csv file into a list of lists
	"""
	with open(filename, 'r') as f:
		lists = [row for row in csv.reader(f, delimiter=',')] # read a csv file into a list of lists

	return lists[1:-1] # skip the first and the last line (comment lines)

def extract_column_from_lists(lists, index):
	"""extract a specific column from a list of lists
	"""
	return map(operator.itemgetter(index), lists[1:])

def main():
	# Step 1: read the csv file into a list of lists
	file_jcr_categories = 'traces/JCR_categories.csv'
	lists = read_csv_into_lists(file_jcr_categories)

	total_categories = len(lists) - 1
	print('Total categories:', total_categories)

	# Step 2:
	header = lists[0] # ['Rank', 'Category', 'Edition', '# Journals', 'Articles', 'Total Cites', 'Median Impact Factor', 'Aggregate Impact Factor', 'Aggregate Immediacy Index', 'Aggregate Cited Half Life', '', 'Aggregate Citing Half Life']
	idx_edition = header.index('Edition')
	idx_category = header.index('Category')

	# Editions
	l = extract_column_from_lists(lists, idx_edition)
	print('Editions:', set(l))

	# Filter out computer science, communication
	sublists = 	[header] + [row for row in lists[1:]
									if row[idx_edition] == 'SCIE'
									and re.search('computer science|communication', row[idx_category], re.IGNORECASE)]

	# format print
	print_formatted_lists(sublists)


def print_formatted_lists(lists):
	"""format print into fixed width (the maximum length of each column)
	"""
	# calculate the maximum length of each column
	column_max_len = [max(len(item) for item in t) for t in zip(*lists)] # [4, 48, 7, 10, 8, 11, 20, 23, 25, 25, 0, 26]
	print(column_max_len)

	for row in lists:
		# OR '%-0*s' % (column_max_len[idx], item)

		# replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
		s = '\t'.join(['{value:<{width}}'.format(value=item, width=column_max_len[idx]) 
						for idx, item in enumerate(row[1:], 1)]) # discard the first column 'Rank'

		print(s)

if __name__ == '__main__':
	main()