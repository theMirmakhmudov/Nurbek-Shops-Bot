import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import *
from buttons import *

TOKEN = token

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f" {message.from_user.first_name} salom sizga qanday yordam ber olman agar shopga kirmoqch bo'lsangiz /shop tugmasini bosing.")
    print(message.from_user.first_name)


@dp.message(Command("shop"))
async def shop(message: Message):
    await message.answer(f" {message.from_user.first_name} shop turini tanlang", reply_markup=keyword)

    @dp.message(F.text == "erkaklar kiyimi👚")
    async def keyimlar(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/upbBmapdjXNvU1im8", caption="my shop",
                                   reply_markup=season)

        @dp.message(F.text == "orqaga")
        async def palt(message: Message):
            await message.answer("tanlang", reply_markup=keyword)

        @dp.message(F.text == "qish❄️")
        async def qish(mes: Message):
            await mes.answer_photo(photo="https://images.app.goo.gl/2JjuhuBUpqTmNdJq8", caption="my shop",
                                   reply_markup=wenKey)

            @dp.message(F.text == "back")
            async def palt(message: Message):
                await message.answer("tanlang", reply_markup=season)

    @dp.message(F.text == "Palto 🧥")
    async def palto(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/LxHrLfZFvyZbGSZw6",
                                   caption="Camel Klasik Palto\n500 USD 💵\nMan clothse: 50/M Boy: 188 cm\nsize: 98 cm Bel: 85 cm Basen: 99 cm",
                                   reply_markup=shopKey.as_markup())

    @dp.message(F.text == "Etik 🥾")
    async def etik(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/images/g/7gsAAOSwUkJjafsg/s-l500.png",
                                   caption="man's shoes\nsize40,41,42,43", reply_markup=shopKeys.as_markup())

    @dp.message(F.text == "Qulqop 🧤")
    async def qolqop(message: Message):
        await message.answer_photo(photo="https://down-my.img.susercontent.com/file/76bb3892ac78629977115524f3f0cf1c",
                                   caption="man gloves\nnarx30$", reply_markup=shopGloves.as_markup())

    @dp.message(F.text == "Sharf 🧣")
    async def scarf(message: Message):
        await message.answer_photo(photo="https://m.media-amazon.com/images/I/81GNdnAjGMS._AC_SX679_.jpg",
                                   caption="scarf\nfor men\nnarx-15$", reply_markup=shopscarf.as_markup())

    @dp.message(F.text == "bahor🍀")
    async def bahor(mes: Message):
        await mes.answer_photo(
            photo="https://cdn.britannica.com/05/155405-050-F8969EE6/Spring-flowers-fruit-trees-bloom.jpg",
            caption="my shop",
            reply_markup=shopSpring)

        @dp.message(F.text == "back")
        async def palt(message: Message):
            await message.answer("tanlang", reply_markup=season)

    @dp.message(F.text == "jacket🧥")
    async def jacket(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/images/g/eWwAAOSwZmNjv3X~/s-l500.jpg",
                                   caption="size 40,41,42\nnarxi-21%", reply_markup=spring_shops.as_markup())

        @dp.message(F.text == "shoes👟")
        async def shoesSpring(message: Message):
            await message.answer_photo(photo="https://i.ebayimg.com/thumbs/images/g/~UAAAOSwMmZlVEQo/s-l300.webp",
                                       caption="size 40,41,42\n\nnarx-40$", reply_markup=spring_shops_s.as_markup())

            @dp.message(F.text == "pants👖")
            async def pants(message: Message):
                await message.answer_photo(photo="https://i.ebayimg.com/images/g/wiYAAOSwA-NlLgxy/s-l1600.jpg",
                                           caption="size 50,51,43,52,3,2,43\n\n narx-4$",
                                           reply_markup=spring_shops_s_s.as_markup())

    @dp.message(F.text == "ko'ylak👕")
    async def koylak(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/thumbs/images/g/FcwAAOSwjEhk-DmQ/s-l300.webp",
                                   caption="size all\n\n narx-10$", reply_markup=spring_shops_s_s_s.as_markup())

    @dp.message(F.text == "yoz🌞")
    async def yoz(mes: Message):
        await mes.answer_photo(
            photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl9XmncHKZzwjaa1li1OWq0rDYHdMpewL1CzDI2AXnvQ&s",
            caption="my shop", reply_markup=summer)

        @dp.message(F.text == "back")
        async def palt(message: Message):
            await message.answer("tanlang", reply_markup=season)

    @dp.message(F.text == "cap🧢")
    async def jacket_t(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/thumbs/images/g/ouoAAOSw~8Jkw7ns/s-l300.webp",
                                   caption="size all\n\nnarx-21$", reply_markup=summer_shops.as_markup())

    @dp.message(F.text == "t-shirt👕")
    async def jacket(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/thumbs/images/g/KnMAAOSwLvNlDJn0/s-l300.webp",
                                   caption="size all \n\nnarx-30$", reply_markup=summer_shops_s.as_markup())

    @dp.message(F.text == "short🩳")
    async def jacket(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/thumbs/images/g/ip0AAOSwFrdkavJA/s-l300.webp",
                                   caption="size all \n\nnarx:10$", reply_markup=summer_shops_s_s.as_markup())

    @dp.message(F.text == "shoes")
    async def jacket(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/thumbs/images/g/cBEAAOSw5VNahNGH/s-l300.webp",
                                   caption="size 40,41,42\n\nnarx: 12$", reply_markup=summer_shops_s_s_s.as_markup())

    @dp.message(F.text == "kuz🌧")
    async def kuz(mes: Message):
        await mes.answer_photo(
            photo="https://assets.website-files.com/620e6fc20903c76d73735e50/633d7f6ce2cd6b44d7876461_Autumn%20PD%20Blog.jpg",
            caption="my shop", reply_markup=autumn)

        @dp.message(F.text == "back")
        async def palt(message: Message):
            await message.answer("tanlang", reply_markup=season)

    @dp.message(F.text == "autumn jacket🧥")
    async def jacket_t(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/images/g/0DsAAOSweC1hwNIy/s-l500.jpg",
                                   caption="size all\n\nnarx:13$", reply_markup=autumn_shops_s_s_s.as_markup())

    @dp.message(F.text == "shirt👚")
    async def jacket_s(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/thumbs/images/g/RuEAAOSw7tBjRcsr/s-l300.webp",
                                   caption="size all\n\nnarx:26$", reply_markup=autumn_shops.as_markup())

    @dp.message(F.text == "pants👖")
    async def jacket_q(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/thumbs/images/g/uN0AAOSw70lk4zND/s-l300.webp",
                                   caption="size all\n\nnarx:11$", reply_markup=autumn_shops_s.as_markup())

    @dp.message(F.text == "headdress🧢")
    async def jacket_d(message: Message):
        await message.answer_photo(photo="https://i.ebayimg.com/thumbs/images/g/x~gAAOSwTN1lDnNq/s-l300.webp",
                                   caption="size all\n\nnarx:10$", reply_markup=autumn_shops_s_s.as_markup())

    @dp.message(F.text == "texnika")
    async def texnika(message: Message):
        await message.answer_photo(
            photo="https://static1.tgstat.ru/channels/_0/2c/2c8ce211e1ca3397dcfbb2a479086077.jpg", caption="my shop",
            reply_markup=technique_s)

        @dp.message(F.text == "orqaga")
        async def palt(message: Message):
            await message.answer("tanlang", reply_markup=keyword)

    @dp.message(F.text == "iphone📱")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://support.apple.com/library/content/dam/edam/applecare/images/en_US/iphone/iphone-14-pro-max-colors.png",
            caption="my phone", reply_markup=iphones_s)

        @dp.message(F.text == "⬅️back⬅️")
        async def palt(message: Message):
            await message.answer("tanlang", reply_markup=technique_s)

    @dp.message(F.text == "iphone 15 pro max📱")
    async def iphone(message: Message):
        await message.answer_photo(photo="https://applegod.ru/wp-content/uploads/2023/10/mt233.jpg",
                                   caption="iphone 15 pro max\n512gb\n2023 yil\nnarxi:2000$",
                                   reply_markup=iphone_s_s.as_markup())

    @dp.message(F.text == "iphone 14 pro max📱")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://assets.swappie.com/cdn-cgi/image/width=600,height=600,fit=contain,format=auto/swappie-iphone-14-pro-max-deep-purple-back.png?v=40",
            caption="iphone 14 pro max\n512gb \m2022-yil\narxi:1300$", reply_markup=iphone_s_s_s.as_markup())

    @dp.message(F.text == "iphone 13 pro max📱")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://mini-io-api.texnomart.uz/catalog/product/968/96806/175896/548bcc51-3dbe-4241-ba8a-321de51c89bd.jpg",
            caption="iphone 13 pro max\n256gb\n2022-yil\nnarxi:1000$", reply_markup=iphone_s_s_s_s.as_markup())

    @dp.message(F.text == "iphone 12 pro max📱")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://kattabozor.s3.eu-central-1.amazonaws.com/ri/2f9cb57abead1bc02d13ce9fba1646cea490fea50e2e2fee1487546c4b3fcd47_x67M1g_480l.jpg",
            caption="iphone 12 pro max\n256gb\n2022-yil\nnarxi:800$", reply_markup=iphone_s_s_s_s_s.as_markup())

    @dp.message(F.text == "iphone 11 pro max📱")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://assets.swappie.com/cdn-cgi/image/width=600,height=600,fit=contain,format=auto/swappie-iphone-11-pro-max-midnight-green-back.png?v=40",
            caption="iphone 11 pro max\n256gb\n2022-yil\nnarxi:600$", reply_markup=iphone_s_s_s_s_s_s.as_markup())

    @dp.message(F.text == "iphone xs  max📱")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://olcha.uz/image/600x600/products/2018-11-21/apple-iphone-xs-max-512gb-grey-1-6299-0.jpg",
            caption="iphone xs max\n256gb\n2021-yil\nnarxi:400$", reply_markup=iphone_s_s_s_s_s_s_s.as_markup())

    @dp.message(F.text == "iphone x📱")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://olcha.uz/image/400x400/products/2018-09-14/apple-iphone-x-256gb-silver-5049-2.jpg",
            caption="iphone x\n256gb\n2020-yil\nnarxi:350$", reply_markup=iphone_s_s_s_s_s_s_s_s_s.as_markup())

    @dp.message(F.text == "iphone 15 pro 📱")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://twigo.ru/center/iblock/e54/7ufptps8aii2bvvz5udegdbr0iq674t3/z40qdsp954f0hyp06y052u2z3vdiywfw.jpeg",
            caption="iphone 15 pro\n256gb\n2023-yil\nnarxi:1600$", reply_markup=iphone_s_s_s_s_s_s_s.as_markup())

    ##############laptop///////////////////////////////////////////////////////////////////laptop/////////////////////////////////////////////////////////////////////////////
    @dp.message(F.text == "laptop💻")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiEsE6uFc87_TrIEeGsSYdGPYBcs9g9hik5A&usqp=CAU",
            caption="my laptop", reply_markup=laptop)

        @dp.message(F.text == "⬅️back⬅️")
        async def palt(message: Message):
            await message.answer("tanlang", reply_markup=technique_s)

    ####################laptops######################laptops#/////////////////////////////////////////////////////////////////////////////////////////////
    @dp.message(F.text == "macbook air m1💻")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://frankfurt.apollo.olxcdn.com/v1/files/9f6rs8wukv833-UZ/image;s=1024x576",
            caption="macbok air m1\n512gb\16 operativka\n2023-yil\nnarxi:3000$", reply_markup=macbooks.as_markup())

    @dp.message(F.text == "HP💻")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://main.mobilezone.uz/product-attachment/1/0OhS2urgntM93AGI5qZKoceBbWSlQI0Z.jpg",
            caption="hp core i7\n1tb\n16operativka\n2023-yil\nnarxi:800$", reply_markup=hp.as_markup())

    @dp.message(F.text == "lenova💻")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://assets.asaxiy.uz/product/items/desktop/c4ca4238a0b923820dcc509a6f75849b2023092916392780118RzfzaTcWRB.jpg.webp",
            caption="lenova core i7\n1tb\n8 opretivka\nyil-2023\nnarxi:700$", reply_markup=lenova.as_markup())

    @dp.message(F.text == "asus💻")
    async def iphone(message: Message):
        await message.answer_photo(
            photo="https://notebook.uz/wa-data/public/shop/products/55/21/2155/images/5479/5479.970.jpg",
            caption="asus\n512gb\n8 operativka\n2023-yil\nnarxi:600$", reply_markup=asus.as_markup())


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
