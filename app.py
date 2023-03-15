import datetime  # 작성 시간 기록을 위한 패키지
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, app, session, redirect, url_for, escape
import bcrypt as bc  # 암호화 패키지

client = MongoClient("mongodb+srv://sparta:test@cluster0.280f8z1.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta

app = Flask(__name__)


@app.route('/')  # 메인페이지
def home():
    return render_template('index.html')


@app.route('/join')  # 회원가입 팝업
def join():
    return render_template('join.html')


@app.route('/createUserData', methods=["POST"])
def create_user():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    hashed_pw = bc.hashpw(pw_receive.encode("utf-8"), bc.gensalt()).decode("utf-8")
    # 각 입력값이 비어있을 경우 등록 실패
    if db.Users.find_one({'id': id_receive}) != None:
        return jsonify({'result': 'fail_00', 'msg': '이미 존재하는 아이디입니다.'})
    # db저장
    else:
        doc = {
            'id': id_receive,
            'pw': hashed_pw
        }
        db.Users.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '가입 완료!'})

    # @app.route('/login', methods=["POST"])
    # def login():
    #     id_receive = request.form['id_give']
    #     pw_receive = request.form['pw_give']
    #     user = db.Users.find_one({'id': id_receive})
    #     print(user)
    #     return jsonify({'result': 'success', 'msg': '연결 완료!'})

    # if id_receive == current_id['id'] and current == True:
    #         session['id_give'] = request.form['id_give']   #현정
    #         session['mbti'] = mbti['mbti']
    #         return redirect(url_for('index'))
    # else:
    return jsonify({'msg': '아이디 또는 비밀번호를 확인해 주세요'})


# @app.route('/login')
# def index():
#     if 'id_give' in session:  # session안에 id_give가 있으면 로그인
#         return jsonify({'msg': '어서오세요 %s 님^ㅇ^' %escape(session['id_give'])})
#     return render_template('base.html') #세션 보내버리기
@app.route('/reply', methods=["POST"])
def submit():
    name_receive = request.form['name_give']
    reply_receive = request.form['reply_give']

    doc = {
        'name': name_receive,
        'reply': reply_receive,
        'date':datetime.datetime.now(),
    }
    db.replys.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '저장완료'})

@app.route('/replys', methods=["GET"])
def show_reply():
    replys = list(db.replys.find()['_id':False])

    return jsonify({'comments': replys})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
