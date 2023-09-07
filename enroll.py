
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import altair as alt 


st.set_page_config(
    page_title='Enrollment Metrics',
    page_icon='favicon.ico',
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={'About': 'Enrollment numbers for BMCC ALL Department. Contact esarajlic@bmcc.cuny.edu for more info.'}
)
      
#st.image('/Users/eldarsarajlic/Desktop/Documents/Data_Projects/streamlit2/enrollmetrics.png')            
#st.markdown('<style>/Users/eldarsarajlic/Desktop/Documents/Data_Projects/streamlit2/style.css</style>', unsafe_allow_html=True)

  
# DATA 

spring_03 = pd.read_csv('datasets/spring_2003.csv')  
fall_03 = pd.read_csv('datasets/fall_2003.csv')
spring_04 = pd.read_csv('datasets/spring_2004.csv')
fall_04 = pd.read_csv('datasets/fall_2004.csv')
spring_05 = pd.read_csv('datasets/spring_2005.csv')
fall_05 = pd.read_csv('datasets/fall_2005.csv')
spring_06 = pd.read_csv('datasets/spring_2006.csv')
fall_06 = pd.read_csv('datasets/fall_2006.csv')
spring_07 = pd.read_csv('datasets/spring_2007.csv')
fall_07 = pd.read_csv('datasets/fall_2007.csv')
spring_08 = pd.read_csv('datasets/spring_2008.csv')
fall_08 = pd.read_csv('datasets/fall_2008.csv')
spring_09 = pd.read_csv('datasets/spring_2009.csv')
fall_09 = pd.read_csv('datasets/fall_2009.csv')
spring_10 = pd.read_csv('datasets/spring_2010.csv')
fall_10 = pd.read_csv('datasets/fall_2010.csv')
spring_11 = pd.read_csv('datasets/spring_2011.csv')
fall_11 = pd.read_csv('datasets/fall_2011.csv')
spring_12 = pd.read_csv('datasets/spring_2012.csv')
fall_12 = pd.read_csv('datasets/fall_2012.csv')
spring_13 = pd.read_csv('datasets/spring_2013.csv')
fall_13 = pd.read_csv('datasets/fall_2013.csv')
spring_14 = pd.read_csv('datasets/spring_2014.csv')
fall_14 = pd.read_csv('datasets/fall_2014.csv')
spring_15 = pd.read_csv('datasets/spring_2015.csv')
fall_15 = pd.read_csv('datasets/fall_2015.csv')
spring_16 = pd.read_csv('datasets/spring_2016.csv')
fall_16 = pd.read_csv('datasets/fall_2016.csv')
spring_17 = pd.read_csv('datasets/spring_17.csv')
fall_17 = pd.read_csv('datasets/fall_17.csv')
spring_18 = pd.read_csv('datasets/spring_18.csv')
fall_18 = pd.read_csv('datasets/fall_18.csv')
spring_19 = pd.read_csv('datasets/spring_19.csv')
fall_19 = pd.read_csv('datasets/fall_19.csv')
spring_20 = pd.read_csv('datasets/spring_20.csv')
fall_20 = pd.read_csv('datasets/fall_2020.csv')
spring_21 = pd.read_csv('datasets/spring_21.csv')
fall_21 = pd.read_csv('datasets/fall_21.csv')
spring_22 = pd.read_csv('datasets/spring_22.csv')
fall_22 = pd.read_csv('datasets/fall_22.csv')
spring_23 = pd.read_csv('datasets/spring_23.csv')
spring_23 = spring_23.rename(columns={'Unnamed: 0': 'Course'})
fall_13.columns = ['Course', '# of Sections', '# Enrolled']
spring_17.columns = ['Course', '# of Sections', '# Enrolled']
fall_15.columns = ['Course', '# of Sections', '# Enrolled']
fall_17.columns = ['Course', '# of Sections', '# Enrolled']
fall_20.columns = ['Course', '# of Sections', '# Enrolled']
spring_16 = spring_16.drop(columns=['Unnamed: 3'])
spring_16.dropna(inplace=True)
fall_23 = pd.read_csv('datasets/fall_23.csv')


# CLASS

class DataFramer:
    
    def __init__(self, name, df):
        self.name = name
        if 'Subject' in df.columns:
            df = df.rename(columns={'Subject': 'Course'})
                  
        self.df = df
        self.df.replace(',', '', regex=True, inplace=True)
        self.df.replace('-', '', regex=True, inplace=True)
        self.df['# Enrolled'] = pd.to_numeric(self.df['# Enrolled'], errors='coerce')
        self.df['# Enrolled'] = pd.to_numeric(self.df['# Enrolled'], errors='coerce')
        
    def get_name(self):
        return str(self.name)
    
    def get_df(self):
        return self.df
    
    def get_course(self, pattern):  
        filtered_df = self.df[self.df['Course'].str.contains(pattern)].groupby('Course').first().reset_index()
        return filtered_df 


spring_2003 = DataFramer('2003s', spring_03)
spring_2004 = DataFramer('2004s', spring_04)
spring_2005 = DataFramer('2005s', spring_05)
spring_2006 = DataFramer('2006s', spring_06)
spring_2007 = DataFramer('2007s', spring_07)
spring_2008 = DataFramer('2008s', spring_08)
spring_2009 = DataFramer('2009s', spring_09)
spring_2010 = DataFramer('2010s', spring_10)
spring_2011 = DataFramer('2011s', spring_11)
spring_2012 = DataFramer('2012s', spring_12)
spring_2013 = DataFramer('2013s', spring_13)
spring_2014 = DataFramer('2014s', spring_14)
spring_2015 = DataFramer('2015s', spring_15)
spring_2016 = DataFramer('2016s', spring_16)
spring_2017 = DataFramer('2017s', spring_17)
spring_2018 = DataFramer('2018s', spring_18)
spring_2019 = DataFramer('2019s', spring_19)
spring_2020 = DataFramer('2020s', spring_20)
spring_2021 = DataFramer('2021s', spring_21)
spring_2022 = DataFramer('2022s', spring_22)
spring_2023 = DataFramer('2023s', spring_23)

