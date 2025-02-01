from typing import List
import pandas as pd
from pydantic import BaseModel
import random

from biblexity.configuration import project_configuration
from biblexity.utils import SingletonMeta

class VerseItem(BaseModel):
    text: str
    version: str
    book: str
    chapter: int
    verse: int

    def render(self):
        return f"[{self.version}][{self.book}][{self.chapter}: {self.verse}] {self.text}"

class BibleDataManager(metaclass=SingletonMeta):
    LANG: str = 'french'

    def __init__(self):
        # read bible data
        data = pd.read_json(project_configuration.bible_data_path)
        self.data = data[data['language'] == self.LANG]
        self.data = self.data[self.data['version'] == 'LSG']
        self.verses_item_list: List[VerseItem] = None

    def get_verse(self, version: str, book: str, chapter_number: int, verse_number: int) -> VerseItem:
        verse_df = self.data[(self.data['version'] == version) & (self.data['book_name'] == book) & (self.data['chapter_number'] == chapter_number) & (self.data['verse_number'] == verse_number)]

        verse_item = None
        if verse_df.shape[0] > 0:
            result = verse_df.iloc[0]['verse_text']

            verse_item = VerseItem(
                text = result,
                version = version,
                book = book,
                chapter = chapter_number,
                verse = verse_number
            )

        return verse_item

    def get_all_verses(self) -> List[VerseItem]:

        if not self.verses_item_list:
            verses = self.data.to_dict(orient='records')
            self.verses_item_list = [
                VerseItem(
                    text = verse['verse_text'],
                    version = verse['version'],
                    book = verse['book_name'],
                    chapter = verse['chapter_number'],
                    verse = verse['verse_number']
                )
                for verse in verses
            ]

        return self.verses_item_list

    def get_random_verse(self) -> VerseItem:
        verses_list = self.get_all_verses()
        verse_item = random.choice(verses_list)
        return verse_item


    def get_all_versions(self) -> List[str]:
        return self.data['version'].unique().tolist()


