import plotly.express as px
from pathlib import Path
import pandas as pd 
import random


def get_random_number():
    random_int = random.randint(0, 100)
    print(f"The number is {random_int}.")
    df = pd.DataFrame({"value": [random_int], "timestamp": [pd.Timestamp.now()]})
    return df 


def save_to_csv(df, path):
    df.to_csv(path, index=False, mode='a', header=None) 


def read_from_csv(path):
    df = pd.read_csv(path, header=None, names=["value", "timestamp"])
    return df


def display(df, output_path):
    fig = px.line(df, x='timestamp', y='value', title="Random Values")
    fig.write_html(output_path)
    print(f"Chart saved to {output_path}")



def main():
    # Create directory
    data_path = Path("data")
    data_path.mkdir(parents=True, exist_ok=True)
    data_filename = data_path / "random_number.csv"
    html_filename= data_path / "random_number.html"

    # Generate random numbers
    df = get_random_number()

    # Save to csv
    save_to_csv(df, data_filename)

    # Load full df
    full_df = read_from_csv(data_filename)
    display(full_df, html_filename)
    


if __name__ == "__main__":
    main()

