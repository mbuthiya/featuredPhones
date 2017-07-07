my_buttons = {"1":["a","d","g","j","m","p","t","w",' '],
"2":['b','e','h','k','n','q','u','x'],
"3":['c','f','i','l','o','r','v','y'],
"4":['s','z']}

def get_input():
    print("Enter your sentence")
    user_input = input().lower()
    return user_input



def count_clicks(user_inputs):
    clicks = 0
    for character in user_inputs:
        for key in my_buttons.keys():
            if character in my_buttons[key]:
                clicks = clicks + int(key)

    return clicks

input_sentence = get_input()
num_of_clicks = str(count_clicks(input_sentence))
print(f"You need {num_of_clicks} number of clicks")
