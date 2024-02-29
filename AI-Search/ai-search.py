import argparse
import os
from dotenv import load_dotenv
import google.generativeai as palm
from textwrap import wrap

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in .env file")

palm.configure(api_key=API_KEY)

# print("Searching for models..")
#
# for model in palm.list_models():
#     print(model)

# models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
# model = models[0].name
model = "models/text-bison-001"
print(f"Model: {model} and Type: {type(model)}")

parser = argparse.ArgumentParser(description='Generate text based on a prompt.')
parser.add_argument('prompt', type=str, help='The prompt for text generation')
parser.add_argument('--temp', type=float, default=0, help='The temperature for text generation (default: 0.5)')
parser.add_argument('--max_output_tokens', type=int, default=250, help='The maximum number of output tokens (default: 800)')
parser.add_argument('--top_k', type=int, default=1, help='Top-k sampling parameter (default: 1)')
parser.add_argument('--top_p', type=float, default=0.1, help='Top-p sampling parameter (default: 0.1)')
parser.add_argument('--page', action='store_true', help='Paginate the output (default: False)')
args = parser.parse_args()

prompt = args.prompt
temperature = args.temp
max_output_tokens = args.max_output_tokens
top_k = args.top_k
top_p = args.top_p
paginate = args.page

print("Generating result ....")
completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=temperature,
    max_output_tokens=max_output_tokens,
    top_k=top_k,
    top_p=top_p,
)
generated_text = completion.result

if paginate:
    # Paginate the result
    words = generated_text.split()
    rows = wrap(' '.join(words), width=60)

    # Print each row
    for row in rows:
        print(row)
else:
    # Print the entire text at once
    print(generated_text)

