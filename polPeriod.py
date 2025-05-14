import streamlit as st 
import pandas as pd
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from streamlit_timeline import st_timeline


st.set_page_config(page_title="Short-Term Calculator", layout="wide")
st.write("""

# Short-Term Policy Period Calculator


##### Have a short term policy? Visualize it here to see how your experience changes

""")

# Short-term Policy Inception Date
shortTermStart = st.date_input(" ##### Enter the Start Date of Short-Term Policy")
shortTermStart_str = shortTermStart.isoformat()
# Policy End Date
shortTermEnd = st.date_input(" ##### Enter the End Date of Short-Term Policy")
shortTermEnd_str = shortTermEnd.isoformat()



# POLICY YEAR CALCULATION PRIOR TO SHORT TERM POLICY
# Current Policy minus 1 year
polMinusOne = shortTermStart - relativedelta(years=1)
polMinusOne_str = polMinusOne.isoformat()
# Current Policy minus 2 years
polMinusTwo = polMinusOne - relativedelta(years=1)
polMinusTwo_str = polMinusTwo.isoformat()
# Current Policy minus 3 years
polMinusThree = polMinusTwo - relativedelta(years=1)
polMinusThree_str = polMinusThree.isoformat()
# Current Policy minus 4 years
polMinusFour = polMinusThree - relativedelta(years=1)
polMinusFour_str = polMinusFour.isoformat()



# POLICY YEAR CALCULATION AFTER SHORT TERM POLICY
# Current Policy plus 1 year
polPlusOne = shortTermEnd + relativedelta(years=1)
polPlusOne_str = polPlusOne.isoformat()
# Current Policy plus 2 years
polPlusTwo = polPlusOne + relativedelta(years=1)
polPlusTwo_str = polPlusTwo.isoformat()
# Current Policy plus 3 years
polPlusThree = polPlusTwo + relativedelta(years=1)
polPlusThree_str = polPlusThree.isoformat()
# Current Policy plus 4 years
polPlusFour = polPlusThree + relativedelta(years=1)
polPlusFour_str = polPlusFour.isoformat()
# Current Policy plus 5 years
polPlusFive = polPlusFour + relativedelta(years=1)
polPlusFive_str = polPlusFive.isoformat()





# Calculate year and month difference
yearDiff = shortTermEnd.year - shortTermStart.year
monthDiff = shortTermEnd.month - shortTermStart.month 

# Total Months Difference
totalMonths = yearDiff * 12 + monthDiff
# Adjust for the days within the months
if shortTermEnd.day < shortTermStart.day:
    totalMonths -= 1


st.write(f" #### You're Short Term Policy is: {totalMonths} month(s)")



# Define Dictionary Wrapper with '3 Months or less' scenario and 'More than 3 Months' scenario
shortDict = {}
# One year after shortTermStart
shortOneYear = shortTermStart + relativedelta(years=1)
shortOneYear_str = shortOneYear.isoformat()



if totalMonths <= 3:
    shortDict = [
        {"content": "Effective Ex Mod", "start": shortTermStart_str, "end": polPlusOne_str, "group": 2, "style":"height: 70px;"},
        {"content": f"Experience: {polMinusFour.year}, {polMinusThree.year}, {polMinusTwo.year}", "start": polMinusFour_str, "end": polMinusOne_str, "group": 2, "style":"height: 70px;"},

        {"content": f"{polPlusOne.year} Mod", "start": polPlusOne_str, "end": polPlusTwo_str, "group": 4, "style":"height: 70px;"},
        {"content": f"Experience: {polMinusThree.year}, {polMinusTwo.year}, {polMinusOne.year}", "start": polMinusThree_str, "end": shortTermStart_str, "group": 4, "style":"height: 70px;"},

        {"content": f"{polPlusTwo.year} Mod", "start": polPlusTwo_str, "end": polPlusThree_str, "group": 5, "style":"height: 70px;"},
        {"content": f"Experience: {polMinusTwo.year}, {polMinusOne.year}, SHORT, {shortTermEnd.year}", "start": polMinusTwo_str, "end": polPlusOne_str, "group": 5, "style":"height: 70px;"},

        {"content": f"{polPlusThree.year} Mod", "start": polPlusThree_str, "end": polPlusFour_str, "group": 6, "style":"height: 70px;"},
        {"content": f"Experience: {polMinusOne.year}, SHORT, {shortTermEnd.year}, {polPlusOne.year}", "start": polMinusOne_str, "end": polPlusTwo_str, "group": 6, "style":"height: 70px;"},

        {"content": f"{polPlusFour.year} Mod", "start": polPlusFour_str, "end": polPlusFive_str, "group": 7, "style":"height: 70px;"},
        {"content": f"Experience: SHORT, {shortTermEnd.year}, {polPlusOne.year}, {polPlusTwo.year}", "start": shortTermStart_str, "end": polPlusThree_str, "group": 7, "style":"height: 70px;"},
        ]
