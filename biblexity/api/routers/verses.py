from typing import List

from fastapi import APIRouter
from biblexity.core.bible_data import BibleDataManager, VerseItem

router = APIRouter(
    prefix='/bible',
    tags=['verses']
)

@router.get('/versions')
def get_all_version():
    return BibleDataManager().get_all_versions()

@router.get('/version/{version}/book/{book}/chapter/{chapter}/verse/{verse}')
def get_verse(book: str, chapter: int, verse: int, version: str = 'BDS') -> VerseItem:
    return BibleDataManager().get_verse(
        version=version,
        book=book,
        chapter_number=chapter,
        verse_number=verse
    )

@router.get('/verse/random')
def get_verse() -> VerseItem:
    return BibleDataManager().get_random_verse()

@router.get('/verse/all')
def get_verse() -> List[VerseItem]:
    return BibleDataManager().get_all_verses()[:10]


