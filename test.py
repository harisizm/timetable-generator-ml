import pandas as pd
import openpyxl
import streamlit as st
from PIL import Image

# dummy DataFrame
df = pd.DataFrame({'Time': ['9:00', '10:00'], 'Course': ['Math', 'Physics']})
print(df)