fall_2003 = DataFramer('2003f', fall_03)
fall_2004 = DataFramer('2004f', fall_04)
fall_2005 = DataFramer('2005f', fall_05)
fall_2006 = DataFramer('2006f', fall_06)
fall_2007 = DataFramer('2007f', fall_07)
fall_2008 = DataFramer('2008f', fall_08)
fall_2009 = DataFramer('2009f', fall_09)
fall_2010 = DataFramer('2010f', fall_10)
fall_2011 = DataFramer('2011f', fall_11)
fall_2012 = DataFramer('2012f', fall_12)
fall_2013 = DataFramer('2013f', fall_13)
fall_2014 = DataFramer('2014f', fall_14)
fall_2015 = DataFramer('2015f', fall_15)
fall_2016 = DataFramer('2016f', fall_16)
fall_2017 = DataFramer('2017f', fall_17)
fall_2018 = DataFramer('2018f', fall_18)
fall_2019 = DataFramer('2019f', fall_19)
fall_2020 = DataFramer('2020f', fall_20)
fall_2021 = DataFramer('2021f', fall_21)
fall_2022 = DataFramer('2022f', fall_22)
fall_2023 = DataFramer('2023f', fall_23)

totals_enrolled = pd.DataFrame({'Semester': [spring_2003.get_name(), fall_2003.get_name(),
                                            spring_2004.get_name(), fall_2004.get_name(),
                                            spring_2005.get_name(), fall_2005.get_name(),
                                            spring_2005.get_name(), fall_2005.get_name(),
                                            spring_2006.get_name(), fall_2006.get_name(), 
                                            spring_2007.get_name(), fall_2007.get_name(),
                                            spring_2008.get_name(), fall_2008.get_name(),
                                            spring_2009.get_name(), fall_2009.get_name(),
                                            spring_2010.get_name(), fall_2010.get_name(),
                                            spring_2011.get_name(), fall_2011.get_name(),
                                            spring_2012.get_name(), fall_2012.get_name(),
                                            spring_2013.get_name(), fall_2013.get_name(),
                                            spring_2014.get_name(), fall_2014.get_name(),
                                            spring_2015.get_name(), fall_2015.get_name(),
                                            spring_2016.get_name(), fall_2016.get_name(),
                                            spring_2017.get_name(), fall_2017.get_name(),
                                            spring_2018.get_name(), fall_2018.get_name(),
                                            spring_2019.get_name(), fall_2019.get_name(),
                                            spring_2020.get_name(), fall_2020.get_name(),
                                            spring_2021.get_name(), fall_2021.get_name(),
                                            spring_2022.get_name(), fall_2022.get_name(),
                                            spring_2023.get_name(), fall_2023.get_name()],
                                'ACL': [spring_2003.get_course('ACR')['# Enrolled'].sum(), fall_2003.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2004.get_course('ACR')['# Enrolled'].sum(), fall_2004.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2005.get_course('ACR')['# Enrolled'].sum(), fall_2005.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2005.get_course('ACR')['# Enrolled'].sum(), fall_2005.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2006.get_course('ACR')['# Enrolled'].sum(), fall_2006.get_course('ACR')['# Enrolled'].sum(), 
                                            spring_2007.get_course('ACR')['# Enrolled'].sum(), fall_2007.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2008.get_course('ACR')['# Enrolled'].sum(), fall_2008.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2009.get_course('ACR')['# Enrolled'].sum(), fall_2009.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2010.get_course('ACR')['# Enrolled'].sum(), fall_2010.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2011.get_course('ACR')['# Enrolled'].sum(), fall_2011.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2012.get_course('ACR')['# Enrolled'].sum(), fall_2012.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2013.get_course('ACR')['# Enrolled'].sum(), fall_2013.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2014.get_course('ACR')['# Enrolled'].sum(), fall_2014.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2015.get_course('ACR')['# Enrolled'].sum(), fall_2015.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2016.get_course('ACR')['# Enrolled'].sum(), fall_2016.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2017.get_course('ACR')['# Enrolled'].sum(), fall_2017.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2018.get_course('ACR')['# Enrolled'].sum(), fall_2018.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2019.get_course('ACR')['# Enrolled'].sum(), fall_2019.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2020.get_course('ACR')['# Enrolled'].sum(), fall_2020.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2021.get_course('ACR')['# Enrolled'].sum(), fall_2021.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2022.get_course('ACR')['# Enrolled'].sum(), fall_2022.get_course('ACR')['# Enrolled'].sum(),
                                            spring_2023.get_course('ACL')['# Enrolled'].sum(), fall_2023.get_course('ACL')['# Enrolled'].sum()],
                                  'CRT': [spring_2003.get_course('CRT')['# Enrolled'].sum(), fall_2003.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2004.get_course('CRT')['# Enrolled'].sum(), fall_2004.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2005.get_course('CRT')['# Enrolled'].sum(), fall_2005.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2005.get_course('CRT')['# Enrolled'].sum(), fall_2005.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2006.get_course('CRT')['# Enrolled'].sum(), fall_2006.get_course('CRT')['# Enrolled'].sum(), 
                                            spring_2007.get_course('CRT')['# Enrolled'].sum(), fall_2007.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2008.get_course('CRT')['# Enrolled'].sum(), fall_2008.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2009.get_course('CRT')['# Enrolled'].sum(), fall_2009.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2010.get_course('CRT')['# Enrolled'].sum(), fall_2010.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2011.get_course('CRT')['# Enrolled'].sum(), fall_2011.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2012.get_course('CRT')['# Enrolled'].sum(), fall_2012.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2013.get_course('CRT')['# Enrolled'].sum(), fall_2013.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2014.get_course('CRT')['# Enrolled'].sum(), fall_2014.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2015.get_course('CRT')['# Enrolled'].sum(), fall_2015.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2016.get_course('CRT')['# Enrolled'].sum(), fall_2016.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2017.get_course('CRT')['# Enrolled'].sum(), fall_2017.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2018.get_course('CRT')['# Enrolled'].sum(), fall_2018.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2019.get_course('CRT')['# Enrolled'].sum(), fall_2019.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2020.get_course('CRT')['# Enrolled'].sum(), fall_2020.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2021.get_course('CRT')['# Enrolled'].sum(), fall_2021.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2022.get_course('CRT')['# Enrolled'].sum(), fall_2022.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2023.get_course('CRT')['# Enrolled'].sum(), fall_2023.get_course('CRT')['# Enrolled'].sum()],
                                  'ESL': [spring_2003.get_course('ESL')['# Enrolled'].sum(), fall_2003.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2004.get_course('ESL')['# Enrolled'].sum(), fall_2004.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2005.get_course('ESL')['# Enrolled'].sum(), fall_2005.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2005.get_course('ESL')['# Enrolled'].sum(), fall_2005.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2006.get_course('ESL')['# Enrolled'].sum(), fall_2006.get_course('ESL')['# Enrolled'].sum(), 
                                            spring_2007.get_course('ESL')['# Enrolled'].sum(), fall_2007.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2008.get_course('ESL')['# Enrolled'].sum(), fall_2008.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2009.get_course('ESL')['# Enrolled'].sum(), fall_2009.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2010.get_course('ESL')['# Enrolled'].sum(), fall_2010.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2011.get_course('ESL')['# Enrolled'].sum(), fall_2011.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2012.get_course('ESL')['# Enrolled'].sum(), fall_2012.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2013.get_course('ESL')['# Enrolled'].sum(), fall_2013.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2014.get_course('ESL')['# Enrolled'].sum(), fall_2014.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2015.get_course('ESL')['# Enrolled'].sum(), fall_2015.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2016.get_course('ESL')['# Enrolled'].sum(), fall_2016.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2017.get_course('ESL')['# Enrolled'].sum(), fall_2017.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2018.get_course('ESL')['# Enrolled'].sum(), fall_2018.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2019.get_course('ESL')['# Enrolled'].sum(), fall_2019.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2020.get_course('ESL')['# Enrolled'].sum(), fall_2020.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2021.get_course('ESL')['# Enrolled'].sum(), fall_2021.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2022.get_course('ESL')['# Enrolled'].sum(), fall_2022.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2023.get_course('ESL')['# Enrolled'].sum(), fall_2023.get_course('ESL')['# Enrolled'].sum()],
                                  'LIN': [spring_2003.get_course('LIN')['# Enrolled'].sum(), fall_2003.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2004.get_course('LIN')['# Enrolled'].sum(), fall_2004.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2005.get_course('LIN')['# Enrolled'].sum(), fall_2005.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2005.get_course('LIN')['# Enrolled'].sum(), fall_2005.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2006.get_course('LIN')['# Enrolled'].sum(), fall_2006.get_course('LIN')['# Enrolled'].sum(), 
                                            spring_2007.get_course('LIN')['# Enrolled'].sum(), fall_2007.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2008.get_course('LIN')['# Enrolled'].sum(), fall_2008.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2009.get_course('LIN')['# Enrolled'].sum(), fall_2009.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2010.get_course('LIN')['# Enrolled'].sum(), fall_2010.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2011.get_course('LIN')['# Enrolled'].sum(), fall_2011.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2012.get_course('LIN')['# Enrolled'].sum(), fall_2012.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2013.get_course('LIN')['# Enrolled'].sum(), fall_2013.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2014.get_course('LIN')['# Enrolled'].sum(), fall_2014.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2015.get_course('LIN')['# Enrolled'].sum(), fall_2015.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2016.get_course('LIN')['# Enrolled'].sum(), fall_2016.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2017.get_course('LIN')['# Enrolled'].sum(), fall_2017.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2018.get_course('LIN')['# Enrolled'].sum(), fall_2018.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2019.get_course('LIN')['# Enrolled'].sum(), fall_2019.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2020.get_course('LIN')['# Enrolled'].sum(), fall_2020.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2021.get_course('LIN')['# Enrolled'].sum(), fall_2021.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2022.get_course('LIN')['# Enrolled'].sum(), fall_2022.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2023.get_course('LIN')['# Enrolled'].sum(), fall_2023.get_course('LIN')['# Enrolled'].sum()]
                                })

