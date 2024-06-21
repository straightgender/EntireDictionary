from nltk.corpus import wordnet as wn

def get_word_details(word):
    synsets = wn.synsets(word)
    if synsets:
        meanings = [synset.definition() for synset in synsets]
        examples = [example for synset in synsets for example in synset.examples()]
        synonyms = [lemma.name() for synset in synsets for lemma in synset.lemmas()]
        antonyms = []
        for synset in synsets:
            for lemma in synset.lemmas():
                for antonym in lemma.antonyms():
                    antonyms.append(antonym.name())
        return meanings, examples, synonyms, antonyms
    else:
        return None, None, None, None

def main():
    output_file = "D:\\Library\\Python\\meanings.txt"

    with open(output_file, 'w') as f:
        for synset in wn.all_synsets():
            word = synset.name().split('.')[0]  # Extract word from synset name
            meanings, examples, synonyms, antonyms = get_word_details(word)
            f.write(f'Word: {word}\n')
            if meanings:
                for meaning in meanings:
                    f.write(f'Meaning: {meaning}\n')
                if examples:
                    f.write(f'Examples:\n')
                    for example in examples:
                        f.write(f' - {example}\n')
                else:
                    f.write(f'Examples: None\n')
                if synonyms:
                    f.write(f'Synonyms: {", ".join(synonyms)}\n')
                else:
                    f.write(f'Synonyms: None\n')
                if antonyms:
                    f.write(f'Antonyms: {", ".join(antonyms)}\n')
                else:
                    f.write(f'Antonyms: None\n')
            else:
                f.write(f'Meaning: None\nExamples: None\nSynonyms: None\nAntonyms: None\n')
            f.write('\n' * 3)  # Leave three empty lines before the next word

if __name__ == "__main__":
    main()
