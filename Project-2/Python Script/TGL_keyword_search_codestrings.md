# TGL Keyword Search: Code Strings Utilized

## Purpose
This document logs the code strings (keyword families, variants, and labels) used in the TGL keyword extraction workflow.

## Normalization Rules (Applied)
- Lowercase all text
- Remove URLs/artifacts
- Remove punctuation/noise characters
- Collapse whitespace
- Remove generic stopwords
- Merge lexical variants into normalized keyword families

## A) Core Legitimacy Code Strings

### `innovation/technology`
- innovation
- innovative
- technology
- tech
- simulator

### `future of golf`
- future of golf
- future

### `tradition`
- tradition
- traditional

### `seriousness`
- serious
- joke

### `real golf`
- real golf
- actual golf
- true golf

### `resistance`
- resist
- resistance
- hate
- trash

### `entertainment`
- entertainment
- entertaining

### `gimmick`
- gimmick
- gimmicky

### `not real`
- not real
- fake golf

### `commercialization`
- commercialization
- commercialized
- commercialisation
- money grab
- cash grab
- profit

## B) Technology Legitimacy Strings

### `simulator`
- simulator
- virtual
- simulated

### `screen graphics`
- screen
- graphics
- digital

### `technology`
- technology
- tech

### `innovation`
- innovation
- innovative

### `future of golf`
- future of golf
- future

### `real golf`
- real golf
- actual golf
- true golf

### `not real`
- not real
- fake golf

### `entertainment`
- entertainment
- entertaining

### `tradition`
- tradition
- traditional

### `fan experience`
- fan experience
- viewer experience
- immersive
- interactive

## C) Commercialization Strings

### `commercialization`
- commercialization
- commercialized
- commercialisation

### `money grab`
- money grab
- cash grab
- profit driven
- profit

### `sponsor`
- sponsor
- sponsors
- sponsorship
- advertising
- ad

### `business model`
- business model
- business
- revenue
- monetization
- monetize

### `investor`
- investor
- investors
- investment

### `views and likes`
- views
- likes
- engagement

### `league growth`
- grow the game
- growing the game
- growth
- expand
- expansion

### `legitimacy`
- legitimacy
- legitimate
- legit

### `future of golf`
- future of golf
- future

### `entertainment`
- entertainment
- entertaining

## D) Code Labels Used
- `LEGIT_POS` = legitimizing
- `LEGIT_NEG` = delegitimizing
- `LEGIT_AMB` = ambivalent

## E) Output Files Associated With These Strings
- `TGL_keyword_dictionary.xlsx`
- `TGL_keyword_dictionary.csv`
- `TGL_keyword_dictionary_with_code_labels.xlsx`
- `TGL_keyword_dictionary_with_code_labels.csv`
