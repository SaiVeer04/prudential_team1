from Company import Company

import csv
from typing import List

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
    "5 to 9 years": Company.Years_Operating.FROM_5_TO_9,
    "10 to 19 years": Company.Years_Operating.FROM_10_TO_19,
    "20 or more years": Company.Years_Operating.MORE_THAN_20
}

dict_increase_decrease = {
    "Decrease": Company.Increase_Decrease.DECREASE,
    "Stay the same": Company.Increase_Decrease.STAY_THE_SAME,
    "Increase": Company.Increase_Decrease.INCREASE
}

dict_yes_no = {
    "Yes": True,
    "No": False
}

dict_revenue = {
    "$0 to $199,999": Company.Total_Revenue.LESS_THAN_200K,
    "$200,000 to $499,999": Company.Total_Revenue.FROM_200K_TO_499K,
    "$500,000 to $999,999": Company.Total_Revenue.FROM_500K_TO_999K,
    "$1,000,000 to $4,999,999": Company.Total_Revenue.FROM_1M_TO_4999K,
    "$5,000,000 to $9,999,999": Company.Total_Revenue.FROM_5M_TO_9999K,
    "More than $10,000,000": Company.Total_Revenue.MORE_THAN_10M
}


dict_innovation = {
    "Developing new products and services": Company.Innovations.DEVELOPING_NEW_PRODUCTS,
    "Implementing new or significantly improved organisational processes/structures": Company.Innovations.IMPLEMENTING_NEW_PROCESSES,
    "Customising/modifying existing products and services": Company.Innovations.CUSTOMISING_EXISTING_PRODUCTS,
    "Other": Company.Innovations.OTHER
}


dict_regularity = {
    "Never": Company.Regularity.NEVER,
    "Irregularly": Company.Regularity.IRREGULARLY,
    "Regularly": Company.Regularity.REGULARLY
}


dict_growth_factors = {
    "Major Barrier": Company.Barriers.MAJOR_BARRIER,
    "Barrier": Company.Barriers.BARRIER,
    "Neither a barrier nor an enabler": Company.Barriers.NEITHER,
    "Enabler": Company.Barriers.ENABLER,
    "Major Enabler": Company.Barriers.MAJOR_ENABLER
}

