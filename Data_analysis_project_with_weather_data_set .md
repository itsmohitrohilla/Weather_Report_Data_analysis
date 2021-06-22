# The Weather DataSet

Big data analysis

The weather dataset is time series data set with per hour information about the weather
condition on a particular location. it records Temp., relative humidity, wind speed, visibility pressure and condition

* The data is available in the form of .csv file. 
* We will use pandas to analyis the data set.


```python
#importing pandas libary

import pandas as pd
```


```python
#reading weather .csv file and assign to the variable 'df'.

df = pd.read_csv('Weather_data.csv')
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2012 0:00</td>
      <td>-1.8</td>
      <td>-3.9</td>
      <td>86</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/1/2012 1:00</td>
      <td>-1.8</td>
      <td>-3.7</td>
      <td>87</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/1/2012 2:00</td>
      <td>-1.8</td>
      <td>-3.4</td>
      <td>89</td>
      <td>7</td>
      <td>4.0</td>
      <td>101.26</td>
      <td>Freezing Drizzle,Fog</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/1/2012 3:00</td>
      <td>-1.5</td>
      <td>-3.2</td>
      <td>88</td>
      <td>6</td>
      <td>4.0</td>
      <td>101.27</td>
      <td>Freezing Drizzle,Fog</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/1/2012 4:00</td>
      <td>-1.5</td>
      <td>-3.3</td>
      <td>88</td>
      <td>7</td>
      <td>4.8</td>
      <td>101.23</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8779</th>
      <td>12/31/2012 19:00</td>
      <td>0.1</td>
      <td>-2.7</td>
      <td>81</td>
      <td>30</td>
      <td>9.7</td>
      <td>100.13</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8780</th>
      <td>12/31/2012 20:00</td>
      <td>0.2</td>
      <td>-2.4</td>
      <td>83</td>
      <td>24</td>
      <td>9.7</td>
      <td>100.03</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8781</th>
      <td>12/31/2012 21:00</td>
      <td>-0.5</td>
      <td>-1.5</td>
      <td>93</td>
      <td>28</td>
      <td>4.8</td>
      <td>99.95</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8782</th>
      <td>12/31/2012 22:00</td>
      <td>-0.2</td>
      <td>-1.8</td>
      <td>89</td>
      <td>28</td>
      <td>9.7</td>
      <td>99.91</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8783</th>
      <td>12/31/2012 23:00</td>
      <td>0.0</td>
      <td>-2.1</td>
      <td>86</td>
      <td>30</td>
      <td>11.3</td>
      <td>99.89</td>
      <td>Snow</td>
    </tr>
  </tbody>
</table>
<p>8784 rows × 8 columns</p>
</div>





# Exploring and analysing the data set deeply to understand easily




```python
#1 - We are useing head() to print top 5 rows from the data.
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2012 0:00</td>
      <td>-1.8</td>
      <td>-3.9</td>
      <td>86</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/1/2012 1:00</td>
      <td>-1.8</td>
      <td>-3.7</td>
      <td>87</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/1/2012 2:00</td>
      <td>-1.8</td>
      <td>-3.4</td>
      <td>89</td>
      <td>7</td>
      <td>4.0</td>
      <td>101.26</td>
      <td>Freezing Drizzle,Fog</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/1/2012 3:00</td>
      <td>-1.5</td>
      <td>-3.2</td>
      <td>88</td>
      <td>6</td>
      <td>4.0</td>
      <td>101.27</td>
      <td>Freezing Drizzle,Fog</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/1/2012 4:00</td>
      <td>-1.5</td>
      <td>-3.3</td>
      <td>88</td>
      <td>7</td>
      <td>4.8</td>
      <td>101.23</td>
      <td>Fog</td>
    </tr>
  </tbody>
</table>
</div>






```python
#2 We are useing 'shape' command to check the size and number of rows and column in the 
#dataframe
```


```python
df.shape
```




    (8784, 8)






```python
#3 we are useing the 'index' command to check the length of index in the data frame.
```


```python
df.index
```




    RangeIndex(start=0, stop=8784, step=1)






```python
#4 we are using the 'columns' command to check names of all column present in the data frame.
```


```python
df.columns
```




    Index(['Date/Time', 'Temp_C', 'Dew Point Temp_C', 'Rel Hum_%',
           'Wind Speed_km/h', 'Visibility_km', 'Press_kPa', 'Weather'],
          dtype='object')






```python
# 5 we are using ".dtypes" to check the data type of each column.
```


```python
df.dtypes
```




    Date/Time            object
    Temp_C              float64
    Dew Point Temp_C    float64
    Rel Hum_%             int64
    Wind Speed_km/h       int64
    Visibility_km       float64
    Press_kPa           float64
    Weather              object
    dtype: object






```python
#6 we are using 'unique()' to check the unique value in the particular column.
```


```python
df['Weather'].unique()
```




    array(['Fog', 'Freezing Drizzle,Fog', 'Mostly Cloudy', 'Cloudy', 'Rain',
           'Rain Showers', 'Mainly Clear', 'Snow Showers', 'Snow', 'Clear',
           'Freezing Rain,Fog', 'Freezing Rain', 'Freezing Drizzle',
           'Rain,Snow', 'Moderate Snow', 'Freezing Drizzle,Snow',
           'Freezing Rain,Snow Grains', 'Snow,Blowing Snow', 'Freezing Fog',
           'Haze', 'Rain,Fog', 'Drizzle,Fog', 'Drizzle',
           'Freezing Drizzle,Haze', 'Freezing Rain,Haze', 'Snow,Haze',
           'Snow,Fog', 'Snow,Ice Pellets', 'Rain,Haze', 'Thunderstorms,Rain',
           'Thunderstorms,Rain Showers', 'Thunderstorms,Heavy Rain Showers',
           'Thunderstorms,Rain Showers,Fog', 'Thunderstorms',
           'Thunderstorms,Rain,Fog',
           'Thunderstorms,Moderate Rain Showers,Fog', 'Rain Showers,Fog',
           'Rain Showers,Snow Showers', 'Snow Pellets', 'Rain,Snow,Fog',
           'Moderate Rain,Fog', 'Freezing Rain,Ice Pellets,Fog',
           'Drizzle,Ice Pellets,Fog', 'Drizzle,Snow', 'Rain,Ice Pellets',
           'Drizzle,Snow,Fog', 'Rain,Snow Grains', 'Rain,Snow,Ice Pellets',
           'Snow Showers,Fog', 'Moderate Snow,Blowing Snow'], dtype=object)






```python
#7 we are using ".nunique" to check the total number of unique value in whole data frame.
```


```python
df.nunique()
```




    Date/Time           8784
    Temp_C               533
    Dew Point Temp_C     489
    Rel Hum_%             83
    Wind Speed_km/h       34
    Visibility_km         24
    Press_kPa            518
    Weather               50
    dtype: int64






```python
#8 We are using ".count()" to check the number of null value in the each column of data frame.
```


```python
df.count()
```




    Date/Time           8784
    Temp_C              8784
    Dew Point Temp_C    8784
    Rel Hum_%           8784
    Wind Speed_km/h     8784
    Visibility_km       8784
    Press_kPa           8784
    Weather             8784
    dtype: int64






