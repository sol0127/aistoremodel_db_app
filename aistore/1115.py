import json
import pandas as pd

#products_num 같이 변경
class AiStore:

    def __init__(self, name, s_id, locate, products_num, inventory):
        self.name = name
        self.s_id=s_id
        self.locate=locate
        self.products_num=products_num
        self.inventory=inventory #데이터프레임

    def set_product(self, p_id, count, price):
        #
        if p_id in self.inventory:
            self.inventory.loc[p_id,'count']+=count
            self.inventory.loc[p_id,'price']=price
            #업데이트
        else:
            self.inventory.append({'p_id':p_id, 'count':count, 'price':price, 's_id':self.s_id})
            #concat을 해도 되고 제일 마지막에 추가해도 됨
            #리스트로 한번 더 씌워주면 행,열 모두 충족하게 됨(데이터프레임) 리스트 안 씌우면 그냥 시리즈라 문제 생김
            #ignore_index s_id에 0들어가면 문제 생기는 걸 해결해줌
        # if in 을 사용하기위해선 시리즈를 배열로 바꿔야할것 문서 참고
        # try 문사용 가능
        # 쿼리후 개수로 파악 가능


    def buy_product(self, s_id, p_id, count, amount):
        #테이블로 가져오면 보여줄 때는 편하지만 쿼리를 계속하게 됨->쿼리할 때마다 돈이 들어감
        #쿼리를 많이 할 거 같으면 한번에 가져오는 테이블 이용하는게 하지만 쿼리를 적게 하는데 한번에 많이 가져오는 테이블 이용하면 통신비용이...
        #한번에 많이 가져오는 건 그만큼 통신비용이 들기때문
        self.inventory=self.inventory.set_index('p_id',drop=False)
        t_price=self.inventory.loc[p_id,'price']*count
        if t_price<=amount:
            change=amount-t_price
            print('잔액은 {}입니다.'.format(change))
            self.inventory.loc[p_id,'count']-=count
            # i_count=self.inventory.loc[p_id,'count']
            # i_count-=count

        else:
            print("금액이 부족합니다.")


    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products_num(self):
        return self.products_num
    def show_products(self, p_df):
        self.inventory=self.inventory.set_index('p_id')
        print(self.inventory)
        for p_id in self.inventory.index:
            print('상품명:{} - 가격:{} (재고{}) id:{}'
                  .format(p_df.loc[p_id,'product'],
                          self.inventory.loc[p_id,'price'],
                          self.inventory.loc[p_id,'count'],
                          self.inventory.loc[p_id,'s_id']
                          ))

    def get_price(self, p_id):
        product =  self.inventory[self.inventory['p_id'] == p_id]
        if len(product) == 0:
            return None

        return product['price'].iloc[0]

    def update_data(self, s_df, iv_df):
        n_df={'s_id':self.s_id, 'name':self.name, 'locate':self.locate, 'products_num':self.products_num}
        s_df.loc[self.s_id]=n_df
        #iv_df.update(self.inventory) #새로 추가되는 줄은 반영 안됨 없는 인덱스(f)는 추가해야함 loc[f]=이렇게 기존에 있는건 재할당해서 괜찮
        #문제는 인벤토리가 순서라는 거
        for idx in self.inventory.index:
            iv_df.loc[idx]=self.inventory.loc[idx]
        #update함수랑, add함수 따로
        #iv_df.loc[self.inventory['s_id']]=self.inventory

        # for p_id in self.inventory:
        #     iv_df.loc[p_id]=self.inventory[p_id]

        # for p_df in self.inventory.index:
        #     if p_df in iv_df["p_id"].values:
        #         iv_df.loc[p_df] = self.inventory.loc[p_df]
        #     else:
        #         iv_df.loc[len(iv_df)] = self.inventory.loc[p_df]
            # print(self.inventory.loc)


def create_store():
    s_name = input('스토어 이름 입력: ')
    s_id = input('스토어 번호 입력: ')
    if s_id in s_df.index:
        print("이미 존재하는 번호입니다.")
        return

    locate = input('스토어 위치 입력: ')
    produc_num = 0
    niv_df={'count':0, 's_id':s_id}
    store = AiStore(s_name, s_id, locate,produc_num, niv_df)
    print('{} 스토어가 생성 되었습니다.'.format(s_name))
    store.update_data(s_df, iv_df)


