from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

keyword = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="erkaklar kiyimi👚"), KeyboardButton(text="texnika")
        ],

    ],
    resize_keyboard=True
)
season = ReplyKeyboardMarkup(
    keyboard=[

        [KeyboardButton(text="qish❄️"), KeyboardButton(text="bahor🍀")],
        [KeyboardButton(text="yoz🌞"), KeyboardButton(text="kuz🌧")],
        [KeyboardButton(text="orqaga")]
    ], resize_keyboard=True
)
####################################################################################################################################################################################
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

key = InlineKeyboardBuilder()
key.row(types.InlineKeyboardButton(text="Camel Classic XL Palto",
                                   url="https://www.kigili.com/kahverengi-klasik-palto-8682607533901/?integration_patern=CAMEL-R&integration_beden=54"))

keyWen = [
    [types.KeyboardButton(text="Palto 🧥"), types.KeyboardButton(text="Etik 🥾")],
    [types.KeyboardButton(text="Qulqop 🧤"), types.KeyboardButton(text="Sharf 🧣")],
    [types.KeyboardButton(text="back")],
]
wenKey = types.ReplyKeyboardMarkup(keyboard=keyWen, resize_keyboard=True)

shopKey = InlineKeyboardBuilder()
shopKey.row(types.InlineKeyboardButton(
    text="Camel Classic XL Palto",
    url="https://www.kigili.com/kahverengi-klasik-palto-8682607533901/?integration_patern=CAMEL-R&integration_beden=54"
))

shopKeys = InlineKeyboardBuilder()
shopKeys.row(types.InlineKeyboardButton(
    text="shoes", url="https://www.ebay.ca/itm/403984453609"
))

shopGloves = InlineKeyboardBuilder()
shopGloves.row(types.InlineKeyboardButton(
    text="gloves", url="https://shopee.com.my/Leather-Gloves-Motorcycle-Gloves-i.252842748.8165358776"
))

shopscarf = InlineKeyboardBuilder()
shopscarf.row(types.InlineKeyboardButton(
    text="scarf", url="https://www.amazon.com/GERINLY-Cotton-Linen-Scarves-Stripe-Crinkle/dp/B075S7GN5M"
))
###################################################################################################################################################################################################################

spring = [
    [types.KeyboardButton(text="jacket🧥"), types.KeyboardButton(text="shoes👟")],
    [types.KeyboardButton(text="pants👖"), types.KeyboardButton(text="ko'ylak👕")],
    [types.KeyboardButton(text="back")],
]
shopSpring = types.ReplyKeyboardMarkup(keyboard=spring, resize_keyboard=True)

spring_shops = InlineKeyboardBuilder()
spring_shops.row(types.InlineKeyboardButton(
    text="jackets",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=spring+jac&_sacat=0&LH_TitleDesc=0&_odkw=jacket+men&_osacat=0"
))

spring_shops_s = InlineKeyboardBuilder()
spring_shops_s.row(types.InlineKeyboardButton(
    text="shoes",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311&_nkw=spring+shoes&_sacat=0&LH_TitleDesc=0&_odkw=spring+jac&_osacat=0"
))

spring_shops_s_s = InlineKeyboardBuilder()
spring_shops_s_s.row(types.InlineKeyboardButton(
    text="pants",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=spring+pants+&_sacat=0&LH_TitleDesc=0&_odkw=pants+men&_osacat=0"
))

spring_shops_s_s_s = InlineKeyboardBuilder()
spring_shops_s_s_s.row(types.InlineKeyboardButton(
    text="shirt",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=spring+shirt&_sacat=0&LH_TitleDesc=0&_odkw=spring+pants+&_osacat=0"
))
################################################################################################################################################################################

sum_me = [
    [types.KeyboardButton(text="cap🧢"), types.KeyboardButton(text="t-shirt👕")],
    [types.KeyboardButton(text="short🩳"), types.KeyboardButton(text="shoes")],
    [types.KeyboardButton(text="back")],
]
summer = types.ReplyKeyboardMarkup(keyboard=sum_me, resize_keyboard=True)

summer_shops = InlineKeyboardBuilder()
summer_shops.row(types.InlineKeyboardButton(
    text="caps",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=summer+cap&_sacat=0&LH_TitleDesc=0&_odkw=spring+shirt&_osacat=0"
))

summer_shops_s = InlineKeyboardBuilder()
summer_shops_s.row(types.InlineKeyboardButton(
    text="T-shirts",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l2632&_nkw=summer+t+shirts+for+men&_sacat=1059&LH_TitleDesc=0&_odkw=summer+cap&_osacat=0"
))

summer_shops_s_s = InlineKeyboardBuilder()
summer_shops_s_s.row(types.InlineKeyboardButton(
    text="shorts",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=summer+short&_sacat=1059&LH_TitleDesc=0&_odkw=summer+t+shirts+for+men&_osacat=1059"
))

summer_shops_s_s_s = InlineKeyboardBuilder()
summer_shops_s_s_s.row(types.InlineKeyboardButton(
    text="shoes",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311&_nkw=summer+sandals+for+men&_sacat=0&LH_TitleDesc=0&_odkw=summer+shoes&_osacat=1059"
))
################################################################################################################################################################################
au_tum = [
    [types.KeyboardButton(text="shirt👚"), types.KeyboardButton(text="pants👖")],
    [types.KeyboardButton(text="headdress🧢"), types.KeyboardButton(text="autumn jacket🧥")],
    [types.KeyboardButton(text="back")],
]
autumn = types.ReplyKeyboardMarkup(keyboard=au_tum, resize_keyboard=True)

