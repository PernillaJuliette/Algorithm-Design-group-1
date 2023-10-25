import csv

print ("Hello users :)")
id = input("Enter the ID number you want to search for: ")

# This the path the '/path/file.csv' to our CSV file
with open('/News/data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # The first column in your CSV file contains the ID
    for row in csv_reader:
        if row and row[0] == id:
            # Found a match, you can access other data in the row as needed
            matched_data = row
            
            break
    else:
        # ID not found
        matched_data = None

if matched_data:
    print("Article data: ", matched_data)
else:
    print("ID not found, There are not that many articles in this CSV file")        