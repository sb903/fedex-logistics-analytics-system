def compute_dca_metrics(df):
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

    dca_metrics["performance_score"] = (
        0.4 * dca_metrics["recovery_rate"] +
        0.3 * dca_metrics["sla_compliance_rate"] +
        0.3 * dca_metrics["avg_recovery_probability"]
    )

    return dca_metrics

