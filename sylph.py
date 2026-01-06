import json
from Task.actions import *
from Task.action_map import action_map
with open('rules.json', 'r') as f:
    sylph_data = json.load(f)
#print(sylph_data)
flag=True
while(flag):
    user_input=input("Enter your query:").strip().lower()
    if user_input=="exit":
        print("Sylph signing off. Goodbye! have a great day ahead!")
        flag=False
    elif user_input in sylph_data:
        if sylph_data[user_input]["type"]=="static":
             print(sylph_data[user_input]["response"])
        else:
            action_name=sylph_data[user_input]["action"]
            if action_name in action_map:
                action_map[action_name]()
            else:
                print("Action not found.")
    else:
        print("I don't understand that query."
              " Please try again or type 'exit' to exit."
              )
        
    