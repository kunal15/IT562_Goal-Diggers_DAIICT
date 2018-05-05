# Book Recommender System based on Reinforcement Learning

The recommender system is based on Multi Armed Bandit approach, in which the arms are the recommendations. The user provides some of the genres which he likes and as iterations pass by, he gives rewards to the recommendations which mould the system on the run. The rewards are in the form of like, dislike and selected. These rewards go to a function to get the overall liking/disliking of the book by the user. Thus, based on these rewards, the recommender system learns and gives recommendations to the user.

## Getting Started

These instructions will get you a copy of the project and you can run it on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
```
Python 3
```
```
PYQT5 

pip3 install pyqt5
```
```
pandas

pip3 install pandas
```
```
sklearn

pip3 install sklearn
```
```
numpy

pip3 install numpy
```
### Setup

To run the code we need to have the data set in the same directory as the other python files.

```
Move "b.csv" to the same directory as "bookre.py"
```
## Running the tests
Steps to run the code. 

```
python bookre.py

A standalone application would pop up
```
```
Enter the Genres you like.
```
```
Give rating to any book from the 10 Recommendations
1) +3 for a like
2) +1 for Selected
3) -3 for dislike
4) -1 for none.
```
```
Press on submit button to proceed to next set of recommendations.
```
## Built With

* [PYQT5](https://pypi.org/project/PyQt5/) - The Desktop app for frontend used

## Authors

* **Mayank Nahar** - *201501040* 
* **Karanraj Singh Saini** - *201501105* 
* **Kunal Khatri** - *201501011* 
* **Parv Chadha** - *201501002* 

## Acknowledgments

* Prof Sourish Dasgupta- For his guidance
