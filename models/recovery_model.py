def compute_recovery_probability(df):
    df["recovery_probability"] = (
        0.4 * df["past_recovery_rate"] +
        0.3 * (1 - df["norm_overdue"]) +
        0.3 * (1 - df["customer_risk_score"])
    )

    df["recovery_probability"] = df["recovery_probability"].clip(0, 1)

    return df

