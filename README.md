# system-idle-preventer
A Python productivity tool that helps users stay focused by preventing unnecessary system idle interruptions.

The script prompts the user to enter a duration in minutes and calculates the corresponding start and end time. During this interval, it periodically simulates minimal user activity by triggering volume key presses using the pyautogui library. These inputs prevent the system from entering an idle state while avoiding interference with active applications. The script runs until the specified time elapses or the user manually exits, helping maintain uninterrupted work sessions.
