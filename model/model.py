import torch
from transformers import GPT2LMHeadModel,  GPT2Tokenizer

class Model():
    def __init__(self):
        print('Loading the Model...')
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.model.load_state_dict(torch.load("model/model.pt",map_location=torch.device('cpu')))
        print('Loading the Tokenizer...')
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        print('Success')

    def generate(self, text):
        input_ids = self.tokenizer.encode(text + self.tokenizer.eos_token,return_tensors="pt")

        output = self.model.generate(
            input_ids, max_length=100,
            pad_token_id=self.tokenizer.eos_token_id,
            top_p=.92,
            top_k=50,
        )

        return self.tokenizer.decode(output[:, input_ids.shape[-1]:][0],skip_special_tokens=True)