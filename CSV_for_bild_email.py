import csv

# with open('source_file.csv','r') as source_file:
#     csv_reader = csv.reader(source_file)

#     with open('output_file.csv','w',newline='') as output_file:
#         csv_writer = csv.writer(output_file, delimiter=',')

#         for row in csv_reader:
#             csv_writer.writerow(row)
#             print("CSV file has been created successfully.")

        
remove_columns = {'Company Name for Emails','Company Name for Emails', 'Email Status','Primary Email Source','Primary Email Verification Source','Email Confidence','Primary Email Catch-all Status','Primary Email Last Verified At','Seniority','Departments','Sub Departments','Contact Owner','Work Direct Phone','Home Phone','Mobile Phone','Other Phone','Stage','Lists','Last Contacted','Account Owner','# Employees','Industry','Keywords','Company City','Company State','Company Country','Company Phone','Technologies','Annual Revenue','Total Funding','Latest Funding','Latest Funding Amount','Last Raised At','Subsidiary of','Subsidiary of (Organization ID)','Email Sent','Email Open','Email Bounced','Replied','Demoed','Number of Retail Locations','Apollo Contact Id','Apollo Account  Id','Secondary Email','Secondary Email Source','Secondary Email Status','Secondary Email Verification Source','Tertiary Email','Tertiary Email Source','Tertiary Email Status','Tertiary Email Verification Source','Primary Intent Topic','Primary Intent Score','Secondary Intent Topic','Secondary Intent Score','Qualify Contact','Apollo Account Id'}

with open('source_file.csv', newline='') as source_file:
    reader = csv.DictReader(source_file)
    fieldnames = [name for name in reader.fieldnames if name not in remove_columns]

    with open('output_file.csv', 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if str(row['Corporate Phone']).strip() == '':
                continue
            filtered = {k: v for k, v in row.items() if k not in remove_columns}
            writer.writerow(filtered)

print("CSV file has been created successfully.")