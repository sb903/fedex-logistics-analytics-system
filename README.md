# fedex-logistics-analytics-system

# AI-Driven Debt Collection Agency (DCA) Management System

## Problem Statement
FedEx manages thousands of overdue customer accounts through external Debt Collection Agencies (DCAs).
The current process is manual, spreadsheet-driven, and lacks real-time visibility, accountability,
and predictive intelligence.

## Our Solution
We propose an AI-driven DCA management platform that:
- Automatically prioritizes overdue cases
- Predicts recovery probability
- Identifies SLA breach risks
- Evaluates DCA performance using data-driven KPIs

## Key Features
- AI-based case prioritization & urgency classification
- Recovery probability prediction
- SLA risk scoring
- DCA performance analytics & leaderboard
- Scalable and explainable scoring logic

## Architecture Overview
Input Data → AI Scoring Engine → Priority & Risk Buckets → Allocation Decisions → Analytics Dashboard

## Technology Stack
- Python
- Pandas, NumPy
- Matplotlib
- Streamlit (UI)
- Jupyter Notebook

## Repository Structure
- `models/` → AI scoring logic
- `analytics/` → DCA performance analytics
- `app/` → Basic working UI
- `notebooks/` → End-to-end prototype
- `data/` → Sample input data

## How to Run
```bash
pip install -r requirements.txt
streamlit run app/app.py
