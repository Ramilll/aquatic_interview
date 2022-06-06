import pandas as pd


def process_df(df: pd.DataFrame):
    """ Parses one hour temperature samples into daily aggregates,
     with the start, end, high, and low of all the values of the Air Temperature
      for each day, at each weather station"""

    df["Measurement Timestamp"] = pd.to_datetime(df["Measurement Timestamp"])
    df.sort_values(by="Measurement Timestamp", inplace=True)
    df["Date"] = df["Measurement Timestamp"].dt.strftime('%m/%d/%Y')

    group_df = df.groupby(by=["Station Name", "Date"])[
        "Air Temperature"].agg(["min", "max", "first", "last"])
    rename_dict = {"min": "Min Temp", "max": "Max Temp",
                   "first": "First Temp", "last": "Last Temp"}
    group_df.rename(columns=rename_dict, inplace=True)

    return group_df


def process_csv(reader, writer):
    data = reader.readlines()

    with open("input.csv", "w") as file:
        for line in data:
            file.write(line)

    output_df = process_df(df=pd.read_csv("input.csv"))
    output_df.to_csv("output.csv", index=True)

    with open("output.csv", "r") as file:
        for line in file:
            writer.write(line)
