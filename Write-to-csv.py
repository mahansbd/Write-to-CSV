import csv

"""Creates a CSV file and applies our inputs to it."""

with open('names.csv', mode='w') as cvsfile:
    fieldnames = ['First_name', 'Last_name']
    writer = csv.DictWriter(cvsfile, fieldnames=fieldnames)
    writer.writeheader()


    """Add names after First_name and Last_name to update CSV file. Add more rows as needed."""

    writer.writerow({"First_name": "John", "Last_name": "Deer"})
    writer.writerow({"First_name": "Mark", "Last_name": "Curry"})
    writer.writerow({"First_name": "Lisa", "Last_name": "Lo"})
    writer.writerow({"First_name": "Brian", "Last_name": "Adam"})
    writer.writerow({"First_name": "Lester", "Last_name": "Thomas"})