```python
#9 we are using "info()"  to check the absic information of the data frame.
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8784 entries, 0 to 8783
    Data columns (total 8 columns):
     #   Column            Non-Null Count  Dtype  
    ---  ------            --------------  -----  
     0   Date/Time         8784 non-null   object 
     1   Temp_C            8784 non-null   float64
     2   Dew Point Temp_C  8784 non-null   float64
     3   Rel Hum_%         8784 non-null   int64  
     4   Wind Speed_km/h   8784 non-null   int64  
     5   Visibility_km     8784 non-null   float64
     6   Press_kPa         8784 non-null   float64
     7   Weather           8784 non-null   object 
    dtypes: float64(4), int64(2), object(2)
    memory usage: 549.1+ KB



```python
#10 we are using "Value_count()" to check the number of unique value with there count in 
#particular column of the data frame.
```


```python
df['Weather'].value_counts()
```




    Mainly Clear                               2106
    Mostly Cloudy                              2069
    Cloudy                                     1728
    Clear                                      1326
    Snow                                        390
    Rain                                        306
    Rain Showers                                188
    Fog                                         150
    Rain,Fog                                    116
    Drizzle,Fog                                  80
    Snow Showers                                 60
    Drizzle                                      41
    Snow,Fog                                     37
    Snow,Blowing Snow                            19
    Rain,Snow                                    18
    Thunderstorms,Rain Showers                   16
    Haze                                         16
    Drizzle,Snow,Fog                             15
    Freezing Rain                                14
    Freezing Drizzle,Snow                        11
    Freezing Drizzle                              7
    Freezing Drizzle,Fog                          6
    Snow,Ice Pellets                              6
    Snow,Haze                                     5
    Snow Showers,Fog                              4
    Rain,Snow,Ice Pellets                         4
    Moderate Snow                                 4
    Freezing Fog                                  4
    Freezing Rain,Fog                             4
    Freezing Drizzle,Haze                         3
    Rain,Haze                                     3
    Thunderstorms,Rain Showers,Fog                3
    Thunderstorms,Rain                            3
    Rain Showers,Snow Showers                     2
    Drizzle,Snow                                  2
    Freezing Rain,Haze                            2
    Thunderstorms                                 2
    Moderate Snow,Blowing Snow                    2
    Rain Showers,Fog                              1
    Thunderstorms,Moderate Rain Showers,Fog       1
    Snow Pellets                                  1
    Rain,Snow Grains                              1
    Drizzle,Ice Pellets,Fog                       1
    Moderate Rain,Fog                             1
    Freezing Rain,Ice Pellets,Fog                 1
    Thunderstorms,Heavy Rain Showers              1
    Rain,Snow,Fog                                 1
    Rain,Ice Pellets                              1
    Thunderstorms,Rain,Fog                        1
    Freezing Rain,Snow Grains                     1
    Name: Weather, dtype: int64



# Tasks

# Q1.                                                                                                    Find all the unique "Wind Speed" value from the data frame


```python
print("Numner of unique value of windspeed = ",df['Wind Speed_km/h'].nunique())
```

    Numner of unique value of windspeed =  34



```python
df['Wind Speed_km/h'].unique() #answer
```




    array([ 4,  7,  6,  9, 15, 13, 20, 22, 19, 24, 30, 35, 39, 32, 33, 26, 44,
           43, 48, 37, 28, 17, 11,  0, 83, 70, 57, 46, 41, 52, 50, 63, 54,  2])



# Q2. Find the number of times when the weather is exactly clear.


```python
clear = df[df['Weather'] == 'Clear'] #answer
```


```python
clear
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>67</th>
      <td>1/3/2012 19:00</td>
      <td>-16.9</td>
      <td>-24.8</td>
      <td>50</td>
      <td>24</td>
      <td>25.0</td>
      <td>101.74</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>114</th>
      <td>1/5/2012 18:00</td>
      <td>-7.1</td>
      <td>-14.4</td>
      <td>56</td>
      <td>11</td>
      <td>25.0</td>
      <td>100.71</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>115</th>
      <td>1/5/2012 19:00</td>
      <td>-9.2</td>
      <td>-15.4</td>
      <td>61</td>
      <td>7</td>
      <td>25.0</td>
      <td>100.80</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>116</th>
      <td>1/5/2012 20:00</td>
      <td>-9.8</td>
      <td>-15.7</td>
      <td>62</td>
      <td>9</td>
      <td>25.0</td>
      <td>100.83</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>117</th>
      <td>1/5/2012 21:00</td>
      <td>-9.0</td>
      <td>-14.8</td>
      <td>63</td>
      <td>13</td>
      <td>25.0</td>
      <td>100.83</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8646</th>
      <td>12/26/2012 6:00</td>
      <td>-13.4</td>
      <td>-14.8</td>
      <td>89</td>
      <td>4</td>
      <td>25.0</td>
      <td>102.47</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>8698</th>
      <td>12/28/2012 10:00</td>
      <td>-6.1</td>
      <td>-8.6</td>
      <td>82</td>
      <td>19</td>
      <td>24.1</td>
      <td>101.27</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>8713</th>
      <td>12/29/2012 1:00</td>
      <td>-11.9</td>
      <td>-13.6</td>
      <td>87</td>
      <td>11</td>
      <td>25.0</td>
      <td>101.31</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>8714</th>
      <td>12/29/2012 2:00</td>
      <td>-11.8</td>
      <td>-13.1</td>
      <td>90</td>
      <td>13</td>
      <td>25.0</td>
      <td>101.33</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>8756</th>
      <td>12/30/2012 20:00</td>
      <td>-13.8</td>
      <td>-16.5</td>
      <td>80</td>
      <td>24</td>
      <td>25.0</td>
      <td>101.52</td>
      <td>Clear</td>
    </tr>
  </tbody>
</table>
<p>1326 rows × 8 columns</p>
</div>




```python
print(" The number of rows and column in dataframe when the weather was clear =",clear.shape)
```

     The number of rows and column in dataframe when the weather was clear = (1326, 8)


# Q3. Find the number of times when the wind was exactly 4km/h.


```python
speed = df[df['Wind Speed_km/h'] == 4] #answer
```


```python
speed
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2012 0:00</td>
      <td>-1.8</td>
      <td>-3.9</td>
      <td>86</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/1/2012 1:00</td>
      <td>-1.8</td>
      <td>-3.7</td>
      <td>87</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>96</th>
      <td>1/5/2012 0:00</td>
      <td>-8.8</td>
      <td>-11.7</td>
      <td>79</td>
      <td>4</td>
      <td>9.7</td>
      <td>100.32</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>101</th>
      <td>1/5/2012 5:00</td>
      <td>-7.0</td>
      <td>-9.5</td>
      <td>82</td>
      <td>4</td>
      <td>4.0</td>
      <td>100.19</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>146</th>
      <td>1/7/2012 2:00</td>
      <td>-8.1</td>
      <td>-11.1</td>
      <td>79</td>
      <td>4</td>
      <td>19.3</td>
      <td>100.15</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8768</th>
      <td>12/31/2012 8:00</td>
      <td>-8.6</td>
      <td>-10.3</td>
      <td>87</td>
      <td>4</td>
      <td>3.2</td>
      <td>101.14</td>
      <td>Snow Showers</td>
    </tr>
    <tr>
      <th>8769</th>
      <td>12/31/2012 9:00</td>
      <td>-8.1</td>
      <td>-9.6</td>
      <td>89</td>
      <td>4</td>
      <td>2.4</td>
      <td>101.09</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8770</th>
      <td>12/31/2012 10:00</td>
      <td>-7.4</td>
      <td>-8.9</td>
      <td>89</td>
      <td>4</td>
      <td>6.4</td>
      <td>101.05</td>
      <td>Snow,Fog</td>
    </tr>
    <tr>
      <th>8772</th>
      <td>12/31/2012 12:00</td>
      <td>-5.8</td>
      <td>-7.5</td>
      <td>88</td>
      <td>4</td>
      <td>12.9</td>
      <td>100.78</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8773</th>
      <td>12/31/2012 13:00</td>
      <td>-4.6</td>
      <td>-6.6</td>
      <td>86</td>
      <td>4</td>
      <td>12.9</td>
      <td>100.63</td>
      <td>Snow</td>
    </tr>
  </tbody>
</table>
<p>474 rows × 8 columns</p>
</div>




```python
print(" The number of rows and column in dataframe \n when the wind speed was exactly 4 km/h =",clear.shape)
```

     The number of rows and column in dataframe 
     when the wind speed was exactly 4 km/h = (1326, 8)


# Q4. Find out all null values in the dataframe.


```python
df.isnull().sum() #answer
```




    Date/Time           0
    Temp_C              0
    Dew Point Temp_C    0
    Rel Hum_%           0
    Wind Speed_km/h     0
    Visibility_km       0
    Press_kPa           0
    Weather             0
    dtype: int64




```python
df.notnull().sum() #answer
```




    Date/Time           8784
    Temp_C              8784
    Dew Point Temp_C    8784
    Rel Hum_%           8784
    Wind Speed_km/h     8784
    Visibility_km       8784
    Press_kPa           8784
    Weather             8784
    dtype: int64



# Q5 Rename the "weather" column name to "weather_condition".


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8784 entries, 0 to 8783
    Data columns (total 8 columns):
     #   Column            Non-Null Count  Dtype  
    ---  ------            --------------  -----  
     0   Date/Time         8784 non-null   object 
     1   Temp_C            8784 non-null   float64
     2   Dew Point Temp_C  8784 non-null   float64
     3   Rel Hum_%         8784 non-null   int64  
     4   Wind Speed_km/h   8784 non-null   int64  
     5   Visibility_km     8784 non-null   float64
     6   Press_kPa         8784 non-null   float64
     7   Weather           8784 non-null   object 
    dtypes: float64(4), int64(2), object(2)
    memory usage: 549.1+ KB



```python
col_change = df.rename(columns = {'Weather' : 'Weather_condition'})  #answer
```


```python
col_change.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8784 entries, 0 to 8783
    Data columns (total 8 columns):
     #   Column             Non-Null Count  Dtype  
    ---  ------             --------------  -----  
     0   Date/Time          8784 non-null   object 
     1   Temp_C             8784 non-null   float64
     2   Dew Point Temp_C   8784 non-null   float64
     3   Rel Hum_%          8784 non-null   int64  
     4   Wind Speed_km/h    8784 non-null   int64  
     5   Visibility_km      8784 non-null   float64
     6   Press_kPa          8784 non-null   float64
     7   Weather_condition  8784 non-null   object 
    dtypes: float64(4), int64(2), object(2)
    memory usage: 549.1+ KB


# Q6 What is the mean  of 'Visibility' ?


```python
df['Visibility_km'].mean()  #answer
```




    27.664446721311478



