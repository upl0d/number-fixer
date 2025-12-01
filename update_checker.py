import requests
def checkUpdate(version_label,print_info):

    with open("version.txt", "r") as f:
        current_version = f.read().split('"')[1]
    urlVersion = requests.get("https://raw.githubusercontent.com/upl0d/number-fixer/main/version.txt")
    if not urlVersion.status_code == 200:
        version_label.config(text="Error connection")
        return
    latest_version = urlVersion.text.split('"')[1]
    if latest_version > current_version:
        version_label.config(text=f"Update Available: {latest_version}")
        updateMain(print_info)
    else:
        version_label.config(text=f"Up-to-date: {current_version}")
def updateMain(print_info):
    urlMain = requests.get("https://raw.githubusercontent.com/upl0d/number-fixer/main/main.py")
    if urlMain.status_code == 200:
        with open("main_new.py", "w", encoding="utf-8") as f:
            f.write(urlMain.text)
        print_info("تم تنزيل النسخة الجديدة من main.py")
    else:
        print_info(f"فشل التنزيل، رمز الخطأ: {urlMain.status_code}")