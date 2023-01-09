import streamlit as st
from components.multipage import MultiPage
import components.about as about, components.cloud as cloud

app = MultiPage()

app.add_page("About",about.app)
app.add_page("Clouds",cloud.app)

app.run()
