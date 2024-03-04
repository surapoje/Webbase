# import db as con
# import datetime
# # max_primary_d = con.selectData(table='designs', column='max(designid)')
# # print(max_primary_d[0][0])
# # # # TO_DATE'2024-02-27'
# x = datetime.datetime.now()
# # print(x)
# # print(x.strftime('%x'),x.strftime('%X'))
# # print(x.strftime('%X'))
# y = f"{x.strftime('%x')}"
# print(y)
# insert_design = "'2',TO_DATE('%s', 'yyyy/mm/dd')"%(y)
# print(insert_design)
# # print(insert_design)w
# insert_state_design = con.insertData(table='designs', primary_key='5', values=insert_design)
# import streamlit as st
# number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
# st.write('The current number is ', number)

# user_data = con.selectData(table='users', condition=f"name='surapoje'")
# print(user_data)
# print(user_data[0])
# print(user_data[0][0])

s = [1,2,3]
for i in s:
    print(i)