# GPT model : Benchmark

## Content

The following repository consists of a benchmark of Language Models (GPT-3.5 : text-davinci-003, BERT, and GPT-2) in the case of text summarization task of 115 sentences from the test dataset of the CNN-DailyMail News from Kaggle (https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail).

## To use ChatGPT

Before running the scripts, and to be able to use ChatGPT for the experiments, you have to put your api key on *openai_key.txt* to be able to use the OpenAI models. To get it, you must an OpenAI account available by doing the following steps:

1. Navigate to https://platform.openai.com/
2. Click on your avatar in the top right-hand corner of the dashboard.
2. Select View API Keys.
3. Click Create new secret key.

API Key Good Practice Safety are available on OpenAI website : https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety

For the moment, only BERT, GPT-2 and text-davinci-003 (fine-tuned GPT-3) models are evaluated.

## How to run

Located at the root of the project, you can generate the summarized sentences by writing in your terminal:
```sh
python experiments/summarization_task.py
  ```

On the following repository, the results are given as *results/generated_summary.txt*. To get the average value of BLEU, ROUGE and BLEURT metrics over the 115 sentences summarized, you have to write:

```sh
python experiments/benchmark.py
  ```

Creating a table : *model_summarization_score.csv* in *results* folder.

## Requirements

Python 3.11.2

- bert-extractive-summarizer==0.10.1
- openai==0.27.4
- rouge==1.0.1
- tensorflow==2.12.0
- tensorflow-datasets==4.9.2
- torch==2.0.0
- transformers==4.28.1

You also have to install BLEURT metric from https://github.com/google-research/bleurt#readme such as they stated:

```sh
pip install --upgrade pip  # ensures that pip is current
git clone https://github.com/google-research/bleurt.git
cd bleurt
pip install .
  ```