# Q7. What is the Standard deviation of Pressure in the data?


```python
df['Press_kPa'].std() #answer
```




    0.8440047459486483



# Q8 what is the variance of Relative humadity in the data frame.


```python
df['Rel Hum_%'].var()
```




    286.24855019850196



# Q9 Find all instance when snow was recorded.


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather_condition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2012 0:00</td>
      <td>-1.8</td>
      <td>-3.9</td>
      <td>86</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/1/2012 1:00</td>
      <td>-1.8</td>
      <td>-3.7</td>
      <td>87</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/1/2012 2:00</td>
      <td>-1.8</td>
      <td>-3.4</td>
      <td>89</td>
      <td>7</td>
      <td>4.0</td>
      <td>101.26</td>
      <td>Freezing Drizzle,Fog</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/1/2012 3:00</td>
      <td>-1.5</td>
      <td>-3.2</td>
      <td>88</td>
      <td>6</td>
      <td>4.0</td>
      <td>101.27</td>
      <td>Freezing Drizzle,Fog</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/1/2012 4:00</td>
      <td>-1.5</td>
      <td>-3.3</td>
      <td>88</td>
      <td>7</td>
      <td>4.8</td>
      <td>101.23</td>
      <td>Fog</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['Weather_condition'].str.contains('Snow')] #answer
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather_condition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>41</th>
      <td>1/2/2012 17:00</td>
      <td>-2.1</td>
      <td>-9.5</td>
      <td>57</td>
      <td>22</td>
      <td>25.0</td>
      <td>99.66</td>
      <td>Snow Showers</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1/2/2012 20:00</td>
      <td>-5.6</td>
      <td>-13.4</td>
      <td>54</td>
      <td>24</td>
      <td>25.0</td>
      <td>100.07</td>
      <td>Snow Showers</td>
    </tr>
    <tr>
      <th>45</th>
      <td>1/2/2012 21:00</td>
      <td>-5.8</td>
      <td>-12.8</td>
      <td>58</td>
      <td>26</td>
      <td>25.0</td>
      <td>100.15</td>
      <td>Snow Showers</td>
    </tr>
    <tr>
      <th>47</th>
      <td>1/2/2012 23:00</td>
      <td>-7.4</td>
      <td>-14.1</td>
      <td>59</td>
      <td>17</td>
      <td>19.3</td>
      <td>100.27</td>
      <td>Snow Showers</td>
    </tr>
    <tr>
      <th>48</th>
      <td>1/3/2012 0:00</td>
      <td>-9.0</td>
      <td>-16.0</td>
      <td>57</td>
      <td>28</td>
      <td>25.0</td>
      <td>100.35</td>
      <td>Snow Showers</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8779</th>
      <td>12/31/2012 19:00</td>
      <td>0.1</td>
      <td>-2.7</td>
      <td>81</td>
      <td>30</td>
      <td>9.7</td>
      <td>100.13</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8780</th>
      <td>12/31/2012 20:00</td>
      <td>0.2</td>
      <td>-2.4</td>
      <td>83</td>
      <td>24</td>
      <td>9.7</td>
      <td>100.03</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8781</th>
      <td>12/31/2012 21:00</td>
      <td>-0.5</td>
      <td>-1.5</td>
      <td>93</td>
      <td>28</td>
      <td>4.8</td>
      <td>99.95</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8782</th>
      <td>12/31/2012 22:00</td>
      <td>-0.2</td>
      <td>-1.8</td>
      <td>89</td>
      <td>28</td>
      <td>9.7</td>
      <td>99.91</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>8783</th>
      <td>12/31/2012 23:00</td>
      <td>0.0</td>
      <td>-2.1</td>
      <td>86</td>
      <td>30</td>
      <td>11.3</td>
      <td>99.89</td>
      <td>Snow</td>
    </tr>
  </tbody>
</table>
<p>583 rows × 8 columns</p>
</div>



# Q10. Find all instance when wind speed is above 24 and visibility is 25


