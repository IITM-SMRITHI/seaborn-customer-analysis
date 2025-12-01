import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from PIL import Image

# Set matplotlib to use Agg backend for compatibility
matplotlib.use('Agg')

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

# Create figure - 512/64 = 8 inches exactly
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)
fig.patch.set_facecolor('white')

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

# Set subplots_adjust to remove any margins
plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1)

# Save with specific settings to ensure exact size
fig.savefig('_temp_chart.png', dpi=64, format='png', pad_inches=0, bbox_inches='tight')
plt.close()

# Use PIL to ensure exactly 512x512
img = Image.open('_temp_chart.png')
if img.size != (512, 512):
    img_resized = img.resize((512, 512), Image.Resampling.LANCZOS)
    img_resized.save('chart.png', format='PNG')
else:
    img.save('chart.png', format='PNG')

print('Chart saved as chart.png with exact dimensions 512x512 pixels')