totals_sections = pd.DataFrame({'Semester': [spring_2003.get_name(), fall_2003.get_name(),
                                            spring_2004.get_name(), fall_2004.get_name(),
                                            spring_2005.get_name(), fall_2005.get_name(),
                                            spring_2005.get_name(), fall_2005.get_name(),
                                            spring_2006.get_name(), fall_2006.get_name(), 
                                            spring_2007.get_name(), fall_2007.get_name(),
                                            spring_2008.get_name(), fall_2008.get_name(),
                                            spring_2009.get_name(), fall_2009.get_name(),
                                            spring_2010.get_name(), fall_2010.get_name(),
                                            spring_2011.get_name(), fall_2011.get_name(),
                                            spring_2012.get_name(), fall_2012.get_name(),
                                            spring_2013.get_name(), fall_2013.get_name(),
                                            spring_2014.get_name(), fall_2014.get_name(),
                                            spring_2015.get_name(), fall_2015.get_name(),
                                            spring_2016.get_name(), fall_2016.get_name(),
                                            spring_2017.get_name(), fall_2017.get_name(),
                                            spring_2018.get_name(), fall_2018.get_name(),
                                            spring_2019.get_name(), fall_2019.get_name(),
                                            spring_2020.get_name(), fall_2020.get_name(),
                                            spring_2021.get_name(), fall_2021.get_name(),
                                            spring_2022.get_name(), fall_2022.get_name(),
                                            spring_2023.get_name(), fall_2023.get_name()],
                                'ACL': [spring_2003.get_course('ACR')['# of Sections'].sum(), fall_2003.get_course('ACR')['# of Sections'].sum(),
                                            spring_2004.get_course('ACR')['# of Sections'].sum(), fall_2004.get_course('ACR')['# of Sections'].sum(),
                                            spring_2005.get_course('ACR')['# of Sections'].sum(), fall_2005.get_course('ACR')['# of Sections'].sum(),
                                            spring_2005.get_course('ACR')['# of Sections'].sum(), fall_2005.get_course('ACR')['# of Sections'].sum(),
                                            spring_2006.get_course('ACR')['# of Sections'].sum(), fall_2006.get_course('ACR')['# of Sections'].sum(), 
                                            spring_2007.get_course('ACR')['# of Sections'].sum(), fall_2007.get_course('ACR')['# of Sections'].sum(),
                                            spring_2008.get_course('ACR')['# of Sections'].sum(), fall_2008.get_course('ACR')['# of Sections'].sum(),
                                            spring_2009.get_course('ACR')['# of Sections'].sum(), fall_2009.get_course('ACR')['# of Sections'].sum(),
                                            spring_2010.get_course('ACR')['# of Sections'].sum(), fall_2010.get_course('ACR')['# of Sections'].sum(),
                                            spring_2011.get_course('ACR')['# of Sections'].sum(), fall_2011.get_course('ACR')['# of Sections'].sum(),
                                            spring_2012.get_course('ACR')['# of Sections'].sum(), fall_2012.get_course('ACR')['# of Sections'].sum(),
                                            spring_2013.get_course('ACR')['# of Sections'].sum(), fall_2013.get_course('ACR')['# of Sections'].sum(),
                                            spring_2014.get_course('ACR')['# of Sections'].sum(), fall_2014.get_course('ACR')['# of Sections'].sum(),
                                            spring_2015.get_course('ACR')['# of Sections'].sum(), fall_2015.get_course('ACR')['# of Sections'].sum(),
                                            spring_2016.get_course('ACR')['# of Sections'].sum(), fall_2016.get_course('ACR')['# of Sections'].sum(),
                                            spring_2017.get_course('ACR')['# of Sections'].sum(), fall_2017.get_course('ACR')['# of Sections'].sum(),
                                            spring_2018.get_course('ACR')['# of Sections'].sum(), fall_2018.get_course('ACR')['# of Sections'].sum(),
                                            spring_2019.get_course('ACR')['# of Sections'].sum(), fall_2019.get_course('ACR')['# of Sections'].sum(),
                                            spring_2020.get_course('ACR')['# of Sections'].sum(), fall_2020.get_course('ACR')['# of Sections'].sum(),
                                            spring_2021.get_course('ACR')['# of Sections'].sum(), fall_2021.get_course('ACR')['# of Sections'].sum(),
                                            spring_2022.get_course('ACR')['# of Sections'].sum(), fall_2022.get_course('ACR')['# of Sections'].sum(),
                                            spring_2023.get_course('ACL')['# of Sections'].sum(), fall_2023.get_course('ACL')['# of Sections'].sum()],
                                  'CRT': [spring_2003.get_course('CRT')['# of Sections'].sum(), fall_2003.get_course('CRT')['# of Sections'].sum(),
                                            spring_2004.get_course('CRT')['# of Sections'].sum(), fall_2004.get_course('CRT')['# of Sections'].sum(),
                                            spring_2005.get_course('CRT')['# of Sections'].sum(), fall_2005.get_course('CRT')['# of Sections'].sum(),
                                            spring_2005.get_course('CRT')['# of Sections'].sum(), fall_2005.get_course('CRT')['# of Sections'].sum(),
                                            spring_2006.get_course('CRT')['# of Sections'].sum(), fall_2006.get_course('CRT')['# of Sections'].sum(), 
                                            spring_2007.get_course('CRT')['# of Sections'].sum(), fall_2007.get_course('CRT')['# of Sections'].sum(),
                                            spring_2008.get_course('CRT')['# of Sections'].sum(), fall_2008.get_course('CRT')['# of Sections'].sum(),
                                            spring_2009.get_course('CRT')['# of Sections'].sum(), fall_2009.get_course('CRT')['# of Sections'].sum(),
                                            spring_2010.get_course('CRT')['# of Sections'].sum(), fall_2010.get_course('CRT')['# of Sections'].sum(),
                                            spring_2011.get_course('CRT')['# of Sections'].sum(), fall_2011.get_course('CRT')['# of Sections'].sum(),
                                            spring_2012.get_course('CRT')['# of Sections'].sum(), fall_2012.get_course('CRT')['# of Sections'].sum(),
                                            spring_2013.get_course('CRT')['# of Sections'].sum(), fall_2013.get_course('CRT')['# of Sections'].sum(),
                                            spring_2014.get_course('CRT')['# of Sections'].sum(), fall_2014.get_course('CRT')['# of Sections'].sum(),
                                            spring_2015.get_course('CRT')['# of Sections'].sum(), fall_2015.get_course('CRT')['# of Sections'].sum(),
                                            spring_2016.get_course('CRT')['# of Sections'].sum(), fall_2016.get_course('CRT')['# of Sections'].sum(),
                                            spring_2017.get_course('CRT')['# of Sections'].sum(), fall_2017.get_course('CRT')['# of Sections'].sum(),
                                            spring_2018.get_course('CRT')['# of Sections'].sum(), fall_2018.get_course('CRT')['# of Sections'].sum(),
                                            spring_2019.get_course('CRT')['# of Sections'].sum(), fall_2019.get_course('CRT')['# of Sections'].sum(),
                                            spring_2020.get_course('CRT')['# of Sections'].sum(), fall_2020.get_course('CRT')['# of Sections'].sum(),
                                            spring_2021.get_course('CRT')['# of Sections'].sum(), fall_2021.get_course('CRT')['# of Sections'].sum(),
                                            spring_2022.get_course('CRT')['# of Sections'].sum(), fall_2022.get_course('CRT')['# of Sections'].sum(),
                                            spring_2023.get_course('CRT')['# of Sections'].sum(), fall_2023.get_course('CRT')['# of Sections'].sum()],
                                  'ESL': [spring_2003.get_course('ESL')['# of Sections'].sum(), fall_2003.get_course('ESL')['# of Sections'].sum(),
                                            spring_2004.get_course('ESL')['# of Sections'].sum(), fall_2004.get_course('ESL')['# of Sections'].sum(),
                                            spring_2005.get_course('ESL')['# of Sections'].sum(), fall_2005.get_course('ESL')['# of Sections'].sum(),
                                            spring_2005.get_course('ESL')['# of Sections'].sum(), fall_2005.get_course('ESL')['# of Sections'].sum(),
                                            spring_2006.get_course('ESL')['# of Sections'].sum(), fall_2006.get_course('ESL')['# of Sections'].sum(), 
                                            spring_2007.get_course('ESL')['# of Sections'].sum(), fall_2007.get_course('ESL')['# of Sections'].sum(),
                                            spring_2008.get_course('ESL')['# of Sections'].sum(), fall_2008.get_course('ESL')['# of Sections'].sum(),
                                            spring_2009.get_course('ESL')['# of Sections'].sum(), fall_2009.get_course('ESL')['# of Sections'].sum(),
                                            spring_2010.get_course('ESL')['# of Sections'].sum(), fall_2010.get_course('ESL')['# of Sections'].sum(),
                                            spring_2011.get_course('ESL')['# of Sections'].sum(), fall_2011.get_course('ESL')['# of Sections'].sum(),
                                            spring_2012.get_course('ESL')['# of Sections'].sum(), fall_2012.get_course('ESL')['# of Sections'].sum(),
                                            spring_2013.get_course('ESL')['# of Sections'].sum(), fall_2013.get_course('ESL')['# of Sections'].sum(),
                                            spring_2014.get_course('ESL')['# of Sections'].sum(), fall_2014.get_course('ESL')['# of Sections'].sum(),
                                            spring_2015.get_course('ESL')['# of Sections'].sum(), fall_2015.get_course('ESL')['# of Sections'].sum(),
                                            spring_2016.get_course('ESL')['# of Sections'].sum(), fall_2016.get_course('ESL')['# of Sections'].sum(),
                                            spring_2017.get_course('ESL')['# of Sections'].sum(), fall_2017.get_course('ESL')['# of Sections'].sum(),
                                            spring_2018.get_course('ESL')['# of Sections'].sum(), fall_2018.get_course('ESL')['# of Sections'].sum(),
                                            spring_2019.get_course('ESL')['# of Sections'].sum(), fall_2019.get_course('ESL')['# of Sections'].sum(),
                                            spring_2020.get_course('ESL')['# of Sections'].sum(), fall_2020.get_course('ESL')['# of Sections'].sum(),
                                            spring_2021.get_course('ESL')['# of Sections'].sum(), fall_2021.get_course('ESL')['# of Sections'].sum(),
                                            spring_2022.get_course('ESL')['# of Sections'].sum(), fall_2022.get_course('ESL')['# of Sections'].sum(),
                                            spring_2023.get_course('ESL')['# of Sections'].sum(), fall_2023.get_course('ESL')['# of Sections'].sum()],
                                  'LIN': [spring_2003.get_course('LIN')['# of Sections'].sum(), fall_2003.get_course('LIN')['# of Sections'].sum(),
                                            spring_2004.get_course('LIN')['# of Sections'].sum(), fall_2004.get_course('LIN')['# of Sections'].sum(),
                                            spring_2005.get_course('LIN')['# of Sections'].sum(), fall_2005.get_course('LIN')['# of Sections'].sum(),
                                            spring_2005.get_course('LIN')['# of Sections'].sum(), fall_2005.get_course('LIN')['# of Sections'].sum(),
                                            spring_2006.get_course('LIN')['# of Sections'].sum(), fall_2006.get_course('LIN')['# of Sections'].sum(), 
                                            spring_2007.get_course('LIN')['# of Sections'].sum(), fall_2007.get_course('LIN')['# of Sections'].sum(),
                                            spring_2008.get_course('LIN')['# of Sections'].sum(), fall_2008.get_course('LIN')['# of Sections'].sum(),
                                            spring_2009.get_course('LIN')['# of Sections'].sum(), fall_2009.get_course('LIN')['# of Sections'].sum(),
                                            spring_2010.get_course('LIN')['# of Sections'].sum(), fall_2010.get_course('LIN')['# of Sections'].sum(),
                                            spring_2011.get_course('LIN')['# of Sections'].sum(), fall_2011.get_course('LIN')['# of Sections'].sum(),
                                            spring_2012.get_course('LIN')['# of Sections'].sum(), fall_2012.get_course('LIN')['# of Sections'].sum(),
                                            spring_2013.get_course('LIN')['# of Sections'].sum(), fall_2013.get_course('LIN')['# of Sections'].sum(),
                                            spring_2014.get_course('LIN')['# of Sections'].sum(), fall_2014.get_course('LIN')['# of Sections'].sum(),
                                            spring_2015.get_course('LIN')['# of Sections'].sum(), fall_2015.get_course('LIN')['# of Sections'].sum(),
                                            spring_2016.get_course('LIN')['# of Sections'].sum(), fall_2016.get_course('LIN')['# of Sections'].sum(),
                                            spring_2017.get_course('LIN')['# of Sections'].sum(), fall_2017.get_course('LIN')['# of Sections'].sum(),
                                            spring_2018.get_course('LIN')['# of Sections'].sum(), fall_2018.get_course('LIN')['# of Sections'].sum(),
                                            spring_2019.get_course('LIN')['# of Sections'].sum(), fall_2019.get_course('LIN')['# of Sections'].sum(),
                                            spring_2020.get_course('LIN')['# of Sections'].sum(), fall_2020.get_course('LIN')['# of Sections'].sum(),
                                            spring_2021.get_course('LIN')['# of Sections'].sum(), fall_2021.get_course('LIN')['# of Sections'].sum(),
                                            spring_2022.get_course('LIN')['# of Sections'].sum(), fall_2022.get_course('LIN')['# of Sections'].sum(),
                                            spring_2023.get_course('LIN')['# of Sections'].sum(), fall_2023.get_course('LIN')['# of Sections'].sum()]
                                })

