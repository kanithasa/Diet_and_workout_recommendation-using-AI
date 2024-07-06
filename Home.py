
import streamlit as st

st.set_page_config(page_title='NutriFitBuddy', page_icon='images\logo.png')

# A workaround using st.markdown() to apply some style sheets to the page
st.markdown(
    f"""
        <style>
            /* Add a background to the page, but I don't use it here */
            # .stApp {{
            #     background: url("https://thumbs.dreamstime.com/b/healthy-clean-eating-layout-vegetarian-food-diet-nutrition-concept-various-fresh-vegetables-ingredients-salad-white-105567339.jpg");
            #     background-repeat: no-repeat;
            #     background-size: cover;
            # }}

            /* Make the default header of streamlit invisible */
            .css-18ni7ap.e8zbici2 {{
                opacity: 0
            }}

            /* Make the default footer of streamlit invisible */
            .css-h5rgaw.egzxvld1 {{
            opacity: 0
            }}

            /* Change width and padding of the page */
            .block-container.css-91z34k.egzxvld4 {{
            width: 100%;
            padding: 0.5rem 1rem 10rem;
            max-width: none;
            }}

            /* Change padding of the pages list in the sidebar */
            .css-uc76bn.e1fqkh3o9 {{
            padding-top: 2rem;
            padding-bottom: 0.25rem;
            }}
        </style>
        """, unsafe_allow_html=True
    )
# A workaround using st.columns() to move logo and title to the center of the page
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([0.5, 0.5, 1, 0.75, 1, 0.75, 0.5, 0.5])
with col4:
    st.image(image='images\logo.png', width=140)
with col5:
    st.markdown("""<br/><h1 style="display: inline;">NutriFitBuddy</h1>
                    <i style="font-size: 22px;">Fitness Guide</i>
                """, unsafe_allow_html=True)
    
st.write("""
NutriFitBuddy is an all-in-one fitness application designed to assist users in managing their diet and workout routines. 
The app utilizes Fuzzy Logic to provide personalized plans based on user inputs and requirements.
""")

st.write("""
### Why Use NutriFitBuddy?
NutriFitBuddy offers personalized and adaptable fitness plans tailored to your specific needs. 
From customized diet recommendations to dynamic workout routines, achieve your fitness goals efficiently and effectively.
""")
st.image(image=r'images\nutri.png', use_column_width=True)

# Explanation of available functionalities
st.write("""
### Functionalities:

#### Customized Plans
NutriFitBuddy specializes in crafting personalized diet plans and workout routines tailored explicitly to individual user inputs. Leveraging innovative algorithms, the application analyzes user-provided data such as gender, height, weight, and fitness stage to generate plans designed to meet specific health and fitness goals. These plans consider various factors, including nutritional requirements and exercise intensity, ensuring a customized approach to achieving optimal results.

#### Dynamic Modifications
The application empowers users with the flexibility to make real-time adjustments to their plans effortlessly. By simply modifying inputs like weight and fitness stage without the need for manual submission, NutriFitBuddy automatically recalibrates the generated plans. This dynamic capability ensures that users receive updated and relevant guidance in response to their evolving fitness journey, allowing for seamless progress tracking and adaptability.

#### Comprehensive Information
NutriFitBuddy doesn't just offer plans; it provides comprehensive information and insights into various dishes and exercises. Users gain access to a wealth of detailed nutritional data, including macronutrient breakdowns, ingredient lists, cooking instructions, and exercise descriptions. This depth of information empowers informed decision-making, enabling users to select dishes and exercises aligned with their dietary preferences and fitness objectives.

#### Seamless Navigation
The application's intuitive interface facilitates effortless navigation across its diverse range of pages. Users can seamlessly explore and search for dishes or exercises through dedicated functional pages. This streamlined experience ensures ease of use, allowing individuals to find and access relevant information swiftly, promoting an engaging and efficient user experience.
""")