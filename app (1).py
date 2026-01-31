import streamlit as st
import pandas as pd
import numpy as np

# Import AI logic
from models.priority_engine import compute_priority
from models.recovery_model import compute_recovery_probability
from models.sla_risk_model import compute_sla_risk

import streamlit as st
import pandas as pd

# Import AI pipeline
from models.priority_engine import compute_priority
from models.recovery_model import compute_recovery_probability
from models.sla_risk_model import compute_sla_risk
from models.dca_performance import compute_dca_metrics

st.title("FedEx AI-Driven DCA Management Dashboard")

uploaded_file = st.file_uploader("Upload Case Data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Basic validation
    required_cols = [
        "case_id",
        "invoice_amount",
        "overdue_days",
        "customer_risk",
        "past_recovery_rate"
    ]

    if not all(col in df.columns for col in required_cols):
        st.error("Uploaded file is missing required columns.")
        st.stop()

    # Run AI pipeline
    df = compute_priority(df)
    df = compute_recovery_probability(df)
    df = compute_sla_risk(df)

    st.subheader("Sample Processed Cases")
    st.dataframe(df.head(10))

    # Priority Distribution
    st.subheader("AI-Based Case Priority Distribution")
    st.bar_chart(df["priority_bucket"].value_counts())

    # SLA Risk Distribution
    st.subheader("SLA Breach Risk Distribution")
    st.bar_chart(df["sla_risk_bucket"].value_counts())

    # -----------------------------
    # DCA PERFORMANCE LEADERBOARD
    # -----------------------------
    st.subheader("DCA Performance Leaderboard")

    dca_metrics = compute_dca_metrics(df)

    st.dataframe(
        dca_metrics[
            ["dca_id", "recovery_rate", "sla_compliance_rate", "performance_score"]
        ]
    )

    st.bar_chart(
        dca_metrics.set_index("dca_id")["performance_score"]
    )



