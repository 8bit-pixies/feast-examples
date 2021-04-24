import pandas as pd
from datetime import datetime, timedelta
import numpy as np

retrieval_date = datetime.utcnow().replace(tzinfo=None)
retrieval_outside_max_age_date = retrieval_date + timedelta(1)
event_date = retrieval_date - timedelta(2)
creation_date = retrieval_date - timedelta(1)

customers = [1001, 1002, 1003, 1004, 1005]
daily_transactions = [np.random.rand() * 10 for _ in customers]
total_transactions = [np.random.rand() * 100 for _ in customers]

transactions_df = pd.DataFrame(
    {
        "event_timestamp": [event_date for _ in customers],
        "created_timestamp": [creation_date for _ in customers],
        "user_id": customers,
        "daily_transactions": daily_transactions,
        "total_transactions": total_transactions,
    }
)

customer_df = pd.DataFrame(
    {
        "event_timestamp": [retrieval_date- timedelta(1) for _ in customers]
        + [retrieval_outside_max_age_date for _ in customers],
        "user_id": customers + customers,
    }
)

transactions_df.to_parquet("transactions.parquet")
customer_df.to_parquet("../../customers.parquet")