from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import sys

client = language.LanguageServiceClient()

def sentiment_analyze(stri):
   text = stri
   document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)

   sentiment = client.analyze_sentiment(document=document).document_sentiment

   print('Text: {}'.format(text))
   print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


def entities_analyze(stri):
    text = stri
    document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)

    entities = client.analyze_entities(document).entities

    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION','EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

    for entity in entities:
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
        print(u'{:<16}: {}'.format('metadata', entity.metadata))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',entity.metadata.get('wikipedia_url', '-')))

def syntax_analyze(stri):
    text = stri

    document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)

    tokens = client.analyze_syntax(document).tokens

    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM','PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
    for token in tokens:
        print(u'{}: {}'.format(pos_tag[token.part_of_speech.tag],token.text.content))

def entity_sentiment_analyze(stri):
    text = stri

    document = types.Document(content=text.encode('utf-8'),type=enums.Document.Type.PLAIN_TEXT)

    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    result = client.analyze_entity_sentiment(document, encoding)

    for entity in result.entities:
        print('Mentions: ')
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
            print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
            print(u'  Content : {}'.format(mention.text.content))
            print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
            print(u'  Sentiment : {}'.format(mention.sentiment.score))
            print(u'  Type : {}'.format(mention.type))
        print(u'Salience: {}'.format(entity.salience))
        print(u'Sentiment: {}\n'.format(entity.sentiment))

def classify_content(stri):
    text = stri

    document = types.Document(content= text.encode('utf-8') ,type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    for category in categories:
        print(u'=' * 20)
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))
