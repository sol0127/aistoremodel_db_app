import pandas as pd
import json

class Customer: #고객이 존재하면 그 안에서 기능

    def __init__(self, customer, accounts):
        self.customer = customer # series
        self.accounts = accounts # dataframe 여기만 바뀔뿐 전체 데이터가 안바뀜 가장 좋은건 전체 디비 업뎃 후 내부 업뎃
        #여기선 내부 업뎃 후 외부 업뎃 update()

    def add_amount(self, a_id, amount):
        if a_id in self.accounts.index:
            self.accounts.loc[a_id, 'amount']+=amount
            self.customer['total_amount']=self.get_total_amount()
            self.cutomer['rat']=self.get_rat()
        else:
            print("해당 계좌가 없습니다.")
        # for i in range(len(self.accounts)):
        #     if a_id==self.accounts.loc[i]['a_id']:
        #         self.accounts.loc[i]['amount']+=amount
        #     else:
        #         print("해당 계좌가 없습니다.")

    def sub_amount(self, a_id, amount):
        if a_id in self.accounts.index:
            if self.accounts.loc[a_id, 'amount']>=amount:
                self.accounts.loc[a_id, 'amount']-=amount
                self.customer['total_amount']=self.get_total_amount()
            else:
                print("계좌 금액이 부족합니다.")
        else:
            print("해당 계좌가 존재하지 않습니다.")
        # for i in range(len(self.accounts)):
        #     if a_id==self.accounts.loc[i]['a_id']:
        #         if self.accounts.loc[i]['amount']>=amount:
        #             self.accounts.loc[i]['amount']-=amount
        #         else:
        #             print("계좌 금액이 부족합니다.")
        #     else:
        #         print("해당 계좌가 존재하지 않습니다.")

    def add_account(self, a_id):
        if a_id in self.accounts.index:
            print("이미 있는 계좌번호입니다.")
        else:
            self.accounts.loc[a_id] = {'a_id': a_id, 'password': 0, 'c_id': self.get_cid(), 'amount': 0}
            self.customer['account_num']+=1
        # for i in range(len(self.accounts)):
        #     if a_id ==self.accounts.loc[i]['a_id']:
        #         print("이미 있는 계좌번호입니다.")
        #     else:
        #         self.accounts.loc[a_id]={'a_id':a_id, 'password':0, 'c_id':self.get_cid(), 'amount':0}
        #         self.customer['account_num']+=1
            # self.update(self.customer,self.customer)

    def get_total_amount(self,c_id):
        self.accounts.loc[c_id,'amount'].sum()

        # for i in range(len(self.accounts)):
        #     t_amount+=self.accounts.loc[i]['amount'] #함수를 활용하자!
        #     self.customer[self.customer['c_id']==c_id]['total_amount']=t_amount

    def get_rat(self):
        total_amount = self.get_total_amount()
        if total_amount > 100000:
            rat = 'vvip'
        elif total_amount > 10000:
            rat = 'vip'
        elif total_amount > 1000:
            rat = 'gold'
        elif total_amount > 100:
            rat = 'silver'
        else:
            rat = 'bronze'

        return rat

    def update(self, c_df, a_df):
        #a_df, c_df가 변경되어야 하는거
        #c_df.loc[self.customer['c_id']->1c에 해당되는 거]
        # self.customer.update(c_df) #반대로 됨
        # self.accounts.update(a_df)
        c_df.loc[self.customer['c_id']]=self.customer
        a_df.update(self.accounts)

    def get_name(self):
        return self.customer['name']

    def get_cid(self):
        return self.customer['c_id']

    def get_accounts(self):
        return self.accounts

    def get_customer(self):
        return self.customer


def create_customer():
    c_name = input('고객 이름 입력:')
    c_id = input('고객 번호 입력:')
    # c_id 있는지 확인
    c_list={'c_id':c_id, 'name':c_name, 'account_num':0, 'total_amount':0, 'rat':'normal'}
    c_df.loc[c_id]=c_list
    # c_df.loc[c_df['c_id'] == c_id] = customer 인덱스는 고유한 값으로 해야(주의) c_df.loc[c_id] = customer
    # pd.concat([c_df, pd.DataFrame([customer])], ignore_index=False) 인덱스 무시할지 무시하면 다음 순서로 들어옴
    #ignore_index안하면 내가 원하는 인덱스가 아닌 다음 인덱스로 들어가게 됨 concat은 마지막 줄에 들어감
    print('{} 고객이 생성 되었습니다.'.format(c_name))
    #c_df.update(c_df) #여기보단...

