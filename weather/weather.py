import pandas as pd
import sys

my_data = pd.read_csv("stats.we", sep='  ', header = None, names=["City","Date","Weather"], engine='python')
my_data.Date = my_data.Date.astype('datetime64[ns]')

def Add(City, Date, Weather):
    if len((my_data[(my_data.City == City) & (my_data.Date == Date)]) > 0):
        print("already exists")
    else:
        fd = open('stats.we','a')
        fd.write(f'{City}  {Date}  {Weather}\n')
        fd.close()


def Forecast(City, Date):
    if len((my_data[(my_data.City == City) & (my_data.Date == Date)]) > 0):
        print(f"Weather forecast for {Date} in city {City} {my_data[(my_data.City == City) & (my_data.Date == Date)].iloc[0].Weather} degrees Celsius")

    elif len(my_data[(my_data.City == City)]) == 0:
        print("No information about this City")

    elif len(my_data[(my_data.Date < Date) & (my_data.City == City)]) == 0:
        df = my_data[(my_data.Date > Date) & (my_data.City == City)]
        dff = my_data[(my_data.Date < Date) & (my_data.City == City)]
        print(dff)
        print(f"Weather forecast for {Date} in city {City} {df[df.Date == df.Date.min()].iloc[0].Weather} degrees Celsius")

    elif len(my_data[(my_data.Date > Date) & (my_data.City == City)]) == 0:
        df2 = my_data[(my_data.Date < Date) & (my_data.City == City)]
        print(f"Weather forecast for {Date} in city {City} {df2[df2.Date == df2.Date.max()].iloc[0].Weather} degrees Celsius")

    else:
        df = my_data[(my_data.Date > Date) & (my_data.City == City)]
        df2 = my_data[(my_data.Date < Date) & (my_data.City == City)]
        print(f"Weather forecast for {Date} in city {City} {0.5 * (df[df.Date == df.Date.min()].iloc[0].Weather + df2[df2.Date == df2.Date.max()].iloc[0].Weather)} degrees Celsius")


if __name__ == "__main__":
    command_name = sys.argv[1]
    city = sys.argv[2]
    date = sys.argv[3]
    if command_name == "add":
        weather = sys.argv[4]
        Add(city, date, weather)
    if command_name == "forecast":
        Forecast(city, date)
