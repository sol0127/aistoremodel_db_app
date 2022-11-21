import pandas as pd
class AiStore:

    def __init__(self, name, s_id, locate, products_num, inventory):
        self.name = name
        self.s_id=s_id
        self.locate=locate
        self.products_num=products_num
        self.inventory=inventory

    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products_num(self):
        return self.products_num

if __name__ == '__main__':

    s_df = pd.read_csv('./stores.csv')
    s_df=s_df.set_index('s_id')
    p_df = pd.read_csv('./products.csv')
    p_df=p_df.set_index('p_id')
    iv_df = pd.read_csv('./inventory.csv')

    # print(s_df)
    # print(p_df)
    # print(iv_df)

    # print(s_df['name'])
    # print(s_df[['name']])
    # print(s_df.iloc[0])
    # print(s_df.iloc[[0]])
    # for store in s_df:
    #     print(store)

    # for store in s_df:
    #     print('스토어이름:{} 스토어 아이디:{} 스토어 위치:{} 등록상품:{}'
    #           .format(,
    #                   str(store['s_id']),
    #                   str(store['locate']),
    #                   str(store['products_num'])))

    #print(s_df.loc[0])

    # print(len(s_df))
    #print(s_df)

    #print(s_df['s_id'])
    # for i in range(len(s_df)):
    #     print(s_df.loc[i,'name'])
    #     print("하나씩 지점명 출력중")

    # id='s1'
    # print(s_df['s_id'])
    #
    # for i in range(len(s_df)):
    #     if s_df.iloc[i]['s_id']==id:
    #         print("yes")
    #     else:
    #         print("no")

    #sp_df=p_df['p_id']
    # print(sp_df)
    # print(sp_df[0])
    # i='p1'
    #
    # if i in sp_df.loc:
    #     print('yes')
    # else:
    #     print('no')

    # i='p1'
    # siv_df=iv_df['p_id']
    # print(siv_df)
    #
    # if i in siv_df.loc:
    #     print("yes")
    # else:
    #     print("no")

    # print(s_df)
    # for s_id in s_df.index:
    #     print('스토어 이름:{}'.format(s_df.loc[s_id,'name']))
    #     # print(s_df.loc[s_id,'name'])
    #     print('스토어 아이디:{}'.format(s_df.loc[s_id]))
    #     #print(s_df.loc[s_id,'s_id'])


#해결 못함
    # print(iv_df)
    # s_id='s1'
    # print(iv_df[iv_df['s_id']==s_id])
    # print(s_df.loc[s_id,'name'])
    # s_id = 's1'
    # print(iv_df[iv_df['s_id']==s_id])
    # ss_df=iv_df[iv_df['s_id']==s_id]
    # for p_id in ss_df.index:
    #     print(p_df[p_df['p_id']==p_id])
    #     print('ho')
    #p_df[iv_df['p_id']=='p_id']



    # if s_id==iv_df.loc['s_id']:
    #     for p_id in iv_df:
    #         print('상품명:{} - 가격:{} (재고{}) id:{}'
    #               .format(p_df['product'],
    #                       iv_df['price'],
    #                       iv_df['count'],
    #                       p_id))

    # s_id='s1'
    # ss_df=iv_df[iv_df['s_id']==s_id]
    # ss_df=ss_df.set_index('p_id')
    # for p_id in ss_df.index:
    #     print('상품명:{} - 가격:{} (재고{}) id:{}'
    #           .format(p_df.loc[p_id,'product'],
    #                   ss_df.loc[p_id,'price'],
    #                   ss_df.loc[p_id,'count'],
    #                   p_id))

    # p_id='p1'
    # print(p_df.loc[p_id,'product'])

    s_id='s1'
    p_id='p1'
    print(iv_df.loc[p_id,s_id,'count'])