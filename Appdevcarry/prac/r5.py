import shelve
class Question:
    def __init__(self, qid, qd, qa):
        self.qid = qid
        self.qd = qd
        self.qa = qa
    def get_qid(self):
        return self.qid
    def get_qd(self):
        return self.qd
    def get_qa(self):
        return self.qa
def menu():
    while True:
        print('1 is add')
        print('2 is view')
        print('3 is exit')
        try:
            slt = int(input('Select 1-3'))
        except ValueError:
            slt = 3
        if slt == 1:
            add()
        elif slt == 2:
            display()
        elif slt == 3:
            print('End of program')
            break
        else:
            print('Please enter valid input')
def add():
    id = int(input('Enter question id: '))
    des = input('Enter question description: ')
    ans = input('Enter question answer: ')
    question_dict[id] = Question(id, des, ans)
    db['question'] = question_dict
    print('Question added')
def display():
    qn = int(input('Enter question id to display: '))
    if qn in question_dict:
        q = question_dict[id]
        return 'Question: {} Desctiption: {} Answer: {}'.format(q.get_qid, q.get_qd, q.get_qa)
    else:
        print('no such qn')
db = shelve.open('r22.txt','c')
question_dict = {}
try:
    if 'question' in db:
        question_dict = db['question']
    else:
        db['question'] = question_dict
except:
    print('Error in opening DB.db')
else:
    menu()
