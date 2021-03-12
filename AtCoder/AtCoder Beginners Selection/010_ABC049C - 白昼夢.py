s = input()

# 入力文字を4種の文字列でreplaceをかけ、空白にする
s = s.replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")

# replaceの結果、何も残らなければYESを出力
if len(s) == 0:
    print("YES")
else:
    print("NO")