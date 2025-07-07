import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Load the model
model = tensorflow.keras.models.load_model("keras_model.h5", compile=False)

# Load the labels
with open("labels.txt", "r", encoding="utf-8") as file:
    class_names = file.readlines()

# Load the image to test
image = Image.open("test.jpg").convert("RGB")
image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
data[0] = normalized_image_array

# Predict the result
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index].strip()
confidence_score = prediction[0][index]

# Print result
print("النتيجة:", class_name)
print("نسبة التأكد:", round(confidence_score * 100, 2), "%")