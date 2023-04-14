from transformers import pipeline
from speech_to_text import *

mainOut = ""

def summary(path):
    text = startConvertion(pathName = path)
    summarizer = pipeline(task = 'summarization', model='/model_files', tokenizer='/model_files')
    output = summarizer(text, max_length=int(len(text.replace(" ", ""))/4), min_length=int(len(text)/8), do_sample=False)
    output = output[0]['summary_text']
    global mainOut
    mainOut = output
    return output