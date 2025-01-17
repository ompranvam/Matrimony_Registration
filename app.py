import pandas as pd
import streamlit as st
import sqlite3 
###libraries for pdf generator
from fpdf import FPDF
import os
import tempfile
from datetime import datetime, date



## connection to sqlite3
conn = sqlite3.connect('customer.db')
cursor = conn.cursor()



## Create Table

cursor.execute('''CREATE TABLE IF NOT EXISTS members (
    Member_Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Gender TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Birth_City TEXT NOT NULL,
    Marital_status TEXT NOT NULL,
    Mother_tongue TEXT NOT NULL,
    Religion TEXT NOT NULL,
    Class TEXT NOT NULL,
    Caste TEXT NOT NULL,
    Sub_caste TEXT NOT NULL,
    Rasi TEXT NOT NULL,
    Star TEXT NOT NULL,
    DOB TEXT NOT NULL,
    Height REAL NOT NULL,
    Weight REAL NOT NULL,
    Physical_status TEXT,
    Complexion TEXT,
    Blood_Group TEXT,
    Others TEXT,
    Smoking TEXT,
    Drinking TEXT,
    Diet TEXT,
    Education TEXT NOT NULL,
    Course TEXT,
    Occupation TEXT,
    Annual_Income REAL,
    Family_Status TEXT,
    Family_Value TEXT,
    Residing_City TEXT,
    Brothers INTEGER,
    Married_Brothers INTEGER,
    Sisters INTEGER,
    Married_Sisters INTEGER,
    Age_From INTEGER,
    Partner_Height REAL,
    Partner_Religion TEXT,
    Partner_Class TEXT,
    Partner_Caste TEXT,
    Partner_Subcaste TEXT,
    Partner_Physical TEXT,
    Partner_Marital TEXT,
    Partner_Education TEXT,
    Partner_Occupation TEXT,
    Partner_Smoking TEXT,
    Partner_Drinking TEXT,
    Partner_Diet TEXT,
    Notes TEXT,
    Mobile_no TEXT NOT NULL,
    Alternative_mobile_no TEXT NOT NULL,
    Contact_person TEXT,
    Contact_Email TEXT,
    Registration_Date TEXT NOT NULL,
    Photo_image BLOB,
    Horoscope_image BLOB)''')



# Set page configuration
st.set_page_config(
    page_title="Matrimony Registration Form",  # Title of the web page
    page_icon="💑" ,  # Icon that will appear on the browser tab (can use emojis or image URL)
    layout="wide",  # Layout options: "centered" (default) or "wide"
    initial_sidebar_state="collapsed",  # Sidebar state: "auto", "expanded", or "collapsed"
)

def set_background_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background color
background_color = "#302b30"  # Use any valid CSS color (name, HEX, RGB, etc.)
set_background_color(background_color)


