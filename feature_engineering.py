from data_preprocessing import target_treatment_group_data
import numpy as np

target_treatment_group_data['treatment_plan.time_between_campaign_start_and_consultation_completed'] = (
    target_treatment_group_data['treatment_plan.goals.consultation_completed_date'] -
    target_treatment_group_data['treatment_plan.campaign_created_date']
)

target_treatment_group_data['treatment_plan.time_between_campaign_start_and_viewed_treatment_plan'] = (
    target_treatment_group_data['treatment_plan.goals.viewed_treatment_plan_date'] -
    target_treatment_group_data['treatment_plan.campaign_created_date']
)

target_treatment_group_data['treatment_plan.time_between_campaign_start_and_viewed_checkout_page'] = (
    target_treatment_group_data['treatment_plan.goals.viewed_checkout_page_date'] -
    target_treatment_group_data['treatment_plan.campaign_created_date']
)

target_treatment_group_data['treatment_plan.time_between_campaign_start_and_consultation_completed'] = (
    target_treatment_group_data['treatment_plan.goals.consultation_completed_date'] -
    target_treatment_group_data['treatment_plan.campaign_created_date']
)

target_treatment_group_data['treatment_plan.time_between_campaign_start_and_purchase_date'] = (
    target_treatment_group_data['treatment_plan.goals.purchase_date'] -
    target_treatment_group_data['treatment_plan.campaign_created_date']
)


target_treatment_group_data['PURCHASED'] = target_treatment_group_data['treatment_plan.goals.purchase_date'].notna()

time_between_cols = [
    time_between_col
    for time_between_col in target_treatment_group_data.columns
    if "time_between" in time_between_col
]

for col in time_between_cols:
    target_treatment_group_data[col] = target_treatment_group_data[col].dt.total_seconds()
    target_treatment_group_data[col] = target_treatment_group_data[col].astype(float)

target_treatment_group_data.to_pickle('target_treatment_group_data.pkl')