else:
    shortDict = [
        {"content": "Effective Mod", "start": shortTermStart_str, "end": shortOneYear_str, "group": 2, "style":"height: 70px;"},
        {"content": f"Experience: {polMinusFour.year}, {polMinusThree.year}, {polMinusTwo.year}", "start": polMinusFour_str, "end": polMinusOne_str, "group": 2, "style":"height: 70px;"},
        {"content": "Short Mod", "start": shortOneYear_str, "end": polPlusOne_str, "group": 3, "style":"height: 70px;"},
        {"content": f"Experience: {polMinusThree.year}, {polMinusTwo.year}, {polMinusOne.year}", "start": polMinusThree_str, "end": shortTermStart_str, "group": 3, "style":"height: 70px;"},
        
        {"content": f"{polPlusOne.year} Mod", "start": polPlusOne_str, "end": polPlusTwo_str, "group": 4, "style":"height: 70px;"},
        {"content": f"Experience: {polMinusTwo.year}, {polMinusOne.year}, SHORT", "start": polMinusTwo_str, "end": shortTermEnd_str, "group": 4, "style":"height: 70px;"},

        {"content": f"{polPlusTwo.year} Mod", "start": polPlusTwo_str, "end": polPlusThree_str, "group": 5, "style":"height: 70px;"},
        {"content": f"Experience: {polMinusOne.year}, SHORT, {shortTermEnd.year}", "start": polMinusOne_str, "end": polPlusOne_str, "group": 5, "style":"height: 70px;"},

        {"content": f"{polPlusThree.year} Mod", "start": polPlusThree_str, "end": polPlusFour_str, "group": 6, "style":"height: 70px;"},
        {"content": f"Experience: SHORT, {shortTermEnd.year}, {polPlusOne.year}", "start": shortTermStart_str, "end": polPlusTwo_str, "group": 6, "style":"height: 70px;"},

        {"content": f"{polPlusFour.year} Mod", "start": polPlusFour_str, "end": polPlusFive_str, "group": 7, "style":"height: 70px;"},
        {"content": f"Experience: {shortTermEnd.year}, {polPlusOne.year}, {polPlusTwo.year}", "start": shortTermEnd_str, "end": polPlusThree_str, "group": 7, "style":"height: 70px;"},
    ]



items = [
    # Timeline for Policy Period
    {"content": f"{polMinusFour.year} - {polMinusThree.year}", "start": polMinusFour_str, "end":polMinusThree_str, "group": 1, "style":"background-color: #ffca91; border-color: black; height: 70px; height: 70px;"},
    {"content": f"{polMinusThree.year} - {polMinusTwo.year}", "start": polMinusThree_str, "end":polMinusTwo_str, "group": 1, "style":"background-color: #ffca91; border-color: black; height: 70px;"},
    {"content": f"{polMinusTwo.year} - {polMinusOne.year}", "start": polMinusTwo_str, "end":polMinusOne_str, "group": 1, "style":"background-color: #ffca91; border-color: black; height: 70px;"},
    {"content": f"{polMinusOne.year} - {shortTermStart.year}", "start": polMinusOne_str, "end":shortTermStart_str, "group": 1, "style":"background-color: #ffca91; border-color: black; height: 70px;"},
    {"content": f"SHORT", "start": shortTermStart_str, "end":shortTermEnd_str, "group": 1, "style":"background-color: #ffb3f1; border-color: black; height: 70px;"},
    {"content": f"{shortTermEnd.year} - {polPlusOne.year}", "start": shortTermEnd_str, "end":polPlusOne_str, "group": 1, "style":"background-color: #ffca91; border-color: black; height: 70px;"},
    {"content": f"{polPlusOne.year} - {polPlusTwo.year}", "start": polPlusOne_str, "end":polPlusTwo_str, "group": 1, "style":"background-color: #ffca91; border-color: black; height: 70px;"},
    {"content": f"{polPlusTwo.year} - {polPlusThree.year}", "start": polPlusTwo_str, "end":polPlusThree_str, "group": 1, "style":"background-color: #ffca91; border-color: black; height: 70px;"},
    {"content": f"{polPlusThree.year} - {polPlusFour.year}", "start": polPlusThree_str, "end":polPlusFour_str, "group": 1, "style":"background-color: #ffca91; border-color: black; height: 70px;"},
    {"content": f"{polPlusFour.year} - {polPlusFive.year}", "start": polPlusFour_str, "end":polPlusFive_str, "group": 1, "style":"background-color: #ffca91; border-color: black; height: 70px;"},
    # Timeline for Effective Ex Mod and Experience Range
    *shortDict,
]

groups = [
    {"id": 1, "content": "Policy Periods"},
    {"id": 2, "content": "Effective Ex Mod"},
    {"id": 3, "content": "Short Ex Mod"},
    {"id": 4, "content": f"{polPlusOne.year} Mod"},
    {"id": 5, "content": f"{polPlusTwo.year} Mod"},
    {"id": 6, "content": f"{polPlusThree.year} Mod"},
    {"id": 7, "content": f"{polPlusFour.year} Mod"},
]

# polMinusFive = polMinusFour - relativedelta(years=1)
# polMinusFive_str = polMinusFive.isoformat()

# polPlusFive = polPlusFour + relativedelta(years=1)
# polPlusFive_str = polPlusFive.isoformat()

options = {
    "orientation": {"axis": "both"},
    "groupOrder": "id",
    "groupHeightMode": "fixed",
    "stack": False,
    "align": "center",
    "maxHeight": 700,
    "showCurrentTime": False,
    "zoomKey": 'ctrlKey',
    "horizontalScroll": True,
}


timeline = st_timeline(items, groups,options, height="700px")
st.write(timeline)