class Prudential_dataset_parser():
    def read() -> List[Company]:
        # List of companies to return
        records = list()
        # Open dataset at dataset.csv
        with open('dataset.csv', mode='r') as dataset:
            ds_reader = csv.reader(dataset, delimiter=',')
            line_count = 0
            # For every row of the file:
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

                    employment_projections = dict_increase_decrease.get(row[9])
                    # Throw error if expected change in number of employees could not be determined
                    if employment_projections is None:
                        raise ValueError(f'Employment projections for record {row[0]} indeterminable: {row[9]}')

                    can_access_skills = dict_yes_no.get(row[10])
                    # Throw error if company's access to needed skills could not be determined
                    if employment_projections is None:
                        raise ValueError(f'Access to needed skills for record {row[0]} indeterminable: {row[10]}')

                    # If the cell is filled, that means that company is having a shortage in that column's skill
                    skills_in_short_supply = Company.Skill_Shortage(
                        (row[11] != ''),
                        (row[12] != ''),
                        (row[13] != ''),
                        (row[14] != ''),
                        (row[15] != ''),
                        (row[16] != ''),
                        (row[17] != ''),
                        (row[18] != ''),
                        (row[19] != ''),
                        (row[20] != ''),
                        (row[21] != ''),
                        (row[22] != ''),
                        (row[23] != ''),
                        (row[24] != ''),
                        (row[25] != ''),
                        (row[26] != '')
                    )

                    total_revenue = dict_revenue.get(row[27])

                    # If cell is empty, set percentage equal to 0, otherwise the value of the cell
                    regional_revenues = Company.Regional_Revenue(
                        (0, row[28])[row[28] == ''],
                        (0, row[29])[row[29] == ''],
                        (0, row[30])[row[30] == ''],
                        (0, row[31])[row[31] == '']
                    )

                    was_company_profitable = dict_yes_no.get(row[32])

                    did_profit_meet_expectations = dict_yes_no.get(row[33])

                    expected_change_in_profit = dict_increase_decrease.get(row[34])

                    expected_change_in_industry_profit = dict_increase_decrease.get(row[35])

                    does_company_export_ICT = dict_regularity.get(row[36])

                    # If cell is not empty, that means the company exports the product of that column
                    ICT_exports = Company.ICT_Exports(
                        (row[37] != ''),
                        (row[38] != ''),
                        (row[39] != ''),
                        (row[40] != ''),
                        (row[41] != ''),
                        (row[42] != ''),
                        (row[43] != ''),
                        (row[44] != ''),
                        (row[45] != ''),
                        (row[46] != ''),
                        (row[47] != '')
                    )

                    # If cell is not empty, that means the company exports the region of that column
                    export_regions = Company.Export_Regions(
                        (row[48] != ''),
                        (row[49] != ''),
                        (row[50] != ''),
                        (row[51] != ''),
                        (row[52] != ''),
                        (row[53] != ''),
                        (row[54] != ''),
                        (row[55] != ''),
                        (row[56] != ''),
                        (row[57] != ''),
                        (row[58] != ''),
                        (row[59] != '')
                    )

                    top_5_export_regions = [row[60], row[61], row[62], row[63], row[64]]

                    top_5_future_export_regions = [row[65], row[66], row[67], row[68], row[69]]

                    main_innovation_focus = dict_innovation.get(row[70])

                    percent_revenue_RnD = (0, row[71])[row[71] == '']

                    # For every growth factor column, take the contents and get the corresponding enum value from the dict,
                    # and use it in the Growth_Factor tuple
                    industry_growth_factors = Company.Growth_Factors(
                        dict_growth_factors.get(row[72]),
                        dict_growth_factors.get(row[73]),
                        dict_growth_factors.get(row[74]),
                        dict_growth_factors.get(row[75]),
                        dict_growth_factors.get(row[76]),
                        dict_growth_factors.get(row[77]),
                        dict_growth_factors.get(row[78]),
                        dict_growth_factors.get(row[79]),
                        dict_growth_factors.get(row[80]),
                        dict_growth_factors.get(row[81]),
                        dict_growth_factors.get(row[82]),
                        dict_growth_factors.get(row[83]),
                        dict_growth_factors.get(row[84]),
                        dict_growth_factors.get(row[85]),
                        dict_growth_factors.get(row[86]),
                        dict_growth_factors.get(row[87]),
                        dict_growth_factors.get(row[88]),
                        dict_growth_factors.get(row[89])
                    )

                    line_count += 1

                    # With every value determined, add the Company in this row to the list
                    records.append(
                        Company(
                            industry_sector,  # Q2
                            ownership_status,  # Q3
                            hq_location,  # Q4
                            years_in_victoria,  # Q5
                            employed,  # Q6
                            employment_projections,  # Q7
                            can_access_skills,  # Q8
                            skills_in_short_supply,  # Q9
                            total_revenue,  # Q10
                            regional_revenues,  # Q11
                            was_company_profitable,  # Q12
                            did_profit_meet_expectations,  # Q13
                            expected_change_in_profit,  # Q14
                            expected_change_in_industry_profit,  # Q15
                            does_company_export_ICT,  # Q16
                            ICT_exports,  # Q17
                            export_regions,  # Q18
                            top_5_export_regions,  # Q19
                            top_5_future_export_regions,  # Q20
                            main_innovation_focus,  # Q21
                            percent_revenue_RnD,  # Q22
                            industry_growth_factors  # Q23
                        )
                    )

            # Return populated list
            return records
