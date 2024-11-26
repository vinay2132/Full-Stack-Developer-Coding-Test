```markdown
# Full Stack Developer Coding Test

This repository contains solutions for the Full Stack Developer Coding Test. The test is divided into three parts, each focusing on different aspects of full-stack development:

1. **Image Processing and Machine Learning**  
2. **Backend and API Development**  
3. **Data Handling and Augmented Reality Integration**

Candidates are encouraged to complete one or more sections based on their strengths and expertise. Each part has been implemented to meet the specified requirements and includes detailed documentation for understanding and usage.

---

## Table of Contents
- [Part 1: Image Processing and Machine Learning](#part-1-image-processing-and-machine-learning)
- [Part 2: Backend and API Development](#part-2-backend-and-api-development)
- [Part 3: Data Handling and Augmented Reality Integration](#part-3-data-handling-and-augmented-reality-integration)
- [Installation](#installation)
- [Video Demonstrations](#video-demonstrations)

---

## Part 1: Image Processing and Machine Learning

**Task:** Perform object detection on images of shelves using a pre-trained machine learning model.

### Requirements
- Use OpenCV for image pre-processing (e.g., resizing, normalization).
- Leverage a pre-trained model like YOLO or Faster R-CNN for object detection.
- Output bounding box coordinates for detected products in sample images.

### Features
- Correct application of OpenCV for image pre-processing.
- Integration of Faster R-CNN for object detection.
- Code is modular, well-documented, and easy to understand.

### Prerequisites
- Google Colab account or any Python environment with GPU support.
- Python 3.x installed.
- Access to Google Drive for saving and loading images.

### Required Libraries
- `torch`
- `torchvision`
- `Pillow`
- `matplotlib`
- `opencv-python`

---

## Part 2: Backend and API Development

**Task:** Create a Flask-based RESTful API to manage product information with CRUD operations.

### API Endpoints
1. **`GET /products`**  
   Retrieve the list of all products.  
   **Response:** JSON object containing all products.

2. **`GET /products/<int:product_id>`**  
   Retrieve a specific product by its ID.  
   **Response:** JSON object with product details.

3. **`POST /products`**  
   Add a new product.  
   **Request Body:**
   ```json
   {
     "product_name": "string",
     "product_cost": "integer (optional, default=0)",
     "product_value": "integer (optional, default=1)"
   }
   ```  
   **Response:** JSON object of the newly added product.

4. **`PUT /products/<int:product_id>`**  
   Update an existing product by ID.  
   **Request Body:**
   ```json
   {
     "product_name": "string (optional)",
     "product_cost": "integer (optional)",
     "product_value": "integer (optional)"
   }
   ```  
   **Response:** JSON object with the updated product.

5. **`DELETE /products/<int:product_id>`**  
   Delete a product by its ID.  
   **Response:** JSON object with a success message.

---

## Part 3: Data Handling and Augmented Reality Integration

**Task:** Simulate AR integration by overlaying text and effects on detected objects in images.

### Features
- Use OpenCV to draw bounding boxes around detected objects.
- Overlay text on images based on detection results.
- Add AR-style visual effects such as dynamic color changes or semi-transparent graphics.

### Prerequisites
- Python 3.x installed.
- OpenCV library (`cv2`).

---

## Installation

To set up the environment for any part of the test, ensure you have the required libraries installed:

1. Clone this repository:
   ```bash
   git clone https://github.com/vinay2132/full-stack-developer-coding-test.git
   cd full-stack-developer-coding-test
   ```

2. Install dependencies for each part:
   - **Part 1:**
     ```bash
     pip install torch torchvision Pillow matplotlib opencv-python
     ```
   - **Part 2:**
     ```bash
     pip install flask
     ```
   - **Part 3:**
     ```bash
     pip install opencv-python
     ```

3. Follow the instructions in the respective sections to run the code.

---

## Video Demonstrations

- **Part 1: Object Detection on Shelves with Faster R-CNN**  
  [Watch Video](https://drive.google.com/file/d/125oNsBaoq1x-Ra5YvhbSlxvvAczxY1x6/view?usp=sharing)

- **Part 2: Product Management API**  
  [Watch Video](https://drive.google.com/file/d/1M04j6TzYq3d495a3OCFUXB6gWj7RsBjY/view?usp=sharing)

- **Part 3: Object Detection with Augmented Reality (AR) Effects**  
  [Watch Video](https://drive.google.com/file/d/1qLcaXvTZxLbquHAWTs3mMFrXgw4JWkME/view?usp=sharing)

---

## Notes

- Each section is independent, and you can run them separately based on your interests and expertise.
- Ensure your environment meets the prerequisites for the section you wish to run.

**Author:** Daram Vinay
**Contact:** [your-daramvinay12@gmail.com](mailto:daramvinay12@gmail.com)  
```
