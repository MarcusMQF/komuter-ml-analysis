#!/usr/bin/env python3
"""
Script to merge all KomuterPulse notebooks into a final summary
"""

import json
import os
from pathlib import Path

def merge_notebooks(notebook_files, output_file):
    """
    Merge multiple Jupyter notebooks into a single notebook
    """
    merged_notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.9"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    # Add title cell
    title_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# KomuterPulse: Complete Machine Learning Pipeline\n",
            "\n",
            "## Real-time Transit Intelligence Platform for KTM Komuter Services\n",
            "\n",
            "**Team: Artificial Not Intelligent**\n",
            "- Mah Qing Fung\n",
            "- Ajax Kang AJ\n",
            "- Chong Yu En\n",
            "- Lee Yi Mei\n",
            "- Oi Kay Yi\n",
            "\n",
            "**Course**: WIA1006 Machine Learning  \n",
            "**Institution**: Faculty of Computer Science & Information Technology, University of Malaya\n",
            "\n",
            "---\n",
            "\n",
            "This comprehensive notebook contains the complete machine learning pipeline for KomuterPulse, from initial data exploration through final model evaluation and selection.\n",
            "\n",
            "## Table of Contents\n",
            "1. **Data Exploration** - Understanding the KTM Komuter ridership dataset\n",
            "2. **Data Preprocessing** - Cleaning and preparing data for analysis\n",
            "3. **Feature Engineering** - Creating meaningful features for model training\n",
            "4. **Model Development** - Training multiple ML models:\n",
            "   - 4a. LSTM Neural Network\n",
            "   - 4b. Linear Regression\n",
            "   - 4c. XGBoost\n",
            "   - 4d. Prophet Time Series\n",
            "   - 4e. Random Forest\n",
            "5. **Model Evaluation** - Comprehensive evaluation and selection\n",
            "\n",
            "---\n"
        ]
    }
    merged_notebook["cells"].append(title_cell)
    
    for i, notebook_file in enumerate(notebook_files):
        if not os.path.exists(notebook_file):
            print(f"Warning: {notebook_file} not found, skipping...")
            continue
            
        print(f"Processing {notebook_file}...")
        
        try:
            with open(notebook_file, 'r', encoding='utf-8') as f:
                notebook = json.load(f)
            
            # Add section header
            section_titles = {
                "01_data_exploration.ipynb": "# 1. Data Exploration",
                "02_data_preprocessing.ipynb": "# 2. Data Preprocessing", 
                "03_feature_engineering.ipynb": "# 3. Feature Engineering",
                "04a_LSTM.ipynb": "# 4a. LSTM Model Development",
                "04b_LinearRegression.ipynb": "# 4b. Linear Regression Model",
                "04c_XGBoost.ipynb": "# 4c. XGBoost Model",
                "04d_Prophet.ipynb": "# 4d. Prophet Time Series Model",
                "04e_RandomForest.ipynb": "# 4e. Random Forest Model",
                "05_model_evaluation.ipynb": "# 5. Model Evaluation & Selection"
            }
            
            filename = os.path.basename(notebook_file)
            if filename in section_titles:
                section_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [f"\n{section_titles[filename]}\n\n---\n"]
                }
                merged_notebook["cells"].append(section_cell)
            
            # Add all cells from the notebook
            if "cells" in notebook:
                for cell in notebook["cells"]:
                    # Skip empty cells
                    if cell.get("source", []):
                        merged_notebook["cells"].append(cell)
                        
        except Exception as e:
            print(f"Error processing {notebook_file}: {e}")
            continue
    
    # Write merged notebook
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_notebook, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Successfully merged {len(notebook_files)} notebooks into {output_file}")
    print(f"📊 Total cells: {len(merged_notebook['cells'])}")

def main():
    # Define notebook files in order
    notebook_files = [
        "01_data_exploration.ipynb",
        "02_data_preprocessing.ipynb", 
        "03_feature_engineering.ipynb",
        "04a_LSTM.ipynb",
        "04b_LinearRegression.ipynb",
        "04c_XGBoost.ipynb", 
        "04d_Prophet.ipynb",
        "04e_RandomForest.ipynb",
        "05_model_evaluation.ipynb"
    ]
    
    output_file = "final_summary.ipynb"
    
    print("🚀 KomuterPulse Notebook Merger")
    print("="*50)
    print(f"Merging {len(notebook_files)} notebooks...")
    
    merge_notebooks(notebook_files, output_file)
    
    print(f"\n🎉 Merge complete! Open {output_file} in Jupyter to view the complete pipeline.")

if __name__ == "__main__":
    main() 