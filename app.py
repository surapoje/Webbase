import datetime
import streamlit as st
import db as con
from streamlit_extras.stylable_container import stylable_container

if 'login_pass' not in st.session_state:
    st.session_state['login_pass'] = False

if 'username' not in st.session_state:
    st.session_state['username'] = ''
if 'userID' not in st.session_state:
    st.session_state['userID'] = ''
if 'data_detail' not in st.session_state:
    st.session_state['data_detail']=[]
if 'checker' not in st.session_state:
    st.session_state['checker'] = False
if 'checker2' not in st.session_state:
    st.session_state['checker2'] = False

checker = False
checker2 = False
# data_list = []
st.set_page_config(
    page_title="Home-Tae-shirt",
    page_icon="👕",
    layout="wide",
    initial_sidebar_state="expanded"
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

with st.container(border=True):
    col1,col2,col3, col4, col5 = st.columns([1,9,1,1,1])
    with col1:
        # with stylable_container(
        #     key="green_button",
        #     css_styles="""
        #         button{
        #             background-color: transparent;
        #             color: white;
        #             border: 10px;
        #             border-color: azure;
        #             }
        #         """,
        # ):
        if st.session_state.login_pass == True:
            button_4 = st.button('UserInfo',use_container_width=True)
            if button_4:
                st.switch_page("pages/user.py")
        else:
            st.write("")

    with col2:
        st.write("")
    with col3:
        if st.session_state.login_pass == True:
            backet = st.empty()
        else:
            st.write("")


    with col4:
        if st.session_state.login_pass == True:
            st.write('')
            # button_clear = st.button('Clear',use_container_width=True)
        else:
            button_2 = st.button('Register',use_container_width=True)
            if button_2:
                st.switch_page("pages/register.py")
    with col5:
        if st.session_state.login_pass == True:
            st.write('')
            # button_3 = st.button('Order list',use_container_width=True)
            # if button_3:
            #     st.switch_page("pages/Order_list.py")
        else:
            button_1 = st.button('login',use_container_width=True)
            if button_1:
                st.switch_page("pages/login.py")

with st.container(border=True):
    if st.session_state.login_pass == True:
        st.header('%s has login!!'%(st.session_state.username))
    else:
        st.header('Welcome Homie,Please login or register before using PROMP :heart:')
# with st.container(border=True):
#     st.header('')
#     st.header('')
#     st.header('')
with st.container(border=True):
    alert_box = st.empty()
    text_input = st.text_input('Promp:')
    if text_input:
        if st.session_state.login_pass == True:
            st.write("You entered: ", text_input)
            text_input = str(text_input)
            date = datetime.datetime.now()
            print(text_input)
            
            import requests

            API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
            headers = {"Authorization": "Bearer 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"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.content
            image_bytes = query({
                "inputs": text_input,
            })
            # You can access the image with PIL.Image for example
            import io
            from PIL import Image
            image = Image.open(io.BytesIO(image_bytes))
            ratio_1 = 0.25
            out = image.resize([int(ratio_1 * s) for s in image.size])
            print('size_in_web : %s'%(str(out.size)))


            with st.container(border=True):
                col1,col2,col3 = st.columns([1,1,2])
                with col1:
                    st.image(out)
                    with col2:
                        st.image('static/shirt.png')
                        with col3:
                            option_type = st.selectbox(
                                "What's your type?",
                                ('T-shirt', 'polo shirt')
                            )
                            if option_type == 'polo shirt':
                                d = 70
                            else:
                                d = 50
                            option_gender = st.selectbox(
                                "What's your gender?",
                                ('ชาย', 'หญิง'))
                            if option_gender == 'ชาย':
                                option_size_m = st.selectbox(
                                    "What's size do you want?",
                                    ('S', 'M', 'L', 'XL', '2XL', '3XL', '4XL'))
                                if option_size_m == 'S':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('38'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('26'))
                                    with col2:
                                        price = d+100
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_m == 'M':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('40'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('27'))
                                    with col2:
                                        price = d+110
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_m == 'L':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('42'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('28'))
                                    with col2:
                                        price = d+120
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_m == 'XL':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('44'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('29'))
                                    with col2:
                                        price = d+130
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_m == '2XL':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('46'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('30'))
                                    with col2:
                                        price = d+140
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_m == '3XL':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('48'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('31'))
                                    with col2:
                                        price = d+150
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_m == '4XL':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('50'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('32'))
                                    with col2:
                                        price = d+160
                                        st.write('ราคา : %s บาท'%(price))
                            if option_gender == 'หญิง':
                                option_size_f = st.selectbox(
                                    "What's size do you want?",
                                    ('XXS', 'XS', 'S', 'M', 'L', 'XL', '2XL'))
                                if option_size_f == 'XXS':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('31'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('25'))
                                    with col2:
                                        price = d+100
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_f == 'XS':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('33'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('26'))
                                    with col2:
                                        price = d+110
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_f == 'S':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('35'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('27'))
                                    with col2:
                                        price = d+120
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_f == 'M':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('37'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('28'))
                                    with col2:
                                        price = d+130
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_f == 'L':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('39'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('29'))
                                    with col2:
                                        price = d+140
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_f == 'XL':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('41'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('30'))
                                    with col2:
                                        price = d+150
                                        st.write('ราคา : %s บาท'%(price))
                                if option_size_f == '2XL':
                                    col1,col2 = st.columns(2)
                                    with col1:
                                        st.write('รอบอก: %s นิ้ว'%('43'))
                                        st.write('ความยาวตัว: %s นิ้ว'%('31'))
                                    with col2:
                                        price = d+160
                                        st.write('ราคา : %s บาท'%(price))
                            number = st.number_input( 'how many',min_value=1, max_value=10, value=1, step=1)
                            st.write('Total price: %s'%(number*price))
                            col2,col3 = st.columns(2)
                            with col2:
                                b_button = st.button('buy',use_container_width=True)
                                if b_button:
                                    design_name = str(text_input)
                                    y = f"{date.strftime('%x')}"
                                    print(y)
                                    insert_design = "'%s',TO_DATE('%s', 'mm/dd/yy')"%(design_name,y)
                                    max_primary_d = con.selectData(table='designs', column='max(designid)')
                                    max_primary_d = max_primary_d[0][0]
                                    if max_primary_d == None:
                                        max_primary_d = 0
                                    # insert into users values (designid, designname, DESIGNS_DATE);
                                    insert_state_design = con.insertData(table='designs', primary_key=max_primary_d+1, values=insert_design)

                                    gender = option_gender
                                    
                                    if gender == 'ชาย':
                                        size = option_size_m
                                    else:
                                        size = option_size_f
                                    
                                    Type = option_type
                                    # tag = hash(f"'{max_primary_d}', '{Type}', '{gender}','{size}'")
                                    max_pk = con.selectData(table='designs', column='max(designid)')
                                    max_pk = max_pk[0][0]
                                    insert_shirt = f"'{max_pk}', '{Type}', '{gender}','{size}', '{price}', '{max_pk}'"
                                    max_primary_s = con.selectData(table='shirts', column='max(shirtid)')
                                    max_primary_s = max_primary_s[0][0]
                                    if max_primary_s == None:
                                        max_primary_s = 0
                                    # insert into users values (designid, designname, DESIGNS_DATE);
                                    insert_state_shirt = con.insertData(table='shirts', primary_key=max_primary_s+1, values=insert_shirt)
                                    

                                    userid = st.session_state.userID
                                    max_pk_s = con.selectData(table='shirts', column='max(shirtid)')
                                    max_pk_s = max_pk_s[0][0]

                                    insert_order = f"'{userid}', '{max_pk_s}', '{number}','สั่ง', '{number*price}', TO_DATE('{y}', 'mm/dd/yy')"
                                    max_primary_o = con.selectData(table='orders', column='max(orderid)')
                                    max_primary_o = max_primary_o[0][0]
                                    if max_primary_o == None:
                                        max_primary_o = 0
                                    insert_state_order = con.insertData(table='orders', primary_key=max_primary_o+1, values=insert_order)

                                    max_pk_o = con.selectData(table='orders', column='max(orderid)')
                                    max_pk_o = max_pk_o[0][0]

                                    max_primary_sh = con.selectData(table='shipping', column='max(shippingid)')
                                    max_primary_sh = max_primary_sh[0][0]
                                    if max_primary_sh == None:
                                        max_primary_sh = 0
                                    insert_shipping = f"'{max_pk_o}', 'กำลังแพ็คของ', 'ST{max_primary_sh+1}', TO_DATE('{y}', 'mm/dd/yy')"
                                    insert_state_shipping = con.insertData(table='shipping', primary_key=max_primary_sh+1, values=insert_shipping)
                                    if insert_state_design and insert_state_shirt and insert_state_order and insert_shipping:
                                        st.write('complete')
                                        
                                    # if insert_state_design and insert_state_shirt:
                                    #     st.switch_page('pages/cashing.py')

                            with col3:
                                t_button = st.button('backet',use_container_width=True)
                                if t_button:
                                    # st.session_state.checker = False
                                    design_name = str(text_input)
                                    y = f"{date.strftime('%x')}"
                                    print(y)
                                    insert_design = "'%s',TO_DATE('%s', 'mm/dd/yy')"%(design_name,y)
                                    max_primary_d = con.selectData(table='designs', column='max(designid)')
                                    max_primary_d = max_primary_d[0][0]
                                    if max_primary_d == None:
                                        max_primary_d = 0
                                    # insert into users values (designid, designname, DESIGNS_DATE);
                                    insert_state_design = con.insertData(table='designs', primary_key=max_primary_d+1, values=insert_design)
                                    # print(max_primary_d+1,':',insert_design)
                                    gender = option_gender
                                    
                                    if gender == 'ชาย':
                                        size = option_size_m
                                    else:
                                        size = option_size_f
                                    
                                    Type = option_type
                                    # tag = hash(f"'{max_primary_d}', '{Type}', '{gender}','{size}'")
                                    max_pk = con.selectData(table='designs', column='max(designid)')
                                    max_pk = max_pk[0][0]
                                    insert_shirt = f"'{max_pk}', '{Type}', '{gender}','{size}', '{price}', '{max_pk}'"
                                    max_primary_s = con.selectData(table='shirts', column='max(shirtid)')
                                    max_primary_s = max_primary_s[0][0]
                                    if max_primary_s == None:
                                        max_primary_s = 0
                                    # insert into users values (designid, designname, DESIGNS_DATE);
                                    insert_state_shirt = con.insertData(table='shirts', primary_key=max_primary_s+1, values=insert_shirt)
                                    # print(max_primary_s+1,':',insert_shirt)

                                    userid = st.session_state.userID
                                    max_pk_s = con.selectData(table='shirts', column='max(shirtid)')
                                    max_pk_s = max_pk_s[0][0]

                                    insert_order = f"'{userid}', '{max_pk_s}', '{number}','สั่ง', '{number*price}', TO_DATE('{y}', 'mm/dd/yy')"
                                    max_primary_o = con.selectData(table='orders', column='max(orderid)')
                                    max_primary_o = max_primary_o[0][0]
                                    if max_primary_o == None:
                                        max_primary_o = 0
                                    insert_state_order = con.insertData(table='orders', primary_key=max_primary_o+1, values=insert_order)
                                    if insert_state_design and insert_state_shirt and insert_state_order:
                                        st.warning('complete',icon="✅")
                                    data = [max_primary_o+1,out]
                                    st.session_state.data_detail.append(data)
                                    print(st.session_state.data_detail)
                                    # print(max_primary_o,':',insert_order)
                                    # st.session_state.checker = True
                                    checker = True


        else:
            alert_box.warning('Dude,please login...:heart:', icon="⚠️")

if checker == True:
    with st.container(border=True):
        st.header('Backet')
        for i in st.session_state.data_detail:
            print(i)
            uid = con.selectData(table='orders', column='userid',condition=f"orderid = '{i[0]}'")
            sid = con.selectData(table='orders', column='shirtid',condition=f"orderid = '{i[0]}'")
            q = con.selectData(table='orders', column='quantity',condition=f"orderid = '{i[0]}'")
            total = con.selectData(table='orders', column='totalprice',condition=f"orderid = '{i[0]}'")
            date = con.selectData(table='orders', column='orders_date',condition=f"orderid = '{i[0]}'")
            print(uid)
            uid = uid[0][0]#userID
            sid = sid[0][0]#shirtID
            q   =   q[0][0]#quantity
            total = total[0][0]#Total
            date = date[0][0]#date

            did = con.selectData(table='shirts', column='designid',condition=f"shirtid = '{sid}'")
            t = con.selectData(table='shirts', column='type',condition=f"shirtid = '{sid}'")
            sex = con.selectData(table='shirts', column='sex',condition=f"shirtid = '{sid}'")
            s_size = con.selectData(table='shirts', column='shirt_size',condition=f"shirtid = '{sid}'")
            p = con.selectData(table='shirts', column='price',condition=f"shirtid = '{sid}'")

            did = did[0][0]
            t = t[0][0]
            sex = sex[0][0]
            s_size = s_size[0][0]
            p = p[0][0]

            Promp = con.selectData(table='designs', column='designname',condition=f"designid = '{did}'")
            Promp = Promp[0][0]
            
            contrain = st.container(border=True)
            with contrain:
                col = st.columns(3)
                with col[0]:
                    st.image(i[1])
                with col[1]:
                    st.write('Promp:',f'{Promp}')
                    st.write(f'ปี-เดือน-วัน:{date.date()}')
                    # st.write(f'{uid}')
                    st.write(f'Gender:{sex}')
                    st.write('Type:',f'{t}')
                with col[2]:
                    st.write('Size:',f'{s_size}')
                    st.write(f'Quantity:{q}')
                    st.write(f'Total:{total}')
        st.session_state.checker2 = True

if st.session_state.checker2 == True:
    col_fb,col_fd = st.columns(2)
    with col_fb:
        button_b = st.button('buys')
        if button_b:
            orders_1 =[]
            for i in st.session_state.data_detail:
                print('confirm:',i)
                oid_2 = i[0]
                orders_1.append(oid_2)
            y = f"{date.strftime('%x')}"
            # max_primary_sh = con.selectData(table='shipping', column='max(shippingid)')
            # max_primary_sh = max_primary_sh[0][0]
            # if max_primary_sh == None:
            #     max_primary_sh = 0
            for i in orders_1:
                # insert_shipping = f"'{i}', 'กำลังแพ็คของ', 'ST{max_primary_sh+1}', TO_DATE('{y}', 'mm/dd/yy')"
                max_primary_sh = con.selectData(table='shipping', column='max(shippingid)')
                max_primary_sh = max_primary_sh[0][0]
                if max_primary_sh == None:
                    max_primary_sh = 0
                insert_shipping = f"'{i}', 'กำลังแพ็คของ', 'ST{max_primary_sh+1}', TO_DATE('{y}', 'mm/dd/yy')"
                insert_state_shipping = con.insertData(table='shipping', primary_key=max_primary_sh+1, values=insert_shipping)
                if insert_shipping:
                    print(max_primary_sh+1,':',i,':','complete')
                    st.warning('Enjoy with your shirt',icon="✅")
            st.session_state.checker2 = False
            st.session_state.data_detail = []

    with col_fd:
        button_d = st.button('discard')
        if button_d:
            orders = []
            shirts = []
            designs = []
            for i in st.session_state.data_detail:
                oid = i[0]
                orders.append(oid)
                sid = con.selectData(table='orders', column='shirtid',condition=f"orderid = '{i[0]}'")
                sid = sid[0][0]#shirtID
                shirts.append(sid)
                did = con.selectData(table='shirts', column='designid',condition=f"shirtid = '{sid}'")
                did = did[0][0]
                designs.append(did)

            print(orders)
            print(shirts)
            print(designs)
            for i in orders:
                del_order = con.deleteData(table='orders',condition=f"orderid = '{i}'")
                if del_order:
                    print('orderid:',i,'has deleted')
            for i in shirts:
                del_shirts = con.deleteData(table='shirts',condition=f"shirtid = '{i}'")
                if del_shirts:
                    print('shirtid:',i,'has deleted')
            for i in designs:
                del_design = con.deleteData(table='designs',condition=f"designid = '{i}'")
                if del_design:
                    print('designid:',i,'has deleted')
            st.session_state.data_detail = []
            # st.session_state.checker = False
            st.session_state.checker2 = False
            st.warning('Now,Backet is empty',icon="🔥")

                    # del_order = con.deleteData(table='orders',condition=f"orderid = '{oid}'")
                    # del_shirt = con.deleteData(table='shirts',condition=f"orderid = '{sid}'")
                    # del_design = con.deleteData(table='designs',condition=f"orderid = '{did}'")
                    # if del_order and del_shirt and del_design:
                    #     st.write('complete')




        # ratio_2 = 0.2
        # image_t = image_save.resize([int(ratio_2 * s) for s in image_save.size])
        # image_t.show()
        # print('size_out_web : %s'%(str(image_t.size)))


print("kuy")