autumn_shops = InlineKeyboardBuilder()
autumn_shops.row(types.InlineKeyboardButton(
    text="shirts",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=autumn+shirt+for+men&_sacat=0&LH_TitleDesc=0&_odkw=embroidered+shirts+women+fall+autumn&_osacat=0"
))

autumn_shops_s = InlineKeyboardBuilder()
autumn_shops_s.row(types.InlineKeyboardButton(
    text="pants",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=autumn+pANTS&_sacat=0&LH_TitleDesc=0&_odkw=autumn+shirt+for+men&_osacat=0"
))

autumn_shops_s_s = InlineKeyboardBuilder()
autumn_shops_s_s.row(types.InlineKeyboardButton(
    text="headdress",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=cap&_sacat=0&LH_TitleDesc=0&_odkw=autumn+headdress+for+men&_osacat=0"
))

autumn_shops_s_s_s = InlineKeyboardBuilder()
autumn_shops_s_s_s.row(types.InlineKeyboardButton(
    text="autumn jacket",
    url="https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311&_nkw=autumn+jacket+for+men&_sacat=0&LH_TitleDesc=0&_odkw=cap&_osacat=0"
))




###############################################################TEXNIKA######################################################################################################

technique=[
    [types.KeyboardButton(text="iphone📱"), types.KeyboardButton(text="laptop💻")],
    [KeyboardButton(text="orqaga")]
]
technique_s = types.ReplyKeyboardMarkup(keyboard=technique, resize_keyboard=True)

iphone_s=[
    [types.KeyboardButton(text="iphone 15 pro max📱"), types.KeyboardButton(text="iphone 14 pro max📱")],
    [types.KeyboardButton(text="iphone 13 pro max📱"), types.KeyboardButton(text="iphone 12 pro max📱")],
    [types.KeyboardButton(text="iphone 11 pro max📱"), types.KeyboardButton(text="iphone xs  max📱")],
    [types.KeyboardButton(text="iphone 15 pro 📱"), types.KeyboardButton(text="iphone x📱"),types.KeyboardButton(text='⬅️back⬅️')],
    # [types.KeyboardButton(text="⬅️back⬅️")]

]
iphones_s= types.ReplyKeyboardMarkup(keyboard=iphone_s, resize_keyboard=True)

iphone_s_s = InlineKeyboardBuilder()
iphone_s_s.row(types.InlineKeyboardButton(
    text="iphone 15 pro max",
    url="https://t.me/Applemarketuzbb"))

iphone_s_s_s= InlineKeyboardBuilder()
iphone_s_s_s.row(types.InlineKeyboardButton(
    text="iphone 14 pro max",
    url="https://t.me/Applemarketuzbb"))

iphone_s_s_s_s= InlineKeyboardBuilder()
iphone_s_s_s_s.row(types.InlineKeyboardButton(
    text="iphone 13 pro max",
    url="https://t.me/Applemarketuzbb"))

iphone_s_s_s_s_s= InlineKeyboardBuilder()
iphone_s_s_s_s_s.row(types.InlineKeyboardButton(
    text="iphone 12 pro max",
    url="https://t.me/Applemarketuzbb"))

iphone_s_s_s_s_s_s= InlineKeyboardBuilder()
iphone_s_s_s_s_s_s.row(types.InlineKeyboardButton(
    text="iphone 11 pro max",
    url="https://t.me/Applemarketuzbb"))

iphone_s_s_s_s_s_s_s= InlineKeyboardBuilder()
iphone_s_s_s_s_s_s_s.row(types.InlineKeyboardButton(
    text="iphone  xs max",
    url="https://t.me/Applemarketuzbb"))

iphone_s_s_s_s_s_s_s_s= InlineKeyboardBuilder()
iphone_s_s_s_s_s_s_s_s.row(types.InlineKeyboardButton(
    text="iphone 15 pro ",
    url="https://t.me/Applemarketuzbb"))

iphone_s_s_s_s_s_s_s_s_s= InlineKeyboardBuilder()
iphone_s_s_s_s_s_s_s_s_s.row(types.InlineKeyboardButton(
    text="iphone x ",
    url="https://t.me/Applemarketuzbb"))

##############laptop///////////////////////////////////////////////////////////////////laptop////////////////////////////////////////////////////////////////////////////
laptop_s=[
    [types.KeyboardButton(text="macbook air m1💻"), types.KeyboardButton(text="HP💻")],
    [types.KeyboardButton(text="lenova💻"), types.KeyboardButton(text="asus💻")],
[types.KeyboardButton(text="⬅️back⬅️")]
]
laptop = types.ReplyKeyboardMarkup(keyboard=laptop_s, resize_keyboard=True)

lenova= InlineKeyboardBuilder()
lenova.row(types.InlineKeyboardButton(
    text="lenova ",
    url="https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText=lenova&isPremium=y&secondFlag=true&tagScene=search"))

macbooks= InlineKeyboardBuilder()
macbooks.row(types.InlineKeyboardButton(
    text="macbook air m1💻",
    url="https://www.apple.com/uz/macbook-air-m1/"))

hp= InlineKeyboardBuilder()
hp.row(types.InlineKeyboardButton(
    text="HP",
    url="https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText=hp+core+i7&isPremium=y&secondFlag=true&tagScene=search"))

asus= InlineKeyboardBuilder()
asus.row(types.InlineKeyboardButton(
    text="asus 💻",
    url="https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText=asus&isPremium=y&secondFlag=true&tagScene=search"))


