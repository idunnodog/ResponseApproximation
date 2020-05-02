import pandas as pd
import numpy as np


# get percentile from dataframe
def percentile(n):
    def percentile_(x):
        return np.percentile(x, n)

    percentile_.__name__ = 'percentile_%s' % n
    return percentile_


# get count for dataframe
def getCount(n):
    def getCount_(x):
        return len(x)

    getCount_.__name__ = 'getCount_%s' % n
    return getCount_


# upload file to dataframe
def uploadFileToDataFrame(file):
    print("1/4 Upload data from file")
    return pd.read_csv(file, sep=',', usecols=['Start_Time', 'Display_Process_Name', 'exec_time'])


# get list of processes
def getProcessesName(df):
    return df['Display_Process_Name'].unique()


# group by time and queue
def groupByTimeAndQueue(df):
    print("2/4 Group data to get total count")
    #df['time'] = df['Start_Time'].str.extract('(?<=^)(.*:..):{1}', expand=True)
    df['time'] = df['Start_Time'].str.extract('(?<=^)(.*:[0-9])', expand=True)
    #    df2 = df.groupby(['time', 'Display_Process_Name'], as_index=False)['exec_time'].agg(
    #        [np.mean, np.min, np.max, percentile(90), getCount(90)])
    df2 = df.groupby(['time', 'Display_Process_Name'], as_index=False)['exec_time'].agg(
        [np.mean, percentile(90), getCount(90)])
    df2 = df2.reset_index()
    df_count = df2[df2['Display_Process_Name'] == "Out/fuck/queue4.rq"].copy()
    df_count = df_count.reset_index()
    df_count.rename(columns={'getCount_90': 'load'}, inplace=True)
    return df2, df_count


def mergeDataToAddAxis(file):
    df = groupByTimeAndQueue(uploadFileToDataFrame(file))
    print("3/4 Merge data")
    return pd.merge(df[1][['time', 'load']],
                    df[0],
                    on='time',
                    how='left')
    #return df

class StatHandler:
    @staticmethod
    def getData():
        result = mergeDataToAddAxis(r'/Users/computer/Documents/ResponseApproximation/Data/30_03_2020_15_00_sec.csv')
        processes = getProcessesName(result)
        return result,processes