```python
df.loc[(df['Wind Speed_km/h'] > 24 ) & (df['Visibility_km'] == 25.0)] #answer
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather_condition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>23</th>
      <td>1/1/2012 23:00</td>
      <td>5.3</td>
      <td>2.0</td>
      <td>79</td>
      <td>30</td>
      <td>25.0</td>
      <td>99.31</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1/2/2012 0:00</td>
      <td>5.2</td>
      <td>1.5</td>
      <td>77</td>
      <td>35</td>
      <td>25.0</td>
      <td>99.26</td>
      <td>Rain Showers</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1/2/2012 1:00</td>
      <td>4.6</td>
      <td>0.0</td>
      <td>72</td>
      <td>39</td>
      <td>25.0</td>
      <td>99.26</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1/2/2012 2:00</td>
      <td>3.9</td>
      <td>-0.9</td>
      <td>71</td>
      <td>32</td>
      <td>25.0</td>
      <td>99.26</td>
      <td>Mostly Cloudy</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1/2/2012 3:00</td>
      <td>3.7</td>
      <td>-1.5</td>
      <td>69</td>
      <td>33</td>
      <td>25.0</td>
      <td>99.30</td>
      <td>Mostly Cloudy</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8705</th>
      <td>12/28/2012 17:00</td>
      <td>-8.6</td>
      <td>-12.0</td>
      <td>76</td>
      <td>26</td>
      <td>25.0</td>
      <td>101.34</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>8753</th>
      <td>12/30/2012 17:00</td>
      <td>-12.1</td>
      <td>-15.8</td>
      <td>74</td>
      <td>28</td>
      <td>25.0</td>
      <td>101.26</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>8755</th>
      <td>12/30/2012 19:00</td>
      <td>-13.4</td>
      <td>-16.5</td>
      <td>77</td>
      <td>26</td>
      <td>25.0</td>
      <td>101.47</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>8759</th>
      <td>12/30/2012 23:00</td>
      <td>-12.1</td>
      <td>-15.1</td>
      <td>78</td>
      <td>28</td>
      <td>25.0</td>
      <td>101.52</td>
      <td>Mostly Cloudy</td>
    </tr>
    <tr>
      <th>8760</th>
      <td>12/31/2012 0:00</td>
      <td>-11.1</td>
      <td>-14.4</td>
      <td>77</td>
      <td>26</td>
      <td>25.0</td>
      <td>101.51</td>
      <td>Cloudy</td>
    </tr>
  </tbody>
</table>
<p>308 rows × 8 columns</p>
</div>



# Q11. What is the mean value of each column against each weather condition?


```python
df.groupby(['Weather_condition']).mean() #answer
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
    </tr>
    <tr>
      <th>Weather_condition</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Clear</th>
      <td>6.825716</td>
      <td>0.089367</td>
      <td>64.497738</td>
      <td>10.557315</td>
      <td>30.153243</td>
      <td>101.587443</td>
    </tr>
    <tr>
      <th>Cloudy</th>
      <td>7.970544</td>
      <td>2.375810</td>
      <td>69.592593</td>
      <td>16.127315</td>
      <td>26.625752</td>
      <td>100.911441</td>
    </tr>
    <tr>
      <th>Drizzle</th>
      <td>7.353659</td>
      <td>5.504878</td>
      <td>88.243902</td>
      <td>16.097561</td>
      <td>17.931707</td>
      <td>100.435366</td>
    </tr>
    <tr>
      <th>Drizzle,Fog</th>
      <td>8.067500</td>
      <td>7.033750</td>
      <td>93.275000</td>
      <td>11.862500</td>
      <td>5.257500</td>
      <td>100.786625</td>
    </tr>
    <tr>
      <th>Drizzle,Ice Pellets,Fog</th>
      <td>0.400000</td>
      <td>-0.700000</td>
      <td>92.000000</td>
      <td>20.000000</td>
      <td>4.000000</td>
      <td>100.790000</td>
    </tr>
    <tr>
      <th>Drizzle,Snow</th>
      <td>1.050000</td>
      <td>0.150000</td>
      <td>93.500000</td>
      <td>14.000000</td>
      <td>10.500000</td>
      <td>100.890000</td>
    </tr>
    <tr>
      <th>Drizzle,Snow,Fog</th>
      <td>0.693333</td>
      <td>0.120000</td>
      <td>95.866667</td>
      <td>15.533333</td>
      <td>5.513333</td>
      <td>99.281333</td>
    </tr>
    <tr>
      <th>Fog</th>
      <td>4.303333</td>
      <td>3.159333</td>
      <td>92.286667</td>
      <td>7.946667</td>
      <td>6.248000</td>
      <td>101.184067</td>
    </tr>
    <tr>
      <th>Freezing Drizzle</th>
      <td>-5.657143</td>
      <td>-8.000000</td>
      <td>83.571429</td>
      <td>16.571429</td>
      <td>9.200000</td>
      <td>100.202857</td>
    </tr>
    <tr>
      <th>Freezing Drizzle,Fog</th>
      <td>-2.533333</td>
      <td>-4.183333</td>
      <td>88.500000</td>
      <td>17.000000</td>
      <td>5.266667</td>
      <td>100.441667</td>
    </tr>
    <tr>
      <th>Freezing Drizzle,Haze</th>
      <td>-5.433333</td>
      <td>-8.000000</td>
      <td>82.000000</td>
      <td>10.333333</td>
      <td>2.666667</td>
      <td>100.316667</td>
    </tr>
    <tr>
      <th>Freezing Drizzle,Snow</th>
      <td>-5.109091</td>
      <td>-7.072727</td>
      <td>86.090909</td>
      <td>16.272727</td>
      <td>5.872727</td>
      <td>100.520909</td>
    </tr>
    <tr>
      <th>Freezing Fog</th>
      <td>-7.575000</td>
      <td>-9.250000</td>
      <td>87.750000</td>
      <td>4.750000</td>
      <td>0.650000</td>
      <td>102.320000</td>
    </tr>
    <tr>
      <th>Freezing Rain</th>
      <td>-3.885714</td>
      <td>-6.078571</td>
      <td>84.642857</td>
      <td>19.214286</td>
      <td>8.242857</td>
      <td>99.647143</td>
    </tr>
    <tr>
      <th>Freezing Rain,Fog</th>
      <td>-2.225000</td>
      <td>-3.750000</td>
      <td>89.500000</td>
      <td>15.500000</td>
      <td>7.550000</td>
      <td>99.945000</td>
    </tr>
    <tr>
      <th>Freezing Rain,Haze</th>
      <td>-4.900000</td>
      <td>-7.450000</td>
      <td>82.500000</td>
      <td>7.500000</td>
      <td>2.400000</td>
      <td>100.375000</td>
    </tr>
    <tr>
      <th>Freezing Rain,Ice Pellets,Fog</th>
      <td>-2.600000</td>
      <td>-3.700000</td>
      <td>92.000000</td>
      <td>28.000000</td>
      <td>8.000000</td>
      <td>100.950000</td>
    </tr>
    <tr>
      <th>Freezing Rain,Snow Grains</th>
      <td>-5.000000</td>
      <td>-7.300000</td>
      <td>84.000000</td>
      <td>32.000000</td>
      <td>4.800000</td>
      <td>98.560000</td>
    </tr>
    <tr>
      <th>Haze</th>
      <td>-0.200000</td>
      <td>-2.975000</td>
      <td>81.625000</td>
      <td>10.437500</td>
      <td>7.831250</td>
      <td>101.482500</td>
    </tr>
    <tr>
      <th>Mainly Clear</th>
      <td>12.558927</td>
      <td>4.581671</td>
      <td>60.667142</td>
      <td>14.144824</td>
      <td>34.264862</td>
      <td>101.248832</td>
    </tr>
    <tr>
      <th>Moderate Rain,Fog</th>
      <td>1.700000</td>
      <td>0.800000</td>
      <td>94.000000</td>
      <td>17.000000</td>
      <td>6.400000</td>
      <td>99.980000</td>
    </tr>
    <tr>
      <th>Moderate Snow</th>
      <td>-5.525000</td>
      <td>-7.250000</td>
      <td>87.750000</td>
      <td>33.750000</td>
      <td>0.750000</td>
      <td>100.275000</td>
    </tr>
    <tr>
      <th>Moderate Snow,Blowing Snow</th>
      <td>-5.450000</td>
      <td>-6.500000</td>
      <td>92.500000</td>
      <td>40.000000</td>
      <td>0.600000</td>
      <td>100.570000</td>
    </tr>
    <tr>
      <th>Mostly Cloudy</th>
      <td>10.574287</td>
      <td>3.131174</td>
      <td>62.102465</td>
      <td>15.813920</td>
      <td>31.253842</td>
      <td>101.025288</td>
    </tr>
    <tr>
      <th>Rain</th>
      <td>9.786275</td>
      <td>7.042810</td>
      <td>83.624183</td>
      <td>19.254902</td>
      <td>18.856536</td>
      <td>100.233333</td>
    </tr>
    <tr>
      <th>Rain Showers</th>
      <td>13.722340</td>
      <td>9.187766</td>
      <td>75.159574</td>
      <td>17.132979</td>
      <td>22.816489</td>
      <td>100.404043</td>
    </tr>
    <tr>
      <th>Rain Showers,Fog</th>
      <td>12.800000</td>
      <td>12.100000</td>
      <td>96.000000</td>
      <td>13.000000</td>
      <td>6.400000</td>
      <td>99.830000</td>
    </tr>
    <tr>
      <th>Rain Showers,Snow Showers</th>
      <td>2.150000</td>
      <td>-1.500000</td>
      <td>76.500000</td>
      <td>22.500000</td>
      <td>21.700000</td>
      <td>101.100000</td>
    </tr>
    <tr>
      <th>Rain,Fog</th>
      <td>8.273276</td>
      <td>7.219828</td>
      <td>93.189655</td>
      <td>14.793103</td>
      <td>6.873276</td>
      <td>100.500862</td>
    </tr>
    <tr>
      <th>Rain,Haze</th>
      <td>4.633333</td>
      <td>2.066667</td>
      <td>83.333333</td>
      <td>11.666667</td>
      <td>6.700000</td>
      <td>100.540000</td>
    </tr>
    <tr>
      <th>Rain,Ice Pellets</th>
      <td>0.600000</td>
      <td>-0.600000</td>
      <td>92.000000</td>
      <td>24.000000</td>
      <td>9.700000</td>
      <td>100.120000</td>
    </tr>
    <tr>
      <th>Rain,Snow</th>
      <td>1.055556</td>
      <td>-0.566667</td>
      <td>89.000000</td>
      <td>28.388889</td>
      <td>11.672222</td>
      <td>99.951111</td>
    </tr>
    <tr>
      <th>Rain,Snow Grains</th>
      <td>1.900000</td>
      <td>-2.100000</td>
      <td>75.000000</td>
      <td>26.000000</td>
      <td>25.000000</td>
      <td>100.600000</td>
    </tr>
    <tr>
      <th>Rain,Snow,Fog</th>
      <td>0.800000</td>
      <td>0.300000</td>
      <td>96.000000</td>
      <td>9.000000</td>
      <td>6.400000</td>
      <td>100.730000</td>
    </tr>
    <tr>
      <th>Rain,Snow,Ice Pellets</th>
      <td>1.100000</td>
      <td>-0.175000</td>
      <td>91.500000</td>
      <td>23.250000</td>
      <td>6.000000</td>
      <td>100.105000</td>
    </tr>
    <tr>
      <th>Snow</th>
      <td>-4.524103</td>
      <td>-7.623333</td>
      <td>79.307692</td>
      <td>20.038462</td>
      <td>11.171795</td>
      <td>100.536103</td>
    </tr>
    <tr>
      <th>Snow Pellets</th>
      <td>0.700000</td>
      <td>-6.400000</td>
      <td>59.000000</td>
      <td>35.000000</td>
      <td>2.400000</td>
      <td>99.700000</td>
    </tr>
    <tr>
      <th>Snow Showers</th>
      <td>-3.506667</td>
      <td>-7.866667</td>
      <td>72.350000</td>
      <td>19.233333</td>
      <td>20.158333</td>
      <td>100.963500</td>
    </tr>
    <tr>
      <th>Snow Showers,Fog</th>
      <td>-10.675000</td>
      <td>-11.900000</td>
      <td>90.750000</td>
      <td>13.750000</td>
      <td>7.025000</td>
      <td>101.292500</td>
    </tr>
    <tr>
      <th>Snow,Blowing Snow</th>
      <td>-5.410526</td>
      <td>-7.621053</td>
      <td>84.473684</td>
      <td>34.842105</td>
      <td>4.105263</td>
      <td>99.704737</td>
    </tr>
    <tr>
      <th>Snow,Fog</th>
      <td>-5.075676</td>
      <td>-6.364865</td>
      <td>90.675676</td>
      <td>17.324324</td>
      <td>4.537838</td>
      <td>100.688649</td>
    </tr>
    <tr>
      <th>Snow,Haze</th>
      <td>-4.020000</td>
      <td>-6.860000</td>
      <td>80.600000</td>
      <td>5.000000</td>
      <td>4.640000</td>
      <td>100.782000</td>
    </tr>
    <tr>
      <th>Snow,Ice Pellets</th>
      <td>-1.883333</td>
      <td>-3.666667</td>
      <td>87.666667</td>
      <td>23.833333</td>
      <td>7.416667</td>
      <td>100.548333</td>
    </tr>
    <tr>
      <th>Thunderstorms</th>
      <td>24.150000</td>
      <td>19.750000</td>
      <td>77.000000</td>
      <td>7.500000</td>
      <td>24.550000</td>
      <td>100.230000</td>
    </tr>
    <tr>
      <th>Thunderstorms,Heavy Rain Showers</th>
      <td>10.900000</td>
      <td>9.000000</td>
      <td>88.000000</td>
      <td>9.000000</td>
      <td>2.400000</td>
      <td>100.260000</td>
    </tr>
    <tr>
      <th>Thunderstorms,Moderate Rain Showers,Fog</th>
      <td>19.600000</td>
      <td>18.500000</td>
      <td>93.000000</td>
      <td>15.000000</td>
      <td>3.200000</td>
      <td>100.010000</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain</th>
      <td>20.433333</td>
      <td>18.533333</td>
      <td>89.000000</td>
      <td>15.666667</td>
      <td>19.833333</td>
      <td>100.420000</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain Showers</th>
      <td>20.037500</td>
      <td>17.618750</td>
      <td>86.375000</td>
      <td>18.312500</td>
      <td>15.893750</td>
      <td>100.233750</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain Showers,Fog</th>
      <td>21.600000</td>
      <td>18.700000</td>
      <td>84.000000</td>
      <td>19.666667</td>
      <td>9.700000</td>
      <td>100.063333</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain,Fog</th>
      <td>20.600000</td>
      <td>18.600000</td>
      <td>88.000000</td>
      <td>19.000000</td>
      <td>4.800000</td>
      <td>100.080000</td>
    </tr>
  </tbody>
