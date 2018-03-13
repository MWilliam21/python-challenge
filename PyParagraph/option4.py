import os
import re
import string
import glob
def isdigit(mylist):
    return [x for x in mylist if not any(c.isdigit() for c in x)]
def split_sentences(st):
    st = st.strip() + '. '
    sentences = re.split(r'(?<![A-Z.])[.?!][.?!"\s]+', st)
    return sentences[:-1]
def mean(numbers):
   return float(sum(numbers)) / max(len(numbers), 1)

list_of_files= glob.glob('raw_data/*.txt')


## extracting file
for file_name in list_of_files:

## opening and reading the file
    with open(file_name,'r',newline="",encoding='utf-8') as textfile:
        textreader= textfile.read()
        ## adjusting the text so it would take out 
        new_txt= re.sub(r'(?<![A-Za-z])[\"\'\?]|(?= )',r'',textreader)
        word_count=new_txt.split()
        new_word_count=(isdigit(word_count))
        new_sentences_count=(split_sentences(textreader))
        length_of_sentences=list(map(len, new_sentences_count))
        length_of_words=list(map(len, new_word_count))
        
        
        print("Paragraph Analysis")
        print("------------------")
        print("Approximate Word Count: " + str(len(new_word_count)))
        print("Approximate Sentence Count: " + str(len(new_sentences_count)))
        print("Average Letter Count: " + str(mean(length_of_words)))
        print("Average Sentence Length: " + str(mean(length_of_sentences)))
    