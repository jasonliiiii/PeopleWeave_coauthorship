import universities
import json
from collections import Counter

# # Initialize the API
# uni = universities.API()

# # Load the JSON data
# with open('data/author_data.json', 'r') as file:
#     data = json.load(file)

# # Function to find the most common element in a list
# def most_common(lst):
#     if not lst:
#         return None
#     return Counter(lst).most_common(1)[0][0]

# # Function to get the country of an affiliation
# def get_country(affiliation):
#     try:
#         university = uni.lucky(name=affiliation)
#         if university:
#             return university.country
#     except Exception as e:
#         print(f"Error finding country for {affiliation}: {e}")
#     return None

# # Process each author in the dataset
# for author_id, author_info in data.items():
#     countries = []
#     for affiliation in author_info["affiliations"]:
#         country = get_country(affiliation)
#         if country:
#             countries.append(country)
#     most_common_country = most_common(countries)
#     author_info["country"] = most_common_country

# # Save the updated dataset back to a JSON file
# with open('author_data_geo.json', 'w') as file:
#     json.dump(data, file, indent=4)

# print("Updated dataset with country information has been saved.")

uni = universities.API()

# Function to display university information
def display_university_info(university):
    if university:
        print(f"Name: {university.name}")
        print(f"Country: {university.country}")
        print(f"State/Province: {university.stateprov}")
        print(f"Web Pages: {', '.join(university.web_pages)}")
        print(f"Domains: {', '.join(university.domains)}")
        print(f"Country Code: {university.country_code}")
        print("\n")
    else:
        print("University not found.\n")

# Search for a specific university
print("University Information:")
university = uni.lucky(name="Cambridge")
display_university_info(university)