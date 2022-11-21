import pandas as pd

if __name__ == '__main__':
    c_df = pd.read_csv('./customers.csv')
    c_df.set_index('c_id')
    a_df = pd.read_csv('./accounts.csv')
    a_df.set_index('a_id')
    print(c_df)
    print(a_df)

    # print(a_df['a_id'])
    # print(a_df.loc[0]['a_id'])
    #
    # a_id = '11a'
    # if a_id in a_df['a_id']:
    #     print("ho")
    # else:
    #     print("no")

    # c_id='1c'
    #
    # for i in range(len(c_df)):
    #     if c_id ==c_df.loc[i]['c_id']:
    #         print("있음")
    #         customer=c_df.loc[i]
    #         account=a_df[a_df['c_id']==c_id]
    #     else:
    #         print("없음")
    # print(customer)
    # print(account)

    # print(c_df['c_id'])
    # if c_id in c_df['c_id']:
    #     print("yes")
    # else:
    #     print("no")

    # print(c_df)
    # for customer in c_df.loc:
    #     print('00')
    c_id='1c'
    print(c_df[c_df['c_id']==c_id])
    print(c_df[:,[c_id]])