# Repository ist noch PRIVATE !!!!


# NLP Cyber Troll detection
Prediction if a text comes from a Cyber-Troll or a normal User.

### Objectives
Classifing tweets as aggressive or not to help fight trolls.

## Additional Information
Dataset: [Tweets Dataset for Detection of Cyber-Trolls](https://www.kaggle.com/dataturks/dataset-for-detection-of-cybertrolls)  
Tensorflow Version: 2.1.0

### Dataset Information
The dataset is contained in this repository in `/data/cybertroll.data`  
It contains of a set of JSON records in the following format:
```
{ 
   "content":" Get fucking real dude.",
   "annotation":{ 
      "notes":"",
      "label":[ 
         "1"
      ]
   },
   "extras":null
}
```
Where `content` is the text of the tweet and `label` is the classification whether troll or not.  
`0 = Not Cyber-Troll`  
`1 = Cyber Troll`

## Installation

#### GPU Support
If the CUDA drivers are installed the GPU version of Tensorflow can be used.
To do this, un-comment the line `tensorflow-gpu==2.1.0` and comment out `tensorflow==2.1.0` in the `requirements.txt`.
  
By default the CPU version is installed.

#### Installation Steps

1. Create and activate a new environment.
```
conda create -n nlp python=3.6
source activate nlp
```
2. Install Dependencies.
```
pip install -r requirements.txt
```

### Training of the neural network
Start the Jupyter Notebook and follow the instructions.
```
jupyter notebook "NLP Troll Detection Example.ipynb"
```
