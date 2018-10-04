# High Impact Event Sentiment Analysis

## Project Goal
This is the project goal.

## Project Team
- Professor Max Fowler
- Gabriel Quinones
- Akshaya Prasad
- Isaiah Fisher

## Data Collection
#### Source
- We are scraping Tweets relating to [high impact events](#events-being-analyzed) from Twitter.
- We are collecting tweets [using this library](https://github.com/Jefferson-Henrique/GetOldTweets-python)
- Below is a table showing the queries used to collect the tweets.
- Tweets from the day the event occured to a week after are analyzed, and all tweets which contain the search terms are collected.

|                          Event                          | Search Terms                                                           |
|:-------------------------------------------------------|:----------------------------------------------------------------:|
| Aurora theater shooting                                 | "aurora shooting"  "theatre shooting"                           |
| Sandy Hook                                              | "sandy hook"                                                    |
| Washington Navy Yard Shooting                           | "navy yard shooting"                                            |
| Umpqua Community College shooting                       | "umpqua college shooting"  "umpqua shooting"                    |
| Colorado Springs Planned Parenthood shooting            | "colorado springs shooting"  "planned parenthood shooting"      |
| San Bernardino attack                                   | "san bernardino attack"                                         |
| Charleston church shooting                              | "charleston church shooting"  "church shooting"                 |
| Orlando nightclub shooting                              | "nightclub shooting"  "orlando nightclub shooting"              |
| Dallas Police officers shooting                         | "dallas police shooting"                                        |
| Fort Lauderdale airport shooting                        | "airport shooting"                                              |
| North Park Elementary School shooting                   | "north park school shooting"  "elementary school schooting"     |
| Las Vegas shooting                                      | "las vegas shooting"                                            |
| Sutherland Springs church shooting                      | "sutherland springs shooting"  "texas church shooting"          |
| Copper Canyon Apartment shooting                        | "colorado apartment shooting"  "copper canyon shooting" "colorado shooting" |
| Stoneman Douglas(Parkland Florida) High School shooting | "parkland shooting"                                             | |Santa Fe High School shooting                           | "santa fe shooting"                                               

### Data Processing
- Tweets are notoriously noisy data so before they are analyzed they must be pre-processed
- Fortunately many libraries exist to help with this task.
- This [preprocessor] library allows us to remove most of the extraneous information from tweets such as URLs, hashtags, and emojis.(https://pypi.org/project/tweet-preprocessor/)
- [Natural Languaga ToolKit(NLTK)](https://www.nltk.org/) library was used to remove [stop words](https://gist.github.com/sebleier/554280) from the tweets.

### Data Analysis

### Events Being Analyzed
1. July 20, 2012 - Aurora theater shooting
2. December 12, 2012 - Sandy Hook
3. September 16, 2013 - Washington Navy Yard shooting
4. October 1, 2015 - Umpqua Community College shooting
5. November 27,2015 - Colorado Springs Planned Parenthood shooting
6. December 2, 2015 - San Bernardino attack
7. June 17, 2015 - Charleston church shooting
8. June 12, 2016 - Orlando nightclub shooting
9. July 7, 2016 - Dallas Police officers shooting
10. January 6, 2017 - Fort Lauderdale airport shooting
11. April 10, 2017 - North Park Elementary School shooting
12. October 1, 2017 - Las Vegas shooting
13. November 5, 2017 - Sutherland Springs church shooting
14. December 31, 2017 - Copper Canyon Apartment shooting
15. February 14, 2018 - Stoneman Douglas(Parkland Florida) High School shooting
16. May 18, 2018 - Santa Fe High School shooting
