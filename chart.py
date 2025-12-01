import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic customer data
n_customers = 150
acquisition_cost = np.random.uniform(50, 500, n_customers)
lifetime_value = acquisition_cost * np.random.uniform(2, 8, n_customers) + np.random.normal(0, 200, n_customers)

# Create DataFrame
df = pd.DataFrame({
    'Acquisition Cost': acquisition_cost,
    'Lifetime Value': lifetime_value
})

# Create figure - exactly 512x512 pixels with 64 DPI = 8x8 inches
plt.figure(figsize=(8, 8), dpi=64)

# Create scatterplot using seaborn
sns.scatterplot(data=df, x='Acquisition Cost', y='Lifetime Value', 
                s=100, alpha=0.6, color='#2E86AB')

# Add labels and title
plt.xlabel('Customer Acquisition Cost ($)', fontsize=12, fontweight='bold')
plt.ylabel('Customer Lifetime Value ($)', fontsize=12, fontweight='bold')
plt.title('Customer Analysis: Acquisition Cost vs Lifetime Value', fontsize=14, fontweight='bold')

# Add grid
plt.grid(True, alpha=0.3, linestyle='--')

# Save figure
plt.savefig('chart.png', dpi=64, format='png')
plt.close()

print('Chart saved as chart.png')
