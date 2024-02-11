
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
spring_24 = pd.read_csv('datasets/spring_2024.csv')


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
spring_2024 = DataFramer('2024s', spring_24)


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
                                            spring_2023.get_name(), fall_2023.get_name(),
                                            spring_2024.get_name()],
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
                                            spring_2023.get_course('ACL')['# Enrolled'].sum(), fall_2023.get_course('ACL')['# Enrolled'].sum(),
                                            spring_2024.get_course('ACL')['# Enrolled'].sum()],
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
                                            spring_2023.get_course('CRT')['# Enrolled'].sum(), fall_2023.get_course('CRT')['# Enrolled'].sum(),
                                            spring_2024.get_course('CRT')['# Enrolled'].sum()],
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
                                            spring_2023.get_course('ESL')['# Enrolled'].sum(), fall_2023.get_course('ESL')['# Enrolled'].sum(),
                                            spring_2024.get_course('ESL')['# Enrolled'].sum()],
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
                                            spring_2023.get_course('LIN')['# Enrolled'].sum(), fall_2023.get_course('LIN')['# Enrolled'].sum(),
                                            spring_2024.get_course('LIN')['# Enrolled'].sum()]
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
                                            spring_2023.get_name(), fall_2023.get_name(),
                                            spring_2024.get_name()],
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
                                            spring_2023.get_course('ACL')['# of Sections'].sum(), fall_2023.get_course('ACL')['# of Sections'].sum(),
                                            spring_2024.get_course('ACL')['# of Sections'].sum()],
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
                                            spring_2023.get_course('CRT')['# of Sections'].sum(), fall_2023.get_course('CRT')['# of Sections'].sum(),
                                            spring_2024.get_course('CRT')['# of Sections'].sum()],
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
                                            spring_2023.get_course('ESL')['# of Sections'].sum(), fall_2023.get_course('ESL')['# of Sections'].sum(),
                                            spring_2024.get_course('ESL')['# of Sections'].sum()],
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
                                            spring_2023.get_course('LIN')['# of Sections'].sum(), fall_2023.get_course('LIN')['# of Sections'].sum(),
                                            spring_2024.get_course('LIN')['# of Sections'].sum()]
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
        
        st.metric(label='Total enrollment', value=2111, delta='+54')                           
        
    with col3:
         st.metric(label='Total sections', value=139, delta='+3')
         
    with col4:
         st.metric(label='Sections cancelled', value=75, delta='-12')
         
    with col5:
         st.metric(label='Teaching faculty', value=46, delta='-1')
    
    
         
# SECOND LINE
 