def show_list():
    for customer in c_df.iloc: #iloc가 for문 안에 들어가면 iterrows랑 비슷한
        print('고객이름:{} 고객번호:{}'
              .format(customer['name'],
                      customer['c_id'],
                      ))


def search_customer(c_id): #customer인스턴스 반환
    #iloc말고 인덱스로 접근
    if c_id in c_df.index:
        #customer=c_df[c_df['c_id']==c_id]
        customer=c_df.loc[c_id]
        accounts=a_df[a_df['c_id']==c_id]
        cus=Customer(customer,accounts)
        return cus
    else:
        print("고객번호를 찾지 못했습니다.")
        return None
    # for i in range(len(c_df)):
    #     if c_id ==c_df.iloc[i]['c_id']:
    #         customer=c_df.iloc[i]
    #         account=a_df[a_df['c_id']==c_id]
    #         cus= Customer(customer,account)
    #         # print(customer)
    #         # print(account)
    #         return cus
    #     else:
    #         return None



def create_acount():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        print("존재하지 않는 계좌번호입니다.")
        return

    acount_num = input('계좌번호 입력:')
    customer.add_account(acount_num)
    customer.update(c_df,a_df)   #업데이트!
    print('{} 고객의 {} 계좌가 등록되었습니다'
          .format(customer.get_name(),
                  acount_num,
                  ))



def show_customer():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    print('{} 고객님 등급:{} 총금액:{} 계좌정보:\n{}'
          .format(customer.get_name(),
                  customer.get_rat(),
                  customer.get_total_amount(),
                  customer.get_accounts()
                  ))


def deposit():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    acount_num = input('계좌번호 입력:')
    amount = input('입금할 금액 입력:')
    customer.add_amount(acount_num,int(amount))
    customer.update(c_df,a_df) #여기서 업데이트!

def withdraw():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    acount_num = input('계좌번호 입력:')
    amount = input('출금할 금액 입력:')
    customer.sub_amount(acount_num,int(amount))
    customer.update(c_df,a_df)

def ca_merge():
    pass


def group_rat_count(): #rename 써보기 /변경 후 다시 받아주는 거 주의
    pass



if __name__ == '__main__':

    c_df = pd.read_csv('./customers.csv')
    c_df=c_df.set_index('c_id', drop=False) #c_id 컬럼 삭제하면 안됨
    a_df = pd.read_csv('./accounts.csv')
    a_df=a_df.set_index('a_id', drop=False)
    print(c_df.dtypes)
    print(a_df.dtypes)

    print('1 - 고객 생성')
    print('2 - 계좌 생성')
    print('3 - 입금')
    print('4 - 출금')
    print('5 - 생성된 고객 리스트 출력')
    print('6 - 고객 정보 출력')
    print('7 - csv 파일로 고객 정보 출력') #tocsv함수 이용해 저장 index 옵션 false 주는 걸 추천(통일성 위해)
    print('8 - csv 파일로 계좌 정보 출력')
    print('9 - csv 파일로 고객 - 계좌 정보 출력') #merge(인덱스 설정 안되어 있어도 컬럼을 기준으로), join(인덱스 필) 차이점
    print('10 - 등급별 고객의 명수 출력') #업데이트할 때 고객등급도 고려해야한다는 거 고객등급도 중복가능->rat기준으로 groupby/ count->c_id (개수 빠지지 않게)

    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요')
        if input1 == '1':
            create_customer()
        elif input1 == '2':
            create_acount()
        elif input1 == '3':
            deposit()
        elif input1 == '4':
            withdraw()
        elif input1 == '5':
            show_list()
        elif input1 == '6':
            show_customer()
        elif input1 == '7':
            pass
        elif input1 == '8':
            pass
        elif input1 == '9':
            ca_merge()
        elif input1 == '10':
            group_rat_count()

        else:
            print('존재하지 않는 명령어 입니다.')