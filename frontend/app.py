import streamlit as st
import requests

API_URL = "http://backend:8000"

st.title("TinyCRM: Contact Manager")

# Contact Form
st.header("Add Contact")
name = st.text_input("Name")
email = st.text_input("Email")
if st.button("Save Contact"):
    response = requests.post(f"{API_URL}/contacts/", params={"name": name, "email": email})
    st.write(response.json())

# Display Contacts
st.header("Saved Contacts")
contacts = requests.get(f"{API_URL}/contacts/").json()["contacts"]
for contact in contacts:
    st.write(f"**{contact['name']}** - {contact['email']}")
