from prefect import flow, task
import plotly.express as px
from pathlib import Path
import pandas as pd 
import random
import time
import pdb


@task()
def get_random_number(max_value=100):
    random_int = random.randint(0, max_value)
    print(f"The number is {random_int}.")
    if random_int > 90:
        raise ValueError("Simulating a failure: The number is too high!")
    df = pd.DataFrame({"value": [random_int], "timestamp": [pd.Timestamp.now()]})
    return df 

@task(name="Save to CSV")
def save_to_csv(df, path):
    df.to_csv(path, index=False, mode='a', header=None) 
    print(f"Saved to {path}")

@task()
def read_from_csv(path):
    print(f"Reading from {path}")
    df = pd.read_csv(path, header=None, names=["value", "timestamp"])
    time.sleep(2)
    return df

@task(name='Display Chart', description="Stores an hmtl file with a chart")
def display(df, output_path):
    fig = px.line(df, x='timestamp', y='value', title="Random Values")
    fig.write_html(output_path)
    print(f"Chart saved to {output_path}")


@flow(name="Random Numbers", retries=2, retry_delay_seconds=2, log_prints=True)
def main(max_value=100):
    print('Starting the flow...')

    # Create directory
    data_path = Path("data")
    data_path.mkdir(parents=True, exist_ok=True)
    csv_filename = data_path / "random_number.csv"
    html_filename = data_path / "random_number.html"

    # Generate random numbers
    df = get_random_number(max_value)

    # Save to csv
    save_to_csv(df, csv_filename)

    # Load full df
    full_df = read_from_csv(csv_filename)
    display(full_df, html_filename)
    


if __name__ == "__main__":
    main.serve(
        name="Dataharvest",
        cron="* * * * *",
        parameters={"max_value": 20},
    )
