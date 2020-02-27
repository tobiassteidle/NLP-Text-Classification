import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.metrics import confusion_matrix

def plot_history(history):
    # summarize history for accuracy
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

def plot_wordcloud(words):
    all_text = ' '.join([text for text in words])
    wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_text)
    plt.figure(figsize=(15, 12))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()

def plot_confusion_matrix(y_test, y_pred, classnames):
    cm = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1), normalize='true')
    plt.figure(figsize=(15, 12))
    plt.matshow(cm, fignum=1)
    plt.colorbar()
    plt.ylabel('True label')
    plt.yticks(np.arange(len(classnames)), labels=classnames)
    plt.xlabel('Predicted label')
    plt.xticks(np.arange(len(classnames)), labels=classnames, rotation='vertical')
    plt.show()

def plot_prediction_bar(prediction, classnames):
    color_map = cm.get_cmap('terrain')
    plt.figure(figsize=(15, 12))
    y_pos = np.arange(len(classnames))
    plt.bar(y_pos, prediction, align='center', color=color_map(prediction))
    plt.xticks(y_pos, classnames, rotation='vertical')
    plt.ylabel('Prediction (%)')
    plt.show()
