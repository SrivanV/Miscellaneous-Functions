# -*- coding: utf-8 -*-
import pandas

def CustomMetrics(InputDataframe):
    
    """
    The function serves to consolidate commonly necessary metrics into one dataframe. Both the input and output of the function is a Pandas dataframe.
    Specifically, the function will return :
            
        * The datatype of your input dataframe's column
        * A boolean flag of whether or not there are missing values in the in the input dataframe
        * The number of null values that exist in each of the input columns
        * The number of unique values in each of the input columns
    """
    
    DataframeMetrics = pandas.DataFrame(index=InputDataframe.columns,columns='ColumnDatatypes #UniqueValues NullValuesPresent #NullValues'.split())
    Columns = list(InputDataframe.columns)
    
    for Values in Columns:        
        DataframeMetrics['ColumnDatatypes'][Values] = InputDataframe[Values].dtypes
        DataframeMetrics['#UniqueValues'][Values] = InputDataframe[Values].nunique()
        DataframeMetrics['#NullValues'][Values] = InputDataframe[Values].isnull().sum()
        DataframeMetrics['NullValuesPresent'][Values] = InputDataframe[Values].isnull().values.any()
    
    print('The dimensions of the input dataframe are: {} rows by {} columns.'.format(len(InputDataframe.index), len(InputDataframe.columns)))
    return DataframeMetrics