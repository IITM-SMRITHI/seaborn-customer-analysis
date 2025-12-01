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

# Create figure with exactly 512x512 pixels (8x8 inches at 64 DPI)
fig = plt.figure(figsize=(8, 8), dpi=64)
ax = fig.add_subplot(111)

# Create scatterplot
sns.scatterplot(data=df, x='Acquisition Cost', y='Lifetime Value',
                s=100, alpha=0.6, color='#2E86AB', ax=ax)

# Add labels and title
ax.set_xlabel('Customer Acquisition Cost ($)', fontsize=12, fontweight='bold')
ax.set_ylabel('Customer Lifetime Value ($)', fontsize=12, fontweight='bold')
ax.set_title('Customer Analysis: Acquisition Cost vs Lifetime Value', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Save without extra padding
plt.savefig('chart.png', dpi=64, bbox_inches=None, pad_inches=0, format='png')
plt.close()

print('Chart saved as chart.png')