</table>
</div>



# Q12. What is minimum and maximum value of each column against each weather condition.


```python
df.groupby('Weather_condition').min()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
    </tr>
    <tr>
      <th>Weather_condition</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Clear</th>
      <td>1/11/2012 1:00</td>
      <td>-23.3</td>
      <td>-28.5</td>
      <td>20</td>
      <td>0</td>
      <td>11.3</td>
      <td>99.52</td>
    </tr>
    <tr>
      <th>Cloudy</th>
      <td>1/1/2012 17:00</td>
      <td>-21.4</td>
      <td>-26.8</td>
      <td>18</td>
      <td>0</td>
      <td>11.3</td>
      <td>98.39</td>
    </tr>
    <tr>
      <th>Drizzle</th>
      <td>1/23/2012 21:00</td>
      <td>1.1</td>
      <td>-0.2</td>
      <td>74</td>
      <td>0</td>
      <td>6.4</td>
      <td>97.84</td>
    </tr>
    <tr>
      <th>Drizzle,Fog</th>
      <td>1/23/2012 20:00</td>
      <td>0.0</td>
      <td>-1.6</td>
      <td>85</td>
      <td>0</td>
      <td>1.0</td>
      <td>98.65</td>
    </tr>
    <tr>
      <th>Drizzle,Ice Pellets,Fog</th>
      <td>12/17/2012 9:00</td>
      <td>0.4</td>
      <td>-0.7</td>
      <td>92</td>
      <td>20</td>
      <td>4.0</td>
      <td>100.79</td>
    </tr>
    <tr>
      <th>Drizzle,Snow</th>
      <td>12/17/2012 15:00</td>
      <td>0.9</td>
      <td>0.1</td>
      <td>92</td>
      <td>9</td>
      <td>9.7</td>
      <td>100.63</td>
    </tr>
    <tr>
      <th>Drizzle,Snow,Fog</th>
      <td>12/18/2012 21:00</td>
      <td>0.3</td>
      <td>-0.1</td>
      <td>92</td>
      <td>7</td>
      <td>2.4</td>
      <td>97.79</td>
    </tr>
    <tr>
      <th>Fog</th>
      <td>1/1/2012 0:00</td>
      <td>-16.0</td>
      <td>-17.2</td>
      <td>80</td>
      <td>0</td>
      <td>0.2</td>
      <td>98.31</td>
    </tr>
    <tr>
      <th>Freezing Drizzle</th>
      <td>1/13/2012 10:00</td>
      <td>-9.0</td>
      <td>-12.2</td>
      <td>78</td>
      <td>6</td>
      <td>4.8</td>
      <td>98.44</td>
    </tr>
    <tr>
      <th>Freezing Drizzle,Fog</th>
      <td>1/1/2012 2:00</td>
      <td>-6.4</td>
      <td>-9.0</td>
      <td>82</td>
      <td>6</td>
      <td>3.6</td>
      <td>98.74</td>
    </tr>
    <tr>
      <th>Freezing Drizzle,Haze</th>
      <td>2/1/2012 11:00</td>
      <td>-5.8</td>
      <td>-8.3</td>
      <td>81</td>
      <td>9</td>
      <td>2.0</td>
      <td>100.28</td>
    </tr>
    <tr>
      <th>Freezing Drizzle,Snow</th>
      <td>1/13/2012 3:00</td>
      <td>-8.3</td>
      <td>-10.4</td>
      <td>79</td>
      <td>6</td>
      <td>2.4</td>
      <td>99.19</td>
    </tr>
    <tr>
      <th>Freezing Fog</th>
      <td>1/22/2012 6:00</td>
      <td>-19.0</td>
      <td>-22.9</td>
      <td>71</td>
      <td>0</td>
      <td>0.2</td>
      <td>101.97</td>
    </tr>
    <tr>
      <th>Freezing Rain</th>
      <td>1/13/2012 11:00</td>
      <td>-6.5</td>
      <td>-9.0</td>
      <td>81</td>
      <td>7</td>
      <td>2.8</td>
      <td>98.22</td>
    </tr>
    <tr>
      <th>Freezing Rain,Fog</th>
      <td>1/17/2012 23:00</td>
      <td>-6.1</td>
      <td>-8.7</td>
      <td>82</td>
      <td>7</td>
      <td>2.8</td>
      <td>98.32</td>
    </tr>
    <tr>
      <th>Freezing Rain,Haze</th>
      <td>2/1/2012 14:00</td>
      <td>-4.9</td>
      <td>-7.5</td>
      <td>82</td>
      <td>6</td>
      <td>2.0</td>
      <td>100.34</td>
    </tr>
    <tr>
      <th>Freezing Rain,Ice Pellets,Fog</th>
      <td>12/17/2012 3:00</td>
      <td>-2.6</td>
      <td>-3.7</td>
      <td>92</td>
      <td>28</td>
      <td>8.0</td>
      <td>100.95</td>
    </tr>
    <tr>
      <th>Freezing Rain,Snow Grains</th>
      <td>1/13/2012 9:00</td>
      <td>-5.0</td>
      <td>-7.3</td>
      <td>84</td>
      <td>32</td>
      <td>4.8</td>
      <td>98.56</td>
    </tr>
    <tr>
      <th>Haze</th>
      <td>1/22/2012 12:00</td>
      <td>-11.5</td>
      <td>-16.0</td>
      <td>68</td>
      <td>0</td>
      <td>4.8</td>
      <td>100.35</td>
    </tr>
    <tr>
      <th>Mainly Clear</th>
      <td>1/10/2012 11:00</td>
      <td>-22.8</td>
      <td>-28.0</td>
      <td>20</td>
      <td>0</td>
      <td>12.9</td>
      <td>98.67</td>
    </tr>
    <tr>
      <th>Moderate Rain,Fog</th>
      <td>12/10/2012 8:00</td>
      <td>1.7</td>
      <td>0.8</td>
      <td>94</td>
      <td>17</td>
      <td>6.4</td>
      <td>99.98</td>
    </tr>
    <tr>
      <th>Moderate Snow</th>
      <td>1/12/2012 15:00</td>
      <td>-6.3</td>
      <td>-7.6</td>
      <td>83</td>
      <td>26</td>
      <td>0.6</td>
      <td>99.88</td>
    </tr>
    <tr>
      <th>Moderate Snow,Blowing Snow</th>
      <td>12/27/2012 10:00</td>
      <td>-5.5</td>
      <td>-6.6</td>
      <td>92</td>
      <td>39</td>
      <td>0.6</td>
      <td>100.50</td>
    </tr>
    <tr>
      <th>Mostly Cloudy</th>
      <td>1/1/2012 16:00</td>
      <td>-23.2</td>
      <td>-28.5</td>
      <td>18</td>
      <td>0</td>
      <td>11.3</td>
      <td>98.36</td>
    </tr>
    <tr>
      <th>Rain</th>
      <td>1/1/2012 18:00</td>
      <td>0.3</td>
      <td>-5.7</td>
      <td>40</td>
      <td>0</td>
      <td>4.0</td>
      <td>97.52</td>
    </tr>
    <tr>
      <th>Rain Showers</th>
      <td>1/1/2012 22:00</td>
      <td>1.6</td>
      <td>-7.2</td>
      <td>37</td>
      <td>0</td>
      <td>6.4</td>
      <td>98.51</td>
    </tr>
    <tr>
      <th>Rain Showers,Fog</th>
      <td>10/20/2012 3:00</td>
      <td>12.8</td>
      <td>12.1</td>
      <td>96</td>
      <td>13</td>
      <td>6.4</td>
      <td>99.83</td>
    </tr>
    <tr>
      <th>Rain Showers,Snow Showers</th>
      <td>11/4/2012 8:00</td>
      <td>2.1</td>
      <td>-1.8</td>
      <td>75</td>
      <td>17</td>
      <td>19.3</td>
      <td>101.09</td>
    </tr>
    <tr>
      <th>Rain,Fog</th>
      <td>1/23/2012 18:00</td>
      <td>0.0</td>
      <td>-1.2</td>
      <td>83</td>
      <td>0</td>
      <td>2.0</td>
      <td>98.61</td>
    </tr>
    <tr>
      <th>Rain,Haze</th>
      <td>3/13/2012 7:00</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>81</td>
      <td>7</td>
      <td>4.0</td>
      <td>100.50</td>
    </tr>
    <tr>
      <th>Rain,Ice Pellets</th>
      <td>12/18/2012 5:00</td>
      <td>0.6</td>
      <td>-0.6</td>
      <td>92</td>
      <td>24</td>
      <td>9.7</td>
      <td>100.12</td>
    </tr>
    <tr>
      <th>Rain,Snow</th>
      <td>1/10/2012 5:00</td>
      <td>0.6</td>
      <td>-1.7</td>
      <td>81</td>
      <td>13</td>
      <td>2.4</td>
      <td>98.18</td>
    </tr>
    <tr>
      <th>Rain,Snow Grains</th>
      <td>12/21/2012 0:00</td>
      <td>1.9</td>
      <td>-2.1</td>
      <td>75</td>
      <td>26</td>
      <td>25.0</td>
      <td>100.60</td>
    </tr>
    <tr>
      <th>Rain,Snow,Fog</th>
      <td>12/8/2012 21:00</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>96</td>
      <td>9</td>
      <td>6.4</td>
      <td>100.73</td>
    </tr>
    <tr>
      <th>Rain,Snow,Ice Pellets</th>
      <td>12/21/2012 1:00</td>
      <td>0.9</td>
      <td>-0.7</td>
      <td>88</td>
      <td>17</td>
      <td>4.8</td>
      <td>99.85</td>
    </tr>
    <tr>
      <th>Snow</th>
      <td>1/10/2012 1:00</td>
      <td>-16.7</td>
      <td>-24.6</td>
      <td>41</td>
      <td>0</td>
      <td>1.0</td>
      <td>97.75</td>
    </tr>
    <tr>
      <th>Snow Pellets</th>
      <td>11/24/2012 15:00</td>
      <td>0.7</td>
      <td>-6.4</td>
      <td>59</td>
      <td>35</td>
      <td>2.4</td>
      <td>99.70</td>
    </tr>
    <tr>
      <th>Snow Showers</th>
      <td>1/12/2012 7:00</td>
      <td>-13.3</td>
      <td>-19.3</td>
      <td>52</td>
      <td>0</td>
      <td>2.4</td>
      <td>99.49</td>
    </tr>
    <tr>
      <th>Snow Showers,Fog</th>
      <td>12/26/2012 9:00</td>
      <td>-11.3</td>
      <td>-12.7</td>
      <td>89</td>
      <td>7</td>
      <td>4.0</td>
      <td>100.63</td>
    </tr>
    <tr>
      <th>Snow,Blowing Snow</th>
      <td>1/13/2012 21:00</td>
      <td>-12.0</td>
      <td>-16.2</td>
      <td>70</td>
      <td>24</td>
      <td>0.6</td>
      <td>98.11</td>
    </tr>
    <tr>
      <th>Snow,Fog</th>
      <td>12/16/2012 15:00</td>
      <td>-10.1</td>
      <td>-12.0</td>
      <td>77</td>
      <td>4</td>
      <td>1.2</td>
      <td>99.38</td>
    </tr>
    <tr>
      <th>Snow,Haze</th>
      <td>2/1/2012 17:00</td>
      <td>-4.3</td>
      <td>-7.2</td>
      <td>80</td>
      <td>0</td>
      <td>4.0</td>
      <td>100.61</td>
    </tr>
    <tr>
      <th>Snow,Ice Pellets</th>
      <td>12/10/2012 3:00</td>
      <td>-4.3</td>
      <td>-5.9</td>
      <td>76</td>
      <td>19</td>
      <td>2.8</td>
      <td>99.40</td>
    </tr>
    <tr>
      <th>Thunderstorms</th>
      <td>7/16/2012 1:00</td>
      <td>21.6</td>
      <td>19.4</td>
      <td>67</td>
      <td>0</td>
      <td>24.1</td>
      <td>99.84</td>
    </tr>
    <tr>
      <th>Thunderstorms,Heavy Rain Showers</th>
      <td>5/29/2012 6:00</td>
      <td>10.9</td>
      <td>9.0</td>
      <td>88</td>
      <td>9</td>
      <td>2.4</td>
      <td>100.26</td>
    </tr>
    <tr>
      <th>Thunderstorms,Moderate Rain Showers,Fog</th>
      <td>7/17/2012 6:00</td>
      <td>19.6</td>
      <td>18.5</td>
      <td>93</td>
      <td>15</td>
      <td>3.2</td>
      <td>100.01</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain</th>
      <td>5/25/2012 20:00</td>
      <td>19.4</td>
      <td>18.2</td>
      <td>83</td>
      <td>4</td>
      <td>16.1</td>
      <td>100.19</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain Showers</th>
      <td>5/29/2012 16:00</td>
      <td>11.0</td>
      <td>7.0</td>
      <td>68</td>
      <td>7</td>
      <td>6.4</td>
      <td>99.65</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain Showers,Fog</th>
      <td>6/29/2012 3:00</td>
      <td>19.5</td>
      <td>16.1</td>
      <td>80</td>
      <td>7</td>
      <td>9.7</td>
      <td>99.71</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain,Fog</th>
      <td>7/17/2012 5:00</td>
      <td>20.6</td>
      <td>18.6</td>
      <td>88</td>
      <td>19</td>
      <td>4.8</td>
      <td>100.08</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('Weather_condition').max()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
    </tr>
    <tr>
      <th>Weather_condition</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Clear</th>
      <td>9/9/2012 5:00</td>
      <td>32.8</td>
      <td>20.4</td>
      <td>99</td>
      <td>33</td>
      <td>48.3</td>
      <td>103.63</td>
    </tr>
    <tr>
      <th>Cloudy</th>
      <td>9/9/2012 23:00</td>
      <td>30.5</td>
      <td>22.6</td>
      <td>99</td>
      <td>54</td>
      <td>48.3</td>
      <td>103.65</td>
    </tr>
    <tr>
      <th>Drizzle</th>
      <td>9/30/2012 3:00</td>
      <td>18.8</td>
      <td>17.7</td>
      <td>96</td>
      <td>30</td>
      <td>25.0</td>
      <td>101.56</td>
    </tr>
    <tr>
      <th>Drizzle,Fog</th>
      <td>9/30/2012 2:00</td>
      <td>19.9</td>
      <td>19.1</td>
      <td>100</td>
      <td>28</td>
      <td>9.7</td>
      <td>102.07</td>
    </tr>
    <tr>
      <th>Drizzle,Ice Pellets,Fog</th>
      <td>12/17/2012 9:00</td>
      <td>0.4</td>
      <td>-0.7</td>
      <td>92</td>
      <td>20</td>
      <td>4.0</td>
      <td>100.79</td>
    </tr>
    <tr>
      <th>Drizzle,Snow</th>
      <td>12/19/2012 18:00</td>
      <td>1.2</td>
      <td>0.2</td>
      <td>95</td>
      <td>19</td>
      <td>11.3</td>
      <td>101.15</td>
    </tr>
    <tr>
      <th>Drizzle,Snow,Fog</th>
      <td>12/22/2012 3:00</td>
      <td>1.1</td>
      <td>0.6</td>
      <td>98</td>
      <td>32</td>
      <td>9.7</td>
      <td>100.15</td>
    </tr>
    <tr>
      <th>Fog</th>
      <td>9/22/2012 0:00</td>
      <td>20.8</td>
      <td>19.6</td>
      <td>100</td>
      <td>22</td>
      <td>9.7</td>
      <td>103.04</td>
    </tr>
    <tr>
      <th>Freezing Drizzle</th>
      <td>2/1/2012 5:00</td>
      <td>-2.3</td>
      <td>-3.3</td>
      <td>93</td>
      <td>26</td>
      <td>12.9</td>
      <td>101.02</td>
    </tr>
    <tr>
      <th>Freezing Drizzle,Fog</th>
      <td>12/10/2012 5:00</td>
      <td>-0.3</td>
      <td>-2.3</td>
      <td>94</td>
      <td>33</td>
      <td>8.0</td>
      <td>101.27</td>
    </tr>
    <tr>
      <th>Freezing Drizzle,Haze</th>
      <td>2/1/2012 13:00</td>
      <td>-5.0</td>
      <td>-7.7</td>
      <td>83</td>
      <td>11</td>
      <td>4.0</td>
      <td>100.36</td>
    </tr>
    <tr>
      <th>Freezing Drizzle,Snow</th>
      <td>3/2/2012 12:00</td>
      <td>-3.3</td>
      <td>-4.6</td>
      <td>94</td>
      <td>24</td>
      <td>12.9</td>
      <td>101.18</td>
    </tr>
    <tr>
      <th>Freezing Fog</th>
      <td>3/17/2012 6:00</td>
      <td>-0.1</td>
      <td>-0.3</td>
      <td>99</td>
      <td>9</td>
      <td>0.8</td>
      <td>102.85</td>
    </tr>
    <tr>
      <th>Freezing Rain</th>
      <td>2/1/2012 7:00</td>
      <td>0.3</td>
      <td>-1.7</td>
      <td>92</td>
      <td>28</td>
      <td>16.1</td>
      <td>101.00</td>
    </tr>
    <tr>
      <th>Freezing Rain,Fog</th>
      <td>12/17/2012 1:00</td>
      <td>0.1</td>
      <td>-0.9</td>
      <td>93</td>
      <td>26</td>
      <td>9.7</td>
      <td>101.01</td>
    </tr>
    <tr>
      <th>Freezing Rain,Haze</th>
      <td>2/1/2012 15:00</td>
      <td>-4.9</td>
      <td>-7.4</td>
      <td>83</td>
      <td>9</td>
      <td>2.8</td>
      <td>100.41</td>
    </tr>
    <tr>
      <th>Freezing Rain,Ice Pellets,Fog</th>
      <td>12/17/2012 3:00</td>
      <td>-2.6</td>
      <td>-3.7</td>
      <td>92</td>
      <td>28</td>
      <td>8.0</td>
      <td>100.95</td>
    </tr>
    <tr>
      <th>Freezing Rain,Snow Grains</th>
      <td>1/13/2012 9:00</td>
      <td>-5.0</td>
      <td>-7.3</td>
      <td>84</td>
      <td>32</td>
      <td>4.8</td>
      <td>98.56</td>
    </tr>
    <tr>
      <th>Haze</th>
      <td>3/13/2012 23:00</td>
      <td>14.1</td>
      <td>11.1</td>
      <td>86</td>
      <td>17</td>
      <td>9.7</td>
      <td>102.97</td>
    </tr>
    <tr>
      <th>Mainly Clear</th>
      <td>9/9/2012 9:00</td>
      <td>33.0</td>
      <td>21.2</td>
      <td>99</td>
      <td>63</td>
      <td>48.3</td>
      <td>103.59</td>
    </tr>
    <tr>
      <th>Moderate Rain,Fog</th>
      <td>12/10/2012 8:00</td>
      <td>1.7</td>
      <td>0.8</td>
      <td>94</td>
      <td>17</td>
      <td>6.4</td>
      <td>99.98</td>
    </tr>
    <tr>
      <th>Moderate Snow</th>
      <td>12/27/2012 9:00</td>
      <td>-4.9</td>
      <td>-6.7</td>
      <td>93</td>
      <td>39</td>
      <td>0.8</td>
      <td>100.67</td>
    </tr>
    <tr>
      <th>Moderate Snow,Blowing Snow</th>
      <td>12/27/2012 12:00</td>
      <td>-5.4</td>
      <td>-6.4</td>
      <td>93</td>
      <td>41</td>
      <td>0.6</td>
      <td>100.64</td>
    </tr>
    <tr>
      <th>Mostly Cloudy</th>
      <td>9/9/2012 2:00</td>
      <td>32.4</td>
      <td>24.4</td>
      <td>100</td>
      <td>83</td>
      <td>48.3</td>
      <td>103.65</td>
    </tr>
    <tr>
      <th>Rain</th>
      <td>9/5/2012 2:00</td>
      <td>22.8</td>
      <td>20.4</td>
      <td>99</td>
      <td>52</td>
      <td>48.3</td>
      <td>102.26</td>
    </tr>
    <tr>
      <th>Rain Showers</th>
      <td>9/8/2012 16:00</td>
      <td>26.4</td>
      <td>23.0</td>
      <td>97</td>
      <td>41</td>
      <td>48.3</td>
      <td>102.31</td>
    </tr>
    <tr>
      <th>Rain Showers,Fog</th>
      <td>10/20/2012 3:00</td>
      <td>12.8</td>
      <td>12.1</td>
      <td>96</td>
      <td>13</td>
      <td>6.4</td>
      <td>99.83</td>
    </tr>
    <tr>
      <th>Rain Showers,Snow Showers</th>
      <td>12/5/2012 10:00</td>
      <td>2.2</td>
      <td>-1.2</td>
      <td>78</td>
      <td>28</td>
      <td>24.1</td>
      <td>101.11</td>
    </tr>
    <tr>
      <th>Rain,Fog</th>
      <td>9/30/2012 23:00</td>
      <td>21.7</td>
      <td>19.5</td>
      <td>100</td>
      <td>46</td>
      <td>9.7</td>
      <td>101.77</td>
    </tr>
    <tr>
      <th>Rain,Haze</th>
      <td>3/13/2012 9:00</td>
      <td>5.5</td>
      <td>2.9</td>
      <td>86</td>
      <td>17</td>
      <td>9.7</td>
      <td>100.61</td>
    </tr>
    <tr>
      <th>Rain,Ice Pellets</th>
      <td>12/18/2012 5:00</td>
      <td>0.6</td>
      <td>-0.6</td>
      <td>92</td>
      <td>24</td>
      <td>9.7</td>
      <td>100.12</td>
    </tr>
    <tr>
      <th>Rain,Snow</th>
      <td>4/23/2012 3:00</td>
      <td>1.7</td>
      <td>0.5</td>
      <td>94</td>
      <td>52</td>
      <td>25.0</td>
      <td>101.07</td>
    </tr>
    <tr>
      <th>Rain,Snow Grains</th>
      <td>12/21/2012 0:00</td>
      <td>1.9</td>
      <td>-2.1</td>
      <td>75</td>
      <td>26</td>
      <td>25.0</td>
      <td>100.60</td>
    </tr>
    <tr>
      <th>Rain,Snow,Fog</th>
      <td>12/8/2012 21:00</td>
      <td>0.8</td>
      <td>0.3</td>
      <td>96</td>
      <td>9</td>
      <td>6.4</td>
      <td>100.73</td>
    </tr>
    <tr>
      <th>Rain,Snow,Ice Pellets</th>
      <td>12/21/2012 5:00</td>
      <td>1.3</td>
      <td>0.1</td>
      <td>94</td>
      <td>28</td>
      <td>6.4</td>
      <td>100.47</td>
    </tr>
    <tr>
      <th>Snow</th>
      <td>4/27/2012 9:00</td>
      <td>3.7</td>
      <td>0.3</td>
      <td>96</td>
      <td>57</td>
      <td>25.0</td>
      <td>102.73</td>
    </tr>
    <tr>
      <th>Snow Pellets</th>
      <td>11/24/2012 15:00</td>
      <td>0.7</td>
      <td>-6.4</td>
      <td>59</td>
      <td>35</td>
      <td>2.4</td>
      <td>99.70</td>
    </tr>
    <tr>
      <th>Snow Showers</th>
      <td>3/4/2012 21:00</td>
      <td>2.9</td>
      <td>-0.7</td>
      <td>94</td>
      <td>37</td>
      <td>48.3</td>
      <td>102.50</td>
    </tr>
    <tr>
      <th>Snow Showers,Fog</th>
      <td>12/29/2012 13:00</td>
      <td>-10.0</td>
      <td>-11.1</td>
      <td>92</td>
      <td>22</td>
      <td>9.7</td>
      <td>102.52</td>
    </tr>
    <tr>
      <th>Snow,Blowing Snow</th>
      <td>2/25/2012 9:00</td>
      <td>-1.4</td>
      <td>-2.9</td>
      <td>91</td>
      <td>48</td>
      <td>9.7</td>
      <td>100.62</td>
    </tr>
    <tr>
      <th>Snow,Fog</th>
      <td>3/14/2012 19:00</td>
      <td>1.1</td>
      <td>0.8</td>
      <td>99</td>
      <td>35</td>
      <td>9.7</td>
      <td>102.07</td>
    </tr>
    <tr>
      <th>Snow,Haze</th>
      <td>2/1/2012 21:00</td>
      <td>-3.6</td>
      <td>-6.4</td>
      <td>81</td>
      <td>15</td>
      <td>6.4</td>
      <td>100.99</td>
    </tr>
    <tr>
      <th>Snow,Ice Pellets</th>
      <td>3/3/2012 4:00</td>
      <td>0.8</td>
      <td>-1.7</td>
      <td>92</td>
      <td>33</td>
      <td>11.3</td>
      <td>100.96</td>
    </tr>
    <tr>
      <th>Thunderstorms</th>
      <td>7/4/2012 16:00</td>
      <td>26.7</td>
      <td>20.1</td>
      <td>87</td>
      <td>15</td>
      <td>25.0</td>
      <td>100.62</td>
    </tr>
    <tr>
      <th>Thunderstorms,Heavy Rain Showers</th>
      <td>5/29/2012 6:00</td>
      <td>10.9</td>
      <td>9.0</td>
      <td>88</td>
      <td>9</td>
      <td>2.4</td>
      <td>100.26</td>
    </tr>
    <tr>
      <th>Thunderstorms,Moderate Rain Showers,Fog</th>
      <td>7/17/2012 6:00</td>
      <td>19.6</td>
      <td>18.5</td>
      <td>93</td>
      <td>15</td>
      <td>3.2</td>
      <td>100.01</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain</th>
      <td>7/23/2012 18:00</td>
      <td>21.3</td>
      <td>19.1</td>
      <td>93</td>
      <td>30</td>
      <td>24.1</td>
      <td>100.83</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain Showers</th>
      <td>9/8/2012 4:00</td>
      <td>25.5</td>
      <td>23.1</td>
      <td>98</td>
      <td>32</td>
      <td>25.0</td>
      <td>101.06</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain Showers,Fog</th>
      <td>7/31/2012 20:00</td>
      <td>22.9</td>
      <td>21.3</td>
      <td>91</td>
      <td>35</td>
      <td>9.7</td>
      <td>100.64</td>
    </tr>
    <tr>
      <th>Thunderstorms,Rain,Fog</th>
      <td>7/17/2012 5:00</td>
      <td>20.6</td>
      <td>18.6</td>
      <td>88</td>
      <td>19</td>
      <td>4.8</td>
      <td>100.08</td>
    </tr>
  </tbody>
</table>
</div>



# Q13. Show all the record when the weather was Fog.


```python
df[df['Weather_condition'] == 'Fog']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather_condition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2012 0:00</td>
      <td>-1.8</td>
      <td>-3.9</td>
      <td>86</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/1/2012 1:00</td>
      <td>-1.8</td>
      <td>-3.7</td>
      <td>87</td>
      <td>4</td>
      <td>8.0</td>
      <td>101.24</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/1/2012 4:00</td>
      <td>-1.5</td>
      <td>-3.3</td>
      <td>88</td>
      <td>7</td>
      <td>4.8</td>
      <td>101.23</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/1/2012 5:00</td>
      <td>-1.4</td>
      <td>-3.3</td>
      <td>87</td>
      <td>9</td>
      <td>6.4</td>
      <td>101.27</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/1/2012 6:00</td>
      <td>-1.5</td>
      <td>-3.1</td>
      <td>89</td>
      <td>7</td>
      <td>6.4</td>
      <td>101.29</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8716</th>
      <td>12/29/2012 4:00</td>
      <td>-16.0</td>
      <td>-17.2</td>
      <td>90</td>
      <td>6</td>
      <td>9.7</td>
      <td>101.25</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>8717</th>
      <td>12/29/2012 5:00</td>
      <td>-14.8</td>
      <td>-15.9</td>
      <td>91</td>
      <td>4</td>
      <td>6.4</td>
      <td>101.25</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>8718</th>
      <td>12/29/2012 6:00</td>
      <td>-13.8</td>
      <td>-15.3</td>
      <td>88</td>
      <td>4</td>
      <td>9.7</td>
      <td>101.25</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>8719</th>
      <td>12/29/2012 7:00</td>
      <td>-14.8</td>
      <td>-16.4</td>
      <td>88</td>
      <td>7</td>
      <td>8.0</td>
      <td>101.22</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>8722</th>
      <td>12/29/2012 10:00</td>
      <td>-12.0</td>
      <td>-13.3</td>
      <td>90</td>
      <td>7</td>
      <td>6.4</td>
      <td>101.15</td>
      <td>Fog</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 8 columns</p>
