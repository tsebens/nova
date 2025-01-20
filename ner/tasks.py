from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import BasePromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field, ValidationError

from ner.models import Text
from ner.prompts import sentence_prompt
from ner.schemas import TextSchema


class Task(BaseModel):
    """Utility class for defining a unit of work to be facilitated by an LLM. Uses `prompt` to instruct the LLM,
    and ensures that the LLM's response is a valid instance of the `output` class"""
    llm: BaseChatModel = Field(description="LLM object that implements LangChain BaseChatModel interface")
    prompt: BasePromptTemplate = Field(description="Prompt used to communicate task and parameters to LLM agent")
    response_type: type[BaseModel] = Field(description="Pydantic model used to enforce the format of the LLM output")
    valid_output_max_tries: int = Field(description="Maximum number of times to execute the pipeline in order to get a valid output", default=5)

    def execute(self, **kwargs):
        """Build and execute the processing chain"""
        # Occasionally the llm will produce a response which is not a valid instance of the output schema.
        # To account for this, we'll reprocess the input a few times to see if the llm can get it right. We limit the
        # number of tries so that if there is a true root problem, it will eventually be flagged and halt processing
        valid_output = False
        tries = 0
        while not valid_output:
            tries = tries + 1
            try:
                response = (
                    self.prompt
                    | self.llm.with_structured_output(self.response_type)
                ).invoke(kwargs)
                valid_output = True
            except ValidationError as e_:
                if tries > self.valid_output_max_tries:
                    raise e_

        return response


class ModelResponseTask(Task):
    """Subclass of Task which builds an instance of Django object from its resposne"""
    def execute(self, **kwargs):
        response = super().execute(**kwargs)
        return response.Meta.model(**response.model_dump())


SENTENCE_TO_TEXT = ModelResponseTask(
    llm=ChatOpenAI(model="gpt-4o-mini-2024-07-18"),
    prompt=sentence_prompt,
    response_type=TextSchema
)