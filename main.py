#Giriş yazısı ve Adam Asamaca şekilleri olan dosya
import art

#Kelimelerin olduğu dosya
import turkishwords
import englishwords

#Random modülü
import random

#Kelimeleri değişkene ata
trwords = turkishwords.kelime
enwords = englishwords.words

#Giriş yazısı çıktısı al
print(art.art)
#Döngü sonklandırmak için değişken ata
game_over = False
#Tahmin edilen kelimeyi eklemek için boş sözlük oluştur.
guess_words = []
game_status = ""
#Tahmin hakki
guess_right = 6
language = input("Lütfen dil seçiniz. (Türkçe için 'tr': \n"
      "Please choose language ('en' for English: ")
#Oyunu tekrar oynamak istediğini sor ve uygula fonksiyon oluştur.
def play_again():
    #değişkenleri global yap
    global game_over
    global guess_right
    global guess_words
    global game_status
    #Oyunu bitir
    game_over = False
    #Oyun durumu sıfırla
    game_status = ""
    #Tahmin edilen harfleri sıfırlar
    guess_words = []
    #Yeniden oynamak istediğini sor.
    play_again = input("Tekrar oynamak istiyor musunuz? (Evet için 'E' / Hayır için 'H'): \n"
                       "Would you like play again? ('Y' for Yes / 'N' for No): ").lower()
    #Tahmin hakkını 0'la
    guess_right = 0
    guess_right = 6
    #türkçe ile cevap verirse türkçe fonksyionu yeniden başlat
    if play_again == "e":
        turkish()
    elif play_again == "h":
        print("Teşekkür ederiz.")
        game_over = True
    #İngilizce ile cevap verirse ingilizce fonkisyonu yeniden başlat
    elif play_again == "y":
        english()
    elif play_again == "n":
        print("Thanks a lot")
        game_over = True
    #Her ikisi ile ile cevap vermesse hata ekranı ver.
    else:
        print("Yanlış seçim yaptınız. Tekrar deneyiniz.")
        play_again()

#Türkçe için fonkisyon
def turkish():
    # word_len_tr'i global olarak tanımla
    global word_len_tr
    global game_over
    global guess_right
    global game_status
    # Kelimeyi random seç
    choose_word_tr = random.choice(trwords)
    # Seçilen kelimeyi seç ve her harf için _ ekle
    word_len_tr = "_" * len(choose_word_tr)

    #oyun bitene kadar kullanılacak döngü.
    while not game_over:
        #Kullanıcıdan harf tahmin etmesini iste
        guess = input("Lütfen harf tahmin edin.: ").lower()

        #Tahmin edilen zaten tahmin edildiyse uyarı ekranı
        if guess in guess_words:
            print("Bu harfi zaten seçtiniz başka bir harf seçin")
            continue

        #Tahmin edilen harfi sözlüğe ekle
        guess_words.append(guess)

        #Tahmin edilen harfleri kontrol et
        print(choose_word_tr)

        if guess in choose_word_tr:
            # Tahmin edilen harfin kelime içindeki indekslerini bulun
            indeks = [i for i, letter in enumerate(choose_word_tr) if letter == guess]
            #Tahmin edilen harfleri "_" ile değiştirin.
            for index in indeks:
                word_len_tr = word_len_tr[:index] + guess + word_len_tr[index +1:]
        else:
            #Kelime yanlış seçilirse tahmin hakkından 1 düşün
            guess_right -= 1
            #Kalan tahmin hakkını kullanıya bildirin
            print(f"{guess_right} tahmin hakkınız kaldı.")
        #Oyun durumunu kullanıcıua bildirin
        print("Oyun durumu:", word_len_tr)

        #Kalan tahmin adına göre asılan adamın parçalarını yazdırın.
        if guess_right == 5:
            print(art.hangman[1])
        elif guess_right == 4:
            print(art.hangman[2])
        elif guess_right == 3:
            print(art.hangman[3])
        elif guess_right == 2:
            print(art.hangman[4])
        elif guess_right == 1:
            print(art.hangman[5])
        elif guess_right == 0:
            print(art.hangman[6])
            game_over = True
            play_again()
        #Oyun bittiğini söyleyin ve döngüyü durdurdun.
        if word_len_tr == choose_word_tr:
            print("Tebrikler! Kelimeyi doğru tahmin ettiniz.")
            game_over = True
            play_again()

#For English
def english():
    global word_len_en
    global game_over
    global guess_right
    global game_status
    choose_word_en = random.choice(enwords)
    word_len_en = "_" * len(choose_word_en)
    while not game_over:
        guess = input("Please guess a letter: ").lower()
        if guess in guess_words:
            print("You have already selected this letter, choose another letter")
            continue
        guess_words.append(guess)
        print(choose_word_en)
        game_status = ""
        if guess in choose_word_en:
            indeks = [i for i, letter in enumerate(choose_word_en) if letter == guess]
            for index in indeks:
                word_len_en = word_len_en[:index] + guess + word_len_en[index + 1:]
        else:
            guess_right -= 1
            print(f"{guess_right} you have the right to guess")
        print("Game Status:", word_len_en)
        if guess_right == 5:
            print(art.hangman[1])
        elif guess_right == 4:
            print(art.hangman[2])
        elif guess_right == 3:
            print(art.hangman[3])
        elif guess_right == 2:
            print(art.hangman[4])
        elif guess_right == 1:
            print(art.hangman[5])
        elif guess_right == 0:
            print(art.hangman[6])
            game_over = True
            play_again()
        if word_len_en == choose_word_en:
            print("Congratulations! You guessed the word correctly.")
            game_over = True
            play_again()



if language == "tr":
    turkish()
elif language == "en":
    english()
else:
    print("Yanlış değer girdiğiniz. Lütfen tekrar deneyiniz.\n"
          "Your entered wrong value. Please try again.")