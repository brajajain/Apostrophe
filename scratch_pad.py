import pandas as pd
from connect import ab_test_collection

ab_test_collection_cursor = ab_test_collection.find()

ab_test_collection_df = pd.DataFrame.from_dict(
    ab_test_collection_cursor,
)

print(ab_test_collection_df.head())
