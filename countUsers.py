import csv
# Note: A row in csv.reader = an array of strings with NUM_COLUMNS values

# Paths default to assuming your files are in same directory as script
INPUT_PATH = 'peteyTest2.csv'
OUTPUT_PATH = INPUT_PATH.split('.')[0] + '_counted.csv'
# Name of attribute you want counted
ATTR_NAME = 'not_hashed_user_id'
# Column number of the relevant attribute
ATTR_INDEX = -1
# CSV File Delimiter
COMMA = ','
# Dictionary to accumulate item occurrences 
unique_attr_instances = {}

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

  # Process and write new header row
  header_row = next(csv_reader)
  header_row.insert(ATTR_INDEX+1, 'count')
  csv_writer.writerow(row)


  # LOOP: Process and write new data rows (with count column)
  for row in csv_reader:
    item = row[ATTR_INDEX]
    num_instances = unique_attr_instances[item]
    row.insert(ATTR_INDEX+1, num_instances)
    csv_writer.writerow(row)