with st.container():
    st.markdown('## Overwiew - Spring 2024')  
   
    col1, col2 = st.columns(2)
 
    with col1:
        st.markdown('#### Students')
        variable_selector = st.selectbox('Choose course group enrollment', ['ACL', 'CRT', 'ESL', 'LIN'])
        default_color = '#E6E6E6'
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
        default_color = '#E6E6E6'
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
    
    # ACL
    
    with tab1:
        col1, col2, col3 = st.columns((2,2,2))
        
        with col1:
            custom_color_scheme = alt.Scale(domain=list(spring_2024.get_course('ACL')['Course']),
                                range=['#003264', '#004e8a', '#005e9b', '#0071ae', '#0084c2'])

            chart = alt.Chart(spring_2024.get_course('ACL')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y='# Enrolled',
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Enrollment in Spring 2024', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Enrollment Count')
            st.altair_chart(chart, use_container_width=True)
            
            
        with col2:
            custom_color_scheme = alt.Scale(domain=list(spring_2024.get_course('ACL')['Course']),
                                range=['#FF7F00', '#FF914D', '#FFA07A', '#FFB6C1', '#FFC0CB'])

            chart = alt.Chart(spring_2024.get_course('ACL')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y=alt.Y('# of Sections', axis=alt.Axis(tickCount=3)),
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Course Sections in Spring 2024', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Section Count')
            

            st.altair_chart(chart, use_container_width=True) 

        with col3:
            comparison0 = pd.DataFrame({'Course': spring_2023.get_course('ACL')['Course'],
                           'Spring 2023': [2,3,53,20,24],
                           'Spring 2024': list(spring_2024.get_course('ACL')['# Enrolled'])})
            melted_df0 = pd.melt(comparison0, id_vars='Course', var_name='Semester', value_name='# Enrolled')
            custom_color_scheme = alt.Scale(domain=list(comparison0['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB'])
            
            chart = alt.Chart(melted_df0).mark_line().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Spring 2024']),  # Added sort parameter here
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
        
        # CRT
        
        col1, col2, col3 = st.columns((2,2,2))
        
        with col1:
            # Assuming spring_2024.get_course('CRT') returns a DataFrame
            df_crt = spring_2024.get_course('CRT')

            # Filter out courses with zero enrollment
            df_crt_filtered = df_crt[df_crt['# Enrolled'] > 0]

            # Define custom color scheme
            custom_color_scheme = alt.Scale(
                domain=list(df_crt_filtered['Course']),
                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB', '#4BA3FF', '#9ACFFF']
            )

            # Create the chart
            chart = alt.Chart(df_crt_filtered).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y='# Enrolled',
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            ).properties(
                title=alt.TitleParams(
                    text='Enrollment in Spring 2024 by course', 
                    align='left', 
                    fontSize=16, 
                    fontWeight='bold', 
                    color='#003264'
                )
            ).configure_axis(
                labelAngle=0, 
                title='Enrollment Count'
            )

            st.altair_chart(chart, use_container_width=True)
            
            
        with col2:
            custom_color_scheme = alt.Scale(domain=list(spring_2024.get_course('CRT')['Course']),
                                range=['#FF7F00', '#FF914D', '#FFA07A', '#FFB6C1', '#FFC0CB', '#F2DFFF', '#E1E1FF'])

            chart = alt.Chart(spring_2024.get_course('CRT')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y=alt.Y('# of Sections', axis=alt.Axis(tickCount=3)),
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Course sections in Spring 2024', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Section Count')
            

            st.altair_chart(chart, use_container_width=True)

        with col3:
            courses_of_interest = ["CRT 100", "CRT 120", "CRT 150", "CRT 245", "CRT 100H"]

            spring_2023_crt = spring_2023.get_course('CRT')
            spring_2024_crt = spring_2024.get_course('CRT')

            spring_2023_crt_filtered = spring_2023_crt[spring_2023_crt['Course'].isin(courses_of_interest)]
            spring_2024_crt_filtered = spring_2024_crt[spring_2024_crt['Course'].isin(courses_of_interest)]


            # Create a DataFrame for comparison
            comparison0 = pd.DataFrame({
                'Course': courses_of_interest,
                'Spring 2023': spring_2023_crt_filtered['# Enrolled'],
                'Spring 2024': [584, 22, 20, 21, 19]
            })

            
            melted_df0 = pd.melt(comparison0, id_vars='Course', var_name='Semester', value_name='# Enrolled')
            custom_color_scheme = alt.Scale(domain=list(comparison0['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD'])
            
            chart = alt.Chart(melted_df0).mark_line().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Spring 2024']),  # Added sort parameter here
                y='# Enrolled', 
                color=alt.Color('Course', scale=custom_color_scheme)
            ) + alt.Chart(melted_df0).mark_point().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Fall 2023']),  
                y='# Enrolled',
                color='Course'
            )

            
            title = alt.TitleParams(text='Enrollment comparison with Spring 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')
            
            chart = chart.configure_axis(labelAngle=-0, title='')
            chart = chart.properties(title=title)
            
            st.altair_chart(chart, use_container_width=True)

    with tab3:
        
        # ESL 
        
        col1, col2, col3 = st.columns((2,2,2))
        
        with col1:
            custom_color_scheme = alt.Scale(domain=list(spring_2024.get_course('ESL')['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB', '#4BA3FF', '#9ACFFF'])

            chart = alt.Chart(spring_2024.get_course('ESL')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y='# Enrolled',
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Enrollment in Spring 2024 by course', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Enrollment Count')
            st.altair_chart(chart, use_container_width=True)
            
            
        with col2:
            custom_color_scheme = alt.Scale(domain=list(spring_2024.get_course('ESL')['Course']),
                                range=['#FF7F00', '#FF914D', '#FFA07A', '#FFB6C1', '#FFC0CB', '#F2DFFF', '#E1E1FF'])

            chart = alt.Chart(spring_2024.get_course('ESL')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y=alt.Y('# of Sections', axis=alt.Axis(tickCount=3)),
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Course sections in Spring 2024', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Section Count')
            

            st.altair_chart(chart, use_container_width=True)      
        
        with col3:
            comparison2 = pd.DataFrame({'Course': spring_2024.get_course('ESL')['Course'],
                           'Spring 2023': list(spring_2023.get_course('ESL')['# Enrolled']), 
                           'Spring 2024': list(spring_2024.get_course('ESL')['# Enrolled'])})
            
            melted_df2 = pd.melt(comparison2, id_vars='Course', var_name='Semester', value_name='# Enrolled')
            custom_color_scheme = alt.Scale(domain=list(comparison2['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB', '#4BA3FF'])
            
            chart = alt.Chart(melted_df2).mark_line().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Spring 2024']),  # Added sort parameter here
                y='# Enrolled', 
                color=alt.Color('Course', scale=custom_color_scheme)
            ) + alt.Chart(melted_df2).mark_point().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Spring 2024']),  # And here
                y='# Enrolled',
                color='Course'
            )

            
            title = alt.TitleParams(text='Enrollment comparison with Spring 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')
            
            chart = chart.configure_axis(labelAngle=-0, title='')
            chart = chart.properties(title=title)
                       
            st.altair_chart(chart, use_container_width=True)
            
    with tab4:
       
       # LIN         
        col1, col2, col3 = st.columns((2,2,2))
        
        with col1:
            spring_2024_lin = spring_2024.get_course('LIN')

            # Filter out courses with 0 enrollment
            spring_2024_lin_filtered = spring_2024_lin[spring_2024_lin['# Enrolled'] > 0]
            
            custom_color_scheme = alt.Scale(domain=list(spring_2024.get_course('LIN')['Course']),
                                range=['#003264', '#00487C', '#005B94', '#006EBD', '#007DDB', '#4BA3FF', '#9ACFFF'])

            chart = alt.Chart(spring_2024_lin_filtered).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y='# Enrolled',
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Enrollment in Spring 2024 by course', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Enrollment Count')
            st.altair_chart(chart, use_container_width=True)
            
            
        with col2:
            
            custom_color_scheme = alt.Scale(domain=list(spring_2024.get_course('LIN')['Course']),
                                range=['#FF7F00', '#FF914D', '#FFA07A', '#FFB6C1', '#FFC0CB', '#F2DFFF', '#E1E1FF', '#D0D0FF', '#BEBEFF', '#ACACFF', '#9A9AFF', '#8888FF', '#7676FF'
])

            chart = alt.Chart(spring_2024.get_course('LIN')).mark_bar(
                cornerRadiusTopLeft=3,
                cornerRadiusTopRight=3
            ).encode(
                x='Course',
                y=alt.Y('# of Sections', axis=alt.Axis(tickCount=3)),
                color=alt.Color('Course', scale=custom_color_scheme, legend=None)
            )
            
            title = alt.TitleParams(text='Course sections in Spring 2024', align='left', fontSize=16, fontWeight='bold', color='#003264')

            chart = chart.properties(title=title)
            chart = chart.configure_axis(labelAngle=-0, title='Section Count')
            

            st.altair_chart(chart, use_container_width=True)      
         
        with col3:
            courses = ['LIN 100', 'LIN 101', 'LIN 110', 'LIN 125', 'LIN 140',
                       'LIN 150', 'LIN 250']
            
            spring_24_common = spring_2024.get_course('LIN')[spring_2024.get_course('LIN')['Course'].isin(courses)]
            spring_23_common = spring_2023.get_course('LIN')[spring_2023.get_course('LIN')['Course'].isin(courses)]

            comparison3 = pd.DataFrame({
                'Course': courses,
                'Spring 2023': spring_23_common['# Enrolled'],
                'Spring 2024': [100, 48, 17, 2, 35, 158, 153]
            })
            
            melted_df3 = pd.melt(comparison3, id_vars='Course', var_name='Semester', value_name='# Enrolled')
            custom_color_scheme = alt.Scale(domain=list(comparison3['Course']),
                                range=['#003264', '#1B3D71', '#354D7E', '#4D5D8B', '#666C99', '#807CA6', '#9A8CB3', '#CEACCE', '#E8BCDB', '#FFCCE8', '#FFC2CC', '#FFB7B2', '#004A8D' ]
)
             
            chart = alt.Chart(melted_df3).mark_line().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Spring 2024']),  # Added sort parameter here
                y='# Enrolled', 
                color=alt.Color('Course', scale=custom_color_scheme)
            ) + alt.Chart(melted_df3).mark_point().encode(
                x=alt.X('Semester:O', sort=['Spring 2023', 'Spring 2024']),  # And here
                y='# Enrolled',
                color='Course'
            )

            
            title = alt.TitleParams(text='Enrollment comparison with Spring 2023', align='left', fontSize=16, fontWeight='bold', color='#003264')
            
            chart = chart.configure_axis(labelAngle=-0, title='')
            chart = chart.properties(title=title)
                       
            st.altair_chart(chart, use_container_width=True) 
            
