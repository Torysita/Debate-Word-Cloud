#Word Cloud of the first 2020 Presidential Debate
#by Tory White

import collections
from collections import Counter
import numpy as np
from wordcloud import WordCloud 
from PIL import Image
import matplotlib.pyplot as plt


#/////////////////////////////////
def find_speaker(name):
    speaker_list = []
    for x in transcript:
        namelen = len(name)
        if x[0:namelen+1] == (' ' + name) or x[0:namelen] == name:    
            speaker_list.append(x)
           
    speaker_list = ' '.join(speaker_list).split() 
    #print(speaker_list)
        
    stripped_speech = []
    for i in speaker_list:
        if i not in stopwords:
            stripped_speech.append(i)
    
    speaker_count = {}
    for word in stripped_speech:
        if word in speaker_count.keys():
            speaker_count[word] = speaker_count[word] + 1
        else:
            speaker_count[word] = 1

    d = collections.Counter(speaker_count)
    tot = len(speaker_list)
    
    top_30 = d.most_common(30)
    
    print(name + " spoke a total number of " + str(tot) + " words.")
    for word, count in d.most_common(30):
        print(word, ": ", count)
    
    #PLOT BAR CHART
        plt.bar(word, count)
        plt.title('Word Count')
        plt.xlabel('Word')
        plt.ylabel('Count')
        plt.show()

    
    #WORD CLOUD

    picture = name + ".jpg"

    char_mask = np.array(Image.open(picture))   
    
    # Create a word cloud image
    wc = WordCloud(background_color="white", max_words=1000, mask=char_mask, stopwords=stopwords, contour_width=3, contour_color='lightgrey')

    # Generate a wordcloud
    text = ' '.join(stripped_speech)
    wc.generate(text)
    print(wc)

    # show
    plt.figure(figsize=[30,20])
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

#///////////////////////////////////////


# program starts
doc = open('FirstDebateTranscript.txt', 'r')
transcript = doc.read()
doc.close()

s = open('stopwords.txt', 'r')
stopwords = s.read()
s.close()

transcript = transcript.lower()
transcript = transcript.replace('"', ' ')
transcript = transcript.replace(",", " ")
transcript = transcript.replace('?', " ")
transcript = transcript.replace('!', " ")
transcript = transcript.replace(".", "")
transcript = transcript.replace("-", "")
transcript = transcript.replace("'\'", "")
transcript = transcript.replace("\\", "")
transcript = transcript.split("    ")

# end program here
#//////////////////////////////////////

find_speaker("chris wallace")




