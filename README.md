<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Tumour Detection Prototype</h1>
    <p>This project is a prototype for a tumour detection system. It utilizes OpenCV for image processing to detect and highlight potential tumours in real-time video streams. The prototype pre-processes video frames, identifies contours of interest, and highlights significant areas that could indicate the presence of a tumour.</p>
    
<h2>Prerequisites</h2>
    <p>Before running this prototype, ensure you have the following dependencies installed:</p>
    <ul>
        <li>Python 3.x</li>
        <li>OpenCV (cv2)</li>
        <li>NumPy</li>
    </ul>
    
<h2>Installation</h2>
    <p>No installation is necessary beyond ensuring the above prerequisites are met. Simply clone or download the project files to your local machine.</p>
    
<h2>Project Structure</h2>
    <p>The project consists of two main Python files:</p>
    <ul>
        <li><code>main.py</code> - The primary script that captures video, processes it, and displays the output.</li>
        <li><code>utils.py</code> - Contains helper functions for contour analysis and image manipulation.</li>
    </ul>
    
<h2>Usage</h2>
    <p>To run the prototype:</p>
    <ol>
        <li>Ensure a webcam or video capture device is connected and properly configured on your system.</li>
        <li>Execute the <code>main.py</code> script to start the video capture and analysis.</li>
        <li>Observe the output video stream for highlighted areas, which may indicate potential tumours.</li>
    </ol>
    <p>To exit the application, press the 'ESC' key while the video window is active.</p>
    
<h2>How It Works</h2>
    <p>The prototype performs several steps to analyze video frames:</p>
    <ul>
        <li>Video frames are captured and resized for consistent processing.</li>
        <li>Frames are converted to grayscale and undergo blurring and edge detection to prepare for contour analysis.</li>
        <li>Contours are identified, and the largest rectangular contour is presumed to be of interest for further analysis.</li>
        <li>The identified area is warped to a top-down view, thresholded, and analyzed for dark areas that could indicate tumours.</li>
        <li>Potential tumours are highlighted, and the frame is displayed with an overlay showing the current frames-per-second (FPS) rate.</li>
    </ul>
    
<h2>Limitations and Development</h2>
    <p>This prototype is an initial step towards real-time tumour detection. It has limitations and is currently optimized for specific scenarios. Further development, testing, and validation with medical professionals are necessary to enhance its accuracy and usability in practical applications.</p>
    

</body>
</html>
