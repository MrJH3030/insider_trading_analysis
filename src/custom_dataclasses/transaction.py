from dataclasses import dataclass


@dataclass
class Transaction:
    issuer: str
    bafin_id: str
    isin: str
    reported_entity: str
    position: str
    instrument_type: str
    transaction_type: str
    average_price: str
    currency: str
    aggregated_volume: str
    report_date: str
    transaction_date: str
    transaction_location: str
    activation_timestamp: str


