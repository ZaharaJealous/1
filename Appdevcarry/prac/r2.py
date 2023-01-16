while True:
    information = 'Select the program (1-3) to run: \n1. Add a Question \n2. Display a Question (by id) \n3. Quit the program'
    print(information)
    cmd = int(input('Enter your command (1-3): '))
    try:
        class Add():
            def __init__(self, qid, qd, qa):
                self.__qid = qid
                self.__qd = qd
                self.__qa = qa
            def get_qid(self):
                return self.__qid
            def get_qd(self):
                return self.__qd
            def get_qa(self):
                return self.__qa
            def set_qid(self,qid):
                self.__qid = qid
            def set_qd(self, qd):
                self.__qd = qd
            def set_qa(self,qa):
                self.__qa = qa
        class Display():
            def __init__(self, qidn, dqid,qida):
                self.__qidn = qidn
                self.__dqid = dqid
                self.__qida = qida
            def get_qidn(self):
                return self.__qidn
            def get_dqid(self):
                return self.__dqid
            def get_qida(self):
                return self.__qida
            def set_qidn(self,qidn):
                self.__qidn = qidn
            def set_dqid(self,dqid):
                self.__dqid = dqid
            def set_qida(self,qida):
                self.__qida = qida
            def __str__(self):
                s = 'Question id: {} Description: {} Answer: {}'.format(self.__qidn, self.__dqid, self.__qida)
        if cmd == 1:
            qid = int(input('Enter question id: '))
            qd = input('Enter question description: ')
            qa = input('Enter question answer: ')
            aaa = Add(qid,qd,qa)
            aaa.set_qid(qid)
            aaa.set_qd(qd)
            aaa.set_qa(qa)
            with open('r2.txt','a') as f:
                f.write(str(qid))
                f.write(qd)
                f.write(qa)
            print('A question added to shelve')
        if cmd == 2:
            qidn = int(input('Enter the question id to display: '))
            dqid = qd
            qida = qa
            if qidn == qid:
                ddd = Display(qidn,dqid,qida)
                ddd.set_qidn(qidn)
                ddd.set_dqid(dqid)
                ddd.set_qida(qida)
                with open('r2.txt','r') as f:
                    for line in f:
                        print(line, end= '')
                    #print('Question id: ',f.readline())
                    #print('Description: ', f.readline())
                    #print('Answer: ', f.readline())
            else:
                print('No such question')
        if cmd == 3:
            print('End of program')
            break
    except ValueError:
        print('Please enter valid input')
        information = 'Select the program (1-3) to run: \n1. Add a Question \n2. Display a Question (by id) \n3. Quit the program'
        print(information)
        cmd = int(input('Enter your command (1-3): '))
