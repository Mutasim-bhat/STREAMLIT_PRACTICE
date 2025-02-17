import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import altair as alt

data= pd.DataFrame(
    np.random.randn(100, 3),
    columns=['A', 'B', 'C']
)
# line chart
st.line_chart(data)
# area chart
st.area_chart(data)
# bar chart
st.bar_chart(data)
# scatter plot
plt.scatter(data['A'], data['B'])
st.pyplot()
plt.title('Scatter plot')
plt.xlabel('A')
plt.ylabel('B')
# altair chart
chart = alt.Chart(data).mark_circle().encode(
    x='A',
    y='B',
    size='C',
    color='C',
    tooltip=['A', 'B', 'C']
).interactive()