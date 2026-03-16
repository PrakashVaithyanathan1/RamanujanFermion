import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# ---------------------------------------------------------
# 1. CORE PHYSICS ENGINE
# ---------------------------------------------------------
def get_mock_theta_an(n):
    if n <= 0: return 1
    n_prime = n - (1/24)
    exponent = np.pi * np.sqrt(n_prime / 6)
    prefactor = 1 / (2 * np.sqrt(n_prime))
    return prefactor * np.exp(exponent)

N_range = np.arange(2, 102, 2)
an_values = [get_mock_theta_an(n) for n in N_range]
mock_energy = [-np.log(an) / n for an, n in zip(an_values, N_range)]
bethe_ansatz_limit = -4 / np.pi 

# ---------------------------------------------------------
# 2. DATA EXPORT (CSV)
# ---------------------------------------------------------
csv_filename = "Ramanujan_Fermion_Data.csv"
df = pd.DataFrame({'System_Size_N': N_range, 'Mock_Theta_Coeff_an': an_values, 'Derived_Energy_E0': mock_energy})
with open(csv_filename, 'w') as f:
    f.write("############################################################\n")
    f.write("# CONCEPTUALIZATION: PRAKASH VAITHYANATHAN, INDIA          #\n")
    f.write("############################################################\n")
    df.to_csv(f, index=False)

# ---------------------------------------------------------
# 3. VISUALIZATION & PDF EXPORT
# ---------------------------------------------------------
pdf_filename = "Ramanujan_Fermion_Report.pdf"
with PdfPages(pdf_filename) as pdf:
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax1 = plt.subplots(figsize=(11, 8.5))

    # Axis 1: Mock Theta (Blue)
    color_an = '#1f77b4'
    ax1.set_xlabel('System Size (N Electrons)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Mock Theta Coefficient a(n)', color=color_an, fontsize=14, fontweight='bold')
    ax1.plot(N_range, an_values, color=color_an, marker='o', lw=2, label='Mock Theta a(n)')
    ax1.set_yscale('log')
    ax1.tick_params(axis='y', labelcolor=color_an)

    # Axis 2: Energy (Red)
    ax2 = ax1.twinx()
    color_e = '#d62728'
    ax2.set_ylabel('Normalized Energy E_0', color=color_e, fontsize=14, fontweight='bold')
    ax2.plot(N_range, mock_energy, color=color_e, marker='s', ls='--', lw=2, label='Mock Energy E_0')
    ax2.axhline(y=bethe_ansatz_limit, color='green', ls=':', lw=3, label=f'Bethe Ansatz ({bethe_ansatz_limit:.4f})')
    ax2.tick_params(axis='y', labelcolor=color_e)

    # UPDATED POSITION: TOP LEFT BRANDING BOX (Empty Space)
    ax1.text(0.02, 0.98, 'Conceptualization: Prakash Vaithyanathan, India', 
             transform=ax1.transAxes, fontsize=13, fontweight='bold', color='black',
             bbox=dict(facecolor='white', alpha=0.9, edgecolor='black', boxstyle='round,pad=0.5'),
             ha='left', va='top')

    plt.title('Validation: Mock Modular Physics vs. Bethe Ansatz', fontsize=16, fontweight='bold', pad=25)
    
    # Legend (Moved to bottom-right to balance the layout)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower right', frameon=True, shadow=True)

    plt.tight_layout()
    pdf.savefig(fig) 
    plt.savefig("mock_modular_validation_final.png", dpi=600)
    plt.show()

print(f"Professional Report generated: {pdf_filename} and {csv_filename}")
