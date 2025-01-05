import cv2
import mediapipe as mp

print("Kütüphaneler yüklendi")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils
mp_draw_styles = mp.solutions.drawing_styles

print("MediaPipe modeli başlatıldı")

cap = cv2.VideoCapture(0)
print("Kamera başlatılmaya çalışılıyor...")

if not cap.isOpened():
    print("Hata: Kamera açılamadı!")
    exit()

print("Kamera başarıyla başlatıldı")

while True:
    success, img = cap.read()
    if not success:
        print("Hata: Kameradan görüntü alınamadı!")
        break
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_draw_styles.get_default_hand_landmarks_style(),
                mp_draw_styles.get_default_hand_connections_style()
            )
            
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id in [4, 8, 12, 16, 20]:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
    
    cv2.imshow("El Algılama", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Program kullanıcı tarafından sonlandırıldı")
        break

print("Program kapatılıyor...")
cap.release()
cv2.destroyAllWindows()
hands.close()
