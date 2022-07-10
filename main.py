from dotenv import load_dotenv
import os

load_dotenv()
from fastapi import FastAPI
from marvel_connection import connect

app = FastAPI()

""" characters = {
    "code": 200,
    "status": "Ok",
    "copyright": "© 2022 MARVEL",
    "attributionText": "Data provided by Marvel. © 2022 MARVEL",
    "attributionHTML": "<a href=\"http://marvel.com\">Data provided by Marvel. © 2022 MARVEL</a>",
    "etag": "af73d293eaf994869106d7df4b5a2ae344b6f5c7",
    "data": {
        "offset": 0,
        "limit": 20,
        "total": 1562,
        "count": 20,
        "results": [
            {
                "id": 1011334,
                "name": "3-D Man",
                "description": "",
                "modified": "2014-04-29T14:18:17-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/e0/535fecbbb9784",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011334",
                "comics": {
                    "available": 12,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011334/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21366",
                            "name": "Avengers: The Initiative (2007) #14"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24571",
                            "name": "Avengers: The Initiative (2007) #14 (SPOTLIGHT VARIANT)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21546",
                            "name": "Avengers: The Initiative (2007) #15"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21741",
                            "name": "Avengers: The Initiative (2007) #16"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21975",
                            "name": "Avengers: The Initiative (2007) #17"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/22299",
                            "name": "Avengers: The Initiative (2007) #18"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/22300",
                            "name": "Avengers: The Initiative (2007) #18 (ZOMBIE VARIANT)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/22506",
                            "name": "Avengers: The Initiative (2007) #19"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/8500",
                            "name": "Deadpool (1997) #44"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/10223",
                            "name": "Marvel Premiere (1972) #35"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/10224",
                            "name": "Marvel Premiere (1972) #36"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/10225",
                            "name": "Marvel Premiere (1972) #37"
                        }
                    ],
                    "returned": 12
                },
                "series": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011334/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1945",
                            "name": "Avengers: The Initiative (2007 - 2010)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2005",
                            "name": "Deadpool (1997 - 2002)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2045",
                            "name": "Marvel Premiere (1972 - 1981)"
                        }
                    ],
                    "returned": 3
                },
                "stories": {
                    "available": 21,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011334/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19947",
                            "name": "Cover #19947",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19948",
                            "name": "The 3-D Man!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19949",
                            "name": "Cover #19949",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19950",
                            "name": "The Devil's Music!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19951",
                            "name": "Cover #19951",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19952",
                            "name": "Code-Name:  The Cold Warrior!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47184",
                            "name": "AVENGERS: THE INITIATIVE (2007) #14",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47185",
                            "name": "Avengers: The Initiative (2007) #14 - Int",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47498",
                            "name": "AVENGERS: THE INITIATIVE (2007) #15",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47499",
                            "name": "Avengers: The Initiative (2007) #15 - Int",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47792",
                            "name": "AVENGERS: THE INITIATIVE (2007) #16",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47793",
                            "name": "Avengers: The Initiative (2007) #16 - Int",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/48361",
                            "name": "AVENGERS: THE INITIATIVE (2007) #17",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/48362",
                            "name": "Avengers: The Initiative (2007) #17 - Int",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/49103",
                            "name": "AVENGERS: THE INITIATIVE (2007) #18",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/49104",
                            "name": "Avengers: The Initiative (2007) #18 - Int",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/49106",
                            "name": "Avengers: The Initiative (2007) #18, Zombie Variant - Int",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/49888",
                            "name": "AVENGERS: THE INITIATIVE (2007) #19",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/49889",
                            "name": "Avengers: The Initiative (2007) #19 - Int",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/54371",
                            "name": "Avengers: The Initiative (2007) #14, Spotlight Variant - Int",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011334/events",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/269",
                            "name": "Secret Invasion"
                        }
                    ],
                    "returned": 1
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/74/3-d_man?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/3-D_Man_(Chandler)?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1011334/3-d_man?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1017100,
                "name": "A-Bomb (HAS)",
                "description": "Rick Jones has been Hulk's best bud since day one, but now he's more than a friend...he's a teammate! Transformed by a Gamma energy explosion, A-Bomb's thick, armored skin is just as strong and powerful as it is blue. And when he curls into action, he uses it like a giant bowling ball of destruction! ",
                "modified": "2013-09-18T15:54:04-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/3/20/5232158de5b16",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1017100",
                "comics": {
                    "available": 4,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1017100/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/47176",
                            "name": "FREE COMIC BOOK DAY 2013 1 (2013) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40632",
                            "name": "Hulk (2008) #53"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40630",
                            "name": "Hulk (2008) #54"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40628",
                            "name": "Hulk (2008) #55"
                        }
                    ],
                    "returned": 4
                },
                "series": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1017100/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/17765",
                            "name": "FREE COMIC BOOK DAY 2013 1 (2013)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3374",
                            "name": "Hulk (2008 - 2012)"
                        }
                    ],
                    "returned": 2
                },
                "stories": {
                    "available": 7,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1017100/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92078",
                            "name": "Hulk (2008) #55",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92079",
                            "name": "Interior #92079",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92082",
                            "name": "Hulk (2008) #54",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92083",
                            "name": "Interior #92083",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92086",
                            "name": "Hulk (2008) #53",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92087",
                            "name": "Interior #92087",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/105929",
                            "name": "cover from Free Comic Book Day 2013 (Avengers/Hulk) (2013) #1",
                            "type": "cover"
                        }
                    ],
                    "returned": 7
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1017100/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/76/a-bomb?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1017100/a-bomb_has?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1009144,
                "name": "A.I.M.",
                "description": "AIM is a terrorist organization bent on destroying the world.",
                "modified": "2013-10-17T14:41:30-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/6/20/52602f21f29ec",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009144",
                "comics": {
                    "available": 52,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009144/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/36763",
                            "name": "Ant-Man & the Wasp (2010) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17553",
                            "name": "Avengers (1998) #67"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/7340",
                            "name": "Avengers (1963) #87"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/4214",
                            "name": "Avengers and Power Pack Assemble! (2006) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/63217",
                            "name": "Avengers and Power Pack (2017) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/63218",
                            "name": "Avengers and Power Pack (2017) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/63219",
                            "name": "Avengers and Power Pack (2017) #5"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/63220",
                            "name": "Avengers and Power Pack (2017) #6"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/64790",
                            "name": "Avengers by Brian Michael Bendis: The Complete Collection Vol. 2 (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/1170",
                            "name": "Avengers Vol. 2: Red Zone (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/1214",
                            "name": "Avengers Vol. II: Red Zone (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/12787",
                            "name": "Captain America (1998) #28"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/7513",
                            "name": "Captain America (1968) #132"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/7514",
                            "name": "Captain America (1968) #133"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/65466",
                            "name": "Captain America by Mark Waid, Ron Garney & Andy Kubert (Hardcover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20367",
                            "name": "Defenders (1972) #57"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/31068",
                            "name": "Incredible Hulks (2010) #606 (VARIANT)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/46168",
                            "name": "Indestructible Hulk (2012) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/43944",
                            "name": "Iron Man (2012) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/49865",
                            "name": "Iron Man (2012) #1"
                        }
                    ],
                    "returned": 20
                },
                "series": {
                    "available": 34,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009144/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/13082",
                            "name": "Ant-Man & the Wasp (2010 - 2011)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/354",
                            "name": "Avengers (1998 - 2004)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1991",
                            "name": "Avengers (1963 - 1996)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/23123",
                            "name": "Avengers and Power Pack (2017)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1046",
                            "name": "Avengers and Power Pack Assemble! (2006)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/23600",
                            "name": "Avengers by Brian Michael Bendis: The Complete Collection Vol. 2 (2017)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/227",
                            "name": "Avengers Vol. 2: Red Zone (2003)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/271",
                            "name": "Avengers Vol. II: Red Zone (2003)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1996",
                            "name": "Captain America (1968 - 1996)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1997",
                            "name": "Captain America (1998 - 2002)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/23810",
                            "name": "Captain America by Mark Waid, Ron Garney & Andy Kubert (2017)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3743",
                            "name": "Defenders (1972 - 1986)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/8842",
                            "name": "Incredible Hulks (2010 - 2011)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/16583",
                            "name": "Indestructible Hulk (2012 - 2014)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2029",
                            "name": "Iron Man (1968 - 1996)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/16593",
                            "name": "Iron Man (2012 - 2014)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/23915",
                            "name": "Iron Man Epic Collection: Doom (2018)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/9718",
                            "name": "Marvel Adventures Super Heroes (2010 - 2012)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/189",
                            "name": "Marvel Masterworks: Captain America Vol. 1 - 2nd Edition (2003)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1506",
                            "name": "MARVEL MASTERWORKS: CAPTAIN AMERICA VOL. 1 HC (2005)"
                        }
                    ],
                    "returned": 20
                },
                "stories": {
                    "available": 54,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009144/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/5800",
                            "name": "Avengers and Power Pack Assemble! (2006) #2",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/5801",
                            "name": "2 of 4 - 4XLS",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/10253",
                            "name": "When the Unliving Strike",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/10255",
                            "name": "Cover #10255",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/10256",
                            "name": "The Enemy Within!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/10259",
                            "name": "Death Before Dishonor!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/10261",
                            "name": "Cover #10261",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/10262",
                            "name": "The End of A.I.M.!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11921",
                            "name": "The Red Skull Lives!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11930",
                            "name": "He Who Holds the Cosmic Cube",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11936",
                            "name": "The Maddening Mystery of the Inconceivable Adaptoid!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11981",
                            "name": "If This Be... Modok",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11984",
                            "name": "A Time to Die -- A Time to Live!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11995",
                            "name": "At the Mercy of the Maggia",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/15243",
                            "name": "Look Homeward, Avenger",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/17518",
                            "name": "Captain America (1968) #132",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/17519",
                            "name": "The Fearful Secret of Bucky Barnes",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/17520",
                            "name": "Captain America (1968) #133",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/17521",
                            "name": "Madness In the Slums",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28233",
                            "name": "In Sin Airy X",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009144/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/characters/1009144/aim.?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/A.I.M.?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1009144/aim.?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1010699,
                "name": "Aaron Stack",
                "description": "",
                "modified": "1969-12-31T19:00:00-0500",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010699",
                "comics": {
                    "available": 14,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010699/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40776",
                            "name": "Dark Avengers (2012) #177"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40773",
                            "name": "Dark Avengers (2012) #179"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40774",
                            "name": "Dark Avengers (2012) #180"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40778",
                            "name": "Dark Avengers (2012) #181"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40787",
                            "name": "Dark Avengers (2012) #182"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40786",
                            "name": "Dark Avengers (2012) #183"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/38073",
                            "name": "Hulk (2008) #43"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/11910",
                            "name": "Universe X (2000) #6"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/11911",
                            "name": "Universe X (2000) #7"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/11912",
                            "name": "Universe X (2000) #8"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/11913",
                            "name": "Universe X (2000) #9"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/11903",
                            "name": "Universe X (2000) #10"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/11904",
                            "name": "Universe X (2000) #11"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/11905",
                            "name": "Universe X (2000) #12"
                        }
                    ],
                    "returned": 14
                },
                "series": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010699/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/789",
                            "name": "Dark Avengers (2012 - 2013)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3374",
                            "name": "Hulk (2008 - 2012)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2085",
                            "name": "Universe X (2000 - 2001)"
                        }
                    ],
                    "returned": 3
                },
                "stories": {
                    "available": 27,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010699/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25634",
                            "name": "Universe X (2000) #10",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25635",
                            "name": "Interior #25635",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25637",
                            "name": "Universe X (2000) #12",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25638",
                            "name": "Interior #25638",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25647",
                            "name": "Universe X (2000) #6",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25648",
                            "name": "Interior #25648",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25649",
                            "name": "Universe X (2000) #7",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25650",
                            "name": "Interior #25650",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25651",
                            "name": "Universe X (2000) #8",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25652",
                            "name": "Interior #25652",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25653",
                            "name": "Universe X (2000) #9",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/25654",
                            "name": "Interior #25654",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/67100",
                            "name": "Universe X (2000) #11",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/89190",
                            "name": "Hulk (2008) #43",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/90002",
                            "name": "Interior #90002",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92370",
                            "name": "Dark Avengers (2012) #179",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92371",
                            "name": "Interior #92371",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92372",
                            "name": "Dark Avengers (2012) #180",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92373",
                            "name": "Interior #92373",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92376",
                            "name": "Dark Avengers (2012) #177",
                            "type": "cover"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010699/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/2809/aaron_stack?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1010699/aaron_stack?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1009146,
                "name": "Abomination (Emil Blonsky)",
                "description": "Formerly known as Emil Blonsky, a spy of Soviet Yugoslavian origin working for the KGB, the Abomination gained his powers after receiving a dose of gamma radiation similar to that which transformed Bruce Banner into the incredible Hulk.",
                "modified": "2012-03-20T12:32:12-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/50/4ce18691cbf04",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009146",
                "comics": {
                    "available": 54,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009146/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17547",
                            "name": "Avengers (1998) #61"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17548",
                            "name": "Avengers (1998) #62"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/1098",
                            "name": "Avengers Vol. 1: World Trust (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/8557",
                            "name": "Earth X (1999) #7"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/4241",
                            "name": "EARTH X TPB [NEW PRINTING] (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20863",
                            "name": "Hulk (2008) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/2499",
                            "name": "Hulk: Destruction (2005) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14424",
                            "name": "Hulk (1999) #24"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14425",
                            "name": "Hulk (1999) #25"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14428",
                            "name": "Hulk (1999) #28"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14450",
                            "name": "Hulk (1999) #50"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14451",
                            "name": "Hulk (1999) #51"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14453",
                            "name": "Hulk (1999) #53"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14454",
                            "name": "Hulk (1999) #54"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/8948",
                            "name": "Incredible Hulk (1962) #137"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/8982",
                            "name": "Incredible Hulk (1962) #171"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/9005",
                            "name": "Incredible Hulk (1962) #194"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/9006",
                            "name": "Incredible Hulk (1962) #195"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/9007",
                            "name": "Incredible Hulk (1962) #196"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/9011",
                            "name": "Incredible Hulk (1962) #200"
                        }
                    ],
                    "returned": 20
                },
                "series": {
                    "available": 27,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009146/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/354",
                            "name": "Avengers (1998 - 2004)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/158",
                            "name": "Avengers Vol. 1: World Trust (2003)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/378",
                            "name": "Earth X (1999 - 2000)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1806",
                            "name": "EARTH X TPB [NEW PRINTING] (2006)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3374",
                            "name": "Hulk (2008 - 2012)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/465",
                            "name": "Hulk (1999 - 2008)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/924",
                            "name": "Hulk: Destruction (2005)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2021",
                            "name": "Incredible Hulk (1962 - 1999)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2983",
                            "name": "Incredible Hulk Annual (1976 - 1994)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/22424",
                            "name": "Incredible Hulk Epic Collection: The Hulk Must Die (2017)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/212",
                            "name": "Incredible Hulk Vol. 4: Abominable (2003)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/244",
                            "name": "Incredible Hulk Vol. IV: Abominable (2003)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/8842",
                            "name": "Incredible Hulks (2010 - 2011)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2572",
                            "name": "Iron Man (1998 - 2004)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/977",
                            "name": "Irredeemable Ant-Man (2006 - 2007)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2423",
                            "name": "Irredeemable Ant-Man Vol. 1: Low-Life (2007)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3722",
                            "name": "Killraven (2002 - 2003)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2437",
                            "name": "KILLRAVEN PREMIERE HC (2007)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/32108",
                            "name": "Maestro: World War M (2022 - Present)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/21675",
                            "name": "Marvel Cinematic Universe Guidebook: The Avengers Initiative (2017)"
                        }
                    ],
                    "returned": 20
                },
                "stories": {
                    "available": 64,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009146/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4946",
                            "name": "4 of 4 - 4XLS",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/5496",
                            "name": "Irredeemable Ant-Man (2006) #1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/12370",
                            "name": "Cover #12370",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/12372",
                            "name": "Whosoever Harms the Hulk..!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18419",
                            "name": "[none]",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18420",
                            "name": "The Stars Mine Enemy",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18488",
                            "name": "Incredible Hulk (1962) #171",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18489",
                            "name": "Revenge",
                            "type": ""
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18534",
                            "name": "Incredible Hulk (1962) #194",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18535",
                            "name": "The Day of the Locust!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18536",
                            "name": "Incredible Hulk (1962) #195",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18537",
                            "name": "Warfare In Wonderland!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18538",
                            "name": "Incredible Hulk (1962) #196",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18539",
                            "name": "The Abomination Proclamation!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18546",
                            "name": "Incredible Hulk (1962) #200",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18547",
                            "name": "An Intruder In the Mind!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18776",
                            "name": "Cover #18776",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18877",
                            "name": "Incredible Hulk (1962) #364",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18878",
                            "name": "Countdown Part 4: The Abomination",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18881",
                            "name": "Incredible Hulk (1962) #366",
                            "type": "cover"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009146/events",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/296",
                            "name": "Chaos War"
                        }
                    ],
                    "returned": 1
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/81/abomination?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Abomination?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1009146/abomination_emil_blonsky?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1016823,
                "name": "Abomination (Ultimate)",
                "description": "",
                "modified": "2012-07-10T19:11:52-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1016823",
                "comics": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1016823/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40638",
                            "name": "Hulk (2008) #50"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/15717",
                            "name": "Ultimate X-Men (2001) #26"
                        }
                    ],
                    "returned": 2
                },
                "series": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1016823/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3374",
                            "name": "Hulk (2008 - 2012)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/474",
                            "name": "Ultimate X-Men (2001 - 2009)"
                        }
                    ],
                    "returned": 2
                },
                "stories": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1016823/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/31883",
                            "name": "Free Preview of THE INCREDIBLE HULK #50",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92098",
                            "name": "Hulk (2008) #50",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/92099",
                            "name": "Interior #92099",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 3
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1016823/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/81/abomination?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1016823/abomination_ultimate?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1009148,
                "name": "Absorbing Man",
                "description": "",
                "modified": "2013-10-24T14:32:08-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/1/b0/5269678709fb7",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009148",
                "comics": {
                    "available": 96,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009148/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/43507",
                            "name": "A+X (2012) #8"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/7045",
                            "name": "Avengers (1963) #183"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/7046",
                            "name": "Avengers (1963) #184"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/7142",
                            "name": "Avengers (1963) #270"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/36481",
                            "name": "Avengers Academy (2010) #16"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/36480",
                            "name": "Avengers Academy (2010) #17"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/36479",
                            "name": "Avengers Academy (2010) #18"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/36484",
                            "name": "Avengers Academy (2010) #19"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17776",
                            "name": "Avengers Annual (1967) #20"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/63662",
                            "name": "Black Bolt (2017) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/64278",
                            "name": "Black Bolt (2017) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/66533",
                            "name": "Black Bolt (2017) #11"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/65327",
                            "name": "Black Bolt Vol. 1: Hard Time (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/12783",
                            "name": "Captain America (1998) #24"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20427",
                            "name": "Dazzler (1981) #18"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20428",
                            "name": "Dazzler (1981) #19"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/8499",
                            "name": "Deadpool (1997) #43"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/15541",
                            "name": "Fantastic Four (1998) #22"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/13151",
                            "name": "Fantastic Four (1961) #330"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/41433",
                            "name": "Fear Itself (2010) #2 (3rd Printing Variant)"
                        }
                    ],
                    "returned": 20
                },
                "series": {
                    "available": 48,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009148/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/16450",
                            "name": "A+X (2012 - 2014)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1991",
                            "name": "Avengers (1963 - 1996)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/9086",
                            "name": "Avengers Academy (2010 - 2012)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1988",
                            "name": "Avengers Annual (1967 - 1994)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/23121",
                            "name": "Black Bolt (2017 - 2018)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/23778",
                            "name": "Black Bolt Vol. 1: Hard Time (2017)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1997",
                            "name": "Captain America (1998 - 2002)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3745",
                            "name": "Dazzler (1981 - 1986)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2005",
                            "name": "Deadpool (1997 - 2002)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2121",
                            "name": "Fantastic Four (1961 - 1998)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/421",
                            "name": "Fantastic Four (1998 - 2012)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/13691",
                            "name": "Fear Itself (2010 - 2011)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/13857",
                            "name": "Fear Itself: Fellowship of Fear (2011)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/13827",
                            "name": "Fear Itself: The Worthy (2011)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/31372",
                            "name": "Gamma Flight (2021)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/20084",
                            "name": "Heroes for Hire (1997 - 1999)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/465",
                            "name": "Hulk (1999 - 2008)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/20552",
                            "name": "Illuminati (2015 - 2016)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/24278",
                            "name": "Immortal Hulk (2018 - Present)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/24891",
                            "name": "Immortal Hulk Vol. 2: The Green Door (2019)"
                        }
                    ],
                    "returned": 20
                },
                "stories": {
                    "available": 109,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009148/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4988",
                            "name": "1 of 1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/7866",
                            "name": "Punisher War Journal (2006) #4",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/10997",
                            "name": "Journey Into Mystery (1952) #114",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/10998",
                            "name": "The Stronger I Am, the Sooner I Die",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11000",
                            "name": "Journey Into Mystery (1952) #115",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11001",
                            "name": "The Vengeance of the Thunder God",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11022",
                            "name": "Journey Into Mystery (1952) #120",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11023",
                            "name": "With My Hammer In Hand",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11025",
                            "name": "Journey Into Mystery (1952) #121",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11026",
                            "name": "The Power!  The Passion!  The Pride!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11028",
                            "name": "Journey Into Mystery (1952) #122",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11029",
                            "name": "Where Mortals Fear To Tread!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11031",
                            "name": "Journey Into Mystery (1952) #123",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/11032",
                            "name": "While a Universe Trembles",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/12951",
                            "name": "Fantastic Four (1961) #330",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/12952",
                            "name": "Good Dreams!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/14628",
                            "name": "Avengers (1963) #183",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/14630",
                            "name": "Avengers (1963) #184",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/14823",
                            "name": "Avengers (1963) #270",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/16688",
                            "name": "Thor (1966) #206",
                            "type": "cover"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 4,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009148/events",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/238",
                            "name": "Civil War"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/302",
                            "name": "Fear Itself"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/270",
                            "name": "Secret Wars"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/273",
                            "name": "Siege"
                        }
                    ],
                    "returned": 4
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/84/absorbing_man?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Absorbing_Man?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1009148/absorbing_man?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1009149,
                "name": "Abyss",
                "description": "",
                "modified": "2014-04-29T14:10:43-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/30/535feab462a64",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009149",
                "comics": {
                    "available": 8,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009149/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/13943",
                            "name": "Uncanny X-Men (1963) #402"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/13945",
                            "name": "Uncanny X-Men (1963) #404"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/13946",
                            "name": "Uncanny X-Men (1963) #405"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/13947",
                            "name": "Uncanny X-Men (1963) #406"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/13970",
                            "name": "Uncanny X-Men (1963) #429"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/13972",
                            "name": "Uncanny X-Men (1963) #431"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/12386",
                            "name": "X-Men: Alpha (1995) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/2539",
                            "name": "X-Men: The Complete Age of Apocalypse Epic Book 2 (Trade Paperback)"
                        }
                    ],
                    "returned": 8
                },
                "series": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009149/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2258",
                            "name": "Uncanny X-Men (1963 - 2011)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2104",
                            "name": "X-Men: Alpha (1995)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1583",
                            "name": "X-Men: The Complete Age of Apocalypse Epic Book 2 (2005)"
                        }
                    ],
                    "returned": 3
                },
                "stories": {
                    "available": 8,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009149/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/26281",
                            "name": "A Beginning",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28352",
                            "name": "Utility of Myth",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28356",
                            "name": "Army Ants",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28358",
                            "name": "Ballroom Blitzkrieg",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28360",
                            "name": "Staring Contests are for Suckers",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28407",
                            "name": "The Draco Part One: Sins of the Father",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28411",
                            "name": "The Draco Part Three",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28413",
                            "name": "The Draco Part Four",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 8
                },
                "events": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009149/events",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/227",
                            "name": "Age of Apocalypse"
                        }
                    ],
                    "returned": 1
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/85/abyss?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Abyss_(alien)?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1009149/abyss?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1010903,
                "name": "Abyss (Age of Apocalypse)",
                "description": "",
                "modified": "1969-12-31T19:00:00-0500",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/3/80/4c00358ec7548",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010903",
                "comics": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010903/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/18099",
                            "name": "Weapon X (1995) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/12386",
                            "name": "X-Men: Alpha (1995) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/2539",
                            "name": "X-Men: The Complete Age of Apocalypse Epic Book 2 (Trade Paperback)"
                        }
                    ],
                    "returned": 3
                },
                "series": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010903/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3635",
                            "name": "Weapon X (1995)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2104",
                            "name": "X-Men: Alpha (1995)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1583",
                            "name": "X-Men: The Complete Age of Apocalypse Epic Book 2 (2005)"
                        }
                    ],
                    "returned": 3
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010903/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/26280",
                            "name": "X-Men: Alpha (1994) #1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/38448",
                            "name": "X-Facts",
                            "type": ""
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010903/events",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/227",
                            "name": "Age of Apocalypse"
                        }
                    ],
                    "returned": 1
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/85/abyss?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Abyss_(Age_of_Apocalypse)?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1010903/abyss_age_of_apocalypse?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1011266,
                "name": "Adam Destine",
                "description": "",
                "modified": "1969-12-31T19:00:00-0500",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011266",
                "comics": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011266/comics",
                    "items": [],
                    "returned": 0
                },
                "series": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011266/series",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011266/stories",
                    "items": [],
                    "returned": 0
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011266/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/2902/adam_destine?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Destine,_Adam?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1011266/adam_destine?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1010354,
                "name": "Adam Warlock",
                "description": "Adam Warlock is an artificially created human who was born in a cocoon at a scientific complex called The Beehive.",
                "modified": "2013-08-07T13:49:06-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/a/f0/5202887448860",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010354",
                "comics": {
                    "available": 188,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010354/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/62151",
                            "name": "All-New Guardians of the Galaxy Vol. 3: Infinity Quest (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17271",
                            "name": "Annihilation: Conquest (2007) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17405",
                            "name": "Annihilation: Conquest (2007) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17645",
                            "name": "Annihilation: Conquest (2007) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20686",
                            "name": "Annihilation: Conquest (2007) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20885",
                            "name": "Annihilation: Conquest (2007) #5"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21016",
                            "name": "Annihilation: Conquest (2007) #6"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/12412",
                            "name": "Avengers Forever (1998) #9"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/1033",
                            "name": "Avengers Legends Vol. I: Avengers Forever (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20731",
                            "name": "CLANDESTINE CLASSIC PREMIERE HC (Hardcover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20187",
                            "name": "Doctor Strange, Sorcerer Supreme (1988) #27"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20193",
                            "name": "Doctor Strange, Sorcerer Supreme (1988) #32"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/20197",
                            "name": "Doctor Strange, Sorcerer Supreme (1988) #36"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/8552",
                            "name": "Earth X (1999) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/8550",
                            "name": "Earth X (1999) #11"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/4241",
                            "name": "EARTH X TPB [NEW PRINTING] (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/12975",
                            "name": "Fantastic Four (1961) #172"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/13195",
                            "name": "Fantastic Four (1961) #370"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/25305",
                            "name": "Guardians of the Galaxy (2008) #17"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/65547",
                            "name": "All-New Guardians of the Galaxy (2017) #150"
                        }
                    ],
                    "returned": 20
                },
                "series": {
                    "available": 82,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010354/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/23058",
                            "name": "All-New Guardians of the Galaxy (2017)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/22778",
                            "name": "All-New Guardians of the Galaxy Vol. 3: Infinity Quest (2018)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3061",
                            "name": "Annihilation: Conquest (2007)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2111",
                            "name": "Avengers Forever (1998 - 1999)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/93",
                            "name": "Avengers Legends Vol. I: Avengers Forever (2002)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3874",
                            "name": "CLANDESTINE CLASSIC PREMIERE HC (2008)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3741",
                            "name": "Doctor Strange, Sorcerer Supreme (1988 - 1996)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/378",
                            "name": "Earth X (1999 - 2000)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1806",
                            "name": "EARTH X TPB [NEW PRINTING] (2006)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2121",
                            "name": "Fantastic Four (1961 - 1998)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/4885",
                            "name": "Guardians of the Galaxy (2008 - 2010)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/27554",
                            "name": "Guardians Of The Galaxy Annual (2019)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/26496",
                            "name": "Guardians Of The Galaxy Vol. 2: Faithless (2020)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/22422",
                            "name": "GUARDIANS OF THE GALAXY: ROAD TO ANNIHILATION VOL. 2 TPB (2017)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2021",
                            "name": "Incredible Hulk (1962 - 1999)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2983",
                            "name": "Incredible Hulk Annual (1976 - 1994)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/26307",
                            "name": "Infinity By Starlin & Hickman (2019)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/24050",
                            "name": "Infinity Countdown (2018)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/24300",
                            "name": "Infinity Countdown Prime (2018)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/23991",
                            "name": "Infinity Countdown: Adam Warlock (2018)"
                        }
                    ],
                    "returned": 20
                },
                "stories": {
                    "available": 217,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010354/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1412",
                            "name": "Cover #1412",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1602",
                            "name": "Cover #1602",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1800",
                            "name": "Cover #1800",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1842",
                            "name": "Cover #1842",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/3758",
                            "name": "WARLOCK (2004) #3",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/3760",
                            "name": "WARLOCK (2004) #1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/3762",
                            "name": "WARLOCK (2004) #2",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/3764",
                            "name": "WARLOCK (2004) #4",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/12568",
                            "name": "Fantastic Four (1961) #172",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/12569",
                            "name": "Cry, the Bedeviled Planet!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/13121",
                            "name": "Forever Evil",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18500",
                            "name": "Incredible Hulk (1962) #177",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18501",
                            "name": "Peril of the Paired Planets",
                            "type": ""
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/18503",
                            "name": "Triumph On Terra-Two",
                            "type": ""
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19847",
                            "name": "Cover #19847",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19848",
                            "name": "Performance",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19859",
                            "name": "Days of Future Present Part 4",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19860",
                            "name": "You Must Remember This",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19883",
                            "name": "The Adventures of Lockheed the Space Dragon and His Pet Girl, Kitty",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/19884",
                            "name": "The Saga of Storm: Goddess of Thunder",
                            "type": "cover"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 8,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010354/events",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/293",
                            "name": "Annihilation: Conquest"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/233",
                            "name": "Atlantis Attacks"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/235",
                            "name": "Blood and Thunder"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/240",
                            "name": "Days of Future Present"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/29",
                            "name": "Infinity War"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/263",
                            "name": "Mutant Massacre"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/271",
                            "name": "Secret Wars II"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/280",
                            "name": "X-Tinction Agenda"
                        }
                    ],
                    "returned": 8
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/2854/adam_warlock?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Warlock,_Adam?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1010354/adam_warlock?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1010846,
                "name": "Aegis (Trey Rollins)",
                "description": "",
                "modified": "1969-12-31T19:00:00-0500",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/5/e0/4c0035c9c425d",
                    "extension": "gif"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010846",
                "comics": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010846/comics",
                    "items": [],
                    "returned": 0
                },
                "series": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010846/series",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010846/stories",
                    "items": [],
                    "returned": 0
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1010846/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/95/aegis?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Aegis_%28Trey_Rollins%29?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1010846/aegis_trey_rollins?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1017851,
                "name": "Aero (Aero)",
                "description": "",
                "modified": "2021-08-27T17:52:34-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1017851",
                "comics": {
                    "available": 28,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1017851/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76349",
                            "name": "Aero (2019) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76350",
                            "name": "Aero (2019) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76351",
                            "name": "Aero (2019) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76352",
                            "name": "Aero (2019) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76353",
                            "name": "Aero (2019) #5"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76354",
                            "name": "Aero (2019) #6"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76355",
                            "name": "Aero (2019) #7"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76356",
                            "name": "Aero (2019) #8"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76357",
                            "name": "Aero (2019) #9"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76358",
                            "name": "Aero (2019) #10"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76359",
                            "name": "Aero (2019) #11"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/76360",
                            "name": "Aero (2019) #12"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/77001",
                            "name": "Agents of Atlas (2019) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/77003",
                            "name": "Agents of Atlas (2019) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/77005",
                            "name": "Agents of Atlas (2019) #5"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/83989",
                            "name": "Atlantis Attacks (2020) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/83993",
                            "name": "Atlantis Attacks (2020) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/83994",
                            "name": "Atlantis Attacks (2020) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/83995",
                            "name": "Atlantis Attacks (2020) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/83996",
                            "name": "Atlantis Attacks (2020) #5"
                        }
                    ],
                    "returned": 20
                },
                "series": {
                    "available": 5,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1017851/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/27392",
                            "name": "Aero (2019 - 2020)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/27624",
                            "name": "Agents of Atlas (2019)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/29600",
                            "name": "Atlantis Attacks (2020)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/31376",
                            "name": "King In Black: Black Knight (2021)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/28381",
                            "name": "The Marvels (2021 - Present)"
                        }
                    ],
                    "returned": 5
                },
                "stories": {
                    "available": 28,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1017851/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169570",
                            "name": "cover from Aero (2019) #1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169572",
                            "name": "cover from Aero (2019) #2",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169574",
                            "name": "cover from Aero (2019) #3",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169576",
                            "name": "cover from Aero (2019) #4",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169578",
                            "name": "cover from Aero (2019) #5",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169580",
                            "name": "cover from Aero (2019) #6",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169582",
                            "name": "cover from Aero (2019) #7",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169584",
                            "name": "cover from Aero (2019) #8",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169586",
                            "name": "cover from Aero (2019) #9",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169588",
                            "name": "cover from Aero (2019) #10",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169590",
                            "name": "cover from Aero (2019) #11",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/169592",
                            "name": "cover from Aero (2019) #12",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/170874",
                            "name": "cover from New Agents of Atlas (2019) #1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/170878",
                            "name": "cover from New Agents of Atlas (2019) #3",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/170882",
                            "name": "cover from New Agents of Atlas (2019) #5",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/178282",
                            "name": "cover from The Marvels (2029) #2",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/178288",
                            "name": "cover from The Marvels (2029) #4",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/178290",
                            "name": "cover from The Marvels (2029) #5",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/178294",
                            "name": "cover from The Marvels (2029) #7",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/178296",
                            "name": "cover from The Marvels (2029) #8",
                            "type": "cover"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1017851/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/characters/1017851/aero_aero?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1017851/aero_aero?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1012717,
                "name": "Agatha Harkness",
                "description": "",
                "modified": "2021-08-06T11:30:56-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/a0/4ce5a9bf70e19",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1012717",
                "comics": {
                    "available": 19,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1012717/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17751",
                            "name": "Avengers (1996) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17756",
                            "name": "Avengers (1996) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17757",
                            "name": "Avengers (1996) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17758",
                            "name": "Avengers (1996) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17762",
                            "name": "Avengers (1996) #8"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21358",
                            "name": "Avengers Fairy Tales (2008) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/77235",
                            "name": "Captain America (2018) #19"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/13304",
                            "name": "Fantastic Four (1961) #94"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/4203",
                            "name": "Marvel Masterworks: The Fantastic Four Vol.10 (Hardcover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/54974",
                            "name": "Scarlet Witch (1994) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/57094",
                            "name": "Scarlet Witch (2015) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/54977",
                            "name": "Scarlet Witch (1994) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/54978",
                            "name": "Scarlet Witch (1994) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/60028",
                            "name": "Scarlet Witch (2015) #13"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21182",
                            "name": "Ultimate Fantastic Four (2003) #54"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21332",
                            "name": "Ultimate Fantastic Four (2003) #55"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21510",
                            "name": "Ultimate Fantastic Four (2003) #56"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/18460",
                            "name": "Vision and the Scarlet Witch (1985) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/18458",
                            "name": "Vision and the Scarlet Witch (1985) #12"
                        }
                    ],
                    "returned": 19
                },
                "series": {
                    "available": 9,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1012717/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3621",
                            "name": "Avengers (1996 - 1997)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3971",
                            "name": "Avengers Fairy Tales (2008)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/24503",
                            "name": "Captain America (2018 - Present)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2121",
                            "name": "Fantastic Four (1961 - 1998)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1693",
                            "name": "Marvel Masterworks: The Fantastic Four Vol.10 (2006)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/20338",
                            "name": "Scarlet Witch (1994)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/20854",
                            "name": "Scarlet Witch (2015 - 2017)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/702",
                            "name": "Ultimate Fantastic Four (2003 - 2009)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3655",
                            "name": "Vision and the Scarlet Witch (1985 - 1986)"
                        }
                    ],
                    "returned": 9
                },
                "stories": {
                    "available": 23,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1012717/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/13503",
                            "name": "The Return of the Frightful Four",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37673",
                            "name": "Avengers (1996) #1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37688",
                            "name": "Avengers (1996) #2",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37690",
                            "name": "Avengers (1996) #3",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37693",
                            "name": "Avengers (1996) #4",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37701",
                            "name": "Avengers (1996) #8",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/39320",
                            "name": "VISION AND THE SCARLET WITCH (1985) #12",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/39325",
                            "name": "Ancestors",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/46790",
                            "name": "Ultimate Fantastic Four (2003) #54",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/46791",
                            "name": "Namor War 1 of 4",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47112",
                            "name": "Ultimate Fantastic Four (2003) #55",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47113",
                            "name": "Namor War 2 of 4",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47169",
                            "name": "Avengers Fairy Tales (2008) #4",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47170",
                            "name": "The Wizard of Oz",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47425",
                            "name": "Ultimate Fantastic Four (2003) #56",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/47426",
                            "name": "3 of 4 - Salem Seven",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/125005",
                            "name": "cover from Scarlet Witch (2016) #1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/130587",
                            "name": "cover from Scarlet Witch (2015) #13",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/135317",
                            "name": "interior to Scarlet Witch (1994) #1",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/135321",
                            "name": "interior to Scarlet Witch (1994) #3",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1012717/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/characters/1012717/agatha_harkness?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Agatha%20Harkness?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1012717/agatha_harkness?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1011297,
                "name": "Agent Brand",
                "description": "",
                "modified": "2013-10-24T13:09:30-0400",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/4/60/52695285d6e7e",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011297",
                "comics": {
                    "available": 27,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011297/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/6120",
                            "name": "Astonishing X-Men (2004) #21"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/6309",
                            "name": "Astonishing X-Men (2004) #22"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/16119",
                            "name": "Astonishing X-Men (2004) #23"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17353",
                            "name": "Astonishing X-Men (2004) #24"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24503",
                            "name": "Astonishing X-Men (2004) #32"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24504",
                            "name": "Astonishing X-Men (2004) #33"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/38318",
                            "name": "Astonishing X-Men (2004) #38"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/38319",
                            "name": "Astonishing X-Men (2004) #40"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/40024",
                            "name": "Astonishing X-Men (2004) #40 (I Am Captain America Variant)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/45950",
                            "name": "Cable and X-Force (2012) #8"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/39890",
                            "name": "Heralds (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/90340",
                            "name": "S.W.O.R.D. (2020) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/90341",
                            "name": "S.W.O.R.D. (2020) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/26232",
                            "name": "S.W.O.R.D. (2009) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/26233",
                            "name": "S.W.O.R.D. (2009) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/90342",
                            "name": "S.W.O.R.D. (2020) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/26234",
                            "name": "S.W.O.R.D. (2009) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/90343",
                            "name": "S.W.O.R.D. (2020) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/30518",
                            "name": "S.W.O.R.D. (2009) #5"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/90344",
                            "name": "S.W.O.R.D. (2020) #5"
                        }
                    ],
                    "returned": 20
                },
                "series": {
                    "available": 7,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011297/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/744",
                            "name": "Astonishing X-Men (2004 - 2013)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/16907",
                            "name": "Cable and X-Force (2012 - 2014)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/13065",
                            "name": "Heralds (2010)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/31083",
                            "name": "S.W.O.R.D. (2020 - Present)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/8233",
                            "name": "S.W.O.R.D. (2009 - 2010)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/22551",
                            "name": "The Mighty Captain Marvel (2017 - 2018)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/32962",
                            "name": "X-Men Red (2022 - Present)"
                        }
                    ],
                    "returned": 7
                },
                "stories": {
                    "available": 31,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011297/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/3353",
                            "name": "Interior #3353",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/7670",
                            "name": "ASTONISHING X-MEN (2004) #21",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/8144",
                            "name": "ASTONISHING X-MEN (2004) #22",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/32919",
                            "name": "ASTONISHING X-MEN (2004) #23",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/36374",
                            "name": "ASTONISHING X-MEN (2004) #24",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/54039",
                            "name": "ASTONISHING X-MEN (2004) #32",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/54041",
                            "name": "ASTONISHING X-MEN (2004) #33",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/57763",
                            "name": "S.W.O.R.D. (2009) #2",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/57765",
                            "name": "S.W.O.R.D. (2009) #3",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/57767",
                            "name": "S.W.O.R.D. (2009) #4",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/69862",
                            "name": "S.W.O.R.D. (2009) #5",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/89830",
                            "name": "ASTONISHING X-MEN (2004) #38",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/89900",
                            "name": "Astonishing X-Men (2004) #38",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/90548",
                            "name": "Heralds TPB",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/90819",
                            "name": "Interior #90819",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/90853",
                            "name": " Interior  Astonishing X-Men (2004) #40",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/90944",
                            "name": "ASTONISHING X-MEN (2004) #40",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/103418",
                            "name": "Cable and X-Force (2012) #8",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/103419",
                            "name": "story from Cable and X-Force (2012) #8",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/133289",
                            "name": "cover from Captain Marvel (2016) #5",
                            "type": "cover"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011297/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/characters/1011297/agent_brand?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Agent_Brand?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1011297/agent_brand?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1011031,
                "name": "Agent X (Nijo)",
                "description": "Originally a partner of the mind-altering assassin Black Swan, Nijo spied on Deadpool as part of the Swan's plan to exact revenge for Deadpool falsely taking credit for the Swan's assassination of the Four Winds crime family, which included Nijo's brother.",
                "modified": "1969-12-31T19:00:00-0500",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011031",
                "comics": {
                    "available": 18,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011031/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17702",
                            "name": "Agent X (2002) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17709",
                            "name": "Agent X (2002) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17710",
                            "name": "Agent X (2002) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17711",
                            "name": "Agent X (2002) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17712",
                            "name": "Agent X (2002) #5"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17713",
                            "name": "Agent X (2002) #6"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17714",
                            "name": "Agent X (2002) #7"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17715",
                            "name": "Agent X (2002) #8"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17716",
                            "name": "Agent X (2002) #9"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17703",
                            "name": "Agent X (2002) #10"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17704",
                            "name": "Agent X (2002) #11"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17705",
                            "name": "Agent X (2002) #12"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17706",
                            "name": "Agent X (2002) #13"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/17707",
                            "name": "Agent X (2002) #14"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/394",
                            "name": "Agent X (2002) #15"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/1649",
                            "name": "Cable & Deadpool (2004) #12"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/21845",
                            "name": "Cable & Deadpool (2004) #46 (Zombie Variant)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/5761",
                            "name": "Cable & Deadpool Vol. 2: The Burnt Offering (Trade Paperback)"
                        }
                    ],
                    "returned": 18
                },
                "series": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011031/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/459",
                            "name": "Agent X (2002 - 2004)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/693",
                            "name": "Cable & Deadpool (2004 - 2008)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1338",
                            "name": "Cable & Deadpool Vol. 2: The Burnt Offering (2007)"
                        }
                    ],
                    "returned": 3
                },
                "stories": {
                    "available": 23,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011031/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1135",
                            "name": "AGENT X (2002) #15",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2484",
                            "name": "CABLE & DEADPOOL (2004) #12",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37514",
                            "name": "AGENT X (2002) #1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37515",
                            "name": "Dead Man's Switch Part One",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37516",
                            "name": "AGENT X (2002) #10",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37518",
                            "name": "AGENT X (2002) #11",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37521",
                            "name": "AGENT X (2002) #13",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37523",
                            "name": "AGENT X (2002) #14",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37525",
                            "name": "AGENT X (2002) #2",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37526",
                            "name": "Dead Man's Switch Part Two",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37527",
                            "name": "AGENT X (2002) #3",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37528",
                            "name": "Dead Man's Switch Part Three",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37529",
                            "name": "AGENT X (2002) #4",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37530",
                            "name": "Dead Man's Switch Part Four",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37531",
                            "name": "AGENT X (2002) #5",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37532",
                            "name": "Dead Man's Switch Part Five",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37533",
                            "name": "AGENT X (2002) #6",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37534",
                            "name": "Dead Man's Switch Part Six",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/37535",
                            "name": "AGENT X (2002) #7",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/67703",
                            "name": "AGENT X (2002) #12",
                            "type": "cover"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011031/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/101/agent_x?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Agent_X_(Nijo)?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1011031/agent_x_nijo?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1009150,
                "name": "Agent Zero",
                "description": "",
                "modified": "1969-12-31T19:00:00-0500",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/60/4c0042121d790",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009150",
                "comics": {
                    "available": 29,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009150/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/100853",
                            "name": "Life of Wolverine Infinity Comic (2022) #6"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/18082",
                            "name": "Weapon X (2002) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/18092",
                            "name": "Weapon X (2002) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/18074",
                            "name": "Weapon X (2002) #12"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/246",
                            "name": "Weapon X (2002) #13"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/2204",
                            "name": "Weapon X: Days of Future Now (2005) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/2324",
                            "name": "Weapon X: Days of Future Now (2005) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/2438",
                            "name": "Weapon X: Days of Future Now (2005) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/2439",
                            "name": "Weapon X: Days of Future Now (2005) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/3016",
                            "name": "Weapon X: Days of Future Now (2005) #5"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/3357",
                            "name": "Weapon X: Days of Future Now (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/18408",
                            "name": "Weapon X: The Draft – Agent Zero (2002) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14182",
                            "name": "Wolverine (1988) #60"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14183",
                            "name": "Wolverine (1988) #61"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14184",
                            "name": "Wolverine (1988) #62"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14185",
                            "name": "Wolverine (1988) #63"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14186",
                            "name": "Wolverine (1988) #64"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14189",
                            "name": "Wolverine (1988) #67"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14190",
                            "name": "Wolverine (1988) #68"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/14211",
                            "name": "Wolverine (1988) #87"
                        }
                    ],
                    "returned": 20
                },
                "series": {
                    "available": 10,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009150/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/34445",
                            "name": "Life of Wolverine Infinity Comic (2022 - Present)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/543",
                            "name": "Weapon X (2002 - 2004)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/869",
                            "name": "Weapon X: Days of Future Now (2005)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1478",
                            "name": "Weapon X: Days of Future Now (2006)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3649",
                            "name": "Weapon X: The Draft – Agent Zero (2002)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2262",
                            "name": "Wolverine (1988 - 2003)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/84",
                            "name": "WOLVERINE/DEADPOOL: WEAPON X TPB (1999)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3643",
                            "name": "X-Man (1995 - 2000)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/2265",
                            "name": "X-Men (1991 - 2001)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/3637",
                            "name": "X-Men Unlimited (1993 - 2003)"
                        }
                    ],
                    "returned": 10
                },
                "stories": {
                    "available": 31,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009150/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1131",
                            "name": "WEAPON X (2002) #13",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4603",
                            "name": "1 of 5 - 5XLS",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4605",
                            "name": "2 of 5 - 5XLS",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4606",
                            "name": "3 of 5 - 5XLS",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4608",
                            "name": "4 of 5 - 5XLS",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4610",
                            "name": "5 of 5 - 5XLS",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28706",
                            "name": "The Hunted Part 2",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28712",
                            "name": "The Hunted Part 5",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28738",
                            "name": "The Logan Files Epilogue",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28881",
                            "name": "Counting Coup",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28883",
                            "name": "Nightmare Quest!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28885",
                            "name": "Reunion!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28887",
                            "name": "Bastions of Glory!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28889",
                            "name": "What Goes Around...",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28895",
                            "name": "Valley O' Death",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28897",
                            "name": "Epsilon Red",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/28941",
                            "name": "Showdown In Lowtown",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/29125",
                            "name": "Last Stand",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/29139",
                            "name": "Over...Again",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/38511",
                            "name": "Second Contact",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009150/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/102/agent_zero?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Agent_Zero?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1009150/agent_zero?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1011198,
                "name": "Agents of Atlas",
                "description": "",
                "modified": "2016-02-03T10:25:22-0500",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/a0/4ce18a834b7f5",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011198",
                "comics": {
                    "available": 45,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011198/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/77001",
                            "name": "Agents of Atlas (2019) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/23659",
                            "name": "Agents of Atlas (2009) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/4801",
                            "name": "Agents of Atlas (2006) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/23660",
                            "name": "Agents of Atlas (2009) #1 (50/50 COVER)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/5089",
                            "name": "Agents of Atlas (2006) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/23825",
                            "name": "Agents of Atlas (2009) #2"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/27402",
                            "name": "Agents of Atlas (2009) #2 (BACHALO 2ND PRINTING VARIANT)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/23824",
                            "name": "Agents of Atlas (2009) #2 (MCGUINNESS VARIANT)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/5241",
                            "name": "Agents of Atlas (2006) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24015",
                            "name": "Agents of Atlas (2009) #3"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24016",
                            "name": "Agents of Atlas (2009) #3 (MCGUINNESS VARIANT)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24017",
                            "name": "Agents of Atlas (2009) #3 (Wolverine Art Appreciation Variant)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/5404",
                            "name": "Agents of Atlas (2006) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24219",
                            "name": "Agents of Atlas (2009) #4"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/5665",
                            "name": "Agents of Atlas (2006) #5"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24221",
                            "name": "Agents of Atlas (2009) #5"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24222",
                            "name": "Agents of Atlas (2009) #5 (MCGUINNESS VARIANT)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/5842",
                            "name": "Agents of Atlas (2006) #6"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24360",
                            "name": "Agents of Atlas (2009) #6"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/24361",
                            "name": "Agents of Atlas (2009) #7"
                        }
                    ],
                    "returned": 20
                },
                "series": {
                    "available": 13,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011198/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/27624",
                            "name": "Agents of Atlas (2019)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1097",
                            "name": "Agents of Atlas (2006 - 2007)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/6807",
                            "name": "Agents of Atlas (2009)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1980",
                            "name": "AGENTS OF ATLAS PREMIERE HC (2007)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/24134",
                            "name": "Agents of Atlas: The Complete Collection Vol. 1 (2018)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/29600",
                            "name": "Atlantis Attacks (2020)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/9782",
                            "name": "Atlas (2010)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/9181",
                            "name": "Avengers Vs. Atlas (2010)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/6415",
                            "name": "Dark Reign: New Nation (2008)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/27620",
                            "name": "Incoming! (2019)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/27505",
                            "name": "War of the Realms: New Agents of Atlas (2019)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/27374",
                            "name": "War Of The Realms: New Agents Of Atlas (2019)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/22365",
                            "name": "Wolverine: Prehistory (2017)"
                        }
                    ],
                    "returned": 13
                },
                "stories": {
                    "available": 52,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011198/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6008",
                            "name": "1 of 6 - 6 XLS-",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6009",
                            "name": "1 of 6 - 6 XLS-",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6010",
                            "name": "2 of 6 - 6 XLS -",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6011",
                            "name": "2 of 6 - 6 XLS -",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6012",
                            "name": "3 of 6 - 6 XLS -",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6013",
                            "name": "3 of 6 - 6 XLS -",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6014",
                            "name": "4 of 6 - 6 XLS -",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6015",
                            "name": "4 of 6 - 6 XLS -",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6016",
                            "name": "5 of 6 - 6 XLS -",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6017",
                            "name": "5 of 6 - 6 XLS -",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6018",
                            "name": "5 of 6 - Story A - 6XLS",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/6019",
                            "name": "5 of 6 - Story A - 6XLS",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/51050",
                            "name": "1 of 1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/52393",
                            "name": "1 of 3",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/52395",
                            "name": "1 of 3",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/52861",
                            "name": "2 of 3",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/52863",
                            "name": "2 of 3",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/53263",
                            "name": "3 of 3",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/53265",
                            "name": "3 of 3",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/53266",
                            "name": "3 of 3",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 20
                },
                "events": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011198/events",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/318",
                            "name": "Dark Reign"
                        }
                    ],
                    "returned": 1
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/characters/1011198/agents_of_atlas?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Agents_of_Atlas?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1011198/agents_of_atlas?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1011175,
                "name": "Aginar",
                "description": "",
                "modified": "1969-12-31T19:00:00-0500",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011175",
                "comics": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011175/comics",
                    "items": [],
                    "returned": 0
                },
                "series": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011175/series",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011175/stories",
                    "items": [],
                    "returned": 0
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011175/events",
                    "items": [],
                    "returned": 0
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/105/aginar?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Aginar?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1011175/aginar?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            },
            {
                "id": 1011136,
                "name": "Air-Walker (Gabriel Lan)",
                "description": "",
                "modified": "1969-12-31T19:00:00-0500",
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011136",
                "comics": {
                    "available": 4,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011136/comics",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/4108",
                            "name": "Annihilation: Silver Surfer (2006) #1"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/5589",
                            "name": "Heroes Reborn: Iron Man (Trade Paperback)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/16330",
                            "name": "Iron Man (1996) #11"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/comics/16331",
                            "name": "Iron Man (1996) #12"
                        }
                    ],
                    "returned": 4
                },
                "series": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011136/series",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1078",
                            "name": "Annihilation: Silver Surfer (2006)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/1814",
                            "name": "Heroes Reborn: Iron Man (2006)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/series/13577",
                            "name": "Iron Man (1996 - 1998)"
                        }
                    ],
                    "returned": 3
                },
                "stories": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011136/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/5925",
                            "name": "Annihilation: Silver Surfer (2006) #1",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/34082",
                            "name": "Magical Mystery Tour",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/34085",
                            "name": "Matters of the Heart",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 3
                },
                "events": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011136/events",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/events/229",
                            "name": "Annihilation"
                        }
                    ],
                    "returned": 1
                },
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/characters/109/air-walker?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "wiki",
                        "url": "http://marvel.com/universe/Air-Walker_(Gabriel_Lan)?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "comiclink",
                        "url": "http://marvel.com/comics/characters/1011136/air-walker_gabriel_lan?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ]
            }
        ]
    }
}
 """
