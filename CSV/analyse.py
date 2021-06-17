from Company import Company
from readCSV import Prudential_dataset_parser

from typing import List

records = Prudential_dataset_parser.read()

class Analyse():
    """
    Filtering functions
    ============================================================================
    """
    def filter_location(location: str) -> List[str]:
        matching_records = list()
        records = Prudential_dataset_parser.read()

        for record in records:
            if(record.hq_location == location):
                matching_records.append(record)

        return matching_records

    def filter_private() -> List[str]:
        matching_records = list()
        records = Prudential_dataset_parser.read()

        for record in records:
            if(
                (record.ownership_status == Company.Ownership.PRIVATE_FOREIGN) |
                (record.ownership_status == Company.Ownership.PRIVATE_HALF_AUS) |
                (record.ownership_status == Company.Ownership.PRIVATE_FULL_AUS)
            ):
                matching_records.append(record)

        return matching_records

    def filter_public() -> List[str]:
        matching_records = list()
        records = Prudential_dataset_parser.read()

        for record in records:
            if(
                (record.ownership_status == Company.Ownership.LISTED_ON_ASX) |
                (record.ownership_status == Company.Ownership.LISTED_ON_FOREIGN_EXCHANGE)
            ):
                matching_records.append(record)

        return matching_records

	def filter_profitability(profitable: bool) -> List[str]:
		matching_records = list()
		records = Prudential_dataset_parser.read()

		for record in records:
			if(record.was_company_profitable == profitable):
				matching_records.append(record)

		return matching_records

	"""
	Sorting functions
	============================================================================
	"""

	# TODO write sorting functions
