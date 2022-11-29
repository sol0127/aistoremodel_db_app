import pandas as pd

s_df = pd.read_csv('./static/stores.csv')
s_df = s_df.set_index('s_id', drop=False)
p_df = pd.read_csv('./static/products.csv')
iv_df = pd.read_csv('./static/inventory.csv')

class AiStore:

    def __init__(self, name, s_id, locate, products_num, inventory):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products_num = products_num
        self.inventory = inventory

    def add_product(self, p_id, count, price, idx):
        #
        #p_list=self.get_product(p_id)

        # slist = self.get_inventory()
        # siv = slist[slist['p_id'] == p_id]

        pdf=p_df.set_index('p_id')
        n_product = {'p_id': p_id, 'p_name':pdf.loc[p_id,'product'], 'count': count, 'price': price, 's_id': self.s_id}
        print(pdf.loc[p_id,'product'])
        self.inventory.loc[idx] = n_product
        self.products_num = len(self.inventory)
        return n_product

    def set_product(self, p_id, count:int, price:int):
        product =  self.inventory[self.inventory['p_id'] == p_id]
        product['count'] += count
        product['price'] = price
        self.inventory.update(product)

    def is_product(self, p_id):
        product = self.inventory[self.inventory['p_id'] == p_id]
        if len(product) == 0:
            return False
        else:
            return True
    def buy_product(self, p_id, count):

        product =  self.inventory[self.inventory['p_id'] == p_id]
        product = product[product['count'] > count]
        if len(product) == 0:
            return

        product['count'] -= count
        self.inventory.update(product)

    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products_num(self):
        return self.products_num

    def get_inventory(self):
        return self.inventory

    def get_menu(self):
        # {'p_name': p_name, 'price': int(price), 'count': int(count), 'p_id':p_id} 형태로 인벤토리의 상품들을 메뉴리스트에 추가

        menu = []

        #inven = iv_df[iv_df['s_id'] == s_id]
        ip_df=self.get_inventory()
        #ip_df = inven.merge(p_df, on='p_id')
        ip_df = ip_df.set_index('p_id')
        for p_id in ip_df.index:
            menu.append({'p_id': p_id, 'p_name': ip_df.loc[p_id, 'product'], 'count': ip_df.loc[p_id, 'count'],
                         'price': ip_df.loc[p_id, 'price']})

        print(menu)
        return menu

    def get_product(self, p_id):
        # p_id 해당하는 상품 반환 인벤토리에서 쿼리 후 .iloc[0] 을 통해 상품 가져올것
        # if p_id in iv_df:
        #     p_name=p_df.iloc[0]
        #     price=iv_df.iloc[2]
        #     count=iv_df.iloce[1]
        # return {'p_name': p_name, 'price': int(price), 'count': int(count), 'p_id':p_id}
        piv = iv_df[iv_df['p_id'] == p_id]
        piv = piv.merge(p_df, on='p_id')
        for i in range(len(piv)):
            pl={'p_name': piv.iloc[i]['product'], 'price': piv.iloc[i]['price'], 'count': piv.iloc[i]['count'], 'p_id':p_id}
        return pl




def create_store(s_id, s_name, locate):

    store = {'s_id': s_id, 'name': s_name,
             'locate': locate,
             'products_num': 0,}

    s_df.loc[s_id] = store
    print('{} 스토어가 생성 되었습니다.'.format(store['name']))


def show_list(s_id = None):
    if s_id is None:
        sr = []
        for s_id in s_df.index:
            inven = iv_df[iv_df['s_id'] == s_id]
            ip_df = inven.merge(p_df, on='p_id')
            s_list = []
            for p_id in ip_df.index:
                s_list.append(ip_df.loc[p_id, 'product'])
            sr.append(
                {'s_id': s_id, 'name': s_df.loc[s_id, 'name'],
                 'locate': s_df.loc[s_id, 'locate'], 'product': s_list})
        return sr
    else:
        if s_id in s_df.index:
            inven = iv_df[iv_df['s_id'] == s_id]
            ip_df = inven.merge(p_df, on='p_id')
            s_list = []
            for p_id in ip_df.index:
                s_list.append(ip_df.loc[p_id, 'product'])
            sr = {'s_id': s_id, 'name': s_df.loc[s_id, 'name'],
                  'locate': s_df.loc[s_id, 'locate'], 'product': s_list}
        print(sr)
        return sr

def search_store(s_id):
    print(s_id)
    if s_id in s_df.index:
        store = s_df.loc[s_id]
        # 인벤토리에서 s_id에 해당하는 상품 쿼리 후 p_df 와 p_id를 기준으로 머지 (인벤토리가 왼쪽이 되야함)
        inven = iv_df[iv_df['s_id'] == s_id]
        inventory = inven.merge(p_df, on='p_id')

        return AiStore(store['name'],
                       store['s_id'],
                       store['locate'],
                       store['products_num'],
                       inventory)
    else:
        print('스토어를 찾지 못했습니다.')
        return None

def get_products():
    return p_df.to_dict('records')

def set_product(store, p_id, price, count):

    if store.is_product(p_id):
        store.set_product(p_id, int(count), int(price))
    else:
        idx = len(iv_df)
        n_product = store.add_product(p_id, int(count), int(price), idx)
        iv_df.loc[idx] = n_product

def update(store: AiStore):
    s_df[store.get_id()] = {'s_id': store.get_id(),
                       'name': store.get_name(),
                       'locate': store.get_locate(),
                       'products_num': store.get_products_num(), }
    iv_df.update(store.get_inventory())

