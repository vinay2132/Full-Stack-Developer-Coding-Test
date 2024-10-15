import cv2

def adding_effects(image, obj_det, base_color=(255, 0, 0), font_scale=0.6, thickness=2):

    for i, detection in enumerate(obj_det):
        label = detection['label']
        confidence = detection['confidence']
        (x_minimum, y_minimum, x_maxim, y_maxim) = detection['box']

        color_shift = i * 40 % 255  # Gradual color shift for AR effect
        dyn_color = (base_color[0], color_shift, base_color[2])

        cv2.rectangle(image, (x_minimum, y_minimum), (x_maxim, y_maxim), dyn_color, thickness)

        standared_value = 2  
        img_overlay = image.copy()
        cv2.rectangle(img_overlay, (x_minimum - standared_value, y_minimum - standared_value), (x_maxim + standared_value, y_maxim + standared_value), dyn_color, -1)
        cv2.addWeighted(img_overlay, 0.3, image, 0.7, 0, image)  # Adjust transparency

        obj_text = f"{label}: {confidence:.2f}"

        obj_txt_values = (x_minimum, y_minimum - 10 if y_minimum - 10 > 10 else y_minimum + 20)

        cv2.putText(image, obj_text, obj_txt_values, cv2.FONT_HERSHEY_SIMPLEX, font_scale, dyn_color, thickness)

    return image

obj_det = [
    {"label": "Bottle", "confidence": 0.88, "box": (30, 50, 200, 300)},
    {"label": "Can", "confidence": 0.76, "box": (250, 80, 400, 320)},
]

image = cv2.imread('shelf_image.jpg')

img_add_effect = adding_effects(image, obj_det)

cv2.imshow('AR Effect img_overlay', img_add_effect)
cv2.waitKey(0)  
cv2.destroyAllWindows()

cv2.imwrite('shelf_image_with_ar_effect.jpg', img_add_effect)
