import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def main():
    print("PyTorch version:", torch.__version__)
    print("Transformers library loaded successfully.")
    
    try:
        print("Starting to load tokenizer...")
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        print("Tokenizer loaded successfully.")
    except Exception as e:
        print(f"Error loading tokenizer: {e}")
        return

    try:
        print("Starting to load model...")
        model = GPT2LMHeadModel.from_pretrained('gpt2')
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    print("All components loaded successfully!")

if __name__ == "__main__":
    main()