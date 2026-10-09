import random
hand = ["グー", "パー", "チョキ"]
while True:
    computer = random.choice(hand)
    you = input("グー、パー、チョキのいずれかを入力してください: ")
    while you not in hand:
        print("正しい手を入力してください。")
        you = input("もう一度入力してください: ")
    print("あなたの手は", you, "です。")
    print("コンピューターの手は", computer, "です。")
    if you == computer:
        print("あいこです。")
    elif (you == "グー" and computer == "チョキ") or (you == "パー" and computer == "グー") or (you == "チョキ" and computer == "パー"):
        print("あなたの勝ちです。")
    else:
        print("コンピューターの勝ちです。")
    play_again = input("もう一度プレイしますか？ (はい/いいえ): ")
    if play_again.lower() != "はい":
        break

print("ゲームを終了します。")