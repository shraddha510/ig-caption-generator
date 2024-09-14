import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def main():
    print("PyTorch version:", torch.__version__)
    print("Transformers library loaded successfully.")
    
    print("Starting to load model...")
    model = GPT2LMHeadModel.from_pretrained('distilgpt2', verbose=True)
    print("Model loaded successfully.")
    
    print("Starting to load tokenizer...")
    tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2', verbose=True)
    print("Tokenizer loaded successfully.")

if __name__ == "__main__":
    main()