# NLP Text Classification
Classification of short texts like headlines or tweets.

## Additional Information
Dataset: [News Category Dataset](https://www.kaggle.com/rmisra/news-category-dataset)  
Dataset: [Tweets Dataset for Detection of Cyber-Trolls](https://www.kaggle.com/dataturks/dataset-for-detection-of-cybertrolls)
  
Tensorflow Version: 2.1.0

### Dataset Information
#### News dataset
The dataset is contained in this repository in `/data/news_train.data` and `/data/news_test.data`
It contains of a set of JSON records in the following format:
```
{
   "category":"ENTERTAINMENT",
   "headline":"Jim Carrey Blasts 'Castrato' Adam Schiff And Democrats In New Artwork",
   "authors":"Ron Dicker",
   "link":"https://www.huffingtonpost.com/entry/jim-carrey-adam-schiff-democrats_us_5b0950e8e4b0fdb2aa53e675",
   "short_description":"The actor gives Dems an ass-kicking for not fighting hard enough against Donald Trump.",
   "date":"2018-05-26"
}
```

#### Cybertroll dataset
The dataset is contained in this repository in `/data/cybertroll_train.data` and `/data/cybertroll_test.data`   
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

##### 1. Create and activate a new environment.
```
conda create -n nlp python=3.6
source activate nlp
```
##### 2. Install Dependencies.
```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

##### 3. Test if GPU support is working (optional GPU only)
To check if GPU is used for Tensorflow execute
```
python test_gpu.py
```

The Output should be something like (depends on your graphic card):
```
2020-02-08 08:28:39.981439: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudart64_101.dll
2020-02-08 08:28:45.061725: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library nvcuda.dll
2020-02-08 08:28:45.102095: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1555] Found device 0 with properties:
pciBusID: 0000:02:00.0 name: GeForce GTX 1070 computeCapability: 6.1
coreClock: 1.7465GHz coreCount: 15 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 238.66GiB/s
...
...
...
Default GPU Device:/device:GPU:0
```

### Training of the neural network
Start the Jupyter Notebook and follow the instructions.
```
jupyter notebook "NLP Text Classification.ipynb"
```
