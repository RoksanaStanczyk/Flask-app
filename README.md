# Flask-app

To run program please type:
1) docker build -t flask_app:v1.0 . 
2) docker run --rm -it -p 5000:5000 flask_app:v1.0
3) request available http://localhost:5000/plot?a=1&b=0&c=0&xmin=-5&xmax=5&ymin=0&ymax=10
