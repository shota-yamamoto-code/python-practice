import random
symboles = ["7","BAR","チェリー","ベル"]

while True:
    slot1 = random.choice(symboles)
    slot2 = random.choice(symboles)
    slot3 = random.choice(symboles)

    print(slot1, slot2, slot3)

    if slot1 == slot2 == slot3:
        print("大当たり！") 
    else:
        print("ハズレ")

    print("ここまで実行されました")

    play_again = input("もう一度プレイしますか？ (はい/いいえ): ")
    if play_again != "はい":
        break