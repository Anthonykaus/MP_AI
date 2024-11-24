import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class TransformerCodeGenerator:
    def __init__(self):
        self.model_name_or_path = 'gpt2'
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name_or_path)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name_or_path)

    def generate(self, prompt, max_length=150):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=max_length, num_return_sequences=1)
        generated_code = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_code

# Example usage
if __name__ == "__main__":
    code_gen = TransformerCodeGenerator()
    generated_code = code_gen.generate("Create a CNN for image classification")
    print(generated_code)
