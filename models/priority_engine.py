import pandas as pd

risk_map = {"Low": 0.3, "Medium": 0.6, "High": 1.0}

def normalize(col):
    return (col - col.min()) / (col.max() - col.min())

def compute_priority(df):
    df["customer_risk_score"] = df["customer_risk"].map(risk_map)
    df["norm_overdue"] = normalize(df["overdue_days"])
    df["norm_invoice"] = normalize(df["invoice_amount"])

    df["priority_score"] = (
        0.35 * df["norm_overdue"] +
        0.30 * df["norm_invoice"] +
        0.20 * df["customer_risk_score"] +
        0.15 * (1 - df["past_recovery_rate"])
    )

    df["priority_bucket"] = pd.qcut(
        df["priority_score"],
        q=[0, 0.3, 0.7, 1.0],
        labels=["Low", "Medium", "High"]
    )

    return df

