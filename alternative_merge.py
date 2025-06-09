#!/usr/bin/env python3
"""
Alternative notebook merger using nbconvert
"""

import subprocess
import os

def merge_with_nbconvert():
    """
    Alternative method using nbconvert to merge notebooks
    """
    notebooks = [
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
    
    # Convert each notebook to markdown first
    markdown_files = []
    for nb in notebooks:
        if os.path.exists(nb):
            md_file = nb.replace('.ipynb', '.md')
            try:
                subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown', nb], check=True)
                markdown_files.append(md_file)
                print(f"✅ Converted {nb} to {md_file}")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to convert {nb}")
    
    # Combine markdown files
    combined_md = "final_summary.md"
    with open(combined_md, 'w', encoding='utf-8') as outfile:
        outfile.write("# KomuterPulse: Complete Machine Learning Pipeline\n\n")
        
        for md_file in markdown_files:
            if os.path.exists(md_file):
                with open(md_file, 'r', encoding='utf-8') as infile:
                    outfile.write(f"\n\n---\n\n")
                    outfile.write(infile.read())
                os.remove(md_file)  # Clean up
    
    print(f"✅ Created combined markdown: {combined_md}")

if __name__ == "__main__":
    merge_with_nbconvert() 