st.markdown(
    """
    <style>
    .centered-title-main {
        text-align: center;
        color: green;
        font-size: 3.5em;
        font-weight: bold;
    }
    .centered-title-sub {
        text-align: center;
        color: violet;
        font-size: 2em;
        font-weight: bold;
    }
        .centered-title-sub1 {
        text-align: center;
        color: pink;
        font-size: 1em;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title with the custom class
st.markdown('<div class="centered-title-main">ஓம் பிரணவம் ஜோதிட மையம்</div>', unsafe_allow_html=True)
st.markdown('<div class="centered-title-sub">செங்குந்தர் தெய்வீக மணமாலை',  unsafe_allow_html=True)
st.markdown('<div class="centered-title-sub1">44 SND Road, திருச்செங்கோடு, நாமக்கல் -637211',  unsafe_allow_html=True)
st.markdown('<div class="centered-title-sub1">Contact : 9362040404, 9345118219',  unsafe_allow_html=True)




tabs = st.tabs( [':blue[New Registration]',':green[All Customer Details]',':blue[Search Customer Details & Print]',':red[Update & Delete Members]'])


with tabs[0]:

    col1,col2 = st.columns(2)

    with col1:
    
        # Basic Information
        st.header("Personal Details")
        name = st.text_input("Name:", placeholder="Enter your name")
        gender = st.selectbox("Gender",['','Male','Female'])
        age = st.number_input("Age", min_value=18, max_value=100)
        place_of_birth = st.text_input("Place of Birth", placeholder="e.g., Kangeyam")
        marital_status = st.selectbox("Marital Status", ["Never Married", "Married", "Divorced"])
        mother_tongue = st.text_input("Mother Tongue", placeholder="e.g., Tamil")
        religion = st.selectbox("Choose your Religion", ["Hindu", "Christian", "Musilm", "Converted Christian", "Converted Muslim","Others"])
        Class = st.selectbox("Choose your class", ["OC", "BC", "MBC", "SC", "SCA"])
        caste = st.text_input("Caste", placeholder="e.g., Sengunthar")
        sub_caste = st.text_input("Sub Caste", placeholder="e.g., Semalaikaran Kootam")
        rasi = st.selectbox("Rasi",['','Mesham','Rishabham','Mithunam','Kadkam','Simam','Kani','Tulam','Vrishchikagam','Dhanushu','Makaram','Kumbham','Meenam'])
        star = st.selectbox("Star", ['','Ashwini', 'Bharani', 'Karthikai', 'Rohini', 'Mirukasiridam', 'Thiruvadirai', 'Punaraphusam', 'Phusam', 'Ailyam', 'Magam', 'Pooram', 'Uthiram', 'Astam' ,' Sidhirai','Swathi','Visagam','Anusham','Gatei','Mulam','Puradam','Uthradam','Tiruvonam','Avitam','Sadayam','Puratathi','Uthratathi' , 'Revathi'])
        dob = st.date_input("Date of Birth")

        # Physical Appearanceh
        st.header("Physical Appearance")
        height = st.text_input("Height", placeholder="e.g., 5ft 5in - 165cm")
        weight = st.number_input("Weight (kg)", min_value=35, max_value=150, format="%d")
        physical_status = st.selectbox("Physical Status", ['Normal',"Special"])
        complexion = st.selectbox("Complexion",['','Fair','Light',"Medium","Tan","Dark"])
        blood_group = st.selectbox("Blood Group", ['','B+','O+','A+','AB+','B-','A-','O-','AB-'])
        Other = st.text_input("If Specify")


        # Lifestyle
        st.header("Lifestyle")
        smoking = st.selectbox("Smoking", ["No", "Yes"])
        drinking = st.selectbox("Drinking", ["No", "Yes"])
        diet = st.selectbox("Diet", ["Vegetarian", "Non-Vegetarian"])


        # Photo Upload
        st.header("Upload Profile Photo")
        photo = st.file_uploader("Upload your photo", type=["JPG","jpg", "jpeg", "png"])

        show_photo = st.checkbox("Show Photo")

        if show_photo:
            try:

                st.image(photo, caption="Profile Photo", use_container_width=True)
            except:
                st.error("Please Upload Photo")

        
        # Horoscope Upload
        st.header("Upload Horoscope")
        horoscope = st.file_uploader("Upload your horoscope", type=["jpg", "jpeg", "png"])
        show_horoscope = st.checkbox("Show Horoscope")
        
        if show_horoscope:
            try:
                st.image(horoscope, caption="Profile Photo", use_container_width=True)
            except:
                st.error('Please Upload Horoscope')

        # Education & Career
        st.header("Education & Career")
        education = st.selectbox("Education", ["Non Graduate", "Under Graduate(UG)", "Post Graduate(PG)"])
        course = st.text_input("Courses", placeholder="e.g., BSC - Visual Communication")
        occupation = st.text_input("Occupation", placeholder="e.g., Software Engineer")
        annual_income = st.selectbox("Annual Income", ["None","< 5 Lakhs", "5 Lakhs to 10 Lakhs", "10 Lakhs to 20 Lakhs", "20 Lakhs and above"])


        # Family Details
        st.header("Family Details")
        family_status = st.selectbox("Family Status", ["Upper Middle Class", "Middle Class", "Lower Middle Class"])
        family_value = st.selectbox("Family Value", ["Traditional", "Moderate", "Liberal"])
        residing_city = st.text_input("Residing City", placeholder="e.g., Chennai")
        no_of_brothers = st.number_input("No of Brothers", min_value=0, step=1, format="%d")
        married_brothers = st.number_input("Married Brothers", min_value=0, step=1, format="%d")
        no_of_sisters = st.number_input("No of Sisters", min_value=0, step=1, format="%d")
        married_sisters = st.number_input("Married Sisters", min_value=0, step=1, format="%d")


        # Partner Preference
        st.header("Partner Preference")
        age_from = st.number_input("Preferred Age From", min_value=18, max_value=100)
        partner_height = st.number_input("Partner's Height (in cm)", min_value=0, max_value=300)
        partner_religion = st.selectbox("Partner's Religion", ["Hindu", "Christian", "Musilm", "Converted Christian", "Converted Muslim","Others"])
        partner_class = st.selectbox("Partner's Class", ["OC", "BC", "MBC", "SC", "SCA"])
        partner_caste = st.text_input("Partner's Caste")
        partner_subcaste = st.text_input("Partner's Subcaste")
        partner_physical = st.text_input("Partner's Physical Status")
        partner_marital = st.selectbox("Partner's Marital Status", ["Never Married", "Divorced", "Widowed"])
        partner_education = st.text_input("Partner's Education")
        partner_occupation = st.text_input("Partner's Occupation")
        partner_smoking = st.selectbox("Partner's Smoking", ["No", "Yes"])
        partner_drinking = st.selectbox("Partner's Drinking", ["No", "Yes"])
        partner_diet = st.selectbox("Partner's Diet", ["Vegetarian", "Non-Vegetarian"])
        notes = st.text_input("Other Preference")

        # Contact Details
        st.header("Contact Details")
        mobile_no = st.text_input("Mobile No", placeholder="Enter Mobile Number")
        alternative_mobile_no = st.text_input("Alternative Mobile No", placeholder="Enter Alternate Mobile Number")
        contact_person = st.text_input("Contact Person", placeholder="Enter Contact Person Name")
        contact_email = st.text_input("Contact Email", placeholder="e.g., abc@gmail.com")
        reg_date = st.date_input("Registration Date")
   
   
    with col2:
        
    
        if st.button("Review Profile"):
            try:
                c1, c2 = st.columns(2)
                
                # Column 1: Personal, Education, Family, and Partner Information
                with c1:
                    st.header(":blue[Profile Preview]")
                    st.subheader(":green[Personal Information]")
                    st.write(f"**Name:** {name}")
                    st.write(f"**Gender:** {gender}")
                    st.write(f"**Age:** {age}")
                    st.write(f"**Place of Birth:** {place_of_birth}")
                    st.write(f"**Marital Status:** {marital_status}")
                    st.write(f"**Mother Tongue:** {mother_tongue}")
                    st.write(f"**Religion:** {religion}")
                    st.write(f"**Class:** {Class}")
                    st.write(f"**Caste:** {caste}")
                    st.write(f"**Sub Caste:** {sub_caste}")
                    st.write(f"**Rasi:** {rasi}")
                    st.write(f"**Star:** {star}")
                    st.write(f"**DOB:** {dob}")

                    st.subheader(":green[Physical Apperance]")
                    st.write(f"**Height:** {height}")
                    st.write(f"**Weight:** {weight}")
                    st.write(f"**Physical Status:** {physical_status}")
                    st.write(f"**Complexion:** {complexion}")
                    st.write(f"**Blood Group:** {blood_group}")
                    st.write(f"**Others:** {Other}")
                    st.write(f"**Smoking:** {smoking}")
                    st.write(f"**Drinking:** {drinking}")
                    st.write(f"**Diet:** {diet}")
                    
                    # Education Information
                    st.subheader(":green[Education Details]")
                    st.write(f"**Education:** {education}")
                    st.write(f"**Course:** {course}")
                    st.write(f"**Occupation:** {occupation}")
                    st.write(f"**Annual Income:** {annual_income}")
                    
                    # Family Details
                    st.subheader(":green[Family Details]")
                    st.write(f"**Family Status:** {family_status}")
                    st.write(f"**Family Value:** {family_value}")
                    st.write(f"**No. of Brothers:** {no_of_brothers}")
                    st.write(f"**Married Brothers:** {married_brothers}")
                    st.write(f"**No. of Sisters:** {no_of_sisters}")
                    st.write(f"**Married Sisters:** {married_sisters}")
                    
                    # Partner Preference
                    st.subheader(":green[Partner Preference]")
                    st.write(f"**Age From:** {age_from}")
                    st.write(f"**Height Preference:** {partner_height}")
                    st.write(f"**Religion Preference:** {partner_religion}")
                    st.write(f"**Class Preference:** {partner_class}")
                    st.write(f"**Caste Preference:** {partner_caste}")
                    st.write(f"**Sub Caste Preference:** {partner_subcaste}")
                    st.write(f"**Physical Status Preference:** {partner_physical}")
                    st.write(f"**Marital Status Preference:** {partner_marital}")
                    st.write(f"**Education Preference:** {partner_education}")
                    st.write(f"**Occupation Preference:** {partner_occupation}")
                    st.write(f"**Smoking Preference:** {partner_smoking}")
                    st.write(f"**Drinking Preference:** {partner_drinking}")
                    st.write(f"**Diet Preference:** {partner_diet}")
                    st.write(f"**Notes:** {notes}")
                    
                    # Contact Details
                    st.header(":green[Contact Details]")
                    st.write(f"**Mobile No:** {mobile_no}")
                    st.write(f"**Alternative Mobile No:** {alternative_mobile_no}")
                    st.write(f"**Contact Person:** {contact_person}")
                    st.write(f"**Contact Email:** {contact_email}")
                    st.write(f"**Registration Date:** {reg_date}")

                # Column 2: Photo and Horoscope
                with c2:
                    if photo:
                        st.image(photo, caption="Profile Photo", use_container_width=True)
                    if horoscope:
                        st.image(horoscope, caption="Horoscope", use_container_width=True)

            except Exception as e:
                st.write("Please refill the missing fields")
                st.error(f"Error occurred: {e}")


        if st.button("Submit Profile"):

            try:
                # Convert images to binary (BLOB)
                photo_blob = photo.read() if photo else None
                horoscope_blob = horoscope.read() if horoscope else None


                cursor.execute('''INSERT INTO members (
                Name,Gender, Age, Birth_City, Marital_status, Mother_tongue, Religion, Class, Caste, 
                Sub_caste,Rasi, Star, DOB, Height, Weight, Physical_status, Complexion, 
                Blood_Group, Others, Smoking, Drinking, Diet, Education, Course, Occupation, Annual_Income, 
                Family_Status, Family_Value, Residing_City, Brothers, Married_Brothers, Sisters, 
                Married_Sisters, Age_From, Partner_Height, Partner_Religion, Partner_Class, 
                Partner_Caste, Partner_Subcaste, Partner_Physical, Partner_Marital, Partner_Education, 
                Partner_Occupation, Partner_Smoking, Partner_Drinking, Partner_Diet, Notes, Mobile_no, 
                Alternative_mobile_no, Contact_person, Contact_Email,Registration_Date, Photo_image, Horoscope_image) 
                VALUES (?, ? , ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,? ,? ,?, ?)''', 
                
                (name,gender, age, place_of_birth, marital_status, mother_tongue, religion, Class, caste, sub_caste,rasi,
                star, str(dob), height, weight, physical_status, complexion, blood_group, Other, smoking, 
                drinking, diet, education, course, occupation, annual_income, family_status, family_value, 
                residing_city, no_of_brothers, married_brothers, no_of_sisters, married_sisters, age_from, partner_height, 
                partner_religion, partner_class, partner_caste, partner_subcaste, partner_physical, partner_marital, 
                partner_education, partner_occupation, partner_smoking, partner_drinking, partner_diet, notes, mobile_no, 
                alternative_mobile_no, contact_person, contact_email,reg_date, photo_blob, horoscope_blob))

                # Commit the transaction
                conn.commit()
                st.success("Profile Registerd Successfully")
                # st.write(f"**Member_ID:** {contact_person}")
            except Exception as e:
                st.write("Please refill the missing fields")
                st.error(f"Error occurred: {e}")



with tabs[1]:

    df = pd.read_sql_query("SELECT * FROM members", conn)

    df = df.drop(columns=['Photo_image', 'Horoscope_image'])

    st.dataframe(df,hide_index=True)


with tabs[2]:
    col1,col2  = st.columns(2)

    with col1:

        class PDF(FPDF):
            def header(self):
                self.set_font('Arial', 'B', 12)
                self.image('logo.png', x=45, y=4, w=120)  # Ensure the image path is correct
                self.ln(20)
                self.add_border()
                

            def footer(self):
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

            def add_border(self):
                # Add a border for the entire sheet
                self.set_draw_color(255, 0, 0)  # Set border color to red
                self.set_line_width(0.5)       # Set border thickness
                self.rect(5, 5, 200, 287)     # x, y, width, height (adjust as per your page size)

            
            # def set_unicode_font(self):
            #     # Make sure the Tamil font .ttf file is in the same directory or provide full path
            #     self.add_font('Latha', '', 'Latha.ttf', uni=True)  # Adjust path if needed
            #     self.set_font('Latha', '', 12)  # Use Latha font for Tamil text


        # Function to fetch member data from the database
        def get_customer_data(search_opt, search_que):
            conn = sqlite3.connect('customer.db')
            cursor = conn.cursor()
            
            if search_opt == 'Member ID':
                cursor.execute("SELECT * FROM members WHERE Member_Id = ?", (search_que,))
            elif search_opt == 'Name':
                cursor.execute("SELECT * FROM members WHERE Name LIKE ?", ('%' + search_que + '%',))

            customer_data = cursor.fetchone()
            conn.close()
            return customer_data

        # Function to create PDF
        def create_pdf(customer_data):
            pdf = PDF()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Add a page
            pdf.add_page()
            pdf.add_border()

            # Title
            pdf.set_font("Arial", 'B', 16)
            
            
            pdf.ln(10)

            # Personal Profile
            pdf.set_font("Arial", 'U', 15)
            pdf.cell(200, 10, "Personal Profile", ln=True, align='L')
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, f"Name: {customer_data[1] if customer_data[1] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Gender: {customer_data[2] if customer_data[2] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Age: {customer_data[3] if customer_data[3] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Birth City: {customer_data[4] if customer_data[4] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Marital Status: {customer_data[5] if customer_data[5] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Mother Tongue: {customer_data[6] if customer_data[6] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Religion: {customer_data[7] if customer_data[7] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Class: {customer_data[8] if customer_data[8] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Caste: {customer_data[9] if customer_data[9] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Sub Caste: {customer_data[10] if customer_data[10] else 'N/A'}")
            pdf.set_unicode_font()
            pdf.multi_cell(0, 10, f"Rasi: {customer_data[11] if customer_data[11] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Star: {customer_data[12] if customer_data[12] else 'N/A'}")
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, f"Date of Birth: {customer_data[13] if customer_data[13] else 'N/A'}")
            pdf.ln(5)

            pdf.set_font("Arial", 'U', 15)
            pdf.cell(200, 10, "Physical Apperance", ln=True, align='L')
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, f"Height: {customer_data[14] if customer_data[14] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Weight: {customer_data[15] if customer_data[15] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Physical Status: {customer_data[16] if customer_data[16] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Complexion: {customer_data[17] if customer_data[17] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Blood Group: {customer_data[18] if customer_data[18] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Others: {customer_data[19] if customer_data[19] else 'N/A'}")
            
            pdf.set_font("Arial", 'U', 15)
            pdf.cell(200, 10, "Life Style", ln=True, align='L')
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, f"Smoking: {customer_data[20] if customer_data[20] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Drinking: {customer_data[21] if customer_data[21] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Diet: {customer_data[22] if customer_data[22] else 'N/A'}")
            pdf.ln(5)

            pdf.set_font("Arial", 'U', 15)
            pdf.cell(200, 10, "Education Details", ln=True, align='L')
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, f"Education: {customer_data[23] if customer_data[23] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Course: {customer_data[24] if customer_data[24] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Occupation: {customer_data[25] if customer_data[25] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Annual Income: {customer_data[26] if customer_data[26] else 'N/A'}")
            pdf.ln(5)


            pdf.set_font("Arial", 'U', 15)
            pdf.cell(200, 10, "Family Details", ln=True, align='L')
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, f"Family Status: {customer_data[27] if customer_data[27] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Family Value: {customer_data[28] if customer_data[28] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Residing City: {customer_data[29] if customer_data[29] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Brothers: {customer_data[30] if customer_data[30] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Married Brothers: {customer_data[31] if customer_data[31] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Sisters: {customer_data[32] if customer_data[32] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Married Sisters: {customer_data[33] if customer_data[33] else 'N/A'}")
            pdf.ln(5)

            pdf.set_font("Arial", 'U', 15)
            pdf.cell(200, 10, "Partner Preference", ln=True, align='L')
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, f"Age Preference From: {customer_data[34] if customer_data[34] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Height: {customer_data[35] if customer_data[35] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Religion: {customer_data[36] if customer_data[36] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Class: {customer_data[37] if customer_data[37] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Caste: {customer_data[38] if customer_data[38] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Subcaste: {customer_data[39] if customer_data[39] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Physical Status: {customer_data[40] if customer_data[40] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Marital Status: {customer_data[41] if customer_data[41] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Education: {customer_data[42] if customer_data[42] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Occupation: {customer_data[43] if customer_data[43] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Smoking: {customer_data[44] if customer_data[44] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Drinking: {customer_data[45] if customer_data[45] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Partner Diet: {customer_data[46] if customer_data[46] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Notes: {customer_data[47] if customer_data[47] else 'No Notes Provided'}")

            pdf.ln(5)

            pdf.set_font("Arial", 'U', 15)
            pdf.cell(200, 10, "Contact Details", ln=True, align='L')

            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, f"Mobile No: {customer_data[48] if customer_data[48] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Alternative Mobile No: {customer_data[49] if customer_data[49] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Contact Person: {customer_data[50] if customer_data[50] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Contact Email: {customer_data[51] if customer_data[51] else 'N/A'}")
            pdf.multi_cell(0, 10, f"Registration Date: {customer_data[52] if customer_data[52] else 'N/A'}")




            # Move to the right side for images
            x_start = 120  # X position for the images
            y_start = pdf.get_y() - 50  # Adjust Y position to align images with contact details

            photo_path = customer_data[53]
            if photo_path:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
                    temp_file.write(photo_path)
                    temp_file_path = temp_file.name


                pdf.image(temp_file_path, x=10, y=pdf.get_y(), w=50)
            else:
                pdf.set_xy(x_start, y_start)
                pdf.multi_cell(60, 10, "Photo not available", align='C')


            horoscope_path = customer_data[54]
            if horoscope_path:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
                    temp_file.write(horoscope_path)
                    temp_file_path = temp_file.name


                pdf.image(temp_file_path, x=90, y=pdf.get_y()+5, w=70)
            else:
                pdf.set_xy(x_start, y_start)
                pdf.multi_cell(60, 10, "Photo not available", align='C')
            
            # Output PDF
            output_path = "profile_report.pdf"
            pdf.output(output_path)

            return output_path

        # Streamlit interface for searching by ID or Name
        st.title("Member Search")

        search_opt = st.radio('Search', ('Member ID', 'Name'))

        if search_opt == 'Member ID':
            search_que = st.text_input("Enter Member ID")
            
        elif search_opt == 'Name':
            search_que = st.text_input("Enter Name")

        if search_que:
            customer_data = get_customer_data(search_opt, search_que)

            if customer_data:
                st.write("Customer found. Generating PDF...")

                # Create PDF and provide download link
                pdf_path = create_pdf(customer_data)
                with open(pdf_path, "rb") as f:
                    st.download_button("Download PDF", f, file_name=f"OPJM_profile_{search_que}.pdf")
            else:
                st.error("No customer found with the given details.")
    
    
with tabs[3]:

    col1,col2 = st.columns(2)

    with col1:

        def delete_member_by_id(member_id):
            try:
                with sqlite3.connect('customer.db') as conn:
                    cursor = conn.cursor()
                    # Check if the member exists
                    cursor.execute("SELECT * FROM members WHERE Member_Id = ?", (member_id,))
                    if cursor.fetchone() is None:
                        return "Member ID not found"
                    
                    # Delete the member
                    cursor.execute("DELETE FROM members WHERE Member_Id = ?", (member_id,))
                    conn.commit()
                    return True
            except Exception as e:
                return str(e)

        def delete_member_by_name(name):
            try:
                with sqlite3.connect('customer.db') as conn:
                    cursor = conn.cursor()
                    # Check if the member exists
                    cursor.execute("SELECT * FROM members WHERE Name LIKE ?", ('%' + name + '%',))
                    if cursor.fetchone() is None:
                        return "Member Name not found"
                    
                    # Delete the member
                    cursor.execute("DELETE FROM members WHERE Name LIKE ?", ('%' + name + '%',))
                    conn.commit()
                    return True
            except Exception as e:
                return str(e)

        # Streamlit interface
        Choose_option = st.radio('Choose Option for Deletion', ('Member ID', 'Name'))

        if Choose_option == 'Member ID':
            id = st.text_input("Enter the Member ID")
            
            if id:
                if st.button("Delete by ID"):
                    result = delete_member_by_id(id)
                    if result is True:
                        st.success("Selected Profile Deleted Successfully!")
                    elif result == "Member ID not found":
                        st.warning("Member ID not found in the database.")
                    else:
                        st.error(f"An error occurred: {result}")
            else:
                st.info("Please enter a valid Member ID.")

        elif Choose_option == 'Name':
            name = st.text_input("Enter the Name")
            
            if name:
                if st.button("Delete by Name"):
                    result = delete_member_by_name(name)
                    if result is True:
                        st.success("Selected Profile Deleted Successfully!")
                    elif result == "Name not found":
                        st.warning(f"No member found with name '{name}'.")
                    else:
                        st.error(f"An error occurred: {result}")
            else:
                st.info("Please enter a valid Member Name.")
    
    with col2:

        # Function to fetch existing data by Member ID
        def fetch_member_data(member_id):
            conn = sqlite3.connect("customer.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM members WHERE Member_Id = ?", (member_id,))
            result = cursor.fetchone()
            conn.close()
            return result

        # Function to update member data
        def update_member_data(member_id, updated_data):
            try:
                conn = sqlite3.connect("customer.db")
                cursor = conn.cursor()
                cursor.execute(
                    """UPDATE members SET 
                        Name = ?, Gender = ?, Age = ?, Birth_City = ?, Marital_Status = ?, 
                        Mother_Tongue = ?, Religion = ?, Class = ?, Caste = ?, Sub_Caste = ?, 
                        Rasi = ?, Star = ?, DOB = ?, Height = ?, Weight = ?, 
                        Physical_Status = ?, Complexion = ?, Blood_Group = ?, Others = ?, 
                        Smoking = ?, Drinking = ?, Diet = ?, Education = ?, Course = ?, 
                        Occupation = ?, Annual_Income = ?, Family_Status = ?, Family_Value = ?, 
                        Brothers = ?, Married_Brothers = ?, Sisters = ?, Married_Sisters = ?, 
                        Age_From = ?, Partner_Height = ?, Partner_Religion = ?, Partner_Class = ?, 
                        Partner_Caste = ?, Partner_SubCaste = ?, Partner_Physical = ?, Partner_Marital = ?, 
                        Partner_Education = ?, Partner_Occupation = ?, Partner_Smoking = ?, Partner_Drinking = ?, 
                        Partner_Diet = ?, Notes = ?, Mobile_No = ?, Alternative_Mobile_No = ?, 
                        Contact_Person = ?, Contact_Email = ?, Registration_Date = ? 
                    WHERE Member_Id = ?""",
                    (*updated_data, member_id),
                )
                conn.commit()
                conn.close()
                return True
            except Exception as e:
                return str(e)

        # Streamlit Interface
        st.title("Update Member Profile")

        member_id = st.text_input("Enter Member ID to Update:")
        if member_id:
            member_data = fetch_member_data(member_id)
            if member_data:
                st.success("Member found. You can edit the details below:")
                
                # Personal Details
                name = st.text_input("Name:", value=member_data[1], key="name")
                gender = st.selectbox("Gender", ["", "Male", "Female"], index=["", "Male", "Female"].index(member_data[2]), key="gender")
                age = st.number_input("Age", min_value=18, max_value=100, value=member_data[3], key="age")
                place_of_birth = st.text_input("Place of Birth", value=member_data[4], key="place_of_birth")
                marital_status = st.selectbox("Marital Status", ["Never Married", "Married", "Divorced"], index=["Never Married", "Married", "Divorced"].index(member_data[5]), key="marital_status")
                mother_tongue = st.text_input("Mother Tongue", value=member_data[6], key="mother_tongue")
                religion = st.selectbox("Choose your Religion", ["Hindu", "Christian", "Musilm", "Converted Christian", "Converted Muslim", "Others"], index=["Hindu", "Christian", "Musilm", "Converted Christian", "Converted Muslim", "Others"].index(member_data[7]), key="religion")
                Class = st.selectbox("Choose your class", ["OC", "BC", "MBC", "SC", "SCA"], index=["OC", "BC", "MBC", "SC", "SCA"].index(member_data[8]), key="class")
                caste = st.text_input("Caste", value=member_data[9], key="caste")
                sub_caste = st.text_input("Sub Caste", value=member_data[10], key="sub_caste")
                rasi = st.selectbox("Rasi", ['', 'Mesham', 'Rishabham', 'Mithunam', 'Kadkam', 'Simam', 'Kani', 'Tulam', 'Vrishchikagam', 'Dhanushu', 'Makaram', 'Kumbham', 'Meenam'], index=['', 'Mesham', 'Rishabham', 'Mithunam', 'Kadkam', 'Simam', 'Kani', 'Tulam', 'Vrishchikagam', 'Dhanushu', 'Makaram', 'Kumbham', 'Meenam'].index(member_data[11]), key="rasi")
                star = st.selectbox("Star", ['', 'Ashwini', 'Bharani', 'Karthikai', 'Rohini', 'Mirukasiridam', 'Thiruvadirai', 'Punaraphusam', 'Phusam', 'Ailyam', 'Magam', 'Pooram', 'Uthiram', 'Astam', 'Sidhirai', 'Swathi', 'Visagam', 'Anusham', 'Gatei', 'Mulam', 'Puradam', 'Uthradam', 'Tiruvonam', 'Avitam', 'Sadayam', 'Puratathi', 'Uthratathi', 'Revathi'], index=['', 'Ashwini', 'Bharani', 'Karthikai', 'Rohini', 'Mirukasiridam', 'Thiruvadirai', 'Punaraphusam', 'Phusam', 'Ailyam', 'Magam', 'Pooram', 'Uthiram', 'Astam', 'Sidhirai', 'Swathi', 'Visagam', 'Anusham', 'Gatei', 'Mulam', 'Puradam', 'Uthradam', 'Tiruvonam', 'Avitam', 'Sadayam', 'Puratathi', 'Uthratathi', 'Revathi'].index(member_data[12]), key="star")
                dob = st.date_input("Date of Birth", value=member_data[13], key="dob")
                height = st.text_input("Height", value=member_data[14], key="height")
                weight = st.number_input("Weight (kg)", min_value=35, max_value=150, value=int(member_data[15]), key="weight")
                physical_status = st.selectbox("Physical Status", ["Normal", "Special"], index=["Normal", "Special"].index(member_data[16]), key="physical_status")
                complexion = st.selectbox("Complexion", ['', 'Fair', 'Light', 'Medium', 'Tan', 'Dark'], index=['', 'Fair', 'Light', 'Medium', 'Tan', 'Dark'].index(member_data[17]), key="complexion")
                blood_group = st.selectbox("Blood Group", ['', 'B+', 'O+', 'A+', 'AB+', 'B-', 'A-', 'O-', 'AB-'], index=['', 'B+', 'O+', 'A+', 'AB+', 'B-', 'A-', 'O-', 'AB-'].index(member_data[18]), key="blood_group")
                other = st.text_input("If Specify", value=member_data[19], key="other")
                smoking = st.text_input("Smoking", value=member_data[20], key="smoking")
                drinking = st.text_input("Drinking", value=member_data[21], key="drinking")
                diet = st.text_input("Diet", value=member_data[22], key="diet")


                # Education Details
                education = st.text_input("Education", value=member_data[23])
                course = st.text_input("Course", value=member_data[24])
                occupation = st.text_input("Occupation", value=member_data[25])
                annual_income = st.text_input("Annual Income", value=member_data[26])

                # Family Details
                family_status = st.text_input("Family Status", value=member_data[27])
                family_value = st.text_input("Family Value", value=member_data[28])
                residing_city = st.text_input("Residing City", value=member_data[29])
                no_of_brothers = st.number_input("No. of Brothers", min_value=0, value=int(member_data[30]) if member_data[30] else 0, key="no_of_brothers")
                married_brothers = st.number_input("Married Brothers", min_value=0, value=int(member_data[31]) if member_data[31] else 0, key="married_brothers")
                no_of_sisters = st.number_input("No. of Sisters", min_value=0, value=int(member_data[32]) if member_data[32] else 0, key="no_of_sisters")
                married_sisters = st.number_input("Married Sisters", min_value=0, value=int(member_data[33]) if member_data[33] else 0, key="married_sisters")
                

                # Partner Preference
                age_from = st.number_input("Age From", min_value=18, max_value=100, value=int(member_data[34]) if member_data[34] else 18, key="age_from")
                partner_height = st.text_input("Height Preference", value=member_data[35])
                partner_religion = st.text_input("Religion Preference", value=member_data[36])
                partner_class = st.text_input("Class Preference", value=member_data[37])
                partner_caste = st.text_input("Caste Preference", value=member_data[38])
                partner_subcaste = st.text_input("Sub Caste Preference", value=member_data[39])
                partner_physical = st.text_input("Physical Status Preference", value=member_data[40])
                partner_marital = st.text_input("Marital Status Preference", value=member_data[41])
                partner_education = st.text_input("Education Preference", value=member_data[42])
                partner_occupation = st.text_input("Occupation Preference", value=member_data[43])
                partner_smoking = st.text_input("Smoking Preference", value=member_data[44])
                partner_drinking = st.text_input("Drinking Preference", value=member_data[45])
                partner_diet = st.text_input("Diet Preference", value=member_data[46])
                notes = st.text_area("Notes", value=member_data[47])

                # Contact Details
                mobile_no = st.text_input("Mobile No", value=member_data[48])
                alternative_mobile_no = st.text_input("Alternative Mobile No", value=member_data[49])
                contact_person = st.text_input("Contact Person", value=member_data[50])
                contact_email = st.text_input("Contact Email", value=member_data[51])
                reg_date = st.date_input(
                                            "Registration Date", 
                                            value=datetime.strptime(member_data[52], "%Y-%m-%d").date() if member_data[51] else date.today(),
                                            key="reg_date"
                                        )

                # Update Button
                if st.button("Update Profile"):
                    updated_data = (
                        name, gender, age, place_of_birth, marital_status, mother_tongue, religion, Class, caste, sub_caste,rasi,
                        star, str(dob), height, weight, physical_status, complexion, blood_group, other, smoking, 
                        drinking, diet, education, course, occupation, annual_income, family_status, family_value,residing_city, no_of_brothers, married_brothers, 
                        no_of_sisters, married_sisters, age_from, partner_height, partner_religion, partner_class, 
                        partner_caste, partner_subcaste, partner_physical, partner_marital, partner_education, partner_occupation, 
                        partner_smoking, partner_drinking, partner_diet, notes, mobile_no, alternative_mobile_no, contact_person, 
                        contact_email, reg_date
                    )
                    result = update_member_data(member_id, updated_data)
                    if result is True:
                        st.success("Member profile updated successfully!")
                    else:
                        st.error(f"An error occurred: {result}")
            else:
                st.warning("Member not found. Please check the Member ID.")









