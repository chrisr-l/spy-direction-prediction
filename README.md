# SPY Direction Prediction

Empirical study of SPY next-day direction prediction using OHLCV-derived features, baseline machine learning models, and expanding-window walk-forward evaluation.

## Objective

The goal of this project is to test whether simple daily OHLCV-based features contain usable signal for predicting the next-day direction of SPY.

## Project Structure

- `data/` raw and engineered datasets
- `notebooks/` data preparation and modeling notebooks
- `results/` exported model comparison tables
- `paper/` LaTeX paper
- `src/` utility scripts

## Methods

- Binary next-day direction target
- OHLCV-derived feature engineering
- Logistic regression
- Random forest
- Fixed chronological split
- Expanding-window walk-forward evaluation
- Always-up baseline comparison

## Main Finding

Under the tested feature, model, and evaluation setup, no credible next-day predictive edge was demonstrated.

## Notes

This project does not claim that markets are generally unpredictable. It only documents the empirical outcome of the specific setup tested here.