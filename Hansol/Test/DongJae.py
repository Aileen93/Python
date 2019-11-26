# -*- coding: utf-8 -*-
import csv
import re
import gensim
from nltk.tokenize import word_tokenize
from nltk import pos_tag

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
lemmatizer = WordNetLemmatizer()

def main():
    try:
        resrultSent = []

        # word = line[0];
        word = 'active *admiration *admired *adult *advanced *aggressive *alert *amazed *ambition *amusement *anger *angry *angular *annoyance *annoyed *annoying *antagonistic *anxiety *anxious *appealing *aroused *arrogant *august *auspicious *austere *authority *autonomous *aversion *awake *awareness *awe *awed *bad *balanced *beautiful *belligerent *bewildered *bitter *bold *bored *boredom *boring *bright *brilliant *briskness *calm *calming *calmness *causal *cautious *challenge *challenged *character *cheap *cheerful *childlike *chinese *clarity *classic *classical *clean *clear *cold *comfort *comfortable *compassion *complex *composure *confidence *confident *confused *confusion *consoled *contemporary *contempt *contentment *controlled *controlling *cool *courage *creative *cruel *cute *dangerous *dapper *dark *dazzling *death *delicate *delight *depressed *depressing *depression *depressive *desire *desperate *determination *dignified *dignity *dirty *disappointment *discomfort *disdainful *disgrace *disgust *disgusted *dislike *disorder *distressed *distrust *disturbing *docile *dominant *domination *dreamy *dreary *dull *dullness *dynamic *easy to look at *edgy *elegance *elegant *embarraseed *emotional *emotionally *empathy *empty *empty/void *energetic *energized *enjoying *enthusiam *enthusiasm *envy *excited *exciting *faith *faithful *fascinated *fascinating *fashionable *fast *fear *fearful *female *feminine *forceful *frendly *fresh *freshness *frigidness *frustration *full *futuristic *gaiety *gentle *gloomy *good *good health *gorgeous *grace/charm *graceful *grand *greed *greedy *growth *guided *guilt *happiness *happy *hard *hard to look at *hate *hateful *healthy *heavy *hoarding *hope *hopeful *hostile *hostility *humiliated *humorous *hungry *immaturity *important *impotence *impressed *in pain *inauspicious *indifference *indifferent *infatuated *influenced *influential *ingenious *innocent *intelligence *intense *interest *interesting *introspective *irritated *irritating *jealousy *joy *kind *large *leadership *leisurely *less artistic *light *like *lively *lofty *loneliness *lonely *love *loved *lucurious *luxurious *luxury *magnificent *majestic *male *manlike *masculine *melancholic *melancholy *mellow *modern *modest *more active *more restless *moved *murky *mysterious *mystery *natural *negative *nervous *nervousness *neutral *new *nimble *no emotion *nobility *noble *nostalgic *not fashionable *offensive *old *old-fashioned *open *oppressive *panic *passion *passive *peace *peaceful *plain *plain/simple *playful *pleasant *pleased *pleasure *positive *power *powerful *practical *pride *profoundness *protected *provocation *purity *quiet *racing *rage *refreshed *refreshing *regret *regular *relaced *relaxation *relaxed *relaxing *relief *restless *reverent *revolution *rich *richness *rigid *robust *romantic *rounded *rushing *rustic *sad *sadness *safe *safety *satisfaction *satisfied *selfish-uninterested *sensual *serious *seriousness *shade *shame *sharp *showy *sick *sickness *simple *sin *sleek *sleepy *slow *sluggish *small *smooth *soft *soothed *sorrow *sorrowful *speedy *sporty *spring *stale *startled *steady *stimulated *stramlined *strength *striking *strong *stylish *sultry *surprise *sweet *tende *tender *tense *thick *thin *thirsty *tight *tired *tiring *traditional *tranquilized *transparent *trendy *trust *trustworthy *truth *tumultuous *ugly *unappealing *uncaring *uncomfortable *unconcerned *understanding *unexcited *unhappy *unnatural *unperturbed *unpleasant *unsatisfied *unsociable *upset *vague *very discomfort *very sad *vigorous *vivacious *vivid *void *vulgar *warm *warmth *weak *western *wild *wisdom *worry *yang *youth *youthful *';
        word = word.replace('*', '');
        print(word);

        tokenized_doc = word_tokenize(word)  # tokenized_doc : ['an', 'image', 'forming']
        tagged_doc = pos_tag(tokenized_doc)  # tagged_doc : [('an','DT'), ('image','NN'), ('forming','VBG')]

        i = 0;
        for w in tagged_doc:
            print(w[0]+','+w[1]);
            i = i+1;

    except KeyError:
        print("not in vocabulary")

main()


