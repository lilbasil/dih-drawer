import pyautogui
import time

print("program start in 5 seconds")
time.sleep(5)

#how fast do you want it to be
t = 0.3
#the scale of the peanits
s = 200

#left balls 
pyautogui.dragRel(0, s, duration=t)
pyautogui.dragRel(s/2, 0, duration=t)
pyautogui.dragRel(0, -s, duration=t)

#gap tween balls
pyautogui.dragRel(s/4, 0, duration=t)

#right balls
pyautogui.dragRel(0, s, duration=t)
pyautogui.dragRel(s/2, 0, duration=t)
pyautogui.dragRel(0, -s, duration=t)

#bottom shaft
pyautogui.dragRel(s*1.5, 0, duration=t)

#penile gland
pyautogui.dragRel(0, -s/2, duration=t)
pyautogui.dragRel(-s/2, 0, duration=t)
pyautogui.dragRel(0, s/4, duration=t)
pyautogui.dragRel(s/2, 0, duration=t)
pyautogui.dragRel(-s/2, 0, duration=t)
pyautogui.dragRel(0, s/4, duration=t)
pyautogui.dragRel(0, -s/2, duration=t)

#upper shaft
pyautogui.dragRel(-s*2.25, 0, duration=t)

#complete
pyautogui.dragRel(0, s/2, duration=t)