# CLASSES

with st.container():
    st.markdown('## Classes')
    
    col1, col2, col3 = st.columns((3))
    
    with col1:
        def class_heatmap(df):
            # Filter rows where 'Days', 'Mtg Start', and 'Mtg End' are not NaN
            df_filtered = df.dropna(subset=['Days', 'Mtg Start', 'Mtg End'])

            # Convert 'Mtg Start' and 'Mtg End' to 24-hour format
            df_filtered['Mtg Start'] = pd.to_datetime(df_filtered['Mtg Start'], format='%I:%M:%S %p').dt.strftime('%H:%M')
            df_filtered['Mtg End'] = pd.to_datetime(df_filtered['Mtg End'], format='%I:%M:%S %p').dt.strftime('%H:%M')

            # Expand 'Days' into separate rows
            days_mapping = {
                'M': 'Mon',
                'Tu': 'Tue',
                'W': 'Wed',
                'Th': 'Thu',
                'F': 'Fri',
                'Sa': 'Sat',
                'Su': 'Sun'
            }

            # Function to expand days
            def expand_days(row):
                expanded_days = []
                for key, value in days_mapping.items():
                    if key in row['Days']:
                        expanded_days.append(value)
                return expanded_days

            # Apply function and explode into separate rows
            df_filtered['Expanded Days'] = df_filtered.apply(expand_days, axis=1)
            df_exploded = df_filtered.explode('Expanded Days')

            # Create a 'Time Slot' column combining 'Mtg Start' and 'Mtg End'
            df_exploded['Time Slot'] = df_exploded['Mtg Start'] + '-' + df_exploded['Mtg End']

            # Aggregate data to count the number of classes in each time slot for each day
            df_aggregated = df_exploded.groupby(['Expanded Days', 'Time Slot']).size().reset_index(name='Count')

            days_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

            # Creating the heatmap
            heatmap = alt.Chart(df_aggregated).mark_rect().encode(
                x=alt.X('Expanded Days:O', sort=days_order, title=None, axis=alt.Axis(labelAngle=0)),
                y=alt.Y('Time Slot:O', title=None),
                color=alt.Color('Count:Q', scale=alt.Scale(scheme='blues'), legend=None, title='Number of Classes'),
                tooltip=[alt.Tooltip('Count:Q', title='Number of Classes'), 'Time Slot', 'Expanded Days']
            ).properties(
                title=alt.TitleParams(
                text='Class Times in Spring 2024', 
                align='left', 
                fontSize=16, 
                fontWeight='bold', 
                color='#003264'
            ),
                width=400,
                height=400
            )

            st.altair_chart(heatmap, use_container_width=True) 
            
        query_24 = pd.read_csv('datasets/spring_24_query.csv', header=0)
        
        class_heatmap(query_24) 
        
    with col2:
        # Read the CSV file and check the headers
        query = pd.read_csv('datasets/spring_24_query.csv').fillna(0)  # Assuming the first row is the header

        # Validate that 'Subject' and 'Room' are in the DataFrame columns
        if 'Subject' not in query.columns or 'Room' not in query.columns:
            st.error("DataFrame is missing one or more required columns: 'Subject' or 'Room'")
            st.stop()

        where_df = query[['Subject', 'Room']]
        where_df = where_df[where_df['Room'] != 0]

        def where(df):
            df = df.copy()
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
                        
        title = alt.TitleParams(text='Class mode and location in Spring 2024', align='left', fontSize=16, fontWeight='bold', color='#003264')
        chart = chart.properties(title=title)
        chart = chart.configure_axis(labelAngle=-0, title='')
        
        st.altair_chart(chart, use_container_width=True) 
        
    with col3:
        status = pd.read_csv('datasets/spring_24_query.csv', header=0)
        
        # Assuming this DataFrame has columns named 'Class Stat' and 'Subject'
        status = status[['Class Stat', 'Subject']]
        status.columns = ['Status', 'Course Group']

        # Filter for cancelled classes
        cancelled_classes = status[status['Status'] == 'Cancelled']

        # Correctly group by 'Course Group' to get the count of cancelled classes per course group
        cancelled_summary = cancelled_classes.groupby('Course Group').size().reset_index(name='Count')

        # Construct the chart with corrected data
        chart = alt.Chart(cancelled_summary).mark_bar().encode(
            x=alt.X('Course Group:N', title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Count:Q', title=None),
            color=alt.Color('Course Group:N', scale=custom_color_scale, legend=None)
        ).properties(
            title=alt.TitleParams(
                text='# of Cancelled Classes in Spring 2024', 
                align='left', 
                fontSize=16, 
                fontWeight='bold', 
                color='#003264'
            ),
            width=400,
            height=400
        )

        chart = chart.configure_axis(labelFontSize=12, titleFontSize=14)
        chart = chart.configure_title(fontSize=16)

        st.altair_chart(chart, use_container_width=True)
