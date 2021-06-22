#!/usr/bin/env python
# coding: utf-8

# # The Weather DataSet

# Big data analysis

# The weather dataset is time series data set with per hour information about the weather
# condition on a particular location. it records Temp., relative humidity, wind speed, visibility pressure and condition
# 
# * The data is available in the form of .csv file. 
# * We will use pandas to analyis the data set.

# In[1]:


#importing pandas libary

import pandas as pd


# In[3]:


#reading weather .csv file and assign to the variable 'df'.

df = pd.read_csv('Weather_data.csv')


# In[4]:


df


# 

# # Exploring and analysing the data set deeply to understand easily

# 

# In[35]:


#1 - We are useing head() to print top 5 rows from the data.


# In[5]:


df.head()


# 

# In[ ]:


#2 We are useing 'shape' command to check the size and number of rows and column in the 
#dataframe


# In[7]:


df.shape


# 

# In[8]:


#3 we are useing the 'index' command to check the length of index in the data frame.


# In[9]:


df.index


# 

# In[10]:


#4 we are using the 'columns' command to check names of all column present in the data frame.


# In[12]:


df.columns


# 

# In[13]:


# 5 we are using ".dtypes" to check the data type of each column.


# In[16]:


df.dtypes


# 

# In[17]:


#6 we are using 'unique()' to check the unique value in the particular column.


# In[18]:


df['Weather'].unique()


# 

# In[19]:


#7 we are using ".nunique" to check the total number of unique value in whole data frame.


# In[20]:


df.nunique()


# 

# In[22]:


#8 We are using ".count()" to check the number of null value in the each column of data frame.


# In[25]:


df.count()


# 

# In[26]:


#9 we are using "info()"  to check the absic information of the data frame.


# In[32]:


df.info()


# In[33]:


#10 we are using "Value_count()" to check the number of unique value with there count in 
#particular column of the data frame.


# In[31]:


df['Weather'].value_counts()


# # Tasks

# # Q1.                                                                                                    Find all the unique "Wind Speed" value from the data frame

# In[41]:


print("Numner of unique value of windspeed = ",df['Wind Speed_km/h'].nunique())


# In[36]:


df['Wind Speed_km/h'].unique() #answer


# # Q2. Find the number of times when the weather is exactly clear.

# In[43]:


clear = df[df['Weather'] == 'Clear'] #answer


# In[45]:


clear


# In[57]:


print(" The number of rows and column in dataframe when the weather was clear =",clear.shape)


# # Q3. Find the number of times when the wind was exactly 4km/h.

# In[52]:


speed = df[df['Wind Speed_km/h'] == 4] #answer


# In[53]:


speed


# In[56]:


print(" The number of rows and column in dataframe \n when the wind speed was exactly 4 km/h =",clear.shape)


# # Q4. Find out all null values in the dataframe.

# In[59]:


df.isnull().sum() #answer


# In[60]:


df.notnull().sum() #answer


# # Q5 Rename the "weather" column name to "weather_condition".

# In[83]:


df.info()


# In[87]:


col_change = df.rename(columns = {'Weather' : 'Weather_condition'})  #answer


# In[88]:


col_change.info()


# # Q6 What is the mean  of 'Visibility' ?

# In[91]:


df['Visibility_km'].mean()  #answer


# # Q7. What is the Standard deviation of Pressure in the data?

# In[92]:


df['Press_kPa'].std() #answer


# # Q8 what is the variance of Relative humadity in the data frame.

# In[94]:


df['Rel Hum_%'].var()


# # Q9 Find all instance when snow was recorded.

# In[95]:


df.head()


# In[114]:


df[df['Weather_condition'].str.contains('Snow')] #answer


# # Q10. Find all instance when wind speed is above 24 and visibility is 25

# In[115]:


df.loc[(df['Wind Speed_km/h'] > 24 ) & (df['Visibility_km'] == 25.0)] #answer


# # Q11. What is the mean value of each column against each weather condition?

# In[116]:


df.groupby(['Weather_condition']).mean() #answer


# # Q12. What is minimum and maximum value of each column against each weather condition.

# In[119]:


df.groupby('Weather_condition').min()


# In[120]:


df.groupby('Weather_condition').max()


# # Q13. Show all the record when the weather was Fog.

# In[121]:


df[df['Weather_condition'] == 'Fog']


# # Q14. find all the instance when weather is clear or visibility is above 40

# In[122]:


df.loc[(df['Weather_condition'] == "Clear") & (df["Visibility_km"] > 40)] #answer


# # Q15.Find all the instance when:
#     A . Weather is clear and relative humadity is above 50
#     B . Visiblilty is above 40

# In[125]:


df.loc[(df['Weather_condition'] == 'Clear') & (df['Rel Hum_%'] > 50) | (df["Visibility_km"] > 40)]  #Answer A

df.loc[(df['Weather_condition'] == 'Clear') 
& 
(df['Rel Hum_%'] > 50)
| 
(df["Visibility_km"] > 40)]  #Answer of Q15
# # by Mohit Rohilla

# In[ ]:




