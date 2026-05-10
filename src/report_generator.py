import pandas as pd

# -----------------------------
# GENERATE CSV REPORT
# -----------------------------

def generate_report(data, output_path):

    df = pd.DataFrame(data)

    df = df.sort_values(by="Score", ascending=False)

    df.to_csv(output_path, index=False)

    return df