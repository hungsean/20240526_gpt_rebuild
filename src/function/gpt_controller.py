from tiktoken import encoding_for_model
from openai import OpenAI
import json
from function import openai_api_key


client = OpenAI(
    api_key= openai_api_key
)

def token_len(text: str) -> int:
    encoder = encoding_for_model('gpt-3.5-turbo')
    result = encoder.encode(text)
    return len(result)


def translate_jp_tc(text: str, confirm: bool = True):
    if all(char.isspace() for char in text):
        print("input only space!")
        return None

    text = "translate japanese into 繁體中文 **only translate results** : \"" + text + "\"" 
    text_token_len = token_len(text)

    if confirm == True:
        print("sending this to gpt-3.5-turbo:")
        print("------")
        print(text)
        print("------")
        print("token_len: ", text_token_len)
        check_reply = input("sure to send?(y/n)")
        if check_reply == "n":
            return None
        elif check_reply == "y":
            gpt_reply = send_to_gpt3_5(text)
            return gpt_reply
        else:
            print("error input")
            return None
    else:
        gpt_reply = send_to_gpt3_5(text)
        return gpt_reply
    
def send_to_gpt3_5(content: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= [{
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": content
                }
            ]
            }],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content