# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained
# in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself", "Helena"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressing", "concerning", "horrible", "horribly", "questionable"]
punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]


# censor all instances of the phrase learning algorithms
def censor1(text, word):
    censored_word = "X" * len(word)
    return text.replace(word, censored_word)


print(censor1(email_one, "learning algorithms"))


# censor a whole list of words and phrases
def censor2(text, ls):
    for word in ls:
        if word in text:
            censored_word = "X" * len(word)
        text = text.replace(word, censored_word)
    return text


print(censor2(email_two, proprietary_terms))


# censor any occurrence of a word from the “negative words” list after any “negative” word has occurred twice
def censor3(text, ls, negative_ls):
    for word in ls:
        if word in text:
            censored_word = "X" * len(word)
        text = text.replace(word, censored_word)

    negative_words_index = []
    count = 0
    for negative_word in negative_ls:
        if negative_word in text:
            index_word = [text.index(negative_word), negative_word]
            negative_words_index.append(index_word)
            count += 1

    negative_words_index.sort()
    if count > 2:
        negative_words_index = negative_words_index[2:]
        for index_word in negative_words_index:
            text = text.replace(index_word[1], "Y" * len(index_word[1]))

    return text


print(censor3(email_three, proprietary_terms, negative_words))


# censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in
# email_four that come before AND after a term from those two lists.
def censor4(text, ls):
    words_split = []
    for word in text.split(" "):
        for x in word.split("\n"):
            words_split.append(x)

    words_clean = words_split[:]
    for i in range(len(words_clean)):
        words_clean[i] = words_clean[i].lower()
        for x in punctuation:
            words_clean[i] = words_clean[i].strip(x)

        if words_clean[i] in ls:
            words_clean[i] = words_split[i]
            words_clean[i - 1] = words_split[i - 1]
            words_clean[i + 1] = words_split[i + 1]
            for x in punctuation:
                words_clean[i] = words_clean[i].strip(x)
            words_split[i] = words_split[i].replace(words_clean[i], "X" * len(words_clean[i]))
            words_split[i - 1] = words_split[i - 1].replace(words_clean[i - 1], "B" * len(words_clean[i - 1]))
            words_split[i + 1] = words_split[i + 1].replace(words_clean[i + 1], "A" * len(words_clean[i + 1]))

    return " ".join(words_split)


whole_list = proprietary_terms + negative_words
print(censor4(email_four, whole_list))
