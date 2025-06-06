import cv2 as cv
import mediapipe as mp

# initializing mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)

# initializing drawing module
mp_drawing = mp.solutions.drawing_utils


# function to determine hand gesture
def classify_gesture(hand_landmarks):
    if hand_landmarks:
        landmarks = hand_landmarks[0].landmark

#       calculating distance between landmarks
        thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
        pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]



#        gesture decision
        open_palm = all([
            index_tip.y < thumb_tip.y,
            middle_tip.y < thumb_tip.y,
            ring_tip.y < thumb_tip.y,
            pinky_tip.y < thumb_tip.y
        ])

        closed_palm = all([
            index_tip.y > thumb_tip.y,
            middle_tip.y > thumb_tip.y,
            ring_tip.y > thumb_tip.y,
            pinky_tip.y > thumb_tip.y
        ])

        if open_palm:
            return "open palm"
        elif closed_palm:
            return "closed palm"
        elif (thumb_tip.x < index_tip.x)and (thumb_tip.y < index_tip.y):
            return "thumbs up"
        elif (index_tip.x > middle_tip.x)and (thumb_tip.y > index_tip.y):
            return "peace sign"
        elif (middle_tip.x < thumb_tip.x) and (middle_tip.y < thumb_tip.y):
            return "FUCK YOU TOO BITCH"
        elif (index_tip.x < middle_tip.x) and (index_tip.y < middle_tip.y):
            return "DESI KALLU FUCK"
        else:
            return "unrecognized"

# start video capturing
video_cap = cv.VideoCapture(0)
while True:
    ret, video = video_cap.read()
    BGR_RGB  = cv.cvtColor(video,cv.COLOR_BGR2RGB)

    results = hands.process(video)

    # RGB_BGR = cv.cvtColor(BGR_RGB,cv.COLOR_RGB2BGR)

#   Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Loop over the fingertips (landmarks 4, 8, 12, 16, 20)
            fingertip_ids = [4, 8, 12, 16, 20]
            h, w, _ = BGR_RGB.shape
            for tip_id in fingertip_ids:
                # Get the x and y coordinates of the fingertip
                x = int(hand_landmarks.landmark[tip_id].x * w)
                y = int(hand_landmarks.landmark[tip_id].y * h)

                # Draw a circle at each fingertip
                cv.circle(BGR_RGB, (x, y), 10, (0, 255, 0), -1)  # Green dots

            mp_drawing.draw_landmarks(BGR_RGB,hand_landmarks,mp_hands.HAND_CONNECTIONS)

            # Classify the gesture
            gesture = classify_gesture(results.multi_hand_landmarks)
            cv.putText(video, gesture, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv.imshow('live_video', video)

            #     now we need to end the video also otherwise it will never end and the computer will crash
            # press esc to exit
            if cv.waitKey(20) & 0xFF == ord('d'):
                break