from openai import OpenAI
import json

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="sdhghdQQXfsaLKQaa6T3BlbkFJ-hAVLORsJDMAaoHCW5CmqvEUE2ouO_7wpCqxLhsS4aOhnKHf6mFemxnjlC5WeT1ai7D5INzHQA")
def call_llm(prompt):
    # send request ,Wait for response ,return text   
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
#building a function to process the text
def process_text(text):
    prompt = f"""
    Summarize the following text and return only valid json 
    Required format :
    {{
        "summary": "...',
        "risks": "...',
        "Recommendations": "...'
    }}

    {text}
    """
    response =  call_llm(prompt)
    return response

def safe_parse(json_text):
    try:
        return json.loads(json_text)
    except json.JSONDecodeError:
        return None

# Read the content of the file
with open("input.txt", "r") as file:
    content = file.read()

# Process the text and get the result
result = process_text(content)

data = safe_parse(result)

#Print the result
if data is None:
    print("Invalid JSON response. Raw output:")

else:
    print(result)
