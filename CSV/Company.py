from enum import Enum
from collections import namedtuple


class Company(object):
    'An object representing a company and its needs'


    class Ownership(Enum):
        PRIVATE_ALL_AUS = 1
        PRIVATE_HALF_AUS = 2
        PRIVATE_FOREIGN = 3
        LISTED_ON_ASX = 4
        LISTED_ON_FOREIGN_EXCHANGE = 5


    class Years_Operating(Enum):
        LESS_THAN_2 = 1
        FROM_2_TO_4 = 2
        FROM_5_TO_9 = 3


    Employees = namedtuple("Employees", "permanent_victoria interstate other_victoria overseas")


    Regional_Revenue = namedtuple("Regional_Revenue", "victorian_sales interstate_employees offshore_operations oversea_exports")


    Growth_Factors = namedtuple("Growth_Factors", "domestic_economic_environment cost_of_business availability_of_skilled_employees access_to_finance cost_of_RnD commonwealth_tax_credit nbn cloud_infrastructure data_as_service ease_of_innovation ICT_collaboration commonwealth_regulation commonweatlh_puschasing global_economy exchange_rates import_competition_domestic access_export_markets market_intel_export")


    class Increase_Decrease(Enum):
        DECREASE = 1
        STAY_THE_SAME = 2
        INCREASE = 3


    Skill_Shortage = namedtuple("Skill_Shortage", "ICT_managers ICT_professionals ICT_analysts developer_programmers database_admins ICT_security ICT_network software_engineers technicians trades_workers ICT_sales ICT_trainers research_development management no_shortages other")


    class Total_Revenue(Enum):
        LESS_THAN_200K = 1
        FROM_200K_TO_499K = 2
        FROM_500K_TO_999K = 3
        FROM_1M_TO_4999K = 4
        FROM_5M_TO_9999K = 5
        MORE_THAN_10M = 6


    class Regularity(Enum):
        NEVER = 1
        IRREGULARLY = 2
        REGULARLY = 3


    ICT_Exports = namedtuple("ICT_Exports", "computer_hardware other_ICT_equip computer_software computer_services web_design web_publishing info_storage maintenance telecom_services wholesale_retail_margins other")


    Export_Regions = namedtuple("Export_Regions", "SE_Asia E_Asia S_Asia Middle_East E_Europe W_Europe Africa N_America C_America S_America Oceania_PI Other")


    class Innovations(Enum):
        # Developing new products and services
        DEVELOPING_NEW_PRODUCTS = 1
        # Implementing new or significantly improved operational processes
        IMPLEMENTING_NEW_PROCESSES = 2
        # Customising/modifying existing products and services
        CUSTOMISING_EXISTING_PRODUCTS = 3
        # Other
        OTHER = 4


    class Barriers(Enum):
        MAJOR_BARRIER = -2
        BARRIER = -1
        NEITHER = 0
        ENABLER = 1
        MAJOR_ENABLER = 2
        NOT_APPLICABLE = 999


    def __init__(
        self,
        industry_sector: str,  # Q2
        ownership_status: Ownership,  # Q3
        hq_location: str,  # Q4
        years_in_victoria: Years_Operating,  # Q5
        employed: Employees,  # Q6
        employment_projections: Increase_Decrease,  # Q7
        can_access_skills: bool,  # Q8
        skills_in_short_supply: Skill_Shortage,  # Q9
        total_revenue: Total_Revenue,  # Q10
        regional_revenues: Regional_Revenue,  # Q11
        was_company_profitable: bool,  # Q12
        did_profit_meet_expectations: bool,  # Q13
        expected_change_in_profit: Increase_Decrease,  # Q14
        expected_change_in_industry_profit: Increase_Decrease,  # Q15
        does_company_export_ICT: Regularity,  # Q16
        ICT_exports: ICT_Exports,  # Q17
        export_regions: Export_Regions,  # Q18
        top_5_export_regions: list,  # Q19
        top_5_future_export_regions: list,  # Q20
        main_innovation_focus: Innovations,  # Q21
        percent_revenue_RnD: int,  # Q22
        industry_growth_factors: Growth_Factors  # Q23
    ):
        self.industry_sector = industry_sector
        self.ownership_status = ownership_status
        self.hq_location = hq_location
        self.years_in_victoria = years_in_victoria
        self.employed = employed
        self.employment_projections = employment_projections
        self.can_access_skills = can_access_skills
        self.skills_in_short_supply = skills_in_short_supply
        self.total_revenue = total_revenue
        self.regional_revenues = regional_revenues
        self.was_company_profitable = was_company_profitable
        self.did_profit_meet_expectations = did_profit_meet_expectations
        self.expected_change_in_profit = expected_change_in_profit
        self.expected_change_in_industry_profit = expected_change_in_industry_profit
        self.does_company_export_ICT = does_company_export_ICT
        self.ICT_exports = ICT_exports
        self.export_regions = export_regions
        self.top_5_export_regions = top_5_export_regions
        self.top_5_future_export_regions = top_5_future_export_regions
        self.main_innovation_focus = main_innovation_focus
        self.percent_revenue_RnD = percent_revenue_RnD
        self.industry_growth_factors = industry_growth_factors
