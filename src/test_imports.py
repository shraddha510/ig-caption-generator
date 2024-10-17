print("Starting import tests...")

print("Importing numpy...")
import numpy as np
print(f"NumPy version: {np.__version__}")

print("\nImporting torch...")
import torch
print(f"PyTorch version: {torch.__version__}")

print("\nImporting transformers...")
from transformers import GPT2Tokenizer
print("Transformers imported successfully")

print("\nAll imports successful!")