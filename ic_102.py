def menu():
  while True:
    try:
      flag1 = int(input('''【ウチダ電鉄 交通系 IC カード検証システム】
      1: 乗車駅選択
      2: チャージ機能
      使用する機能を入力してください(終了する場合には99を入力)
      '''))
      if flag1 == 99:
        print('システムを終了します')
        return int(flag1)
      elif flag1 == 1 or flag1 == 2:
        return int(flag1)
      else:
        print('正しい数値を入力してください。')
    except ValueError:
      print('数字を入力してください。')
def select_station():
  while True:
    try:
      flag2 = int(input('''【乗車駅選択】
      1:秋葉原駅から 133円
      2:山梨駅から 4128円
      3:長野駅から 7990円
      乗車した駅を入力してください（キャンセルする場合には99を入力)
      '''))
      if flag2 == 1:
        print('乗車駅は秋葉原で運賃は133円です。')
        return 133
      elif flag2 ==2:
        print('乗車駅は山梨で運賃は4128円です。')
        return 4128
      elif flag2 == 3:
        print('乗車駅は長野で運賃は7990円です。')
        return 7990
      elif flag2 == 99:   
        print('駅の選択をキャンセルしました。')
        return 0
      else:
        print('正しい数値を入力してください。')
    except ValueError:
        print('数字を入力してください。')

def pay(balance, fare):
    print(f"チャージ残高は{balance}円です。")

    if balance < fare:
        print("残高不足です。")

        while balance < fare:
            balance = balance + 3000
            print(f"{3000}円自動チャージします。")

    balance = balance - fare
    print(f"精算後のチャージ残高は{balance}円です。")

    if balance < 500:
        balance = balance + 3000
        print(f"残高が{500}円未満のため{3000}円自動チャージします。")
        print(f"チャージ残高は{balance}円です。")

    return balance

def charge(balance):
    # ここにcharge関数の処理を書いてください
    # 引数と戻り値に何を指定するかは設計書から判断してください
    while True:
      try:
        amount = int(input(f'''【チャージ機能】
          チャージ残高は{balance}円です。
          1: 1000 円
          2: 2000 円
          3: 3000 円
          4: 4000 円
          5: 5000 円
          6: 6000 円
          7: 7000 円
          8: 8000 円
          9: 9000 円
          10: 10000 円
          チャージする金額を選択してください。（キャンセルする場合には99を入力)
          '''))
        if amount == 99:
          print(f'チャージをキャンセルしました。')
          return balance
        elif amount == 1:
          print(f'1000円チャージします。チャージ残高は{1000+balance}円です。')
          return balance + 1000
        elif amount == 2:
          print(f'2000円チャージします。チャージ残高は{2000+balance}円です。')
          return balance + 2000
        elif amount == 3:
          print(f'3000円チャージします。チャージ残高は{3000+balance}円です。')
          return balance + 3000
        elif amount == 4:
          print(f'4000円チャージします。チャージ残高は{4000+balance}円です。')
          return balance + 4000
        elif amount == 5:
          print(f'5000円チャージします。チャージ残高は{5000+balance}円です。')
          return balance + 5000
        elif amount == 6:
          print(f'6000円チャージします。チャージ残高は{6000+balance}円です。')
          return balance + 6000
        elif amount == 7:
          print(f'7000円チャージします。チャージ残高は{7000+balance}円です。')
          return balance + 7000
        elif amount == 8:
          print(f'8000円チャージします。チャージ残高は{8000+balance}円です。')
          return balance + 8000
        elif amount == 9:
          print(f'9000円チャージします。チャージ残高は{9000+balance}円です。')
          return balance + 9000
        elif amount == 10:
          print(f'10000円チャージします。チャージ残高は{10000+balance}円です。')
          return balance + 10000
        else:
          print('正しい数値を入力してください。')
      except ValueError:
        print('数字を入力してください。')
def main():
  balance = int(500)
  while True:
    flag1 = menu()
    if flag1  ==1:
      flag2 = select_station()
      while True:
        if flag2 == 133:
          balance = pay(balance,flag2)
          break
        elif flag2 == 4128:
          balance = pay(balance,flag2)
          break
        elif flag2 == 7990:
          balance = pay(balance,flag2)
          break
        elif flag2 == 0:
          break

    elif flag1 ==2:
        balance = charge(balance)
    elif flag1 == 99:
      break
if __name__ == "__main__":
  main()
