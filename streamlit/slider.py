# import streamlit as st

# age = st.slider("How old are you?", 0, 130, 25)
# st.write("I'm ", age, "years old")

#--------Range of values---------
# import streamlit as st

# values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
# st.write("Values:", values)


#-----------Range time slider----------
import streamlit as st
from datetime import time

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)