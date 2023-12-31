# PhonePe-pulse-visualization

Table of contents
> About The Project

> Getting Started

> Prerequisites

> Installation

> Usage

> Steps

> Run

> Skills Covered


# Concerning the project
This project is focused on cloning a github repository Phone-pe-pulse which contains a large amount of data related to various metrics and statistics.We will be transforming the data in an useful manner and create a streamit dashboard to visualize the data.Creating a live geo map.

# Libraries used
> json
> pymysql
> os
> streamlit
> plotly.express
> streamlit_option_menu
> pandas - are the Python libraries used in this project

# Installation
pip install json
pip install os
pip install plotly
pip install streamlit
pip install pandas
pip install pymysql
pip insatall streamlit_option_menu

# Usage
>> In this Project, Wrote a python program to clone a git hub repository
>> Fetched required data using os library and preprocessed stored it into MySql Database using PyMySql
>> Created different options that user can select and get insights from it
>> created Live geo Map, Analysing the data and visualizing it in 5 different charts based on the option which user selects

# Steps
>> Import all the libraries that are used in this project.
>> Created 6 functions which returns aggregated,map and top data for all states on year wise upto 2023 Quarter 4.
>> Cretaed a function to link mysql and migrate data into SQL Database
>> Created Dashboard on Streamlit and gave optionmenu to navigate through map, analysis, visualize
>> created different selectbox and buttons to make our project work alongside what the user opts

# Run
>> To Run this project we need to go to terminal and change its path to file_loacted_directory
>> Then run streamlit code to execute,
** streamlit run file_name.py
-replace file_name with created python file name
-To run this project use,
**streamlit run phpe.py 
