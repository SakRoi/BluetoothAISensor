import pandas as pd

if '__main__':
    '''Code to filter bad data from the .csv-file to ensure that K-means
    and neural network learn correctly'''

    df = pd.read_csv('data.csv')

    print(df)
    for x in df.index:

        #Delete bad sensor data
        if df.loc[x, "x"] > 2000 or df.loc[x, "x"] < 1100:
            df.drop(x, inplace=True)
            continue

        if df.loc[x, "y"] > 2000 or df.loc[x, "y"] < 1100:
            df.drop(x, inplace=True)
            continue

        if df.loc[x, "z"] > 2000 or df.loc[x, "z"] < 1100:
            df.drop(x, inplace=True)
            continue

        #Delete wrong direction data
        if df.loc[x, "direction"] == 0 and df.loc[x, "x"] < 1700:
            df.drop(x, inplace=True)
            continue

        if df.loc[x, "direction"] == 1 and df.loc[x, "x"] > 1400:
            df.drop(x, inplace=True)
            continue

        if df.loc[x, "direction"] == 2 and df.loc[x, "y"] < 1700:
            df.drop(x, inplace=True)
            continue

        if df.loc[x, "direction"] == 3 and df.loc[x, "y"] > 1400:
            df.drop(x, inplace=True)
            continue

        if df.loc[x, "direction"] == 4 and df.loc[x, "z"] < 1700:
            df.drop(x, inplace=True)
            continue

        if df.loc[x, "direction"] == 5 and df.loc[x, "z"] > 1400:
            df.drop(x, inplace=True)
            continue

    #Write the data to a .csv file
    print(df)
    df.to_csv('data.csv')


