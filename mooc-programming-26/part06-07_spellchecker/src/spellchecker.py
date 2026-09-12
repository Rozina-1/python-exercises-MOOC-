wordlist = []
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / "wordlist.txt"
with open(file_path) as new_file:
    for line in new_file:
        line = line.replace("\n","")
        wordlist.append(line)

sentence = input("Write text: ")
text = sentence.split(" ")
for word in text:
    if word.lower() not in wordlist:
        word = f"*{word}*"
    print(word,end = " ")