from flask import Flask, request, redirect
from flask import render_template
import calc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consequence', methods=['POST'])
def finished():
    #購入価格と残存期間と利率
    price = request.form['price']
    interest = request.form['interest']
    term = request.form['term']

    price = int(price)
    interest = int(interest)
    term = int(term)

    def try_check(price, interest, term):
        if (price == "") or (interest == "") or (term == ""):
            return False

    if try_check(price, interest, term) == False:
        return"""
        <h1>'購入価格、クーポン金額、残存期間を半角の数値で入力してください'</h1>
        <p><a href="/">戻る</a></p>
            """



    #計算
    # 利回り
    y = calc.YieldRatio(price, interest, term)
    #return redirect('/'), y.y_content()

    # 価格
    p = calc.P_Func(price, interest, term)
    #return redirect('/'), p.p_content()

    # 金額デュレーション
    d = calc.D_Dur(price, interest, term)
    #return redirect('/'), d.d_content()

    # 修正デュレーション
    m = calc.M_Dur(price, interest, term)
    #return redirect('/'), m.m_content()

    # マコーレのデュレーション
    dm = calc.D_Mac(price, interest, term)
    #return redirect('/'), dm.dmac_content()

    return render_template('consequence.html',
    yi = y.y_content() * 100,
    pr = p.p_content(),
    dur1 = d.d_content(),
    dur2 = m.m_content(),
    dm = dm.dmac_content()
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
