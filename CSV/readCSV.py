from Company import Company

import csv

records = list()

dict_ownership = {
    "Privately owned (100% Australian)": Company.Ownership.PRIVATE_ALL_AUS,
    "Privately owned (up to 49% foreign owned)": Company.Ownership.PRIVATE_HALF_AUS,
    "Privately owned (50-100% foreign owned)": Company.Ownership.PRIVATE_FOREIGN,
    "Listed on ASX": Company.Ownership.LISTED_ON_ASX,
    "Listed on foreign exchange": Company.Ownership.LISTED_ON_FOREIGN_EXCHANGE
}

dict_years_operating = {
    "Less than 2 years": Company.Years_Operating.LESS_THAN_2,
    "2 to 4 years": Company.Years_Operating.FROM_2_TO_4,
    "5 to 9 years": Company.Years_Operating.FROM_5_TO_9
}

dict_employment_expectations = {
    "Decrease": Company.Increase_Decrease.DECREASE,
    "Stay the same": Company.Increase_Decrease.STAY_THE_SAME,
    "Increase": Company.Increase_Decrease.INCREASE
}

with open('dataset.csv', mode='r') as dataset:
    ds_reader = csv.reader(dataset, delimiter=',')
    line_count = 0
    for row in ds_reader:
        if(line_count < 2):  # Skip first two rows of dataset
            line_count += 1
        else:  # For every record, create a Company object and add it to the list
            industry_sector = row[1]

            ownership_status = dict_ownership.get(row[2])
            # Throw error if ownership status could not be determined
            if ownership_status is None:
                raise ValueError(f'Ownership status for record {row[0]} indeterminable: {row[2]}')

            hq_location = row[3]

            years_in_victoria = dict_years_operating.get(row[4])
            # Throw error if years operating in Victoria could not be determined
            if years_in_victoria is None:
                raise ValueError(f'Years operating in Victoria for record {row[0]} indeterminable: {row[4]}')

            permanent_employees_in_victoria = row[5]
            if (permanent_employees_in_victoria == ''):
                permanent_employees_in_victoria = 0
            temp_employees_in_victoria = row[6]
            if (temp_employees_in_victoria == ''):
                temp_employees_in_victoria = 0
            interstate_employees = row[7]
            if (interstate_employees == ''):
                interstate_employees = 0
            overseas_employees = row[8]
            if (overseas_employees == ''):
                overseas_employees = 0
            employed = Company.Employees(
                permanent_employees_in_victoria,
                temp_employees_in_victoria,
                interstate_employees,
                overseas_employees
            )

            employment_projections = dict_employment_expectations.get(row[9])
            # Throw error if expected change in number of employees could not be determined
            if employment_projections is None:
                raise ValueError(f'Employment projections for record {row[0]} indeterminable: {row[9]}')

            line_count += 1
