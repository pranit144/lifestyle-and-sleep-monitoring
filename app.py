import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = st.file_uploader("Upload your dataset", type=["csv"])
if file_path is not None:
    df = pd.read_csv(file_path)

    # Streamlit app setup
    st.title("Appliance Data Visualization and Bill Estimator")
    st.write("Explore appliance data with histograms, comparisons for z1, z2, and z3, and bill estimation.")

    # Display dataset preview
    st.write("### Dataset Preview")
    st.dataframe(df)

    # Handle Date column (if exists)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date is in datetime format

    # Define appliance columns for zones
    z1_columns = ['z1_Light(kW)', 'z1_Plug(kW)']
    z2_columns = ['z2_Light(kW)', 'z2_Plug(kW)', 'z2_AC1(kW)', 'z2_AC2(kW)', 'z2_AC3(kW)', 'z2_AC4(kW)']
    z3_columns = ['z3_Light(kW)', 'z3_Plug(kW)', 'z4_Light(kW)']

    # Visualizations for Zone 1 (z1)
    st.write("### Zone 1 (z1) Visualizations")
    for col in z1_columns:
        if col in df.columns:
            st.write(f"#### Histogram for {col}")
            plt.figure(figsize=(8, 6))
            plt.hist(df[col].dropna(), bins=20, color='blue', edgecolor='black')
            plt.title(f"Distribution of {col}")
            plt.xlabel("Power Consumption (kW)")
            plt.ylabel("Frequency")
            st.pyplot(plt)

    # Visualizations for Zone 2 (z2)
    st.write("### Zone 2 (z2) Visualizations")
    for col in z2_columns:
        if col in df.columns:
            st.write(f"#### Histogram for {col}")
            plt.figure(figsize=(8, 6))
            plt.hist(df[col].dropna(), bins=20, color='orange', edgecolor='black')
            plt.title(f"Distribution of {col}")
            plt.xlabel("Power Consumption (kW)")
            plt.ylabel("Frequency")
            st.pyplot(plt)

    # Visualizations for Zone 3 (z3)
    st.write("### Zone 3 (z3) Visualizations")
    for col in z3_columns:
        if col in df.columns:
            st.write(f"#### Histogram for {col}")
            plt.figure(figsize=(8, 6))
            plt.hist(df[col].dropna(), bins=20, color='green', edgecolor='black')
            plt.title(f"Distribution of {col}")
            plt.xlabel("Power Consumption (kW)")
            plt.ylabel("Frequency")
            st.pyplot(plt)

    # Pairwise Comparisons Between Zones
    st.write("### Pairwise Comparisons Between Zones")
    st.write("#### Select Columns for Comparison")
    col1, col2 = st.columns(2)
    with col1:
        zone1_column = st.selectbox("Select z1 column", z1_columns, key="z1_col")
        zone2_column = st.selectbox("Select z2 column", z2_columns, key="z2_col")
    with col2:
        zone3_column = st.selectbox("Select z3 column", z3_columns, key="z3_col")

    # Plot comparisons
    if zone1_column and zone2_column:
        st.write(f"#### Scatter Plot: {zone1_column} vs {zone2_column}")
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[zone1_column], y=df[zone2_column], color='purple')
        plt.title(f"{zone1_column} vs {zone2_column}")
        plt.xlabel(zone1_column)
        plt.ylabel(zone2_column)
        st.pyplot(plt)

    if zone2_column and zone3_column:
        st.write(f"#### Scatter Plot: {zone2_column} vs {zone3_column}")
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[zone2_column], y=df[zone3_column], color='brown')
        plt.title(f"{zone2_column} vs {zone3_column}")
        plt.xlabel(zone2_column)
        plt.ylabel(zone3_column)
        st.pyplot(plt)

    if zone1_column and zone3_column:
        st.write(f"#### Scatter Plot: {zone1_column} vs {zone3_column}")
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[zone1_column], y=df[zone3_column], color='red')
        plt.title(f"{zone1_column} vs {zone3_column}")
        plt.xlabel(zone1_column)
        plt.ylabel(zone3_column)
        st.pyplot(plt)

    # Bill Estimation Setup
    st.write("### Bill Estimation and Suggestions")
    # Step 1: Input for power consumption
    power_consumed = st.number_input("Enter power consumption (in kWh):", min_value=0.0, step=0.1)

    # Assume the rate is $0.12 per kWh (this can be modified)
    rate_per_kwh = 0.12

    # Calculate the bill based on the entered power consumption
    if power_consumed > 0:
        bill_amount = power_consumed * rate_per_kwh
        st.write(f"Your estimated bill for {power_consumed} kWh is: ${bill_amount:.2f}")
    else:
        st.write("Please enter a valid power consumption value.")

    # Step 2: Input for bill reduction
    desired_reduction = st.number_input("Enter desired reduction in your bill ($):", min_value=0.0, step=0.1)

    # Calculate the power consumption reduction required
    if desired_reduction > 0 and power_consumed > 0:
        required_reduction_kWh = desired_reduction / rate_per_kwh
        new_power_consumption = power_consumed - required_reduction_kWh
        if new_power_consumption < 0:
            st.write("Your desired bill reduction is greater than your current bill. Try reducing it less.")
        else:
            st.write(
                f"To reduce your bill by ${desired_reduction:.2f}, you need to reduce your power consumption by {required_reduction_kWh:.2f} kWh.")
            st.write(f"Your new target power consumption should be: {new_power_consumption:.2f} kWh.")
    else:
        if desired_reduction > 0:
            st.write("Please enter a valid initial power consumption to calculate the reduction.")
        else:
            st.write("Enter a desired bill reduction to get suggestions on power consumption savings.")
