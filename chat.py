import openai

openai.api_key = "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"

messages = []
while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    chat_response = completion.choices[0].message.content
    print(f"ChatGPT: {chat_response}")
    messages.append({"role": "assistant", "content": chat_response})