# MAIN CONTENT      

with st.sidebar:
     
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.header('About')
        st.markdown('Enrollment dashboard for the *Department of Academic Literacy and Linguistics* at **CUNY Borough of Manhattan Community College**.')
        st.markdown('For more info, contact Eldar Sarajlic, at esarajlic@bmcc.cuny.edu')
           
# FIRST LINE

with st.container():
    
    col1, col2, col3, col4, col5 = st.columns((3,1,1,1,1))

    with col1:
        
        st.image('enrollmetrics.png') 
             
    with col2:   
        
        st.metric(label='Total enrollment', value=2057, delta='+425')                           
        
    with col3:
         st.metric(label='Total sections', value=136, delta='+4')
         
    with col4:
         st.metric(label='Sections cancelled', value=87, delta='-33')
         
    with col5:
         st.metric(label='Teaching faculty', value=47, delta='-2')
    
    
         
# SECOND LINE
 
with st.container():
    st.markdown('## Overwiew - Fall 2023')  
   
    col1, col2 = st.columns(2)
 
    with col1:
        st.markdown('#### Students')
        variable_selector = st.selectbox('Choose course group enrollment', ['ACL', 'CRT', 'ESL', 'LIN'])
        default_color = '#D3D3D3'
        selected_color = '#003264'

        # Line chart
        chart = alt.Chart(totals_enrolled).mark_line().encode(x=alt.X('Semester', sort=None))  
        lines = []
        for var in totals_enrolled.columns[1:]:
            color = alt.value(default_color)
            if var == variable_selector:
                color = alt.value(selected_color)
            line = chart.encode(
                y=var,
                color=color
            )
            lines.append(line)

        chart = alt.layer(*lines).properties()
       
        # Point chart
        point_chart = alt.Chart(totals_enrolled).mark_point().encode(x=alt.X('Semester', sort=None))

        points = []
        for var in totals_enrolled.columns[1:]:
            color = alt.value(default_color)
            if var == variable_selector:
                color = alt.value(selected_color)
            point = point_chart.encode(
                y=var,
                color=color
            )
            points.append(point)

        point_chart = alt.layer(*points).properties()

        
        chart = chart + point_chart
        chart = chart.configure_axis(labelAngle=-0, title='Enrollment Count')
        
        
        st.altair_chart(chart, use_container_width=True)
       
    with col2:
        st.markdown('#### Sections')
        variable_selector = st.selectbox('Choose course group sections', ['ACL', 'CRT', 'ESL', 'LIN'])
        default_color = '#D3D3D3'
        selected_color = '#FF914D'

        # Line chart
        chart = alt.Chart(totals_sections).mark_line().encode(x=alt.X('Semester', sort=None))
        lines = []
        for var in totals_sections.columns[1:]:
            color = alt.value(default_color)
            if var == variable_selector:
                color = alt.value(selected_color)
            line = chart.encode(
                y=var,
                color=color
            )
            lines.append(line)

        chart = alt.layer(*lines).properties()
        chart = chart.configure_axis(labelAngle=-0)
        chart = chart.configure_axis(title='Enrollment Count')

        # Point chart
        point_chart = alt.Chart(totals_sections).mark_point().encode(x=alt.X('Semester', sort=None))

        points = []
        for var in totals_sections.columns[1:]:
            color = alt.value(default_color)
            if var == variable_selector:
                color = alt.value(selected_color)
            point = point_chart.encode(
                y=var,
                color=color
            )
            points.append(point)

        point_chart = alt.layer(*points).properties()

        chart = chart + point_chart
        chart = chart.configure_axis(labelAngle=-0, title='Section Count')

        st.altair_chart(chart, use_container_width=True) 
         
