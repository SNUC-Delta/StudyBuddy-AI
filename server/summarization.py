from transformers import pipeline
from speech_to_text import *
from pdf import pdf


def summary(path, unId):
    text = startConvertion(pathName=path)
    summarizer = pipeline(task='summarization',
                          model='./model_files', tokenizer='./model_files')
    output = summarizer(text, max_length=int(
        len(text.replace(" ", ""))/4), min_length=int(len(text)/8), do_sample=False)
    output = output[0]['summary_text']
    pdf.cell(200, 10, txt=str(output),
             ln=4, align='L')

    pdf.output(f"./dist/PDF/{unId}_pdf.pdf")
    return output
