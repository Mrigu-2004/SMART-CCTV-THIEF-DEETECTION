import cv2

donel = False
doner = False
x1, y1, x2, y2 = 0, 0, 0, 0

def select(event, x, y, flags, param):
    global x1, x2, y1, y2, donel, doner
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        donel = True
    elif event == cv2.EVENT_RBUTTONDOWN:
        x2, y2 = x, y
        doner = True
        print(f"Selection done: Top-left ({x1}, {y1}), Bottom-right ({x2}, {y2})")

def rect_noise():
    global x1, x2, y1, y2, donel, doner
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("select_region")
    cv2.setMouseCallback("select_region", select)

    # Wait for ROI selection
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame from camera.")
            break

        cv2.imshow("select_region", frame)

        if cv2.waitKey(1) == 27 or doner:
            if not (donel and doner and x1 < x2 and y1 < y2):
                print("Invalid region selected. Please try again.")
                donel, doner = False, False
                continue
            cv2.destroyWindow("select_region")
            break

    while True:
        ret1, frame1 = cap.read()
        ret2, frame2 = cap.read()

        if not (ret1 and ret2):
            print("Failed to read frames from camera.")
            break

        # Validate ROI
        frame1only = frame1[y1:y2, x1:x2] if y1 < y2 and x1 < x2 else None
        frame2only = frame2[y1:y2, x1:x2] if y1 < y2 and x1 < x2 else None

        if frame1only is None or frame2only is None or frame1only.size == 0 or frame2only.size == 0:
            print("Invalid or empty ROI. Exiting.")
            break

        # Process ROI
        diff = cv2.absdiff(frame2only, frame1only)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        diff = cv2.blur(diff, (5, 5))
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            max_cnt = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame1, (x + x1, y + y1), (x + w + x1, y + h + y1), (0, 255, 0), 2)
            cv2.putText(frame1, "MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        else:
            cv2.putText(frame1, "NO MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

        # Draw selected ROI
        cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.imshow("esc. to exit", frame1)

        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

# Run the program
#rect_noise()