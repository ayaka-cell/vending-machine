# 自動販売機の初期硬貨
coins = {
    500: 5,
    100: 10,
    50: 10,
    10: 20
}

# ユーザーからの入力
n = int(input("投入金額: "))
x = int(input("商品の価格: "))

if n < x:
    print("投入金額が足りません")
else:
    oturi = n - x
    change = {}
    
    for coin in sorted(coins.keys(), reverse=True):
        if oturi <= 0:
            break
        
        if oturi >= coin:
            # 必要な枚数と余り
            maisuu = oturi // coin
            available = min(maisuu, coins[coin])
            if available > 0:
                change[coin] = available
                # お釣りを引く
                oturi -= available * coin
                coins[coin] -= available

    # お釣りが出せない場合
    if oturi > 0:
        print("買えません")
    else:
        print("お釣り:")
        for coin, count in change.items():
            print(f"{coin}円: {count}枚")