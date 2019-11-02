from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbfocatmo

# # URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('file:///Users/ashleychung/Desktop/Sparta/2_Personal%20Project/Project1019.html',headers=headers)
#
# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup = BeautifulSoup(data.text, 'html.parser')

@app.route('/')
def home():
    return render_template('Project1019.html')

## API 역할을 하는 부분
@app.route('/post', methods=['POST'])
def saving():
    place_receive = request.form['place_give']
    time_receive = request.form['time_give']
    text_receive = request.form['text_give']
    date_receive = request.form['date_give']
    print('aaa')
    history = {'place': place_receive, 'time': time_receive, 'text': text_receive, 'date': date_receive}
    print('bbb')
    db.history.insert_one(history)
    print('ccc')
    return jsonify({'result': 'success'})

@app.route('/post', methods=['GET'])
def listing():

   # place_receive = request.args.get('place_give')
   # time_receive = request.args.get('time_give')
   # text_receive = request.args.get('text_give')
   # date_receive = request.args.get('date_give')
   #
   # result = list(db.history.find({'place':place_receive},{'time':time_receive},{'text':text_receive},{'date':date_receive}))

   result = list(db.history.find({},{'_id':0}))
   print('yyy')

   return jsonify({'result':'success', 'history':list(result)})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)