</div>



# Q14. find all the instance when weather is clear or visibility is above 40


```python
df.loc[(df['Weather_condition'] == "Clear") & (df["Visibility_km"] > 40)] #answer
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather_condition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>351</th>
      <td>1/15/2012 15:00</td>
      <td>-15.4</td>
      <td>-22.8</td>
      <td>53</td>
      <td>24</td>
      <td>48.3</td>
      <td>102.71</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>352</th>
      <td>1/15/2012 16:00</td>
      <td>-15.1</td>
      <td>-22.8</td>
      <td>52</td>
      <td>24</td>
      <td>48.3</td>
      <td>102.79</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>425</th>
      <td>1/18/2012 17:00</td>
      <td>-11.3</td>
      <td>-18.8</td>
      <td>54</td>
      <td>26</td>
      <td>48.3</td>
      <td>101.54</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>440</th>
      <td>1/19/2012 8:00</td>
      <td>-13.7</td>
      <td>-18.4</td>
      <td>68</td>
      <td>19</td>
      <td>48.3</td>
      <td>101.84</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>441</th>
      <td>1/19/2012 9:00</td>
      <td>-12.7</td>
      <td>-17.2</td>
      <td>69</td>
      <td>17</td>
      <td>48.3</td>
      <td>101.73</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8384</th>
      <td>12/15/2012 8:00</td>
      <td>-10.7</td>
      <td>-15.6</td>
      <td>67</td>
      <td>13</td>
      <td>48.3</td>
      <td>102.69</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>8385</th>
      <td>12/15/2012 9:00</td>
      <td>-10.4</td>
      <td>-15.9</td>
      <td>64</td>
      <td>19</td>
      <td>48.3</td>
      <td>102.74</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>8389</th>
      <td>12/15/2012 13:00</td>
      <td>-8.4</td>
      <td>-14.7</td>
      <td>60</td>
      <td>19</td>
      <td>48.3</td>
      <td>102.64</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>8631</th>
      <td>12/25/2012 15:00</td>
      <td>-7.1</td>
      <td>-13.7</td>
      <td>59</td>
      <td>17</td>
      <td>48.3</td>
      <td>101.98</td>
      <td>Clear</td>
    </tr>
    <tr>
      <th>8632</th>
      <td>12/25/2012 16:00</td>
      <td>-7.5</td>
      <td>-13.9</td>
      <td>60</td>
      <td>11</td>
      <td>48.3</td>
      <td>102.03</td>
      <td>Clear</td>
    </tr>
  </tbody>
</table>
<p>313 rows × 8 columns</p>
</div>



# Q15.Find all the instance when:
    A . Weather is clear and relative humadity is above 50
    B . Visiblilty is above 40


```python
df.loc[(df['Weather_condition'] == 'Clear') & (df['Rel Hum_%'] > 50) | (df["Visibility_km"] > 40)]  #Answer A
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date/Time</th>
      <th>Temp_C</th>
      <th>Dew Point Temp_C</th>
      <th>Rel Hum_%</th>
      <th>Wind Speed_km/h</th>
      <th>Visibility_km</th>
      <th>Press_kPa</th>
      <th>Weather_condition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>106</th>
      <td>1/5/2012 10:00</td>
      <td>-6.0</td>
      <td>-10.0</td>
      <td>73</td>
      <td>17</td>
      <td>48.3</td>
      <td>100.45</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>107</th>
      <td>1/5/2012 11:00</td>
      <td>-5.6</td>
      <td>-10.2</td>
      <td>70</td>
      <td>22</td>
      <td>48.3</td>
      <td>100.41</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>108</th>
      <td>1/5/2012 12:00</td>
      <td>-4.7</td>
      <td>-9.6</td>
      <td>69</td>
      <td>20</td>
      <td>48.3</td>
      <td>100.38</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>109</th>
      <td>1/5/2012 13:00</td>
      <td>-4.4</td>
      <td>-9.7</td>
      <td>66</td>
      <td>26</td>
      <td>48.3</td>
      <td>100.40</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>110</th>
      <td>1/5/2012 14:00</td>
      <td>-5.1</td>
      <td>-10.7</td>
      <td>65</td>
      <td>22</td>
      <td>48.3</td>
      <td>100.46</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8749</th>
      <td>12/30/2012 13:00</td>
      <td>-12.4</td>
      <td>-16.2</td>
      <td>73</td>
      <td>37</td>
      <td>48.3</td>
      <td>100.92</td>
      <td>Mostly Cloudy</td>
    </tr>
    <tr>
      <th>8750</th>
      <td>12/30/2012 14:00</td>
      <td>-11.8</td>
      <td>-16.1</td>
      <td>70</td>
      <td>37</td>
      <td>48.3</td>
      <td>100.96</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>8751</th>
      <td>12/30/2012 15:00</td>
      <td>-11.3</td>
      <td>-15.6</td>
      <td>70</td>
      <td>32</td>
      <td>48.3</td>
      <td>101.05</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>8752</th>
      <td>12/30/2012 16:00</td>
      <td>-11.4</td>
      <td>-15.5</td>
      <td>72</td>
      <td>26</td>
      <td>48.3</td>
      <td>101.15</td>
      <td>Mainly Clear</td>
    </tr>
    <tr>
      <th>8756</th>
      <td>12/30/2012 20:00</td>
      <td>-13.8</td>
      <td>-16.5</td>
      <td>80</td>
      <td>24</td>
      <td>25.0</td>
      <td>101.52</td>
      <td>Clear</td>
    </tr>
  </tbody>
</table>
<p>2921 rows × 8 columns</p>
</div>


df.loc[(df['Weather_condition'] == 'Clear') 
& 
(df['Rel Hum_%'] > 50)
| 
(df["Visibility_km"] > 40)]  #Answer of Q15
# by Mohit Rohilla


```python

```
