import random
symboles = ["7","BAR","チェリー","ベル"]
score = 0
play_count = 0
big_win_count = 0
small_win_count = 0

while True:
    play_count += 1
    slot1 = random.choice(symboles)
    slot2 = random.choice(symboles)
    slot3 = random.choice(symboles)

    print(slot1, slot2, slot3)

    if slot1 == slot2 == slot3:
        print("大当たり！") 
        score += 100
        big_win_count += 1
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        print("小当たり！") 
        small_win_count += 1
        score += 30
    else:
        print("ハズレ")

    play_again = input("もう一度プレイしますか？ (はい/いいえ): ")
    if play_again != "はい":
        break
print(f"現在のスコア: {score}")
print(f"プレイ回数: {play_count}")
print(f"大当たり回数: {big_win_count}")
print(f"小当たり回数: {small_win_count}")
