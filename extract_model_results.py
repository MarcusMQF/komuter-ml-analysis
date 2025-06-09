"""
Script to extract model evaluation results for KomuterPulse project
"""

import pickle
import os
from pathlib import Path

def load_pickle_safe(file_path):
    """Safely load a pickle file"""
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def main():
    models_dir = Path("models")
    
    print("=" * 60)
    print("KOMUTERPULSE MODEL EVALUATION RESULTS")
    print("=" * 60)
    
    # LSTM Results
    lstm_results = load_pickle_safe(models_dir / "lstm_test_results.pkl")
    if lstm_results:
        print("\n🧠 LSTM MODEL RESULTS:")
        print("-" * 30)
        for key, value in lstm_results.items():
            print(f"{key}: {value}")
    
    # XGBoost Results
    xgb_results = load_pickle_safe(models_dir / "xgboost_evaluation.pkl")
    if xgb_results:
        print("\n🌳 XGBOOST MODEL RESULTS:")
        print("-" * 30)
        for key, value in xgb_results.items():
            print(f"{key}: {value}")
    
    # Linear Regression Results
    lr_results = load_pickle_safe(models_dir / "linear_regression_evaluation.pkl")
    if lr_results:
        print("\n📈 LINEAR REGRESSION MODEL RESULTS:")
        print("-" * 30)
        for key, value in lr_results.items():
            print(f"{key}: {value}")
    
    # LSTM Model Summary
    lstm_summary = load_pickle_safe(models_dir / "lstm_model_summary.pkl")
    if lstm_summary:
        print("\n🧠 LSTM MODEL SUMMARY:")
        print("-" * 30)
        for key, value in lstm_summary.items():
            print(f"{key}: {value}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main() 