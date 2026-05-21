"""Main runner: generates complete IEEE paper .docx with charts."""
import os
import sys

# Ensure charts exist
print("Step 1: Generating charts...")
from generate_charts import *
np.random.seed(42)
accuracy_epoch()
loss_epoch()
emotion_pie()
session_trend()
confusion_matrix()
architecture_diagram()
cnn_pipeline()
print("  Charts generated successfully.")

# Build Part 1 (Title through Proposed System)
print("Step 2: Building document sections 1-7...")
from paper_part1 import build_paper
doc = build_paper()

# Build Part 2 (Architecture through References)
print("Step 3: Building document sections 8-22...")
from paper_part2 import add_remaining_sections
add_remaining_sections(doc)

# Save final document
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Serien_IEEE_Research_Paper.docx')
doc.save(output_path)
print(f"\nDone! Research paper saved to:\n  {output_path}")
print(f"  File size: {os.path.getsize(output_path) / 1024:.1f} KB")
