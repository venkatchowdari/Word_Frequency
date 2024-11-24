from collections import Counter
import re


def get_frequency(text : str)-> list[tuple[str, int]]:
    lowered_text :str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts :Counter = Counter(words)
    return word_counts.most_common()

def open_file(path : str) -> str:
    return open(path, "r")

def main()->None:
    while(True):
        desion = input("Do you want to open a text file path or type the text (yes or no) :")
        desion = desion.lower()
        desion = desion.strip()
        try:
            if (desion == "yes"):
                path = input("Enter the file path : ")
                file = open_file(path)
                text = file.read()
                word_frequencies : list[tuple[str, int]] = get_frequency(text)
                for word, count in word_frequencies:
                    print(f'{word} : {count}')
                break

            elif(desion == "no"):
                text :str = input("Enter your text : ")
                word_frequencies : list[tuple[str, int]] = get_frequency(text)
                for word, count in word_frequencies:
                    print(f'{word} : {count}')
                break

            else:
                print("Please enter a valid input (yes or no)")
                continue
            
        except FileNotFoundError:
            print("Please enter a valid existing file")
        


if __name__ == '__main__':
    main()
 