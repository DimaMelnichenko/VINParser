import keyboard
import tkinter as tk
import DragScreenshot as dshot
import pyperclip
import OCRparse as ocrparse

file_name = "save.png"

# Функция, которая будет вызвана при нажатии alt+z
def on_activate_a():
    print("Горячая клавиша alt+z нажата!")
    root = tk.Tk()
    app = dshot.DragScreenshotPanel(root, file_name, 1.25)
    app.start()
    root.mainloop()
    pyperclip.copy( ocrparse.get_parsed_text() )


if __name__ == '__main__':
    # Регистрируем горячую клавишу alt+z
    keyboard.add_hotkey('alt+z', on_activate_a)


    print("Слушатель запущен. Нажмите alt+z для парсинга или Ctrl+Shift+X для выхода.")

    # Блокируем выполнение программы, чтобы скрипт не завершался
    keyboard.wait('ctrl+shift+x')