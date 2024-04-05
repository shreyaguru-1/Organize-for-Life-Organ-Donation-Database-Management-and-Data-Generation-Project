import streamlit as st
import psycopg2
import pandas as pd


conn = psycopg2.connect(
    host="localhost",
    database="OrganDonation",
    user="postgres",
    password="rohanvs"
)

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('organ_donor_featured.jpg')  

#st.set_page_config(page_title="Organize For Life", page_icon=":smiley:", layout="wide")
#url('/Users/rohanvs/Desktop/UB_Academics/CSE_560/Project/organ_donor_featured.jpg')
#st.set_page_config(page_title="My Streamlit App", page_icon=":smiley:", layout="wide", page_bg_img="https://example.com/my_background_image.jpg")

cursor = conn.cursor()

dropdown_options = {
    "SELECT statement": "select_table",
    "Select Statement with Where Clause": "select_where_table",
    "COUNT and GROUP BY clause": "count_groupby_clause",
    "JOIN two tables": "join_table",
    "INNER Query": "inner_query",
    "Avg() Operator Query": "avg_operator",
    "DELETE Query": "delete_query",
    "UPDATE Query": "update_query",
}

query_dict = {
    "select_table": "SELECT * FROM USER_INFO;",
    "select_where_table": "SELECT U.USER_ID, U.USER_NAME FROM USER_INFO AS U, DONOR AS D, ORGAn AS O WHERE U.USER_ID=D.USER_ID AND O.USER_ID=D.USER_ID AND O.AVAILIBILITY='Yes';",
    "count_groupby_clause": "SELECT BLOOD_TYPE, COUNT(USER_ID) AS DONORS_COUNT FROM DONOR GROUP BY BLOOD_TYPE;",
    "join_table": "SELECT D.USER_ID, O.ORGAN_TYPE FROM DONOR AS D NATURAL JOIN ORGAN AS O WHERE O.ORGAN_TYPE='Kidney';",
    "inner_query": "SELECT USER_ID, BLOOD_TYPE FROM (SELECT USER_ID, BLOOD_TYPE FROM DONOR) AS USER_ORGAN;",
    "avg_operator": "SELECT AVG(WEIGHT) AS WEI_AVG FROM DONOR WHERE GENDER = 'Male';",
    "delete_query": "DELETE FROM ORGAN WHERE ORGAN_ID = '123' RETURNING *;",
    "update_query": "UPDATE USER_INFO SET PHONE_NUMBER = '5555555555' WHERE USER_ID = '123' RETURNING *;",
}

# Create dropdown menu
selected_option = st.selectbox("Select a Query to run", list(dropdown_options.keys()))

query = ""
if dropdown_options[selected_option] != "input_own_query":
    query = query_dict[dropdown_options[selected_option]]
    df = pd.read_sql(query, conn)

    # Get the number of affected rows for update and delete queries
    if dropdown_options[selected_option] in ["query_delete_record", "query_update_record"]:
        num_affected_rows = cursor.rowcount

    # Display a success message if the query was successful
    if dropdown_options[selected_option] == "query_delete_record" and num_affected_rows > 0:
        st.success(f"Successfully deleted {num_affected_rows} rows.")
    elif dropdown_options[selected_option] == "query_update_record" and num_affected_rows > 0:
        st.success(f"Successfully updated {num_affected_rows} rows.")

# Close database connection
conn.close()

# Display ran query
st.write("Query: ", query)

# Display DataFrame in Streamlit
st.write(df)
