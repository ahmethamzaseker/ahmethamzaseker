meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GG": "Oyunlar bittiğinde oyunun iyi geçtiğini söylemek için kullanılır",
            "HLGH": "Selam vermek için kullanılır",
            "SA": "Oyunun başında selam vermek için kullanılır"
            }
            
# 5 kere bana hangi kelimenin anlamını öğrenmek istediğim sorulsun istiyorum
for i in range(0, 5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in meme_dict.keys():
        print("Aradığınız kelimenin anlamı: ", meme_dict[word])
        # Kelime eşleşiyorsa ne yapmalıyız?
    else:
        print("Aradığınız kelime sözlükte bulunamadı.")
        # Kelime eşleşmiyorsa ne yapmalıyız?
