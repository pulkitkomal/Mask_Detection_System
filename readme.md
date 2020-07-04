# Mask Detection System

We created a mask detection system which will take a video as the input and provide the frames where the people are not wearing a mask. This is a small effort to help the essential workers track down people infected with COVID-19 as most studies show that people not wearing masks are most likely to spread the virus or get infected.

## Screenshots

Video Upload Screen

![Video Upload](https://drive.google.com/uc?export=view&id=1eNhCu171o9D0J4eyz15sLC3o5qFnnKho)

Video Output Screen

![Video Upload](https://drive.google.com/uc?export=view&id=1x-R-7GK2h0mye-HQexglSWyUVKWrkNxl)

Error Screen

![Video Upload](https://drive.google.com/uc?export=view&id=1cX0__fDCuRA0nuC0UtCQnXB6j7x-aEb_)

## The model used 

We implemented and used the model from [PyImageSearch](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/)

## Dependencies
1. [Tensorflow](https://pypi.org/project/tensorflow/)
```python
pip install tensorflow
```
2. [Numpy](https://pypi.org/project/numpy/)
```python
pip install numpy
```
3. [openCV](https://pypi.org/project/opencv-python/)
```python
pip install opencv-python
```
4. [Flask](https://pypi.org/project/Flask/)

```python
pip install Flask
```

## Usage
Open config.py and replace the path with current path.

Open Terminal in directory

```bash
python app.py
```

## Authors

[Kamaljeet Kaur Hunjan](https://www.linkedin.com/in/kamaljeet-kaur-175174199/)

[Pulkit Komal](https://www.linkedin.com/in/pulkit-komal/)

[Adrian Rosebrock](https://www.pyimagesearch.com/author/adrian/)
