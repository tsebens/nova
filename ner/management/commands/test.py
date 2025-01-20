from argparse import ArgumentParser

from django.core.management import BaseCommand
from langchain_openai import ChatOpenAI

from ner.prompts import sentence_prompt
from ner.schemas import TextSchema
from ner.tasks import SENTENCE_TO_TEXT


class Command(BaseCommand):
    help = "Loads data from CAS to CIA using the ORM to construct Trip objects from CAS data, then save them to the CIA."

    def handle(self, *args, **options):
        obj__ = SENTENCE_TO_TEXT.execute(text="New first fuller sentence. First full sentence. Second full sentence. Third full sentence.")
        obj__.save()



