import openai
import pandas as pd
from summarizer import Summarizer,TransformerSummarizer


def generate_openai_response(text):
        """Generate the summarized sentence made by OpenAI

        Args:
            text (str): Text given to OpenAI model

        Returns:
            gpt_answer (str): Answer generated by GPT-3 model
        """
        openai_input = 'Summarize the following sentence : '+text 
        gpt_answer = openai.Completion.create(
                engine='text-davinci-003',              # Model selected. Determines the quality, speed, and cost.
                temperature=0.5,                        # Level of creativity in the response
                prompt=openai_input,                    # What the user typed in
                max_tokens=100,                         # Maximum tokens in the prompt AND response
                n=1,                                    # The number of completions to generate
                stop=None,                              # An optional setting to control response generation
                ).choices[0].text

        # Return the first choice's text
        return gpt_answer


def apply_models(list_text):
        """Application of the different models on text

        Args:
            list_text (list): List of text to summarize

        Returns:
            list_answer (list): List of summary made
        """
        # BERT and GPT-2 Loading
        bert_model = Summarizer()
        GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")

        list_answer = []
        list_answer.append(['BERT', 'GPT-2', 'text-davinci-003'])
        # Summarization of the sentences
        for i in range(len(list_text)):
                bert_summary = ''.join(bert_model(list_text[i], min_length=60))
                gpt2_summary = ''.join(GPT2_model(list_text[i], min_length=60))
                gpt3_summary = generate_openai_response(list_text[i])
                list_answer.append([bert_summary, gpt2_summary, gpt3_summary])
        return list_answer


def save_summary(list_answer):
        """Save the Generated summaries into a file
        named generated_summary.txt

        Args:
            list_answer (list): List of the generated summaries
        """
        with open('results/generated_summary.txt', 'w') as f:
                for line in list_answer:
                        f.write("%s\n" % line)
        

if __name__ == '__main__':
        #Setting of the openai api key
        openai.api_key =  open("openai_key.txt", "r").read()
        #Data Loading
        database = pd.read_csv('data/test.csv')
        test_data = database.sample(frac=0.01, replace=True, random_state=1)
        list_text = test_data["article"].tolist()
        #Model Application
        list_answer = apply_models(list_text)
        #Summarization saving
        save_summary(list_answer)