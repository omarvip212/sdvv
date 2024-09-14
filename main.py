import logging
import requests
from pytube import YouTube
from telegram import Update
from telegram.ext import Application, CommandHandler
from info import BOT_TOKEN, START_MESSAGE, HELP_MESSAGE, COMMANDS, RAPIDAPI_URL, RAPIDAPI_HOST, RAPIDAPI_KEY
import io
import json

# إعداد التسجيل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# وظائف تحميل الملفات
async def download_file(url: str, context: Update):
    try:
        response = requests.get(url)
        response.raise_for_status()  # تحقق من نجاح الطلب   
        return io.BytesIO(response.content)
    except Exception as e:
        await context.message.reply_text(f"حدث خطأ أثناء تحميل الملف: {str(e)}")
        return None

async def download_video(update: Update, context):
    if context.args:
        channel_id = "UCeY0bbntWzzVIaj2z3QigXg"  # معرف القناة
        video_url = context.args[0]  # رابط الفيديو المرسل
        try:
            headers = {
                "x-rapidapi-host": RAPIDAPI_HOST,
                "x-rapidapi-key": RAPIDAPI_KEY
            }
            params = {
                "channelId": channel_id,
                "type": "videos",
                "sortBy": "newest"
            }
            response = requests.get(RAPIDAPI_URL, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                if 'items' in data and len(data['items']) > 0:
                    video_info = data['items'][0]
                    video_download_url = video_info.get('url')  # تأكد من أن هذا هو المفتاح الصحيح
                    if video_download_url:
                        await update.message.reply_text(f"تم العثور على الفيديو. الرابط: {video_download_url}")
                    else:
                        await update.message.reply_text("تم العثور على معلومات الفيديو ولكن الرابط غير متوفر.")
                else:
                    await update.message.reply_text("لم يتم العثور على معلومات الفيديو في الاستجابة.")
            else:
                await update.message.reply_text(f"حدث خطأ في الاستجابة: {response.status_code}\n{response.text}")
        except Exception as e:
            await update.message.reply_text(f"حدث خطأ أثناء معالجة الطلب: {str(e)}")
    else:
        await update.message.reply_text("الرجاء إدخال رابط الفيديو لتحميله.")

async def download_image(update: Update, context):
    if context.args:
        url = context.args[0]
        image_bytes = await download_file(url, update)
        if image_bytes:
            await update.message.reply_photo(photo=image_bytes)
        else:
            await update.message.reply_text("لم يتم تحميل الصورة.")
    else:
        await update.message.reply_text("الرجاء إدخال رابط الصورة لتحميلها.")

# إضافة معالج لبدء المحادثة
async def start(update: Update, context):
    await update.message.reply_text(START_MESSAGE)

# إضافة معالج لمساعدة المستخدم
async def help_command(update: Update, context):
    await update.message.reply_text(HELP_MESSAGE)

# الوظيفة الرئيسية
def main():
    # إنشاء التطبيق وإضافة المعالجات
    application = Application.builder().token(BOT_TOKEN).build()

    # إضافة معالج لتحميل الفيديو
    application.add_handler(CommandHandler("download_video", download_video))
    # إضافة معالج لتحميل الصورة
    application.add_handler(CommandHandler("download_image", download_image))
    
    # إضافة المعالجات الأخرى
    application.add_handler(CommandHandler("start", start))  # start
    application.add_handler(CommandHandler("help", help_command))  # help_command

    # بدء التطبيق
    application.run_polling()  # إضافة هذه السطر لتشغيل التطبيق

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
