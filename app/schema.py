from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic_settings import BaseSettings


class Source(BaseModel):
    id: str
    name: str

class ArticleResponse(BaseModel):
    source: Source
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str


class CNNNewsResponse(BaseModel):
    status: str
    totalResults: int
    articles: List[dict]

class NewsSettings(BaseSettings):
    cnn: str
    


class Location(BaseModel):
    city: str
    country: str
    popular_news_channel: Optional[str] = Field(None, alias="popular_news_channel")


class Locations(BaseModel):
    locations: List[Location]


locations_data = {
    "locations": [
        {
            "city": "New York",
            "country": "USA",
            "popular_news_channel": "CNN"
        },
        {
            "city": "London",
            "country": "UK",
            "popular_news_channel": "BBC News"
        },
        {
            "city": "Tokyo",
            "country": "Japan",
            "popular_news_channel": "NHK"
        },
        {
            "city": "Paris",
            "country": "France",
            "popular_news_channel": "France 24"
        },
        {
            "city": "Berlin",
            "country": "Germany"
        }
    ]
}

validated_locations = Locations(**locations_data)
# print(validated_locations)