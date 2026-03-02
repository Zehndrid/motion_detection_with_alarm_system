#hernandez_dan_efraim_v.
#bscpe_1-4
#activiity_2
#youtube_link https://www.youtube.com/watch?v=QPjPyUJeYYE&t=980s

import threading
import winsound
import cv2
import imutils

video_capture = cv2.VideoCapture(0)

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

return_value, start_frame = video_capture.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

is_alarm_ringing = False
alarm_mode_active = False
motion_counter = 0

def trigger_beep_alarm():
    global is_alarm_ringing
    for beep_count in range(5):
        if not alarm_mode_active:
            break
        print("ALARM")
        winsound.Beep(2500, 1000)
    is_alarm_ringing = False

while True:

    return_value, current_frame = video_capture.read()
    cuurent_frame = imutils.resize(current_frame, width=500)

    if alarm_mode_active:
        frame_black_white = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        frame_black_white = cv2.GaussianBlur(frame_black_white, (5, 5), 0)

        difference = cv2.absdiff(frame_black_white, start_frame)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_black_white

        if threshold.sum() > 300:
            motion_counter += 1
        else:
            if motion_counter > 0:
                motion_counter -= 1
        
        
    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("t"):
        alarm_mode_active = not alarm_mode_active
        motion_counter = 0
    if key_pressed == ord("q"):
        alarm_mode_active = False
        break

video_capture.release()
cv2.destroyAllWindows()