import csv
# Note: A row in csv.reader = an array of strings with NUM_COLUMNS values
import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Generate a copy of the given CSV file with a new column of counts data inserted')
parser.add_argument('-i',
                     type=str,
                     help='the path to your csv file',
                     required=True)
parser.add_argument('-c',
                     type=str,
                     help='the exact case-sensitive name of the column you want to produce counts for',
                     required=True)
parser.add_argument('--sort',
                     action='store_true',
                     default=False,
                     help='activate descending sort by count and given named attribute')
args = parser.parse_args()

# Paths default to assuming your files are in same directory as script
INPUT_PATH = args.i
OUTPUT_PATH = INPUT_PATH.split('.')[0] + '_counted.csv'
should_sort = args.sort

if not os.path.isfile(INPUT_PATH):
  print('Error: The file specified for `-i` does not exist in this directory')
  sys.exit()

# Name of attribute you want counted
ATTR_NAME = args.c
# Column number of the relevant attribute
ATTR_INDEX = -1
# Column number of the relevant attribute's counts
COUNT_INDEX = -1
# CSV File Delimiter
COMMA = ','
# Dictionary to accumulate item occurrences 
unique_attr_instances = {}
# All rows with counts 
counted_rows = []

# Begin reading file
with open(INPUT_PATH) as in_file:
  csv_reader = csv.reader(in_file,  delimiter=COMMA)
  # Capture column number of items whose occurrences we are counting
  ATTR_INDEX = next(csv_reader).index(ATTR_NAME)

  # LOOP: Map unique items to corresponding number of instances
  for row in csv_reader:
    item = row[ATTR_INDEX]
    # Set number of occurrences 
    if item in unique_attr_instances.keys():
      unique_attr_instances[item] += 1
    else:
      unique_attr_instances[item] = 1

with open(INPUT_PATH) as in_file, open(OUTPUT_PATH, 'w') as out_file:
  csv_reader = csv.reader(in_file,  delimiter=COMMA)
  csv_writer = csv.writer(out_file, delimiter=COMMA)

  COUNT_INDEX = ATTR_INDEX + 1

  # Process and write new header row
  header_row = next(csv_reader)
  header_row.insert(COUNT_INDEX, 'count')
  csv_writer.writerow(header_row)


  # LOOP: Process and write new data rows (with count column)
  for row in csv_reader:
    item = row[ATTR_INDEX]
    num_instances = unique_attr_instances[item]
    row.insert(ATTR_INDEX+1, num_instances)
    counted_rows.append(row)

  if(should_sort):
    # Sort by the relevant attribute first, and by counts second
    counted_rows.sort(reverse=True, key=lambda row: (row[COUNT_INDEX], row[ATTR_INDEX]))

  # Write final resultant data, sorted
  for row in counted_rows:
    csv_writer.writerow(row)