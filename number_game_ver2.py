import random

answer=random.randint(1,100)

print("数字当てゲーム")
print("1~100の数字を当ててください")

guess=int(input("予想した数字を入力してください："))
count=1

while guess!=answer and count<10:
    count += 1 
    if guess<1 or guess>100:
        print("1~100の数字を入力してください")
        count -= 1
    elif guess<answer:
        print("もっと大きい")
    else:
        print("もっと小さい")
    guess=int(input("もう一度予想してください："))

if guess==answer:
    print(f"正解です！ {count}回で当てました。")
else:
    print("10回以内に当てられませんでした。")