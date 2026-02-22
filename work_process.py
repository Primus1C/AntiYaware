import pyautogui
import pygetwindow as gw
import random
import time
import os

# Защита: мышь в угол экрана для остановки
pyautogui.FAILSAFE = True

# Имя нашего файла, чтобы скрипт его игнорировал
MY_NAME = "work_process.py"

def smart_mimic():
    print(f"--- work_process запущен (Игнорирую окно: {MY_NAME}) ---")
    
    actions_count = 1

    try:
        while True:
            # Выбираем действие
            action = random.choice(['move', 'scroll', 'switch_all'])
            
            if action == 'move':
                x, y = random.randint(100, 1000), random.randint(100, 700)
                pyautogui.moveTo(x, y, duration=random.uniform(0.7, 1.5))
            #    print(f"[{actions_count}] Движение мыши")

            elif action == 'scroll':
                amount = random.randint(-400, 400)
                pyautogui.scroll(amount)
            #    print(f"[{actions_count}] Скроллинг")

            elif action == 'switch_all':
                # Получаем список всех видимых окон
                all_windows = gw.getAllWindows()
                # Фильтруем: только те, у которых есть заголовок, и это не наш скрипт, и не рабочий стол
                # Фильтруем: исключаем наше окно по точному названию файла и окно терминала
                valid_windows = [w for w in all_windows 
                                if w.title and "work_process_2.py" not in w.title 
                                and "PowerShell" not in w.title 
                                and "Командная строка" not in w.title 
                                and "python.exe" not in w.title.lower()  # Не процесс Python (в любом регистре)
                                and w.title != "Program Manager"]                
                if valid_windows:
                    target = random.choice(valid_windows)
                    try:
                        # Если окно свернуто — разворачиваем его
                        if target.isMinimized:
                            target.restore()
                        target.activate() # Выводим на передний план
            #            print(f"[{actions_count}] Переключил на окно: {target.title[:30]}...")
                    except Exception:
                        # Бывает, что окно закрылось или системное — просто пропускаем
                        pass

            actions_count += 1
            
            # Случайная пауза
            #sleep_time = random.randint(10, 30)
            sleep_time = random.randint(1, 3)
        #    print(f"   ... отдых {sleep_time} сек ...")
            time.sleep(sleep_time)

    except pyautogui.FailSafeException:
        print("\n[СТОП] Сработала защита.")
    except KeyboardInterrupt:
        print("\n[СТОП] Скрипт остановлен.")

if __name__ == "__main__":
    smart_mimic()
