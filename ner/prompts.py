from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, PromptTemplate

sentence_prompt = ChatPromptTemplate(
    messages =
        [
            HumanMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=['text'],
                    input_types={},
                    partial_variables={},
                    template=
                        "You are an AI assistant who identifies individual entities within unstructured text. " 
                        "I will provide you with a block of text. You will respond with the first full sentence in the text."
                        "Text: {text}. "
                        ),
                    additional_kwargs={}
            )
        ],
    input_variables = ('text')
)
