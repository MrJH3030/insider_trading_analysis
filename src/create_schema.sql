DROP TABLE IF EXISTS transactions;


CREATE TABLE transactions (
    issuer VARCHAR (255);
    bafin_id VARCHAR (255);
    isin VARCHAR(255);
    reported_entity VARCHAR(255);
    position VARCHAR(255);
    instrument_type VARCHAR(255);
    transaction_type VARCHAR(255);
    average_price DECIMAL;
    currency VARCHAR(255);
    aggregated_volume DECIMAL;
    report_date DATE;
    transaction_date DATE;
    transaction_location VARCHAR(255);
    activation_timestamp TIMESTAMP;
);