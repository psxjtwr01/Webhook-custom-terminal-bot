from urllib.request import Request, urlopen
import json
import os
import subprocess
import time

testing = False
webhook_url = "webhook here"

if testing == True:
    webhook_url = "webhook here"


def clear():
    os.system("cls")


class BOT:
    def __init__(self, name, webhook_url, avurl):
        self.username = name
        self.message = ""
        self.webhook_url = webhook_url
        self.payload = {
            "content": self.message,
            "username": self.username,
            "avatar_url": avurl,
        }

    def send_message(self, message):
        self.payload["content"] = message
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        }

        req = Request(
            self.webhook_url,
            data=json.dumps(self.payload).encode(),
            headers=self.headers,
        )
        try:
            urlopen(req)
        except Exception as e:
            print("Error",e,"Has occured")

    def changename(self, username):
        self.username = username
        if username is not None:
            self.payload["username"] = username

    def change_webhook(self, newurl):
        if self.webhook_url != newurl:
            with open("webhook.txt", "w") as f:
                f.write("")
                f.write(newurl)
            self.webhook_url = newurl
        else:
            print("Webhooks are the same")

    def change_avatar(self, avatar_url):
        self.payload["avatar_url"] = avatar_url

    def HELP():
        BOT.send_message(
            "CMDS, send_message, changename, change_avatar, change_webhook"
        )


bot = BOT(
    "Simple ur pimple", webhook_url, avurl="https://i.imgur.com/glghDdR.jpeg"
)  # sets the profile picture
bot.changename("Shxdow Bot")
f = True
while f:
    message = input("Enter message: ")
    cmds = [
        "--help",
        "--change name",
        "--change webhook",
        "--change avatar",
        "--calculator",
        "--m",
        "--run py",
        "--quit",
    ]
    prefix = "--"
    if "--" in message:
        command = (
            True  # checks if the message has -- in it which means that it is a command
        )
    else:
        command = False
    if not command:
        bot.send_message(message)
        clear()
        time.sleep(0.50)
        print("sent")
        time.sleep(1)
        clear()
    if command:
        if message == cmds[0]:
            clear()
            print(cmds)
            input("\nPress enter to continue")
            clear()
        elif message == cmds[1]:
            clear()
            bot.changename(input("New username: "))
        elif message == cmds[2]:
            bot.change_webhook(input("Paste in the new url: "))
            try:
                bot.send_message("Webhook url updated succesfully")
                print("Success")
            except:
                print("Failed try with a diffrent url")
        elif message == cmds[3]:
            bot.change_avatar(input("What is the url?: "))
            print("changed avatar (may take a second to load if correct url)")
            time.sleep(1)
            clear()
        elif message == cmds[4]:
            e = input("what is the math equation you want to solve:")
            bot.send_message(e)
            bot.send_message(eval(e))

        elif message == cmds[5]:
            id = input("What is the user id of the person you want to mention: ")
            message = input(
                "What is the message you want to send(use - instead of @): "
            )
            full_message = ""
            x = 0
            for char in message:
                if char != "-":
                    full_message = full_message + f"{char}"
                elif char == "-":
                    if x != 1:
                        full_message = full_message + f"<@{id}>"
                        x = 1
            bot.send_message(full_message)

    elif message == cmds[6]:
        filename = input("What is the file name: ")
        if filename.endswith(".py"):
            with open(filename, "r") as f:
                code = f.read()
                completed_process = subprocess.run(
                    ["python", "-c", code], capture_output=True, text=True
                )
                output = completed_process.stdout.strip()
            bot.send_message(f"***```py\n{code}\n```***")
            bot.send_message(f"***```md\n{output}\n```***")
        else:
            output = exec(filename)
            code = filename
            bot.send_message(f"***```py\n{code}\n```***")
            bot.send_message(f"***```md\n{output}\n```***")

    elif message == cmds[7]:
        bot.send_message("QUITING")
        print("BOT QUITTING") 
        quit()
    else:
        raise ModuleNotFoundError("This command does not exist please try again")

# by Daddy Drexxy 
# => This is version 1.5
