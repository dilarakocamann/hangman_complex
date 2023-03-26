import random

words = 'ant baboon owl bat bear zebra camel shark horse cobra whale'.split()
def getRandomWord(wordList):

    # Tanımlanan dizeler listesinden rastgele bir dize döndür
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

# rastgele seçme işlevini kullanarak indirdiğimiz random kitaplığın bir işlevini oluşturduk
def get_word():
    return random.choice(words)

# oyunun ilerleyişi ile ilgili bir işlev tanımladık
def show_state(word, guesses, wrong_guesses):

    # kelimenin bilinemeyen harfleri için alt çizgi ile göstermek
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)

    # yanlış tahminleri göster
    if len(wrong_guesses) > 0:
        print("Yanlış tahminler: {}".format(" ".join(wrong_guesses)))

    # adamı çiz
    print("")
    if len(wrong_guesses) >= 1:
        print("  0  ")
    if len(wrong_guesses) == 2:
        print("  |  ")
    elif len(wrong_guesses) == 3:
        print(" /|  ")
    elif len(wrong_guesses) >= 4:
        print(" /|\ ")
    if len(wrong_guesses) == 5:
        print(" /   ")
    elif len(wrong_guesses) >= 6:
        print(" / \ ")

# Oyunu oynamak için
def play():
    word = get_word()
    guesses = set()
    wrong_guesses = []
    max_wrong_guesses = 7

    while True:
        # Oyunu göster
        show_state(word, guesses, wrong_guesses)

        # Oyuncunun tahminini al
        guess = input("Bir harf girin: ").lower()

        # Tahminin bir harf olup olmadığını kontrol et
        if len(guess) != 1 or not guess.isalpha():
            print("Geçerli bir harf girin!")
            continue

        # Harfin önceden tahmin edilip edilmediğine bak
        if guess in guesses:
            print("Daha önce girildi.")
            continue

        # Tahminler dizinine tahmin ekle
        guesses.add(guess)

        # Tahminin doğru olup olmadığına bak
        if guess in word:
            if set(word) == guesses:
                show_state(word, guesses, wrong_guesses)
                print("Kazandınız!")
                return
        else:
            wrong_guesses.append(guess)
            if len(wrong_guesses) >= max_wrong_guesses:
                show_state(word, guesses, wrong_guesses)
                print("Doğru cevap '{}'.".format(word))
                return

# Oyunu başlat
play()