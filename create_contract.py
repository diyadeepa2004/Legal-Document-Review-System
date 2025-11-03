from fpdf import FPDF
import os

os.makedirs("data", exist_ok=True)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

content = """FRIENDSHIP & COLLABORATION AGREEMENT

This Agreement is made on 2 November 2025 between:

1. Deepa Nair, residing in Trivandrum ("Party A"), and
2. Diya Abhilash, residing in Kochi ("Party B").

WHEREAS both parties share a mutual love for creativity, coding, and coffee-fueled late-night projects, they hereby agree to collaborate on the Legal Document Review System ("The Project").

TERMS OF COLLABORATION:
1. Party A (Deepa) shall oversee UI design, testing, and emotional support.
2. Party B (Diya) shall manage backend logic, AI integration, and occasional sarcasm.
3. Both parties agree to celebrate small wins with filter coffee and playlist exchanges.

INTELLECTUAL PROPERTY:
All ideas, code, and chaotic brilliance produced during this project belong equally to both parties.

TERMINATION CLAUSE:
This agreement shall remain valid until one party gets bored or until the system starts summarizing emotions accurately-whichever comes first.

SIGNATURES:
Signed digitally in good humor and full caffeine concentration.

Deepa Nair ____________
Diya Abhilash ____________
"""

pdf.multi_cell(0, 10, content)
pdf.output("data/sample_contract.pdf")

print(" Deepa & Diya sample_contract.pdf created successfully!")
