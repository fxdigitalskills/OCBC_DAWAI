import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

# # Set page config and theme
st.set_page_config(
    page_title="Malaysian Price Analysis",
    page_icon="🛒",
    layout="wide"
)

# # Title and description
st.title("Malaysian Price Analysis Dashboard")
st.write("Analysis of essential goods prices from DOSM Price Catcher data")

lookup_2023_11 = Path('data/pricecatcher_lookup_item_2023-11.csv')
transac_rec_2023_11 = Path('data/pricecatcher_2023-11.csv')
transac_rec_2022_12 = Path('data/pricecatcher_2022-12.csv')

# Load data
@st.cache_data  # This caches the data to improve performance
def load_data():
    df_lookup = pd.read_csv(lookup_2023_11)
    df_transac_2022_12 = pd.read_csv(transac_rec_2022_12)
    df_transac_2023_11 = pd.read_csv(transac_rec_2023_11)
    df_2022 = pd.merge(df_transac_2022_12, df_lookup, on='item_code', how='left')
    df_2023 = pd.merge(df_transac_2023_11, df_lookup, on='item_code', how='left')
    return df_2022.assign(year=2022), df_2023.assign(year=2023)

try:
    df_2022, df_2023 = load_data()
    comparison_df = pd.concat([df_2022, df_2023])
    # print(comparison_df)

    # Create comparison dataframe
    # Assuming your CSVs have 'Item' and 'Price' columns
    comparison_data = comparison_df.groupby(['item_category', 'year'])['price'].mean().round(2).reset_index()
    comparison_data['year'] = comparison_data['year'].astype(str)

    # Create bar chart
    fig = px.bar(comparison_data, 
                    x='item_category',
                    y='price',
                    color='year',
                    title='Price Comparison 2022 vs 2023',
                    labels={'item_category': 'Category', 'price': 'Price(RM)', 'year': 'Year'},
                    barmode='group',)

    # Customize layout
    fig.update_layout(
        xaxis_title="Items",
        yaxis_title="Price (RM)",
        yaxis_tickformat='RM %.2f',
    )

    # Display the chart
    st.plotly_chart(fig, height=600)

except Exception as e:
    st.error(f"{e}: Please ensure your CSV files are in the correct format and location")