def show_list():
    for s_id in s_df.index:
        print('스토어 이름:{} 스토어 아이디:{} 스토어 위치:{} 등록상품:{}'
              .format(s_df.loc[s_id,'name'],
                      s_id,
                      s_df.loc[s_id,'locate'],
                      s_df.loc[s_id,'products_num']))

def search_store(s_id):
    if s_id in s_df.index:
        siv_df=iv_df[iv_df['s_id']==s_id]
        store=AiStore(s_df.loc[s_id,'name'],s_id,s_df.loc[s_id,'locate'],s_df.loc[s_id,'products_num'],siv_df)
        return store
    else:
        print("해당 아이디를 가지는 가게가 없습니다.")
        return None

def show_store():
    s_id = input('스토어 번호 입력: ')
    store=search_store(s_id)
    if store is None:
        return
    print('스토어이름:{} 스토어 아이디:{} 스토어 위치:{}'
          .format(s_df.loc[s_id,'name'],
                  s_id,
                  s_df.loc[s_id,'locate'])) #여기 안에 show_product()함수 들어가면 이 함수 먼저 출력 후 print함수 실행됨. iyelt:return이 for문처럼 연속적으로 나오게하는
    print('등록상품:')
    store.show_products(p_df)
def buy():
    s_id = input('스토어 번호 입력: ')
    store=search_store(s_id)
    if store is None:
        return
    p_id = input('상품 아이디 입력:')
    biv_df=iv_df[iv_df['s_id']==s_id]
    biv_df=biv_df.set_index('p_id')
    if p_id in biv_df.index:
        count = input('구매 개수 입력: ')
        count = int(count)
        if count<biv_df.loc[p_id,'count']:
            t_price=count*biv_df.loc[p_id,'price']
            print('총 금액은 {}입니다.'.format(t_price))
            price = input('가격 입력: ')
            price = int(price)
            store.buy_product(s_id, p_id, count, price)
            store.update_data(s_df, iv_df)

        else:
            print("상품 재고가 부족합니다.")
    else:
        print('해당 상품이 존재하지 않습니다.')
def manager_product():

    s_id = input('스토어 번호 입력: ')
    store=search_store(s_id)
    if store is None:
        return
    print("등록 가능 상품:")
    print(p_df)
    p_id = input('상품 아이디 입력: ')
    count = input('재고 개수 입력: ')
    price = input('상품 가격 입력: ')
    store.update_data(s_df,iv_df)

    #set_product이용해 재고 가격 수정


import json
def products_counts():
    piv_df=iv_df.loc[:,['p_id','count']] #주의p_df에 iv_df merge하면 문제 생김 중복되는 걸
    pc_df=p_df.join(piv_df.set_index('p_id'))
    pc_df=pc_df.groupby('product').count
    print(pc_df)
    #p_id 어떻게 지우지.....
    #그룹화하자

if __name__ == '__main__':

    s_df = pd.read_csv('./stores.csv')
    s_df=s_df.set_index('s_id')
    p_df = pd.read_csv('./products.csv')
    p_df=p_df.set_index('p_id')
    iv_df = pd.read_csv('./inventory.csv') #순서 인덱스 유지
    #p_id랑 s_id를 리스트로 묶어서 키로 만들 수 있음


    print('1 - 스토어 생성')
    print('2 - 스토어 리스트 출력')
    print('3 - 스토어 정보 출력')
    print('4 - 상품 구매')
    print('5 - 상품 관리')
    print('6 - csv 파일로 스토어, 재고현황 파일 출력')
    print('7 - 상품명별 전체 재고 개수 출력')


    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요: ')
        if input1 == '1':
            create_store()
        elif input1 == '2':
            show_list()
        elif input1 == '3':
            show_store()
        elif input1 == '4':
            buy()
        elif input1 == '5':
            manager_product()
        elif input1 == '6':
            pass
        elif input1 == '7':
            products_counts()
        else:
            print('존재하지 않는 명령어 입니다.')