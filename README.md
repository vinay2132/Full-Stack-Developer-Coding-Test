# Full-Stack-Developer-Coding-Test

Note to Candidates: We understand that each candidate may have varying levels of expertise
in different areas of the test. Please feel free to focus on the sections where you feel most
confident in showcasing your skills. You are welcome to solve one or more parts of the problem
based on your strengths and expertise. The solutions provided are examples for reference, and
you are encouraged to use your preferred methods and tools to achieve the objectives.

Sections:
Part 1: Image Processing and Machine Learning
Part 2: Backend and API Development
Part 3: Data Handling and Augmented Reality Integration
You can choose to solve any or all parts of the test. Completing multiple sections may provide
more comprehensive insights into your capabilities, but we value the depth and quality of
solutions over quantity.
Submission Timeline: You have one week from receiving this test to complete and submit your
solutions. Please ensure that your code is well-documented and organized, and include any
necessary instructions in a README.md file.

**Part 1: Image Processing and Machine Learning with Python**
Task: Develop a Python script using OpenCV and a pre-trained machine learning model to
perform object detection on images of shelves.

Requirements:

● Use OpenCV for image pre-processing (e.g., resizing, normalization).

● Leverage a pre-trained model like YOLO or Faster R-CNN for object detection.

● Output bounding box coordinates for detected products are provided in the sample images.

Evaluation Criteria:

● Correct application of OpenCV for image processing.

● Implementation and integration of a pre-trained model for object detection.

● Code quality, readability, and documentation.

**Part 2: Backend and API Development with Python**
Task: Create a Flask-based RESTful API to manage a collection of product information,
supporting operations for adding, retrieving, updating, and deleting records.

Requirements:

● Store data in an in-memory structure for testing purposes.

● Implement endpoints with appropriate request/response formats and status codes.

● Ensure the API is capable of handling concurrent requests gracefully.

Evaluation Criteria:

● API design, structure, and documentation.

● Implementation of CRUD operations.

● Error handling and response formatting.

**Part 3: Data Handling and Augmented Reality Integration**
Task: Write a Python script to simulate the integration of detected objects with augmented
reality by overlaying text on images.

Requirements:

● Use OpenCV to draw bounding boxes and overlay text on images based on object
detection results from Part 1.

● Simulate a simple AR effect by adding basic animations or effects using OpenCV (e.g.,
changing colors, adding simple graphics).
Evaluation Criteria:

● Effective manipulation of images using OpenCV.

● Creativity in simulating AR overlays.

● Code efficiency and modularity.


Part - 1

**Object Detection on Shelves with Faster R-CNN**

**Installation**

Prerequisites

Before setting up the project, ensure you have the following:

● Google Colab account or any Python environment with GPU support

● Python 3.x installed

● Access to your Google Drive (for saving and loading images)

Required Libraries

To run the code, you'll need the following Python libraries:

● torchvision

● Pillow

● matplotlib

● torch

● opencv-python

Video recording : 
https://drive.google.com/file/d/125oNsBaoq1x-Ra5YvhbSlxvvAczxY1x6/view?usp=sharing 

Part - 2
**Product Management API**

**Installation **

**Prerequisites**
Python 3.x
Flask


**API Endpoints **

The API has the following endpoints:

**GET /products**
Retrieve the list of all products.

● Method: GET
● Response: JSON object containing a list of all products.


**GET /products/<int:product_id> **
Retrieve a specific product by its ID.

● Method: GET
● Parameters:
   ● product_id (integer): The ID of the product.
● Response: JSON object containing the product details.


**POST /products**
Add a new product to the list.

● Method: POST
● Request Body:
   ● product_name (string): Name of the product (required).
   ● product_cost (integer): Cost of the product (optional, default = 0).
   ● product_value (integer): Value of the product (optional, default = 1).
● Response: JSON object with the newly added product.


**PUT /products/<int:product_id>**
Update an existing product.

● Method: PUT
● Parameters:
   ● product_id (integer): The ID of the product.
● Request Body:
   ● product_name (string): Updated name of the product (optional).
   ● product_cost (integer): Updated cost of the product (optional).
   ● product_value (integer): Updated value of the product (optional).
● Response: JSON object with the updated product.


**DELETE /products/<int:product_id>**
Delete a product by its ID.

● Method: DELETE
● Parameters:
   ● product_id (integer): The ID of the product to be deleted.
● Response: JSON object with a deletion success message.

Video Recording: 
https://drive.google.com/file/d/1M04j6TzYq3d495a3OCFUXB6gWj7RsBjY/view?usp=sharing

Part - 3
**Object Detection with Augmented Reality (AR) Effects**

**Installation

Prerequisites**
  Python 3.x
  OpenCV (cv2)

Video Recording: 
https://drive.google.com/file/d/1qLcaXvTZxLbquHAWTs3mMFrXgw4JWkME/view?usp=sharing