with st.container():
    st.markdown('## Components')
    tab1, tab2, tab3, tab4 = st.tabs(['ACL', 'CRT', 'ESL', 'LIN'])
    
    with tab1:
        col1, col2, col3 = st.columns((2,2,2))
        
        with col1:
            custom_color_scheme = alt.Scale(domain=list(fall_2023.get_course('ACL')['Course']),
                                range=['#003264', '#004e8a', '#005e9b', '#0071ae', '#0084c2'])

            chart = alt.Chart(fall_2023.get_course('ACL')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y='# Enrolled',
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Enrollment in Fall 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Enrollment Count')
            st.altair_chart(chart, use_container_width=True)
            
            
        with col2:
            custom_color_scheme = alt.Scale(domain=list(fall_2023.get_course('ACL')['Course']),
                                range=['#FF7F00', '#FF914D', '#FFA07A', '#FFB6C1', '#FFC0CB'])

            chart = alt.Chart(fall_2023.get_course('ACL')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y=alt.Y('# of Sections', axis=alt.Axis(tickCount=3)),
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Course Sections in Fall 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Section Count')
            

            st.altair_chart(chart, use_container_width=True) 

        with col3:
            comparison0 = pd.DataFrame({'Course': spring_2023.get_course('ACL')['Course'],
                           'Spring 2023': [0,5,0,0,0],
                           'Fall 2023': list(fall_2023.get_course('ACL')['# Enrolled'])})
            melted_df0 = pd.melt(comparison0, id_vars='Course', var_name='Semester', value_name='# Enrolled')
            custom_color_scheme = alt.Scale(domain=list(comparison0['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB'])
            
            chart = alt.Chart(melted_df0).mark_line().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Fall 2023']),  # Added sort parameter here
                y='# Enrolled', 
                color=alt.Color('Course', scale=custom_color_scheme)
            ) + alt.Chart(melted_df0).mark_point().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Fall 2023']),  # And here
                y='# Enrolled',
                color='Course'
            )

            
            title = alt.TitleParams(text='Enrollment comparison with Spring 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')
            
            chart = chart.configure_axis(labelAngle=-0, title='')
            chart = chart.properties(title=title)
                       
            st.altair_chart(chart, use_container_width=True)
            
    with tab2:
                
        col1, col2, col3 = st.columns((2,2,2))
        
        with col1:
            custom_color_scheme = alt.Scale(domain=list(fall_2023.get_course('CRT')['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB', '#4BA3FF', '#9ACFFF'])

            chart = alt.Chart(fall_2023.get_course('CRT')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y='# Enrolled',
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Enrollment in Fall 2023 by course', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Enrollment Count')
            st.altair_chart(chart, use_container_width=True)
            
            
        with col2:
            custom_color_scheme = alt.Scale(domain=list(fall_2023.get_course('CRT')['Course']),
                                range=['#FF7F00', '#FF914D', '#FFA07A', '#FFB6C1', '#FFC0CB', '#F2DFFF', '#E1E1FF'])

            chart = alt.Chart(fall_2023.get_course('CRT')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y=alt.Y('# of Sections', axis=alt.Axis(tickCount=3)),
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Course sections in Fall 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Section Count')
            

            st.altair_chart(chart, use_container_width=True)

        with col3:
            custom_order = ['CRT 100', 'CRT 100.5', 'CRT 100.6', 'CRT 120', 'CRT 150', 'CRT 196',  'CRT 100H']
            new = fall_2023.get_course('CRT')['# Enrolled'].reindex(index=custom_order) 
            new = fall_2023.get_course('CRT')['# Enrolled']
            
            comparison = pd.DataFrame({'Course': spring_2023.get_course('CRT')['Course'],
                           'Spring 2023': list(spring_2023.get_course('CRT')['# Enrolled']), 'Fall 2023': new})
            melted_df = pd.melt(comparison, id_vars='Course', var_name='Semester', value_name='# Enrolled')
            
            custom_color_scheme = alt.Scale(domain=list(comparison['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB', '#4BA3FF', '#9ACFFF'])
            
            
            chart = alt.Chart(melted_df).mark_line().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Fall 2023']),  # Added sort parameter here
                y='# Enrolled', 
                color=alt.Color('Course', scale=custom_color_scheme)
            ) + alt.Chart(melted_df).mark_point().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Fall 2023']),  # And here
                y='# Enrolled',
                color='Course'
            )

            
            title = alt.TitleParams(text='Enrollment comparison with Spring 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')
            
            chart = chart.configure_axis(labelAngle=-0, title='')
            chart = chart.properties(title=title)
                       
            st.altair_chart(chart, use_container_width=True)

    with tab3:
                
        col1, col2, col3 = st.columns((2,2,2))
        
        with col1:
            custom_color_scheme = alt.Scale(domain=list(fall_2023.get_course('ESL')['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB', '#4BA3FF', '#9ACFFF'])

            chart = alt.Chart(fall_2023.get_course('ESL')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y='# Enrolled',
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Enrollment in Fall 2023 by course', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Enrollment Count')
            st.altair_chart(chart, use_container_width=True)
            
            
        with col2:
            custom_color_scheme = alt.Scale(domain=list(fall_2023.get_course('ESL')['Course']),
                                range=['#FF7F00', '#FF914D', '#FFA07A', '#FFB6C1', '#FFC0CB', '#F2DFFF', '#E1E1FF'])

            chart = alt.Chart(fall_2023.get_course('ESL')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y=alt.Y('# of Sections', axis=alt.Axis(tickCount=3)),
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Course sections in Fall 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Section Count')
            

            st.altair_chart(chart, use_container_width=True)      
        
        with col3:
            comparison2 = pd.DataFrame({'Course': fall_2023.get_course('ESL')['Course'],
                            'Fall 2023': list(fall_2023.get_course('ESL')['# Enrolled']),
                           'Spring 2023': list(spring_2023.get_course('ESL')['# Enrolled'])})
            
            melted_df2 = pd.melt(comparison2, id_vars='Course', var_name='Semester', value_name='# Enrolled')
            custom_color_scheme = alt.Scale(domain=list(comparison2['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB', '#4BA3FF'])
            
            chart = alt.Chart(melted_df2).mark_line().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Fall 2023']),  # Added sort parameter here
                y='# Enrolled', 
                color=alt.Color('Course', scale=custom_color_scheme)
            ) + alt.Chart(melted_df2).mark_point().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Fall 2023']),  # And here
                y='# Enrolled',
                color='Course'
            )

            
            title = alt.TitleParams(text='Enrollment comparison with Spring 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')
            
            chart = chart.configure_axis(labelAngle=-0, title='')
            chart = chart.properties(title=title)
                       
            st.altair_chart(chart, use_container_width=True)
            
    with tab4:
                
        col1, col2, col3 = st.columns((2,2,2))
        
        with col1:
            custom_color_scheme = alt.Scale(domain=list(fall_2023.get_course('LIN')['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB', '#4BA3FF', '#9ACFFF'])

            chart = alt.Chart(fall_2023.get_course('LIN')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y='# Enrolled',
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Enrollment in Fall 2023 by course', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Enrollment Count')
            st.altair_chart(chart, use_container_width=True)
            
            
        with col2:
            custom_color_scheme = alt.Scale(domain=list(fall_2023.get_course('LIN')['Course']),
                                range=['#FF7F00', '#FF914D', '#FFA07A', '#FFB6C1', '#FFC0CB', '#F2DFFF', '#E1E1FF', '#D0D0FF', '#BEBEFF', '#ACACFF', '#9A9AFF', '#8888FF', '#7676FF'
])

            chart = alt.Chart(fall_2023.get_course('LIN')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y=alt.Y('# of Sections', axis=alt.Axis(tickCount=3)),
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Course sections in Fall 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Section Count')
            

            st.altair_chart(chart, use_container_width=True)      
         
        with col3:
            
            common_courses = set(fall_2023.get_course('LIN')['Course']).intersection(set(spring_2023.get_course('LIN')['Course']))

            fall_common = fall_2023.get_course('LIN')[fall_2023.get_course('LIN')['Course'].isin(common_courses)].reset_index(drop=True)
            spring_common = spring_2023.get_course('LIN')[spring_2023.get_course('LIN')['Course'].isin(common_courses)].reset_index(drop=True)

            comparison3 = pd.DataFrame({
                'Course': fall_common['Course'],
                'Fall 2023': fall_common['# Enrolled'],
                'Spring 2023': spring_common['# Enrolled']
            })
            
            melted_df3 = pd.melt(comparison3, id_vars='Course', var_name='Semester', value_name='# Enrolled')
            custom_color_scheme = alt.Scale(domain=list(comparison3['Course']),
                                range=['#003264', '#1B3D71', '#354D7E', '#4D5D8B', '#666C99', '#807CA6', '#9A8CB3', '#CEACCE', '#E8BCDB', '#FFCCE8', '#FFC2CC', '#FFB7B2', '#004A8D' ]
)
             
            chart = alt.Chart(melted_df3).mark_line().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Fall 2023']),  # Added sort parameter here
                y='# Enrolled', 
                color=alt.Color('Course', scale=custom_color_scheme)
            ) + alt.Chart(melted_df3).mark_point().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Fall 2023']),  # And here
                y='# Enrolled',
                color='Course'
            )

            
            title = alt.TitleParams(text='Enrollment comparison with Spring 2022', align='left', fontSize=16, fontWeight='bold', color='#003264')
            
            chart = chart.configure_axis(labelAngle=-0, title='')
            chart = chart.properties(title=title)
                       
            st.altair_chart(chart, use_container_width=True) 
            
# CLASSES

with st.container():
    st.markdown('## Classes')
    
    col1, col2, col3 = st.columns((2,2,1))
    
    with col1:
        def class_heatmap(df):
            times = df[df[['Days', 'Mtg Start']].notna().all(axis=1)]
            times.loc[:, 'Mtg Start'] = pd.to_datetime(times['Mtg Start'])
            times.loc[:, 'Mtg End'] = pd.to_datetime(times['Mtg End'])
            times.loc[:, 'Mtg Start'] = times['Mtg Start'].dt.strftime('%H:%M')
            times.loc[:, 'Mtg End'] = times['Mtg End'].dt.strftime('%H:%M')
            
            day_dict = {
            'M': 'Monday',
            'Tu': 'Tuesday',
            'MW': 'Monday, Wednesday',
            'MTh': 'Monday, Thursday',
            'TuTh': 'Tuesday, Thursday',
            'TuF': 'Tuesday, Friday',
            'MTuWTh': 'Monday, Tuesday, Wednesday, Thursday',
            'MWTh': 'Monday, Wednesday, Thursday',
            'MTuTh': 'Monday, Tuesday, Thursday',
            'TuW': 'Tuesday, Wednesday',
            'W': 'Wednesday',
            'Th': 'Thursday',
            'F': 'Friday',
            'Sa': 'Saturday',
            'Su': 'Sunday'}
            
            def convert_days(days):
                output_days = []
                for day in days.split(','):
                    if day.strip() in day_dict:
                        output_days.append(day_dict[day.strip()])
                return output_days
            
            times['Day'] = times['Days'].apply(convert_days).apply(', '.join)
            times = times.assign(Day=times.Day.str.split(","))
            times = times.explode('Day')
            
            day_df = times[['Mtg Start', 'Mtg End', 'Day']]
            
            stacked_days = pd.concat([day_df[day_df['Day']=='Monday'], 
                                day_df[day_df['Day']=='Tuesday'], 
                                day_df[day_df['Day']=='Wednesday'], 
                                day_df[day_df['Day']=='Thursday'],
                                day_df[day_df['Day']=='Friday'],
                                day_df[day_df['Day']=='Saturday'],
                                day_df[day_df['Day']=='Sunday']],
                                axis=0)
            stacked_days['Mtg Start'] = stacked_days['Mtg Start'].astype(str)
            stacked_days['Mtg End'] = stacked_days['Mtg End'].astype(str)

            df_pivot = stacked_days.pivot_table(index='Day', columns=['Mtg Start', 'Mtg End'], aggfunc=len, fill_value=0)

            df_pivot_long = df_pivot.reset_index().melt(id_vars=['Day'], var_name=['Mtg Start', 'Mtg End'], value_name='Count')
            
            ticks = list(df_pivot_long['Mtg Start'].unique())   
            chart = alt.Chart(df_pivot_long).mark_rect().encode(
                y=alt.Y('Mtg Start:N', title='Class start time', scale=alt.Scale(domain=(ticks))),
                x=alt.X('Day:O', sort=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']),
                color=alt.Color('Count:Q', title='# of class meetings', scale=alt.Scale(scheme='blues'), legend=None),
                #tooltip=[alt.Tooltip('Count:Q', title='# of class meetings')]
            ).properties(
                width=400,
                height=400
            )
            
            title = alt.TitleParams(text='Class meetings time of the day in Fall 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')
            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='')

          
            st.altair_chart(chart, use_container_width=True) 
            
        query_23 = pd.read_csv('datasets/FALL-2023-QUERY.csv', header=1)
        
        class_heatmap(query_23)
        
    with col2:
        query = pd.read_csv('datasets/FALL-2023-QUERY.csv', header=1).fillna(0)
        where = query[['Subject', 'Room']]
        where_df = where[where['Room'] != 0]

        def where(df):
            where = df[['Subject', 'Room']]
            where.columns = ['Course', 'Room']
            where.loc[where['Room'].str.contains('OL-02'), 'Room'] = 'Online-async'
            where.loc[where['Room'].str.contains('OL-03'), 'Room'] = 'Online-sync'
            where.loc[where['Room'].str.contains('FH'), 'Room'] = 'Fitterman'
            where.loc[where['Room'].str.contains('MC'), 'Room'] = 'Main Bldg'
            where.loc[where['Room'].str.contains('MU'), 'Room'] = 'Murray'
            where.loc[where['Room'].str.contains('CH'), 'Room']  = 'Inwood'
            where.loc[where['Room'].str.contains('OF'), 'Room']  = 'Off campus'
            
            return where
        
        grouped = where(where_df).groupby(['Course', 'Room']).size().reset_index(name='Count')
        
        custom_color_scale = alt.Scale(
            domain=['ACL', 'CRT', 'ESL', 'LIN'],
            range=[ '#023e8a', '#03045e', '#219ebc', '#8ecae6'])
        
        chart = alt.Chart(grouped).mark_bar().encode(
            x='Count',
            y='Room',
            color=alt.Color('Course', scale=custom_color_scale, legend=None), order=alt.Order('Course', sort='ascending')).properties(
                width=300, height = 400
            )
                        
        title = alt.TitleParams(text='Class mode and location in Fall 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')
        chart = chart.properties(title=title)
        chart = chart.configure_axis(labelAngle=-0, title='')
        
        st.altair_chart(chart, use_container_width=True) 
        
    with col3:
        status = pd.read_csv('datasets/FALL-2023-QUERY.csv', header=1)
        status = status[['Class Stat', 'Subject']]
        status.columns = ['Status', 'Course Group']
        status_pivot = status.pivot_table(index='Status', columns='Course Group', aggfunc=len)
        status_pivot.fillna(0, inplace=True)
        source = pd.DataFrame({'Course Group': ['ACL', 'CRT', 'ESL', 'LIN'], 'Cancelled': status_pivot.iloc[1]})

        custom_color_scale = alt.Scale(
            domain=['ACL', 'CRT', 'ESL', 'LIN'],
            range=[ '#023e8a', '#48cae4', '#03045e', '#219ebc', '#8ecae6'])

        
        chart = alt.Chart(source).mark_bar().encode(
            x=alt.X('Course Group'),
            y=alt.Y('Cancelled', stack=True), color=alt.Color('Course Group', scale=custom_color_scale, legend=None)
            ).properties(
               height = 400
            )
                        
        title = alt.TitleParams(text='Section cancellations in Fall 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')
        chart = chart.properties(title=title)
        
        chart = chart.configure_axis(labelAngle=-0, title='')

        st.altair_chart(chart, use_container_width=True)