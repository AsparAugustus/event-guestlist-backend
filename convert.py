import pandas as pd
import json

def convert_xlsx_to_json(filename):
    # Read the XLSX file into a pandas DataFrame
    df = pd.read_excel(filename)

    # Create a set to store unique names
    unique_names = set()

    # Create a list to store the guest data
    guestData = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract the relevant information from the row
        full_name = row['Name']
        email = row['Email']
        company = row['Company']
        owner = row['Owner']
        invitee_type = row['Type of invitees']

        # Check if the name is already encountered
        if full_name in unique_names:
            continue

        # Add the name to the set of unique names
        unique_names.add(full_name)

        # Create a dictionary for the guest's data
        guest = {
            'full_name': full_name,
            'email': email,
            'company': company,
            'mobile_number': None,
            'checked_in': 0
        }

        # Add the guest's data to the list
        guestData.append(guest)

    # Convert the guestData list to JSON format
    json_data = json.dumps(guestData, indent=4)

    # Return the JSON data
    return json_data

# Example usage
xlsx_file = './file.xlsx'
json_data = convert_xlsx_to_json(xlsx_file)

# Save JSON data to a file
output_file = './output.json'  # Specify the path and name of the output JSON file
with open(output_file, 'w') as file:
    file.write(json_data)

# Print the JSON data
print(json_data)
