from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import cv2
from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Hello, World!")

@gzip.gzip_page
def webcam_feed(request):
    # OpenCV VideoCapture object
    cap = cv2.VideoCapture(0)

    def generate():
        while True:
            # Read a frame from the webcam
            ret, frame = cap.read()

            # Convert the frame to JPEG format
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame in the response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    # Return a StreamingHttpResponse with the generator function
    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')

def webcam_view(request):
    return render(request, 'helloapp/webcam.html')
