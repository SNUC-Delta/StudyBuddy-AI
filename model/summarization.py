from transformers import pipeline
from speech_to_text import *

 
summarizer = pipeline(task = 'summarization', model='/model_files', tokenizer='/model_files')
output = summarizer(text, max_length=int(len(text.replace(" ", ""))/4), min_length=int(len(text)/8), do_sample=False)
output = output[0]['summary_text']

#Run below two lines ones seperately if above code doesn't work and try again with same code. 

#summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#summarizer.save_pretrained('/model_files')
 