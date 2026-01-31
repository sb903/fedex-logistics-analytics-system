import pandas as pd

def compute_sla_risk(df):
    df["sla_risk_score"] = (
        0.5 * df["norm_overdue"] +
        0.3 * df["priority_score"] +
        0.2 * (1 - df["past_recovery_rate"])
    )

    df["sla_risk_bucket"] = pd.cut(
        df["sla_risk_score"],
        bins=[0, 0.4, 0.7, 1.0],
        labels=["Low", "Medium", "High"]
    )

    return df

