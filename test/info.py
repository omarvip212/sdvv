# معلومات البوت
BOT_TOKEN = "7408799052:AAHFLjxTqfL8811SnaIG0wyqN3E-O9pVLiE"

# إضافة معلومات API
RAPIDAPI_URL = "https://youtube-media-downloader.p.rapidapi.com/v2/channel/videos"
RAPIDAPI_HOST = "youtube-media-downloader.p.rapidapi.com"
RAPIDAPI_KEY = "702b49178amsh7c5f598769425e8p1ebb48jsn07301b7728a0"  # استبدل هذا بمفتاح API الخاص بك من RapidAPI

# رسائل البوت
START_MESSAGE = "مرحبًا! أنا بوت بسيط. كيف يمكنني مساعدتك اليوم؟"
HELP_MESSAGE = """
يمكنني الاستجابة للأوامر التالية:
- /start: بدء المحادثة
- /help: عرض هذه الرسالة
- /echo [نص]: تكرار النص الذي تكتبه
- /music: إذا كنت تريد تشغيل الموسيقى، أخبرني بالموسيقى التي تريد تشغيلها
- /video: إذا كنت تريد تشغيل فيديو، أخبرني بالفيديو الذي تريد تشغيله
- /download_video [رابط]: تحميل فيديو من الرابط المقدم.
- /download_image [رابط]: تحميل صورة من الرابط المقدم.
- /upload [ملف]: إذا كنت تريد رفع ملف، أخبرني بالملف الذي تريد رفعه
- /delete [ملف]: إذا كنت تريد حذف ملف، أخبرني بالملف الذي تريد حذفه
- /resize_image [عرض] [ارتفاع]: لتغيير حجم الصورة. استخدم: /resize_image [عرض] [ارتفاع]
- /delete_message: حذف رسالة بالرد عليها بهذا الأمر.
- /ban_user [معرف_المستخدم]: حظر مستخدم من المجموعة. استخدم: /ban_user [معرف_المستخدم]
- /unban_user [معرف_المستخدم]: إلغاء حظر مستخدم من المجموعة. استخدم: /unban_user [معرف_المستخدم]
- /restrict_user [معرف_المستخدم]: تقييد مستخدم في المجموعة. استخدم: /restrict_user [معرف_المستخدم]
- /kick_user [معرف_المستخدم]: طرد مستخدم من المجموعة. استخدم: /kick_user [معرف_المستخدم]
- /mute [معرف_المستخدم]: كتم صوت مستخدم في المجموعة. استخدم: /mute [معرف_المستخدم]
- /unmute [معرف_المستخدم]: إلغاء كتم صوت مستخدم في المجموعة. استخدم: /unmute [معرف_المستخدم]
- /check_links: التحقق من الروابط في رسائل المجموعة.
"""

# أوامر البوت
COMMANDS = {
    "start": "Start the conversation",
    "help": "Display this message",
    "echo": "Repeat the text you type",
    "music": "If you want to play music, tell me the music you want to play",
    "video": "If you want to play a video, tell me the video you want to play",
    "download_video": "Download a video from the provided URL.",
    "download_image": "Download an image from the provided URL.",
    "upload": "If you want to upload a file, tell me the file you want to upload",
    "delete": "If you want to delete a file, tell me the file you want to delete",
    "resize_image": "To resize an image. Use: /resize_image [width] [height]",
    "delete_message": "Delete a message by replying to it with this command.",
    "ban_user": "Ban a user from the group. Use: /ban_user [user_id]",
    "unban_user": "Unban a user from the group. Use: /unban_user [user_id]",
    "restrict_user": "Restrict a user in the group. Use: /restrict_user [user_id]",
    "kick_user": "Kick a user from the group. Use: /kick_user [user_id]",
    "mute": "Mute a user in the group. Use: /mute [user_id]",
    "unmute": "Unmute a user in the group. Use: /unmute [user_id]",
    "check_links": "Check for links in the group messages.",
}

# إضافة إعدادات لتشغيل البوت في المجموعات
GROUP_CHAT_ID = -1002430439953  # استبدل هذا بمعرف المجموعة الخاصة بك