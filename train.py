# get the train data...

from feast import FeatureStore
import pandas as pd
from datetime import datetime

entity_df = pd.DataFrame.from_dict({
    "driver_id": [1001, 1002, 1003, 1004],
    "event_timestamp": [
        datetime(2021, 4, 12, 10, 59, 42),
        datetime(2021, 4, 12, 8,  12, 10),
        datetime(2021, 4, 12, 16, 40, 26),
        datetime(2021, 4, 12, 15, 1 , 12)
    ]
})

store = FeatureStore(repo_path="feast_repo")

training_df = store.get_historical_features(
    entity_df=entity_df, 
    feature_refs = [
        'driver_hourly_stats:conv_rate',
        'driver_hourly_stats:acc_rate',
        'driver_hourly_stats:avg_daily_trips'
    ],
).to_df()

print(training_df.head())

# another feature store

store = FeatureStore(repo_path="feature_transaction")
customer_df = pd.read_parquet("customers.parquet")

training_df = store.get_historical_features(
    entity_df=customer_df, 
    feature_refs = [
        'customer_transactions:total_transactions',
        'customer_transactions:daily_transactions',
    ],
).to_df()

print(training_df.head())

# retreive features from another feature store

store = FeatureStore(repo_path="feature_multi")
# customer_df = pd.read_parquet("customers_multi.parquet")
customer_df = pd.read_parquet("customers_multi_20210424-220241.parquet")

training_df = store.get_historical_features(
    entity_df=customer_df, 
    feature_refs = [
        'customer_transactions:total_transactions',
        'customer_transactions:daily_transactions',
        'customer_events:event',
    ],
).to_df()

print(training_df.head())