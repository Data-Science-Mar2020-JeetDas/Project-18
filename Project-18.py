# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/AIDS-WHO.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project - 18 : Number of deaths by country HIV/AIDS data from WHO");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available country

df0 = df['Unnamed: 0']

print('---------------------------------------------')
print('Available data for following Country : ')
print('---------------------------------------------')
print(df0[3:,])
print('---------------------------------------------')


# Question - D : Number of deaths HIV/AIDS between 0-27 days

df2000 = df['2000']
df2001 = df['2001']
df2002 = df['2002']
df2003 = df['2003']
df2004 = df['2004']

df2005 = df['2005']
df2006 = df['2006']
df2007 = df['2007']
df2008 = df['2008']
df2009 = df['2009']

df2010 = df['2010']
df2011 = df['2011']
df2012 = df['2012']
df2013 = df['2013']
df2014 = df['2014']

df2015 = df['2015']
df2016 = df['2016']
df2017 = df['2017']

# Question - D : Number of deaths HIV/AIDS between 0-27 days-slot-1(2000-2004)

plt.title('Question - D : Number of deaths HIV/AIDS between 0-27 days-slot-1(2000-2004)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2000[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2000")

plt.plot(df2001[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2001")

plt.plot(df2002[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2002")
            
plt.plot(df2003[3:,],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2003")
            
plt.plot(df2004[3:,],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2004")
            
plt.legend()
plt.show()

# Question - D : Number of deaths HIV/AIDS between 0-27 days-Slot-2(2005-2009)

plt.title('Question - D : Number of deaths HIV/AIDS between 0-27 days-Slot-2(2005-2009)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2005[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2005")

plt.plot(df2006[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2006")

plt.plot(df2007[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2007")
            
plt.plot(df2008[3:,],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2008")
            
plt.plot(df2009[3:,],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2009")
            
plt.legend()
plt.show()


# Question - D : Number of deaths HIV/AIDS between 0-27 days-Slot-3(2010-2014)

plt.title('Question - D : Number of deaths HIV/AIDS between 0-27 days-Slot-3(2010-2014)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2010[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2010")

plt.plot(df2011[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2011")

plt.plot(df2012[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2012")
            
plt.plot(df2013[3:,],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2013")
            
plt.plot(df2014[3:,],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2014")
            
plt.legend()
plt.show()

# Question - D : Number of deaths HIV/AIDS between 0-27 days-Slot-4(2015-2017)

plt.title('Question - D : Number of deaths HIV/AIDS between 0-27 days-Slot-3(2010-2014)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2015[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2015")

plt.plot(df2016[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2016")

plt.plot(df2017[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2017")
            
plt.legend()
plt.show()

#--------------------: Question - E :-----------------------------

# Question - E - 1 : Number of deaths HIV/AIDS between 1-59 months-slot-1(2000-2004)

df2000 = df['2000.1']
df2001 = df['2001.1']
df2002 = df['2002.1']
df2003 = df['2003.1']
df2004 = df['2004.1']

df2005 = df['2005.1']
df2006 = df['2006.1']
df2007 = df['2007.1']
df2008 = df['2008.1']
df2009 = df['2009.1']

df2010 = df['2010.1']
df2011 = df['2011.1']
df2012 = df['2012.1']
df2013 = df['2013.1']
df2014 = df['2014.1']

df2015 = df['2015.1']
df2016 = df['2016.1']
df2017 = df['2017.1']

# Question - E - 1 : Number of deaths HIV/AIDS between 1-59 months-slot-1(2000-2004)

plt.title('# Question - E - 1 : Number of deaths HIV/AIDS between 1-59 months-slot-1(2000-2004)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2000[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2000")

plt.plot(df2001[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2001")

plt.plot(df2002[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2002")
            
plt.plot(df2003[3:,],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2003")
            
plt.plot(df2004[3:,],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2004")
            
plt.legend()
plt.show()

# Question - E - 2 : Number of deaths HIV/AIDS between 1-59 months-Slot-2(2005-2009)

plt.title('# Question - E - 2 : Number of deaths HIV/AIDS between 1-59 months-Slot-2(2005-2009)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2005[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2005")

plt.plot(df2006[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2006")

plt.plot(df2007[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2007")
            
plt.plot(df2008[3:,],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2008")
            
plt.plot(df2009[3:,],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2009")
            
plt.legend()
plt.show()


# Question - E - 3 : Number of deaths HIV/AIDS between 1-59 months-Slot-3(2010-2014)

plt.title('# Question - E - 3 : Number of deaths HIV/AIDS between 1-59 months-Slot-3(2010-2014)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2010[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2010")

plt.plot(df2011[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2011")

plt.plot(df2012[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2012")
            
plt.plot(df2013[3:,],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2013")
            
plt.plot(df2014[3:,],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2014")
            
plt.legend()
plt.show()

# Question - E - 4 : Number of deaths HIV/AIDS between 1-59 months-Slot-4(2015-2017)

plt.title('Question - E - 4 : Number of deaths HIV/AIDS between 1-59 months-Slot-4(2015-2017)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2015[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2015")

plt.plot(df2016[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2016")

plt.plot(df2017[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2017")
            
plt.legend()
plt.show()


# Question - F : Number of deaths HIV/AIDS between 0-4 years

#--------------------: Question - F :-----------------------------

df2000 = df['2000.2']
df2001 = df['2001.2']
df2002 = df['2002.2']
df2003 = df['2003.2']
df2004 = df['2004.2']

df2005 = df['2005.2']
df2006 = df['2006.2']
df2007 = df['2007.2']
df2008 = df['2008.2']
df2009 = df['2009.2']

df2010 = df['2010.2']
df2011 = df['2011.2']
df2012 = df['2012.2']
df2013 = df['2013.2']
df2014 = df['2014.2']

df2015 = df['2015.2']
df2016 = df['2016.2']
df2017 = df['2017.2']

#Question - F - 1 : Number of deaths HIV/AIDS between 0-4 years-slot-1(2000-2004)

plt.title('Question - F - 1 : Number of deaths HIV/AIDS between 0-4 years-slot-1(2000-2004)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2000[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2000")

plt.plot(df2001[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2001")

plt.plot(df2002[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2002")
            
plt.plot(df2003[3:,],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2003")
            
plt.plot(df2004[3:,],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2004")
            
plt.legend()
plt.show()

# Question - F - 2 : Number of deaths HIV/AIDS between 0-4 years-Slot-2(2005-2009)

plt.title('# Question - F - 2 : Number of deaths HIV/AIDS between 0-4 years-Slot-2(2005-2009)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2005[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2005")

plt.plot(df2006[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2006")

plt.plot(df2007[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2007")
            
plt.plot(df2008[3:,],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2008")
            
plt.plot(df2009[3:,],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2009")
            
plt.legend()
plt.show()


# Question - F - 3 : Number of deaths HIV/AIDS between 0-4 years-Slot-3(2010-2014)

plt.title('# Question - F - 3 : Number of deaths HIV/AIDS between 0-4 years-Slot-3(2010-2014)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2010[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2010")

plt.plot(df2011[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2011")

plt.plot(df2012[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2012")
            
plt.plot(df2013[3:,],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="4 --> 2013")
            
plt.plot(df2014[3:,],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="5 --> 2014")
            
plt.legend()
plt.show()

# Question - F - 4 : Number of deaths HIV/AIDS between 0-4 years-Slot-4(2015-2017)

plt.title('# Question - F - 4 : Number of deaths HIV/AIDS between 0-4 years-Slot-4(2015-2017)')
plt.xlabel("Country Sl. no --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df2015[3:,],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> 2015")

plt.plot(df2016[3:,],
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> 2016")

plt.plot(df2017[3:,],
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> 2017")
            
plt.legend()
plt.show()

