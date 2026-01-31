import pandas as pd
import numpy as np

def compute_dca_metrics(df):
    """
    Computes DCA-level performance metrics:
    - Recovery rate
    - SLA compliance
    - Overall performance score
    """

    # Simulate DCA assignment (demo purpose)
    np.random.seed(10)
    df["dca_id"] = np.random.choice(
        ["DCA_1", "DCA_2", "DCA_3", "DCA_4"],
        size=len(df)
    )

    # Simulated outcomes
    df["recovered"] = np.random.binomial(
        1, df["recovery_probability"]
    )

    df["sla_breached"] = np.where(
        df["sla_risk_bucket"] == "High", 1, 0
    )

    dca_metrics = df.groupby("dca_id").agg(
        total_cases=("case_id", "count"),
        recovered_cases=("recovered", "sum"),
        avg_recovery_probability=("recovery_probability", "mean"),
        sla_breaches=("sla_breached", "sum")
    ).reset_index()

    dca_metrics["recovery_rate"] = (
        dca_metrics["recovered_cases"] / dca_metrics["total_cases"]
    )

    dca_metrics["sla_compliance_rate"] = (
        1 - dca_metrics["sla_breaches"] / dca_metrics["total_cases"]
    )

    # Final performance score (governance KPI)
    dca_metrics["performance_score"] = (
        0.4 * dca_metrics["recovery_rate"] +
        0.3 * dca_metrics["sla_compliance_rate"] +
        0.3 * dca_metrics["avg_recovery_probability"]
    )

    return dca_metrics

