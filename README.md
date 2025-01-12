# Appliance Data Visualization and Bill Estimator

This project is a Streamlit-based web application designed for visualizing appliance power consumption data across three zones (z1, z2, z3) and estimating electricity bills. The application provides features like histograms, pairwise comparisons, and tools to estimate and reduce electricity bills.

## Features

### 1. Dataset Upload and Preview
- Users can upload a CSV file containing appliance data.
- The application displays a preview of the dataset.

### 2. Data Visualizations
- **Zone 1 (z1):** Visualize power consumption for `z1_Light(kW)` and `z1_Plug(kW)`.
- **Zone 2 (z2):** Visualize power consumption for `z2_Light(kW)`, `z2_Plug(kW)`, and multiple AC units.
- **Zone 3 (z3):** Visualize power consumption for `z3_Light(kW)`, `z3_Plug(kW)`, and `z4_Light(kW)`.
- Histograms for each column visualize the distribution of power consumption.

### 3. Pairwise Comparisons
- Users can select columns from different zones to create scatter plots for pairwise comparisons.
- Compare:
  - z1 vs z2
  - z2 vs z3
  - z1 vs z3

### 4. Bill Estimation
- Users can input their total power consumption (in kWh) to estimate their electricity bill.
- The bill is calculated using a default rate of **$0.12 per kWh** (modifiable in the code).

### 5. Suggestions for Bill Reduction
- Users can enter a desired reduction in their bill.
- The app calculates:
  - The power consumption reduction needed.
  - The target power consumption to achieve the reduction.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/appliance-data-visualization.git
   cd appliance-data-visualization
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the app in your browser.
2. Upload a CSV dataset containing appliance power consumption data. Example columns include:
   - `z1_Light(kW)`, `z1_Plug(kW)`
   - `z2_Light(kW)`, `z2_AC1(kW)`, etc.
   - `z3_Light(kW)`, `z4_Light(kW)`
3. Explore the visualizations and analyze the power consumption data.
4. Estimate electricity bills and get suggestions for reducing power consumption.

## Example Dataset Format

Your CSV file should include columns similar to:

| Date       | z1_Light(kW) | z1_Plug(kW) | z2_Light(kW) | z2_AC1(kW) | z3_Light(kW) | z4_Light(kW) |
|------------|--------------|-------------|--------------|------------|--------------|--------------|
| 2023-01-01 | 0.5          | 0.2         | 1.2          | 0.8        | 0.6          | 0.7          |
| 2023-01-02 | 0.6          | 0.3         | 1.1          | 0.7        | 0.5          | 0.6          |

## Dependencies

- Python 3.7+
- Streamlit
- pandas
- matplotlib
- seaborn

Install them using:
```bash
pip install streamlit pandas matplotlib seaborn
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
