# This program reverses text
def reverse_text(text):
    if text.isalpha():
        return text[::-1]
    else:
        return "Error Reported! Enter text only."


while True:
    original_text = input("Enter a string: ")
    reversed_text = reverse_text(original_text)

    if reversed_text != "Error Reported! Enter text only.":
        print("The reversed text is", reversed_text)
        break
    else:
        print("Error Reported! Enter text only.")
