# cleaned the text by converting it to lowercase and removing special characters to reduce noise.
import re   #regular expression 

#Yeh Python ki ek inbuilt library  "Search & Replace" tool hai. Iski madad se hum text ke andar patterns (jaise numbers, symbols, ya special characters) ko dhoond kar hata sakte hain.

def clean_text(text):   

    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)   #symbol and number khtm krr dena aur spaces rhne do
    return text
