from enum import Enum


class Ownership(Enum):
    PRIVATELY_OWNED = 1
    LISTED_ON_ASX = 2
    LISTED_ON_FOREIGN_EXCHANGE = 3


class Years_Operating(Enum):
    LESS_THAN_2 = 1
    FROM_2_TO_4 = 2
    FROM_5_TO_9 = 3


class Employees(object):
    __slots__ = [
        'permanent_victoria',
        'interstate',
        'other_victoria',
        'overseas'
    ]


class Increase_Decrease(Enum):
    DECREASE = 1
    STAY_THE_SAME = 2
    INCREASE = 3


class Skill_Shortage(object):
    __slots__ = [
        # ICT managers
        'ICT_managers',
        # ICT professionals
        'ICT_professionals',
        # ICT business analysts, systems analysts and programmers
        'ICT_analysts',
        # Developer programmers
        'developer_programmers',
        # Database and systems administrators
        'database_admins',
        # ICT security specialists
        'ICT_security',
        # ICT network and support professionals
        # (e.g. computer network and systems engineers)
        'ICT_network',
        # Software engineers, testers and app programmers
        'software_engineers',
        # Technicians – ICT, telecommunications and electronics
        'technicians',
        # Trades workers – Electrotechnology, electronics and
        # telecommunications
        'trades_workers',
        # ICT sales
        'ICT_sales',
        # ICT trainers
        'ICT_trainers',
        # Research and development
        'research_development',
        # Business management, human resources and other support functions
        'management',
        # Company not currently experiencing skills as being in short supply
        'no_shortages',
        # Other
        'other'
    ]


class Total_Revenue(Enum):
    LESS_THAN_200K = 1
    FROM_200K_TO_499K = 2
    FROM_500K_TO_999K = 3
    FROM_1M_TO_4999K = 4
    FROM_5M_TO_9999K = 5
    MORE_THAN_10M = 6


class Regional_Revenue(object):
    __slots__ = [
        'victorian_sales',
        'interstate_sales',
        'offshore_operations',
        'overseas_exports'
    ]


class Regularity(Enum):
    NEVER = 1
    IRREGULARLY = 2
    REGULARLY = 3


class ICT_Exports(object):
    __slots__ = [
        'computer_hardware',
        'other_ICT_equip',
        'computer_software',
        'computer_services',
        'web_design',
        'web_publishing',
        'info_storage',
        'maintenance',
        'telecom_services',
        'wholesale_retail_margins',
        'other'
    ]


class Export_Regions(object):
    __slots__ = [
        'SE_Asia',
        'E_Asia',
        'S_Asia',
        'Middle_East',
        'E_Europe',
        'W_Europe',
        'Africa',
        'N_America',
        'C_America',
        'S_America',
        'Oceania_PI',
        'Other'
    ]


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


class Growth_Factors(object):
    __slots__ = [
        # Domestic economic environment
        'domestic_economic_environment',
        # Cost of doing business/input costs
        'cost_of_business',
        # Availability of skilled employees
        'availability_of_skilled_employees',
        # Access to finance
        'access_to_finance',
        # Cost of R&D
        'cost_of_RnD',
        # Level of Commonwealth R&D tax credit/incentive
        'commonwealth_tax_credit',
        # NBN as a driver of products and services
        'nbn',
        # Cloud infrastructure as a driver of products and services
        'cloud_infrastructure',
        # Data as a service as a driver of products and services
        'data_as_service',
        # Ease of implementing innovation
        'ease_of_innovation',
        # Ability to collaborate in the ICT industry
        'ICT_collaboration',
        # Commonwealth/State Government regulation
        'commonwealth_regulation',
        # Access to Commonwealth/State Government purchasing markets
        'commonweatlh_puschasing',
        # Global economic environment
        'global_economy',
        # Exchange rates
        'exchange_rates',
        # Competition from imports in domestic markets
        'import_competition_domestic',
        # Access to export markets
        'access_export_markets',
        # Market intelligence about export opportunities
        'market_intel_export'
    ]


class Company(object):
    'An object representing a company and its needs'

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
        top_5_export_regions: str[5],  # Q19
        top_5_future_export_regions: str[5],  # Q20
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