comics = [
            {
                "id": 82967,
                "digitalId": 0,
                "title": "Marvel Previews (2017)",
                "issueNumber": 0,
                "variantDescription": "",
                "description": "",
                "modified": "2019-11-07T08:46:15-0500",
                "isbn": "",
                "upc": "75960608839302811",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "",
                "pageCount": 112,
                "textObjects": [],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/82967",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/82967/marvel_previews_2017?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/23665",
                    "name": "Marvel Previews (2017 - Present)"
                },
                "variants": [
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/82965",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/82970",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/82969",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/74697",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/72736",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/75668",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/65364",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/65158",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/65028",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/75662",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/74320",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/73776",
                        "name": "Marvel Previews (2017)"
                    }
                ],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2099-10-30T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "2019-10-07T00:00:00-0400"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 0
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "images": [],
                "creators": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82967/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/10021",
                            "name": "Jim Nausedas",
                            "role": "editor"
                        }
                    ],
                    "returned": 1
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82967/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82967/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/183698",
                            "name": "cover from Marvel Previews (2017)",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/183699",
                            "name": "story from Marvel Previews (2017)",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82967/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 82965,
                "digitalId": 0,
                "title": "Marvel Previews (2017)",
                "issueNumber": 0,
                "variantDescription": "",
                "description": "",
                "modified": "2019-08-21T17:11:27-0400",
                "isbn": "",
                "upc": "75960608839302611",
                "diamondCode": "JUL190068",
                "ean": "",
                "issn": "",
                "format": "",
                "pageCount": 152,
                "textObjects": [],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/82965",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/82965/marvel_previews_2017?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/23665",
                    "name": "Marvel Previews (2017 - Present)"
                },
                "variants": [
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/82967",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/82970",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/82969",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/74697",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/72736",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/75668",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/65364",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/65158",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/65028",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/75662",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/74320",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/73776",
                        "name": "Marvel Previews (2017)"
                    }
                ],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2099-08-28T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "2019-08-05T00:00:00-0400"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 0
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "images": [],
                "creators": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82965/creators",
                    "items": [],
                    "returned": 0
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82965/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82965/stories",
                    "items": [],
                    "returned": 0
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82965/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 82970,
                "digitalId": 0,
                "title": "Marvel Previews (2017)",
                "issueNumber": 0,
                "variantDescription": "",
                "description": "",
                "modified": "2020-02-07T09:35:32-0500",
                "isbn": "",
                "upc": "75960608839303111",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "",
                "pageCount": 112,
                "textObjects": [],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/82970",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/82970/marvel_previews_2017?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    },
                    {
                        "type": "purchase",
                        "url": "http://comicstore.marvel.com/Marvel-Previews-0/digital-comic/52952?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/23665",
                    "name": "Marvel Previews (2017 - Present)"
                },
                "variants": [
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/82967",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/82965",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/82969",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/74697",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/72736",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/75668",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/65364",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/65158",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/65028",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/75662",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/74320",
                        "name": "Marvel Previews (2017)"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/73776",
                        "name": "Marvel Previews (2017)"
                    }
                ],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2099-01-29T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "2020-01-06T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 0
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/80/5e3d7536c8ada",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/80/5e3d7536c8ada",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82970/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/10021",
                            "name": "Jim Nausedas",
                            "role": "editor"
                        }
                    ],
                    "returned": 1
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82970/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82970/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/183704",
                            "name": "cover from Marvel Previews (2017)",
                            "type": "cover"
                        }
                    ],
                    "returned": 1
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/82970/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 1003,
                "digitalId": 0,
                "title": "Sentry, the (Trade Paperback)",
                "issueNumber": 0,
                "variantDescription": "",
                "description": "On the edge of alcoholism and a failed marriage, Bob Reynolds wakes up to discover his true nature. A forgotten hero, he must unravel the conspiracy to erase his memory from mankind before an evil entity returns.",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "0-7851-0799-1",
                "upc": "",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Trade Paperback",
                "pageCount": 240,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "On the edge of alcoholism and a failed marriage, Bob Reynolds wakes up to discover his true nature. A forgotten hero, he must unravel the conspiracy to erase his memory from mankind before an evil entity returns."
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/1003",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/collection/1003/sentry_the_trade_paperback?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/65",
                    "name": "Sentry, the (1999)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 9.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/c0/4bc66d78f1bee",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/c0/4bc66d78f1bee",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1003/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/55",
                            "name": "Paul Jenkins",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/56",
                            "name": "Jae Lee",
                            "role": "penciller"
                        }
                    ],
                    "returned": 2
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1003/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1003/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/66",
                            "name": "On the edge of alcoholism and a failed marriage, Bob Reynolds wakes up to discover his true nature. A forgotten hero, he must un",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/65143",
                            "name": "SENTRY, THE TPB 0 cover",
                            "type": "cover"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1003/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 331,
                "digitalId": 0,
                "title": "Gun Theory (2003) #4",
                "issueNumber": 4,
                "variantDescription": "",
                "description": "The phone rings, and killer-for-hire Harvey embarks on another hit. But nothing's going right this job. There's little room for error in the business of killing - so what happens when one occurs?\r\n32 PGS./ PARENTAL ADVISORY ...$2.50",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605468-00111",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "The phone rings, and killer-for-hire Harvey embarks on another hit. But nothing's going right this job. There's little room for error in the business of killing - so what happens when one occurs?\r\n32 PGS./ PARENTAL ADVISORY ...$2.50"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/331",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/331/gun_theory_2003_4?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/649",
                    "name": "Gun Theory (2003)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 2.5
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/60/4bc69f11baf75",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/60/4bc69f11baf75",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/331/creators",
                    "items": [],
                    "returned": 0
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/331/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/331/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2263",
                            "name": "Interior #2263",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/65423",
                            "name": "GUN THEORY 4 cover",
                            "type": "cover"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/331/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 428,
                "digitalId": 0,
                "title": "Ant-Man (2003) #4",
                "issueNumber": 4,
                "variantDescription": "",
                "description": "Ant-Man digs deeper into finding out who is leaking those dirty little secrets that are threatening our national security. And who's better at uncovering dirty LITTLE secrets than him??",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605482-00411",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "Ant-Man digs deeper into finding out who is leaking those dirty little secrets that are threatening our national security. And who's better at uncovering dirty LITTLE secrets than him??"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/428",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/428/ant-man_2003_4?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/551",
                    "name": "Ant-Man (2003 - 2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 2.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/4/20/4bc697c680890",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/4/20/4bc697c680890",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/428/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/600",
                            "name": "Clayton Crain",
                            "role": "penciller (cover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/344",
                            "name": "Daniel Way",
                            "role": "writer"
                        }
                    ],
                    "returned": 2
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/428/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/428/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2331",
                            "name": "Cover #2331",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2332",
                            "name": "Interior #2332",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/428/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 1308,
                "digitalId": 0,
                "title": "Marvel Age Spider-Man Vol. 2: Everyday Hero (Digest)",
                "issueNumber": 0,
                "variantDescription": "",
                "description": "\"The Marvel Age of Comics continues! This time around, Spidey meets his match against such classic villains as Electro and the Lizard, and faces the return of one of his first foes: the Vulture! Plus: Spider-Man vs. the Living Brain, Peter Parker's fight with Flash Thompson, and the wall-crawler tackles the high-flying Human Torch!\"",
                "modified": "2018-01-22T15:42:11-0500",
                "isbn": "0-7851-1451-3",
                "upc": "5960611451-00111",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Digest",
                "pageCount": 96,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "\"The Marvel Age of Comics continues! This time around, Spidey meets his match against such classic villains as Electro and the Lizard, and faces the return of one of his first foes: the Vulture! Plus: Spider-Man vs. the Living Brain, Peter Parker's fight with Flash Thompson, and the wall-crawler tackles the high-flying Human Torch!\""
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/1308",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/collection/1308/marvel_age_spider-man_vol_2_everyday_hero_digest?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/1242",
                    "name": "Marvel Age Spider-Man Vol. 2: Everyday Hero (2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/546",
                        "name": "Marvel Age Spider-Man (2004) #8"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/610",
                        "name": "Marvel Age Spider-Man (2004) #7"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/728",
                        "name": "Marvel Age Spider-Man (2004) #6"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/681",
                        "name": "Marvel Age Spider-Man (2004) #5"
                    }
                ],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 5.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/20/4bc665483c3aa",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/6/90/5a664c954a55b",
                        "extension": "jpg"
                    },
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/80/5a6648f8aaccc",
                        "extension": "jpg"
                    },
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/c0/5a6648efbc46c",
                        "extension": "jpg"
                    },
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/4/00/5a6648c368f52",
                        "extension": "jpg"
                    },
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/a/40/4bc689a4ce796",
                        "extension": "jpg"
                    },
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/a/c0/4bc684889f8ed",
                        "extension": "jpg"
                    },
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/50/4bc6809bdc81b",
                        "extension": "jpg"
                    },
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/20/4bc665483c3aa",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 10,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1308/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/694",
                            "name": "Mark Brooks",
                            "role": "penciller (cover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/434",
                            "name": "Michael Ryan",
                            "role": "penciller (cover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/424",
                            "name": "Udon Comics",
                            "role": "colorist"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/692",
                            "name": "Pat Davidson",
                            "role": "inker"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/689",
                            "name": "Derek Fridolfs",
                            "role": "inker"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/6743",
                            "name": "Rich Perrotta",
                            "role": "inker"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/682",
                            "name": "Todd Dezago",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/326",
                            "name": "Daniel Quantz",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/691",
                            "name": "Jonboy Meyers",
                            "role": "penciller"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/688",
                            "name": "Michael OHare",
                            "role": "penciller"
                        }
                    ],
                    "returned": 10
                },
                "characters": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1308/characters",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009610",
                            "name": "Spider-Man (Peter Parker)"
                        }
                    ],
                    "returned": 1
                },
                "stories": {
                    "available": 9,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1308/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2759",
                            "name": "Cover #2759",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2760",
                            "name": "Interior #2760",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2763",
                            "name": "Cover #2763",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2764",
                            "name": "Interior #2764",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2769",
                            "name": "Cover #2769",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2770",
                            "name": "Interior #2770",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2771",
                            "name": "Cover #2771",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2772",
                            "name": "Interior #2772",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/65682",
                            "name": "MARVEL AGE SPIDER-MAN VOL. 2: EVERYDAY HERO 0 cover",
                            "type": "cover"
                        }
                    ],
                    "returned": 9
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1308/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 1994,
                "digitalId": 0,
                "title": "Official Handbook of the Marvel Universe (2004) #13 (TEAMS)",
                "issueNumber": 13,
                "variantDescription": "TEAMS",
                "description": "Heavy-hitting heroes unite! This Official Handbook contains in-depth bios on more than 30 of the Marvel Universe's most awesome assemblages - including the Defenders, Power Pack and the New Thunderbolts! Plus: An all-new cover by superstar artist Tom Grummett, digitally painted by Morry Hollowell.\r<br>48 PGS./All Ages ...$3.99\r<br>",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605695-00111",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "Heavy-hitting heroes unite! This Official Handbook contains in-depth bios on more than 30 of the Marvel Universe's most awesome assemblages - including the Defenders, Power Pack and the New Thunderbolts! Plus: An all-new cover by superstar artist Tom Grummett, digitally painted by Morry Hollowell.\r<br>48 PGS./All Ages ...$3.99\r<br>"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/1994",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/1994/official_handbook_of_the_marvel_universe_2004_13_teams/teams?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/787",
                    "name": "Official Handbook of the Marvel Universe (2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 3.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/20/4bc63a47b8dcb",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/20/4bc63a47b8dcb",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 10,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1994/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/887",
                            "name": "Ronald Byrd",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/902",
                            "name": "Jeff Christiansen",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/903",
                            "name": "Anthony Flamini",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/930",
                            "name": "Richard Green",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/888",
                            "name": "Michael Hoskin",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/897",
                            "name": "Sean Mcquaid",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/394",
                            "name": "Eric J. Moreels",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/899",
                            "name": "Mark OEnglish",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/896",
                            "name": "Stuart Vandal",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/483",
                            "name": "Tom Grummett",
                            "role": "penciller (cover)"
                        }
                    ],
                    "returned": 10
                },
                "characters": {
                    "available": 14,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1994/characters",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009156",
                            "name": "Apocalypse"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009197",
                            "name": "Blink"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009243",
                            "name": "Colossus"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009313",
                            "name": "Gambit"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009349",
                            "name": "Holocaust (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009417",
                            "name": "Magneto"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009447",
                            "name": "Mister Sinister"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009546",
                            "name": "Rogue"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010969",
                            "name": "Sabretooth (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010975",
                            "name": "Shadowcat (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010976",
                            "name": "Silver Samurai (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010979",
                            "name": "Storm (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009636",
                            "name": "Sunfire"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009718",
                            "name": "Wolverine"
                        }
                    ],
                    "returned": 14
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1994/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4614",
                            "name": "Cover #4614",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4615",
                            "name": "Interior #4615",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1994/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 291,
                "digitalId": 0,
                "title": "Ant-Man (2003) #1",
                "issueNumber": 1,
                "variantDescription": "",
                "description": "Size does matter.  And no one knows this more than Hank Pym - a.k.a. Ant-Man. Got a problem with Galactus? Call the FF. Got a problem with, say, mind-controlled cockroaches? Then Ant-Man's your man! And needless to say, it's done a number on our diminutive hero's self-esteem.  When Ant-Man is tapped to infiltrate an international spy ring that has been siphoning secrets out of Washington, he jumps at the chance - unaware that he's being used as a pawn in a larger game of espionage.\r\n32 PGS./PARENTAL ADVISORY...$2.99",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605396-01811",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "Size does matter.  And no one knows this more than Hank Pym - a.k.a. Ant-Man. Got a problem with Galactus? Call the FF. Got a problem with, say, mind-controlled cockroaches? Then Ant-Man's your man! And needless to say, it's done a number on our diminutive hero's self-esteem.  When Ant-Man is tapped to infiltrate an international spy ring that has been siphoning secrets out of Washington, he jumps at the chance - unaware that he's being used as a pawn in a larger game of espionage.\r\n32 PGS./PARENTAL ADVISORY...$2.99"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/291",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/291/ant-man_2003_1?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/551",
                    "name": "Ant-Man (2003 - 2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 2.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/6/e0/4bc6a2497684e",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/6/e0/4bc6a2497684e",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/291/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/600",
                            "name": "Clayton Crain",
                            "role": "penciller (cover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/344",
                            "name": "Daniel Way",
                            "role": "writer"
                        }
                    ],
                    "returned": 2
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/291/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/291/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1806",
                            "name": "Cover #1806",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1807",
                            "name": "Interior #1807",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/291/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 376,
                "digitalId": 0,
                "title": "Ant-Man (2003) #3",
                "issueNumber": 3,
                "variantDescription": "",
                "description": "When Hank Pym - a.k.a. Ant-Man - is tapped by U.S. Intelligence to infiltrate an international spy ring that has been siphoning secrets out of Washington, the diminutive hero jumps at the chance - unaware that he's being used as a pawn in a larger game of espionage.\r32 PGS./PARENTAL ADVISORY...$2.99",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605396-02011",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "When Hank Pym - a.k.a. Ant-Man - is tapped by U.S. Intelligence to infiltrate an international spy ring that has been siphoning secrets out of Washington, the diminutive hero jumps at the chance - unaware that he's being used as a pawn in a larger game of espionage.\r32 PGS./PARENTAL ADVISORY...$2.99"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/376",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/376/ant-man_2003_3?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/551",
                    "name": "Ant-Man (2003 - 2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 2.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/d/70/4bc69c7e9b9d7",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/d/70/4bc69c7e9b9d7",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/376/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/600",
                            "name": "Clayton Crain",
                            "role": "penciller (cover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/344",
                            "name": "Daniel Way",
                            "role": "writer"
                        }
                    ],
                    "returned": 2
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/376/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/376/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1810",
                            "name": "Cover #1810",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1811",
                            "name": "Interior #1811",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/376/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 3627,
                "digitalId": 0,
                "title": "Storm (2006)",
                "issueNumber": 0,
                "variantDescription": "",
                "description": "#N/A",
                "modified": "2015-01-29T20:04:55-0500",
                "isbn": "",
                "upc": "",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "The epic, untold love story between Marvel's two pre-eminent Black super heroes -- Storm and the Black Panther -- is finally told, as only New York Times best-selling author Eric Jerome Dickey can do it!  An orphaned street urchin, living by her wits on the unforgiving plains of Africa as she struggles to harness her slowly-developing mutant powers...A warrior Prince, embarking on his rite of passage as he ponders the great responsibility in his future...And a crew of ruthless mercenaries who'll stop at nothing to capture an elusive creature of legend -- the fabled wind-rider.  What sparks occur when their paths intersect?  Don't miss out on this story, True Believer, as it builds to a July Event that will shake the entire Marvel Universe.\r<br>\r<br>32 PGS./T+ SUGGESTED FOR TEENS AND UP ...$2.99\r<br>"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/3627",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/3627/storm_2006?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/357",
                    "name": "Storm (2006)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 0
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/80/4bc5fe7a308d7",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/80/4bc5fe7a308d7",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/3627/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/370",
                            "name": "Eric Jerome Dickey",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/371",
                            "name": "David Hine",
                            "role": "penciller"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/243",
                            "name": "Mike Mayhew",
                            "role": "penciller (cover)"
                        }
                    ],
                    "returned": 3
                },
                "characters": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/3627/characters",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009629",
                            "name": "Storm"
                        }
                    ],
                    "returned": 1
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/3627/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/496",
                            "name": "Cover #496",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/497",
                            "name": "Interior #497",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/3627/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 1158,
                "digitalId": 0,
                "title": "ULTIMATE X-MEN VOL. 5: ULTIMATE WAR TPB (Trade Paperback)",
                "issueNumber": 0,
                "variantDescription": "",
                "description": "The Ultimates vs. the Ultimate X-Men: the battle begins. When the X-Men do the worst thing they could to humanity, the government orders Captain America, Iron Man, Thor and the rest of the Ultimates to bring them down. A small but lethal army, the Ultimates were created to face these and other newly rising threats to mankind. But the X-Men's founder, Professor X, hasn't been training his students for nothing -- and the youngs mutants just might take out the Ultimates first.",
                "modified": "2018-03-12T16:56:16-0400",
                "isbn": "0-7851-1129-8",
                "upc": "",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Trade Paperback",
                "pageCount": 112,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "The Ultimates vs. the Ultimate X-Men: the battle begins. When the X-Men do the worst thing they could to humanity, the government orders Captain America, Iron Man, Thor and the rest of the Ultimates to bring them down. A small but lethal army, the Ultimates were created to face these and other newly rising threats to mankind. But the X-Men's founder, Professor X, hasn't been training his students for nothing -- and the youngs mutants just might take out the Ultimates first."
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/1158",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/collection/1158/ultimate_x-men_vol_5_ultimate_war_tpb_trade_paperback?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/216",
                    "name": "ULTIMATE X-MEN VOL. 5: ULTIMATE WAR TPB (1999)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/18477",
                        "name": "Ultimate War (2003) #4"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/18476",
                        "name": "Ultimate War (2003) #3"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/18475",
                        "name": "Ultimate War (2003) #2"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/18474",
                        "name": "Ultimate War (2003) #1"
                    }
                ],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "1961-01-01T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 9.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/2/f0/4bc6670c80007",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/2/f0/4bc6670c80007",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 9,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1158/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/232",
                            "name": "Chris Bachalo",
                            "role": "penciller"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/452",
                            "name": "Virtual Calligr",
                            "role": "letterer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/6170",
                            "name": "Olivier Coipel",
                            "role": "penciler"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/312",
                            "name": "Mike Deodato",
                            "role": "penciler"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/181",
                            "name": "Geoff Johns",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/52",
                            "name": "Bruce Jones",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/88",
                            "name": "Mark Millar",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/479",
                            "name": "Paul Mounts",
                            "role": "colorist"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/427",
                            "name": "Tim Townsend",
                            "role": "inker"
                        }
                    ],
                    "returned": 9
                },
                "characters": {
                    "available": 17,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1158/characters",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010908",
                            "name": "Beast (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010911",
                            "name": "Black Widow (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010913",
                            "name": "Captain America (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010917",
                            "name": "Colossus (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011131",
                            "name": "Hawkeye (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011005",
                            "name": "Hulk (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010933",
                            "name": "Iceman (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010946",
                            "name": "Jean Grey (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010943",
                            "name": "Magneto (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011007",
                            "name": "Nick Fury (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010963",
                            "name": "Quicksilver (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010966",
                            "name": "Rogue (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010971",
                            "name": "Scarlet Witch (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010978",
                            "name": "Storm (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011025",
                            "name": "Thor (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009689",
                            "name": "Vanisher (Ultimate)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010992",
                            "name": "Wasp (Ultimate)"
                        }
                    ],
                    "returned": 17
                },
                "stories": {
                    "available": 9,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1158/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/270",
                            "name": "The Ultimates vs. the Ultimate X-Men: the battle begins. When the X-Men do the worst thing they could to humanity, the governmen",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/39348",
                            "name": "Interior #39348",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/39349",
                            "name": "Free Preview of Hulk #50",
                            "type": "promo"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/39351",
                            "name": "Interior #39351",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/39352",
                            "name": "Free Preview of Hulk #50",
                            "type": "promo"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/39354",
                            "name": "Interior #39354",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/39355",
                            "name": "Free Preview of Avengers 65",
                            "type": "promo"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/39357",
                            "name": "Interior #39357",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/65260",
                            "name": "ULTIMATE X-MEN VOL. 5: ULTIMATE WAR 0 cover",
                            "type": "cover"
                        }
                    ],
                    "returned": 9
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1158/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 1332,
                "digitalId": 0,
                "title": "X-Men: Days of Future Past (Trade Paperback)",
                "issueNumber": 0,
                "variantDescription": "",
                "description": "\"Re-live the legendary first journey into the dystopian future of 2013 - where Sentinels stalk the Earth, and the X-Men are humanity's only hope...until they die! Also featuring the first appearance of Alpha Flight, the return of the Wendigo, the history of the X-Men from Cyclops himself...and a demon for Christmas!? \"",
                "modified": "2017-02-28T14:52:22-0500",
                "isbn": "0-7851-1560-9",
                "upc": "5960611560-00111",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Trade Paperback",
                "pageCount": 144,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "\"Re-live the legendary first journey into the dystopian future of 2013 - where Sentinels stalk the Earth, and the X-Men are humanity's only hope...until they die! Also featuring the first appearance of Alpha Flight, the return of the Wendigo, the history of the X-Men from Cyclops himself...and a demon for Christmas!? \""
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/1332",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/collection/1332/x-men_days_of_future_past_trade_paperback?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/1327",
                    "name": "X-Men: Days of Future Past (2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/13683",
                        "name": "Uncanny X-Men (1963) #142"
                    },
                    {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/12460",
                        "name": "Uncanny X-Men (1963) #141"
                    }
                ],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 9.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/d0/58b5cfb6d5239",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/d0/58b5cfb6d5239",
                        "extension": "jpg"
                    },
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/b0/4bc66463ef7f0",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1332/creators",
                    "items": [],
                    "returned": 0
                },
                "characters": {
                    "available": 10,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1332/characters",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009159",
                            "name": "Archangel"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009164",
                            "name": "Avalanche"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009199",
                            "name": "Blob"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009243",
                            "name": "Colossus"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009271",
                            "name": "Destiny"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009472",
                            "name": "Nightcrawler"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009522",
                            "name": "Pyro"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009629",
                            "name": "Storm"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009718",
                            "name": "Wolverine"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009726",
                            "name": "X-Men"
                        }
                    ],
                    "returned": 10
                },
                "stories": {
                    "available": 3,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1332/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/15472",
                            "name": "Days of Future Past",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/27788",
                            "name": "Mind Out of Time!",
                            "type": "interiorStory"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/65738",
                            "name": "X-MEN: DAYS OF FUTURE PAST TPB 0 cover",
                            "type": "cover"
                        }
                    ],
                    "returned": 3
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1332/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 1590,
                "digitalId": 0,
                "title": "Official Handbook of the Marvel Universe (2004) #9 (THE WOMEN OF MARVEL)",
                "issueNumber": 9,
                "variantDescription": "THE WOMEN OF MARVEL",
                "description": "Marvel's leading ladies take center stage! This Official Handbook includes in-depth bios on more than 40 of the House's most powerful women warriors - from Araña to Vindicator! Plus: an all-new cover by superstar artist Greg Land!",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605678-00111",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "Marvel's leading ladies take center stage! This Official Handbook includes in-depth bios on more than 40 of the House's most powerful women warriors - from Araña to Vindicator! Plus: an all-new cover by superstar artist Greg Land!"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/1590",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/1590/official_handbook_of_the_marvel_universe_2004_9_the_women_of_marvel/the_women_of_marvel?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/787",
                    "name": "Official Handbook of the Marvel Universe (2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 3.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/b0/4c7d666c0e58a",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/b0/4c7d666c0e58a",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 12,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1590/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/887",
                            "name": "Ronald Byrd",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/902",
                            "name": "Jeff Christiansen",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/919",
                            "name": "Jonathan Coupersmartt",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/903",
                            "name": "Anthony Flamini",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/888",
                            "name": "Michael Hoskin",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/898",
                            "name": "Bill Lentz",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/897",
                            "name": "Sean Mcquaid",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/394",
                            "name": "Eric J. Moreels",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/899",
                            "name": "Mark OEnglish",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/896",
                            "name": "Stuart Vandal",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/425",
                            "name": "Greg Land",
                            "role": "penciller (cover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/500",
                            "name": "Christopher Sotomayor",
                            "role": "colorist"
                        }
                    ],
                    "returned": 12
                },
                "characters": {
                    "available": 14,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1590/characters",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009156",
                            "name": "Apocalypse"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009197",
                            "name": "Blink"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009243",
                            "name": "Colossus"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009313",
                            "name": "Gambit"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009349",
                            "name": "Holocaust (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009417",
                            "name": "Magneto"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009447",
                            "name": "Mister Sinister"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009546",
                            "name": "Rogue"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010969",
                            "name": "Sabretooth (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010975",
                            "name": "Shadowcat (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010976",
                            "name": "Silver Samurai (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010979",
                            "name": "Storm (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009636",
                            "name": "Sunfire"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009718",
                            "name": "Wolverine"
                        }
                    ],
                    "returned": 14
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1590/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4513",
                            "name": "Cover #4513",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4514",
                            "name": "Interior #4514",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1590/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 384,
                "digitalId": 0,
                "title": "Gun Theory (2003) #3",
                "issueNumber": 3,
                "variantDescription": "",
                "description": "The phone rings, and killer-for-hire Harvey embarks on another hit. But nothing's going right this job. There's little room for error in the business of killing - so what happens when one occurs?\r\n\r\n32 PGS./ PARENTAL ADVISORY ...$2.50",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605492-00411",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "The phone rings, and killer-for-hire Harvey embarks on another hit. But nothing's going right this job. There's little room for error in the business of killing - so what happens when one occurs?\r\n\r\n32 PGS./ PARENTAL ADVISORY ...$2.50"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/384",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/384/gun_theory_2003_3?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/649",
                    "name": "Gun Theory (2003)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 2.5
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/60/4bc69f11baf75",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/60/4bc69f11baf75",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/384/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/576",
                            "name": "Jon Proctor",
                            "role": "penciller (cover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/344",
                            "name": "Daniel Way",
                            "role": "writer"
                        }
                    ],
                    "returned": 2
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/384/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/384/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2538",
                            "name": "Cover #2538",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/2539",
                            "name": "Interior #2539",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/384/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 183,
                "digitalId": 0,
                "title": "Startling Stories: The Incorrigible Hulk (2004) #1",
                "issueNumber": 1,
                "variantDescription": "",
                "description": "",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605429-00811",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "For Doctor Bruce Banner life is anything but normal. But what happens when two women get between him and his alter ego, the Incorrigible Hulk? Hulk confused! \r\nIndy superstar Peter Bagge (THE MEGALOMANIACAL SPIDER-MAN) takes a satirical jab at the Hulk mythos with a tale of dames, debauchery and destruction.\r\n32 PGS./MARVEL PSR...$2.99"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/183",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/183/startling_stories_the_incorrigible_hulk_2004_1?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/565",
                    "name": "Startling Stories: The Incorrigible Hulk (2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 2.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                    "extension": "jpg"
                },
                "images": [],
                "creators": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/183/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/6291",
                            "name": "Peter Bagge",
                            "role": "penciller (cover)"
                        }
                    ],
                    "returned": 1
                },
                "characters": {
                    "available": 1,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/183/characters",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009351",
                            "name": "Hulk"
                        }
                    ],
                    "returned": 1
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/183/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1891",
                            "name": "Cover #1891",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1892",
                            "name": "Interior #1892",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/183/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 1689,
                "digitalId": 0,
                "title": "Official Handbook of the Marvel Universe (2004) #10 (MARVEL KNIGHTS)",
                "issueNumber": 10,
                "variantDescription": "MARVEL KNIGHTS",
                "description": "On the mean streets of the Marvel Universe, the kid gloves come off. Guardian devils, vengeance-seeking vigilantes and enigmatic assassins stalk the city's dark underbelly _ and the urban action unfolds with gritty intensity. The newest entry in Marvel's best-selling Handbook series, OHOTMUMK04 includes in-depth bios on a host of the House's edgiest icons - from Black Panther to Shang-Chi!",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605694-00111",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "On the mean streets of the Marvel Universe, the kid gloves come off. Guardian devils, vengeance-seeking vigilantes and enigmatic assassins stalk the city's dark underbelly _ and the urban action unfolds with gritty intensity. The newest entry in Marvel's best-selling Handbook series, OHOTMUMK04 includes in-depth bios on a host of the House's edgiest icons - from Black Panther to Shang-Chi!"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/1689",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/1689/official_handbook_of_the_marvel_universe_2004_10_marvel_knights/marvel_knights?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/787",
                    "name": "Official Handbook of the Marvel Universe (2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 3.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/30/4bc64df4105b9",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/30/4bc64df4105b9",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 9,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1689/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/887",
                            "name": "Ronald Byrd",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/902",
                            "name": "Jeff Christiansen",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/903",
                            "name": "Anthony Flamini",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/888",
                            "name": "Michael Hoskin",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/897",
                            "name": "Sean Mcquaid",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/394",
                            "name": "Eric J. Moreels",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/900",
                            "name": "Barry Reese",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/896",
                            "name": "Stuart Vandal",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/490",
                            "name": "Pat Lee",
                            "role": "penciller (cover)"
                        }
                    ],
                    "returned": 9
                },
                "characters": {
                    "available": 14,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1689/characters",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009156",
                            "name": "Apocalypse"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009197",
                            "name": "Blink"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009243",
                            "name": "Colossus"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009313",
                            "name": "Gambit"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009349",
                            "name": "Holocaust (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009417",
                            "name": "Magneto"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009447",
                            "name": "Mister Sinister"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009546",
                            "name": "Rogue"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010969",
                            "name": "Sabretooth (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010975",
                            "name": "Shadowcat (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010976",
                            "name": "Silver Samurai (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010979",
                            "name": "Storm (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009636",
                            "name": "Sunfire"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009718",
                            "name": "Wolverine"
                        }
                    ],
                    "returned": 14
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1689/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4612",
                            "name": "Cover #4612",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4613",
                            "name": "Interior #4613",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1689/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 2088,
                "digitalId": 0,
                "title": "Official Handbook of the Marvel Universe (2004) #14 (FANTASTIC FOUR)",
                "issueNumber": 14,
                "variantDescription": "FANTASTIC FOUR",
                "description": "At last, Marvel's First Family gets the OHOTMU treatment! This Official Handbook contains in-depth bios on the family, friends and foes of the Fantastic Four - from Annihilus to the Watcher! Plus: An all-new cover by superstar artist Tom Grummett, digitally painted by Morry Hollowell!\r<br>48 PGS./T+ Suggested for Teens and Up ...$3.99\r<br>\r<br>",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605677-00111",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "At last, Marvel's First Family gets the OHOTMU treatment! This Official Handbook contains in-depth bios on the family, friends and foes of the Fantastic Four - from Annihilus to the Watcher! Plus: An all-new cover by superstar artist Tom Grummett, digitally painted by Morry Hollowell!\r<br>48 PGS./T+ Suggested for Teens and Up ...$3.99\r<br>\r<br>"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/2088",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/2088/official_handbook_of_the_marvel_universe_2004_14_fantastic_four/fantastic_four?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/787",
                    "name": "Official Handbook of the Marvel Universe (2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 3.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/90/4bc6353e5fc56",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/90/4bc6353e5fc56",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 9,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/2088/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/887",
                            "name": "Ronald Byrd",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/902",
                            "name": "Jeff Christiansen",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/903",
                            "name": "Anthony Flamini",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/888",
                            "name": "Michael Hoskin",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/898",
                            "name": "Bill Lentz",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/897",
                            "name": "Sean Mcquaid",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/899",
                            "name": "Mark OEnglish",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/896",
                            "name": "Stuart Vandal",
                            "role": "writer"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/483",
                            "name": "Tom Grummett",
                            "role": "penciller (cover)"
                        }
                    ],
                    "returned": 9
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/2088/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/2088/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4511",
                            "name": "Cover #4511",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4512",
                            "name": "Interior #4512",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/2088/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 1749,
                "digitalId": 0,
                "title": "Official Handbook of the Marvel Universe (2004) #11 (X-MEN - AGE OF APOCALYPSE)",
                "issueNumber": 11,
                "variantDescription": "X-MEN - AGE OF APOCALYPSE",
                "description": "Your complete guide to the epic saga! This Official Handbook includes in-depth bios on more than 40 denizens of the Age of Apocalypse - from Abyss to Weapon X! Plus: An all-new cover by superstar-in-waiting Mark Brooks, digitally painted by Justin Ponsor.\r<br>48 PGS./Marvel PSR ...$3.99\r<br>",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605625-00111",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "Your complete guide to the epic saga! This Official Handbook includes in-depth bios on more than 40 denizens of the Age of Apocalypse - from Abyss to Weapon X! Plus: An all-new cover by superstar-in-waiting Mark Brooks, digitally painted by Justin Ponsor.\r<br>48 PGS./Marvel PSR ...$3.99\r<br>"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/1749",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/1749/official_handbook_of_the_marvel_universe_2004_11_x-men_-_age_of_apocalypse/x-men_-_age_of_apocalypse?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/787",
                    "name": "Official Handbook of the Marvel Universe (2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 3.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/b0/4bc6494ed6eb4",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/b0/4bc6494ed6eb4",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1749/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/694",
                            "name": "Mark Brooks",
                            "role": "penciller (cover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/684",
                            "name": "Mike Raicht",
                            "role": "writer"
                        }
                    ],
                    "returned": 2
                },
                "characters": {
                    "available": 14,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1749/characters",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009156",
                            "name": "Apocalypse"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009197",
                            "name": "Blink"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009243",
                            "name": "Colossus"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009313",
                            "name": "Gambit"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009349",
                            "name": "Holocaust (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009417",
                            "name": "Magneto"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009447",
                            "name": "Mister Sinister"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009546",
                            "name": "Rogue"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010969",
                            "name": "Sabretooth (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010975",
                            "name": "Shadowcat (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010976",
                            "name": "Silver Samurai (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010979",
                            "name": "Storm (Age of Apocalypse)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009636",
                            "name": "Sunfire"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009718",
                            "name": "Wolverine"
                        }
                    ],
                    "returned": 14
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1749/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4153",
                            "name": "Cover #4153",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/4154",
                            "name": "Interior #4154",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/1749/events",
                    "items": [],
                    "returned": 0
                }
            },
            {
                "id": 323,
                "digitalId": 0,
                "title": "Ant-Man (2003) #2",
                "issueNumber": 2,
                "variantDescription": "",
                "description": "Ant-Man digs deeper to find out who is leaking secret information that threatens our national security.\r\n32 pgs./PARENTAL ADVISORY...$2.99",
                "modified": "-0001-11-30T00:00:00-0500",
                "isbn": "",
                "upc": "5960605396-01911",
                "diamondCode": "",
                "ean": "",
                "issn": "",
                "format": "Comic",
                "pageCount": 0,
                "textObjects": [
                    {
                        "type": "issue_solicit_text",
                        "language": "en-us",
                        "text": "Ant-Man digs deeper to find out who is leaking secret information that threatens our national security.\r\n32 pgs./PARENTAL ADVISORY...$2.99"
                    }
                ],
                "resourceURI": "http://gateway.marvel.com/v1/public/comics/323",
                "urls": [
                    {
                        "type": "detail",
                        "url": "http://marvel.com/comics/issue/323/ant-man_2003_2?utm_campaign=apiRef&utm_source=d1b3d83e49ea264e81ec56080afc9ddd"
                    }
                ],
                "series": {
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/551",
                    "name": "Ant-Man (2003 - 2004)"
                },
                "variants": [],
                "collections": [],
                "collectedIssues": [],
                "dates": [
                    {
                        "type": "onsaleDate",
                        "date": "2029-12-31T00:00:00-0500"
                    },
                    {
                        "type": "focDate",
                        "date": "-0001-11-30T00:00:00-0500"
                    }
                ],
                "prices": [
                    {
                        "type": "printPrice",
                        "price": 2.99
                    }
                ],
                "thumbnail": {
                    "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/20/4bc69f33cafc0",
                    "extension": "jpg"
                },
                "images": [
                    {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/20/4bc69f33cafc0",
                        "extension": "jpg"
                    }
                ],
                "creators": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/323/creators",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/600",
                            "name": "Clayton Crain",
                            "role": "penciller (cover)"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/creators/344",
                            "name": "Daniel Way",
                            "role": "writer"
                        }
                    ],
                    "returned": 2
                },
                "characters": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/323/characters",
                    "items": [],
                    "returned": 0
                },
                "stories": {
                    "available": 2,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/323/stories",
                    "items": [
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1808",
                            "name": "Cover #1808",
                            "type": "cover"
                        },
                        {
                            "resourceURI": "http://gateway.marvel.com/v1/public/stories/1809",
                            "name": "Interior #1809",
                            "type": "interiorStory"
                        }
                    ],
                    "returned": 2
                },
                "events": {
                    "available": 0,
                    "collectionURI": "http://gateway.marvel.com/v1/public/comics/323/events",
                    "items": [],
                    "returned": 0
                }
            }
        ]

