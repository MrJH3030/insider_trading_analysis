import xml.etree.ElementTree as ET
from src.custom_dataclasses.transaction import Transaction

ISSUER = 0
BAFIN_ID = 1
ISIN = 2
REPORTED_ENTITY = 3
POSITION = 4
INSTRUMENT_TYPE = 5
TRANSACTION_TYPE = 6
AVERAGE_PRICE = 7
AGGREGATED_VOLUME = 8
REPORT_DATE = 9
TRANSACTION_DATE = 10
TRANSACTION_LOCATION = 11
ACTIVATION_DATE = 12


def load_xml_tree(path):
    tree = ET.parse(path)
    return tree.getroot()

#TODO parse dates as timestamps, null columns etc
def extract_transactions(tree):
    transactions = []
    for row in tree:
        transactions.append(Transaction(
            issuer= row[ISSUER].text,
            bafin_id= row[BAFIN_ID].text,
            isin= row[ISIN].text,
            reported_entity= row[REPORTED_ENTITY].text,
            position= row[POSITION].text,
            instrument_type=row[INSTRUMENT_TYPE].text,
            transaction_type= row[TRANSACTION_TYPE].text,
            average_price= row[AVERAGE_PRICE].text,
            aggregated_volume= row[AGGREGATED_VOLUME].text,
            report_date= row[REPORT_DATE].text,
            transaction_date=row[TRANSACTION_DATE], 
            transaction_location=row[TRANSACTION_LOCATION].text,
            activation_timestamp=row[ACTIVATION_DATE].text )
        )
    #first entry is a description
    return transactions[1:]

def execute(path):
    tree = load_xml_tree(path)
    transactions = extract_transactions(tree)
    print(transactions[1:3])
    return transactions

execute("/home/mb30/insider_analysis/insider_trading_analysis/data/bafin_manager_trading.xml")