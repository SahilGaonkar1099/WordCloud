#Generating Word cloud of words in a input file
import wordcloud# this is most required library for this project
from matplotlib import pyplot as plt#to get our final output on screen we make use of this


def File(): #This function returns file contents as a string of words in lower case.
    Need=input("Enter the file\n")#input the file name
    with open(Need,'r') as F:
        Read=F.read()
    return Read.lower()


def calculate_frequencies():
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    file = File()
    innitial_list_words = file.split()# to string is converted into list of words 
    final_list_words = []
    S1 = ""
    for words in innitial_list_words:
        help_list = []
        for letter in words.strip():
            if letter.isalpha() and letter not in punctuations:
                help_list.append(letter)
            else:
                continue
        S1 = "".join(help_list)

        final_list_words.append(str(S1))
    for i in final_list_words:
        if i.strip() in uninteresting_words:
            final_list_words.remove(i)
    result = {}
    text = " ".join(final_list_words)
    for L in final_list_words:
        if not L in result:
            result[L] = 0
        result[L] += 1
    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)#based on the frequencies of words in a list we generate the word cloud
    return cloud.to_array()



# Display your wordcloud image

myimage = calculate_frequencies()
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()





