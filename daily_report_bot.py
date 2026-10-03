import pyautogui
import pyperclip
import time
import os
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# ---------- Runtime values ----------
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
today = now.strftime("%Y-%m-%d")

output_folder = os.path.expanduser("/Users/cmuthukumaran2/Documents/GenAI/Python/")
excel_filename = f"daily_report_{today}.xlsx"
screenshot_filename = f"daily_report_{today}.png"

os.makedirs(output_folder, exist_ok=True)

print("Daily Report Bot")
print("Date & Time:", timestamp)
print("Starting in 5 seconds...")
print("Move mouse to top-left corner to STOP.")
time.sleep(5)

# ============================================================
# STEP 1: OPEN CHROME
# ============================================================

pyautogui.hotkey("command", "space")
time.sleep(1)

pyautogui.write("Google Chrome")
pyautogui.press("enter")
time.sleep(4)

# ============================================================
# STEP 2: SEARCH WEATHER
# ============================================================

pyautogui.hotkey("command", "l")
pyautogui.write("Bangalore weather today")
pyautogui.press("enter")

time.sleep(6)

# ============================================================
# STEP 3: COPY INFORMATION FROM CHROME
# ============================================================
#
# This uses keyboard navigation rather than fixed coordinates.
# Select all page text, copy it, and use the clipboard.
#

pyautogui.hotkey("command", "a")
pyautogui.hotkey("command", "c")
time.sleep(1)

page_text = pyperclip.paste()

# Keep a small portion of copied information for the report.
# For your demo you can replace this after calibrating the
# exact temperature selection on your Chrome screen.
if page_text.strip():
    fetched_data = page_text.strip().split("\n")[0:5]
    fetched_data = " ".join(fetched_data)
    fetched_data = fetched_data[:150]
else:
    fetched_data = "Bangalore weather checked"

print("Fetched Data:", fetched_data)

comment = "Weather update checked for today"

# ============================================================
# STEP 4: OPEN NUMBERS
# ============================================================

pyautogui.hotkey("command", "space")
time.sleep(1)

pyautogui.write("Numbers")
pyautogui.press("enter")

time.sleep(5)

# ============================================================
# STEP 5: CREATE BLANK SPREADSHEET
# ============================================================

# On the Numbers template chooser, Enter normally opens Blank.
pyautogui.press("enter")
time.sleep(5)

# Click around the first cell A1.
# Adjust this coordinate if necessary on your Mac.
pyautogui.click(300, 250)
time.sleep(1)

# ============================================================
# STEP 6: ENTER HEADER
# ============================================================

pyperclip.copy("Date & Time")
pyautogui.hotkey("command", "v")

pyautogui.press("tab")

pyperclip.copy("Fetched Data")
pyautogui.hotkey("command", "v")

pyautogui.press("tab")

pyperclip.copy("Comment")
pyautogui.hotkey("command", "v")

# ============================================================
# STEP 7: ENTER REPORT ROW
# ============================================================

# Go to A2
pyautogui.press("left", presses=2)
pyautogui.press("down")

pyperclip.copy(timestamp)
pyautogui.hotkey("command", "v")

pyautogui.press("tab")

pyperclip.copy(fetched_data)
pyautogui.hotkey("command", "v")

pyautogui.press("tab")

pyperclip.copy(comment)
pyautogui.hotkey("command", "v")

time.sleep(2)

# ============================================================
# STEP 8: TAKE SCREENSHOT
# ============================================================

screenshot_path = os.path.join(
    output_folder,
    screenshot_filename
)

pyautogui.screenshot(screenshot_path)

print("Screenshot saved:", screenshot_path)

# ============================================================
# STEP 9: SAVE / EXPORT
# ============================================================
#
# Numbers normally saves as .numbers.
# Exporting to Excel is UI/version dependent.
#
# Open File menu so the user can verify/export.
#

pyautogui.hotkey("command", "shift", "s")
time.sleep(2)

print()
print("Report created.")
print("Required Excel filename:", excel_filename)
print("Screenshot:", screenshot_filename)
print()
print("Export the Numbers document using:")
print("File -> Export To -> Excel")
print("and save it as:")
print(excel_filename)