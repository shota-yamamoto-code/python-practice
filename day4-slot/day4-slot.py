import random
symboles = ["7","BAR","チェリー","ベル"]
score = 0

while True:
    slot1 = random.choice(symboles)
    slot2 = random.choice(symboles)
    slot3 = random.choice(symboles)

    print(slot1, slot2, slot3)

    if slot1 == slot2 == slot3:
        print("大当たり！") 
        score += 100
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        print("小当たり！") 
        score += 30
    else:
        print("ハズレ")

    play_again = input("もう一度プレイしますか？ (はい/いいえ): ")
    if play_again != "はい":
        break
print(f"現在のスコア: {score}")
