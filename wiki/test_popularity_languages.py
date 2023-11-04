
import pytest

from wiki.dto.wikipedia.PopularityLanguage import PopularityLanguage
from wiki.data.WikipediaParser import get_popularity_of_languages


@pytest.mark.parametrize("min_popularity",
                         [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
def test_popularity(min_popularity: int):
    websites_data: list[PopularityLanguage] = get_popularity_of_languages()

    for website in websites_data:
        if website.popularity < min_popularity:
            assert False, f"{website.name} has {website.popularity} unique visitors per month. (Expected more than {min_popularity})"

    assert True
