import cv2
import numpy as np
import tensorflow as tf
import torch
import onnx
from onnx2keras import onnx_to_keras

model_path = r'C:\xampp\htdocs\Intelligent_counter\ai_project\el_model\best.pt'

# Load PyTorch model
pytorch_model = torch.load(model_path)

# Convert PyTorch model to ONNX format
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(pytorch_model, dummy_input, 'model.onnx', input_names=['input'], output_names=['output'])

# Convert ONNX model to Keras format
onnx_model = onnx.load('model.onnx')
keras_model = onnx_to_keras(onnx_model, ['input'])

# Load weights into Keras model
weights = pytorch_model.state_dict()
keras_model.set_weights([weights[key].numpy() for key in weights.keys()])


model = tf.keras.models.load_model(keras_model)
# ... (previous code to load the model and capture the camera) ...
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    # Preprocess the frame before passing it to the model
    resized_frame = cv2.resize(frame, (150, 150))  # Resize the frame to (150, 150)
    normalized_frame = resized_frame / 255.0
    input_data = np.expand_dims(normalized_frame, axis=0)
    # Make predictions using the model
    predictions = model.predict(input_data)
    print(predictions)
    confidence=predictions[0]
    # Assuming the model predictions return bounding box coordinates in the format (x_min, y_min, x_max, y_max)
    # or (x_center, y_center, width, height)
    # For example, if the predictions are in (x_min, y_min, x_max, y_max) format:
    """recognized_x, recognized_y, recognized_x_max, recognized_y_max = predictions[0]
    recognized_width = recognized_x_max - recognized_x
    recognized_height = recognized_y_max - recognized_y

    triangle_x = int(recognized_x + recognized_width // 2)
    triangle_y = int(recognized_y)

    # Draw the rectangle on the frame
    cv2.rectangle(frame, (int(recognized_x), int(recognized_y)),
                  (int(recognized_x + recognized_width), int(recognized_y + recognized_height)),
                  (0, 255, 0), 2)  # Green rectangle with a thickness of 2 pixels

"""
    # Draw the triangle at the updated position
    if confidence[0]>0.5 and confidence[1]<0.5 and confidence[2]<0.5:
        print("paper")
    elif confidence[1]>0.5 and confidence[0]<0.5 and confidence[2]<0.5:
        print("rock")
    elif confidence[2]>0.5 and confidence[1]<0.5 and confidence[0]<0.5:
        print("scissors")
    else :
        print("nothing")

    cv2.imshow('Live Camera', frame)


    # Stop capturing video when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
