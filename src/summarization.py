from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

def load_summarization_model(model_path):
    model = load_model(model_path)
    return model

def summarize_text(model, input_text, max_length=50):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([input_text])
    sequence = tokenizer.texts_to_sequences([input_text])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post')
    
    summary = model.predict(padded_sequence)
    summary_text = ' '.join([tokenizer.index_word.get(i, '') for i in np.argmax(summary, axis=-1) if i > 0])
    
    return summary_text

def generate_summary(input_text, model_path):
    model = load_summarization_model(model_path)
    summary = summarize_text(model, input_text)
    return summary