import random

answer=random.randint(1,100)

print("数字当てゲーム")
print("1~100の数字を当ててください")

guess=int(input("予想した数字を入力してください："))
count=1

while guess!=answer:
    count += 1 
    if guess<answer:
        print("もっと大きい")
    else:
        print("もっと小さい")
    guess=int(input("もう一度予想してください："))

print(f"正解です！ {count}回で当てました。")
