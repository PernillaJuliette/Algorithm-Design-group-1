import csv

print ("Hello users :)")
id = input("Enter the ID number:")

# This is the path '/path/file.csv' to the CSV file
with open('/News/data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # The first column in the CSV file contains the ID
    for row in csv_reader:
        if row and row[0] == id:
            # Found a match, access other data in the row
            matched_data = row
            
            break
    else:
        # ID not found
        matched_data = None

if matched_data:
    print("row data: ", matched_data)
else:
    print("row data not found")        