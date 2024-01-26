import streamlit as st
import pandas as pd
import os  # Import os module for file existence check


def main():
    from datetime import datetime, date, time
    # Define app title and layout
    st.set_page_config(page_title="Health Provider Experience", page_icon=":hospital:", layout="wide" )

    # Create a visually appealing UI with clear instructions
    #st.title(":blue[Health Provider Experience]")
    #st.title('''$$\\bigstar $$:hospital: :blue[Health Provider Experience] :hospital: $$\\bigstar $$''')
    st.title(''':hospital: :blue[Health Provider Experience] :hospital:''')
    with st.sidebar:
        st.markdown('''## :wave:$$\\bigstar $$ :red[ATTENTION]  $$\\bigstar $$:wave:''')
        outcome = st.selectbox("Resolved or Not", ["Not Resolved", "Resolved"])
        hospital_date = st.date_input("Date of Visit: Click to select", date.today())
        
    #st.write("Please enter your information below:")
    #st.info("Please enter your information below:")
    #st.subheader("Please enter your information below:")
    st.markdown("#### Please enter your information below:")
    # Collect user input with appropriate input types
    first_name = st.text_input("First Name:")    
    last_name = st.text_input("Last Name:")
    hospital = st.text_input("Hospital:")   
    enrollee_number = st.text_input("Enrollee Number:")
    user_text = st.text_area("Summary of your experience: ")
    st.write(":red[Please make sure you select 'Resolved or Not' option from the left  before submitting:]")
    #st.write(f'Your last name is: **{last_name}**') # **bold text** and variable confirmed

    # Submit button to save data to CSV
    if st.button("Submit"):
        # Create a DataFrame to hold the data
        data = pd.DataFrame({
            "Full Name": [first_name],
            "Last Name": [last_name],
            "Hospital": [hospital],
            "Enrollee Number": [enrollee_number],
            "Experience": [user_text],
            # Add the outcome column
            "Outcome": [outcome],
            "Date of Visit": [hospital_date]
        })

        # Check if the CSV file exists and write the header if it doesn't
        if not os.path.exists("users.csv"):
            data.to_csv("users.csv", mode="a", index=False, header=True)  # Write header only once
        else:
            data.to_csv("users.csv", mode="a", index=False, header=False)  # Append without header

        st.success("Data saved to spreadsheet successfully!")
        st.dataframe(data)
        st.balloons()
        #st.snow()

    # Download button to download the latest data
    if st.button("Download Data"):
        st.download_button(
            label="Download CSV/spreadsheet",
            data=open("users.csv", "rb"),
            file_name="users.csv",
            mime="text/csv"
        )
    
    

if __name__ == "__main__":
    main()
