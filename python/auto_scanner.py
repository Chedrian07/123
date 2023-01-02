import pyautogui as auto
import time
import pyperclip

total_page = 777
book_name = 'ebook'
capture_pos = (1230, 104)
ebook_screen_center_pos = (1889, 554)
sleep_time = 0.5

time.sleep(1.)

for i in range(int(total_page/2)):
    file_name = book_name + '_' + str(i+1).zfill(4) + '.png'
    pyperclip.copy(file_name)

    auto.click(capture_pos)
    time.sleep(sleep_time)

    auto.hotkey('ctrl', 'v')
    time.sleep(sleep_time)

    auto.press('enter')
    time.sleep(sleep_time)

    auto.click(ebook_screen_center_pos)
    time.sleep(sleep_time)

    auto.press('right')
    time.sleep(sleep_time)

    print(str(i+1), '/', int(total_page/2))