MARVEL_TS = os.environ["MARVEL_TS"]
MARVEL_APIKEY = os.environ["MARVEL_APIKEY"]
MARVEL_HASH = os.environ["MARVEL_HASH"]

params = f"ts={MARVEL_TS}&apikey={MARVEL_APIKEY}&hash={MARVEL_HASH}"

@app.get("/searchComics/")
async def search_comics(name: str = None):
    if name:
      character = get_character(name)
      if character:
        return character
      else:
        comic = get_comic(name)
        return comic
    else:
      characters = get_characters()
      return characters


def search(parameter: str, value: str, list):
  for element in list:
    elem = element[f"{parameter}"]
    if value in elem or value == elem:
      return element


def get_characters():
    endpoint = f"/v1/public/characters"
      
    response = connect(endpoint, params)
    response = response.json()
    characters = response["data"]["results"]
    return characters

def get_character(name: str = None):
    endpoint = f"/v1/public/characters"
    
    response = connect(endpoint, params)
    response = response.json()
    characters = response["data"]["results"]

    if name:
      name = name.capitalize()

    character_or_empty = search("name", name, characters)

    if character_or_empty:
      return {
        "id": character_or_empty["id"],
        "name": character_or_empty["name"],
        "image": f"{character_or_empty['thumbnail']['path']}/standard_small.{character_or_empty['thumbnail']['extension']}",
        "appearances": f"{character_or_empty['comics']['available']}",
      }

def get_comic(title: str = None):
    endpoint = f"/v1/public/comics"

    response = connect(endpoint, params)
    response = response.json()
    comics = response["data"]["results"]
    
    if title:
      title = title.capitalize()
    
    comic_or_empty = search("title", title.capitalize(), comics)
    
    if comic_or_empty:
      return {
        "id": comic_or_empty["id"],
        "title": comic_or_empty["title"],
        "image": f"{comic_or_empty['thumbnail']['path']}/standard_small.{comic_or_empty['thumbnail']['extension']}",
        "onsaleDate": f"{comic_or_empty['dates'][0]['date']}",
      }
    return {}