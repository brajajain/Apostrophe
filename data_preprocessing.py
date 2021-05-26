import pandas as pd
import os

from connect import ab_test_collection

pkl_data = 'ab_test_collection_df.pkl'
dir_contents = os.listdir('.')

if pkl_data in dir_contents:
    ab_test_collection_df = pd.read_pickle(pkl_data)
else:
    ab_test_collection_cursor = ab_test_collection.find()

    ab_test_collection_list = list(ab_test_collection_cursor)

    ab_test_collection_df = pd.json_normalize(ab_test_collection_list)

    ab_test_collection_df.set_index(['patient_id', '_id', 'consultation_id'], inplace=True)

    date_cols = []

    for col in ab_test_collection_df.columns:
        first_not_na_col_val = ab_test_collection_df[col].dropna().astype(str).values[0]
        if len(first_not_na_col_val) == 12 and type(first_not_na_col_val) != 'bool':
            date_cols.append(col)

    for col in date_cols:
        ab_test_collection_df[col] = pd.to_datetime(ab_test_collection_df[col], unit='s')

    ab_test_collection_df.to_pickle(f"./{pkl_data}")

groups = [f"{col}" for col in ab_test_collection_df.columns if 'group' in col]

treatment_groups = ['legacy_treatment_plan', 'q1_2021_treatment_plan']

target_treatment_group_data = ab_test_collection_df[
    (ab_test_collection_df['treatment_plan.group'].isin(treatment_groups))
]
