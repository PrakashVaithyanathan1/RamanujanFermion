import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Data Generation
# ---------------------------------------------------------
N = np.arange(2, 62, 2) 
qmc_complexity = 2**N  
mock_modular_complexity = N**4

df = pd.DataFrame({
    'System_Size_N': N,
    'QMC_Cost_Exponential': qmc_complexity,
    'Mock_Modular_Cost_Polynomial': mock_modular_complexity
})

# ---------------------------------------------------------
# 2. Export CSV with BOLD Metadata Header
# ---------------------------------------------------------
csv_filename = "benchmarking_data.csv"
with open(csv_filename, 'w') as f:
    f.write("############################################################\n")
    f.write("# CONCEPTUALIZATION: PRAKASH VAITHYANATHAN, INDIA          #\n")
    f.write("############################################################\n")
    df.to_csv(f, index=False)

print(f"Successfully saved {csv_filename} with bold attribution header.")

# ---------------------------------------------------------
# 3. Scientific Visualization (ULTRA-HIGH VISIBILITY)
# ---------------------------------------------------------
# Using a cleaner style for better LaTeX contrast
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))

# INCREASED Line Width (lw) and Marker Size
ax.plot(N, qmc_complexity, color='#d62728', ls='--', lw=3.0, marker='o', markersize=8, label='Standard QMC (NP-Hard)')
ax.plot(N, mock_modular_complexity, color='#1f77b4', lw=4.0, marker='s', markersize=8, label='Mock Modular (Polynomial)')

# Log scale for the Y axis
ax.set_yscale('log')

# THICKER Axes Labels
ax.set_xlabel('System Size (N Electrons)', fontsize=15, fontweight='bold', color='black')
ax.set_ylabel('Computational Cost (Log Scale)', fontsize=15, fontweight='bold', color='black')

# REMOVED Internal Title to avoid double-captioning in LaTeX

# MAKING TICK NUMBERS BOLD AND VISIBLE
ax.tick_params(axis='both', which='major', labelsize=13, width=2, length=6, labelcolor='black')
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontweight('bold')

# BOLDER ATTRIBUTION BOX (Bottom Right)
ax.text(0.95, 0.05, 'Conceptualization: Prakash Vaithyanathan, India', 
        transform=ax.transAxes, fontsize=14, color='black', fontweight='bold',
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='white', alpha=1.0, edgecolor='black', linewidth=2.0))

# THICKER Legend and Grid
ax.legend(loc='upper left', frameon=True, fontsize=13, edgecolor='black', shadow=True)
ax.grid(True, which="both", ls="-", alpha=0.6, color='#bdbdbd') # Darker grid

# THICKER Border around the entire plot
for spine in ax.spines.values():
    spine.set_linewidth(2)
    spine.set_color('black')

plt.tight_layout()

# SAVING WITH HIGH DPI (600) for crisp printing
plt.savefig("figure2_high_visibility.png", dpi=600, bbox_inches='tight')
print("Successfully saved ultra-sharp figure2_high_visibility.png.")
plt.show()
