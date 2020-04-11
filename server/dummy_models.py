########################################
#          DUMMY Models
#
#   We distribute dummy classes that emulate the models and recommenders of the annotation app.
#   Models need only implement a transfrom method, that takes a string (the sentence) as input.
#
#   Conclusion:
#        Models need a transform method
########################################
from random import randint



class UsrModel:
    """
    Gets user model : default = user's utterance

    """
    def transform(self, sent):

        return sent
class SysDummyModel :
    """
        Emulates the system response
    """

    def transform(self, sent) :
        return "I am a mock model response"

class RedirectionModel :
    """
        Emulates the redirection response
    """

    def transform(self, sent) :
        n = randint(0, 1)
        return []


class BeliefStateDummyModel :
    """
        Emulates the BeliefStateTracker

            "labels": [
                "hotel-book people",
                "hotel-book stay",
                "hotel-book day",
                "hotel-name"
            ]
    """

    def transform(self, sent) :
        return [("hotel-book people", "5")]



class TypeDummyModel :
    """
        Emulates the BeliefStateTracker

            "labels": [
                "request",
                "inform",
                "farewell"
            ]
    """
    def transform(self, sent) :
        return ["request"]


class EmotionalStateModel :
    """
           Emulates the Emotional state tracker

               "labels"    : [

                "satisfied",
                "worried",
                "angry",
                "sceptical",
                "unhappy",
                "neutral"
               ]
       """

    def transform(self, sent) :
        l = [
                "satisfied",
                "worried",
                "angry",
                "sceptical",
                "unhappy",
                "neutral"]
        return ["neutral"]

class SystemDialogActModel :
    """
              Emulates the Dialog acts detector
              random function  : it is a multilabel problem so we emprically know that there can't be more than
              4 dialog acts per user's utterance.
              Therefore we return between  and 4 objects from the list

    """

    def transform(self, sent):
        return ['Greet', 'Ask', 'Request']
class UserDialogActModel :
    """
              Emulates the Dialog acts detector
              random function  : it is a multilabel problem so we emprically know that there can't be more than
              4 dialog acts per user's utterance.
              Therefore we return between  and 4 objects from the list

                  "labels"    : [

                "request",
                "inform",
                "hello",
                "farewell",
                "abandon",
                "accept",
                "acknowledgeThanks",
                "agree",
                "answer",
                "apologise",
                "attribute",
                "bye",
                "clarify",
                "complete",
                "confirm",
                "contradict",
                "disagree",
                "disapprove",
                "disConfirm",
                "emphatic",
                "enumerate",
                "exclaim",
                "explain",
                "greet",
                "hesitate",
                "identifySelf",
                "insult",
                "negate",
                "nominate",
                "offer",
                "pardon",
                "phatic",
                "predict",
                "refer",
                "refuse",
                "rejectSelf",
                "report",
                "retract",
                "selfTalk",
                "state",
                "suggest",
                "swear",
                "thank",
                "thirdParty",
                "unclassifiable",
                "uninterpretable"
                  ]
          """
    def transform(self, sent) :
        l =  [
                "ask",
                "request",
                "hello",
                "inform",
                "farewell",
                "abandon",
                "accept",
                "acknowledgeThanks",
                "agree",
                "answer",
                "apologise",
                "attribute",
                "bye",
                "clarify",
                "complete",
                "confirm",
                "contradict",
                "disagree",
                "disapprove",
                "disConfirm",
                "emphatic",
                "enumerate",
                "exclaim",
                "explain",
                "greet",
                "hesitate",
                "identifySelf",
                "insult",
                "negate",
                "nominate",
                "offer",
                "pardon",
                "phatic",
                "predict",
                "refer",
                "refuse",
                "rejectSelf",
                "report",
                "retract",
                "selfTalk",
                "state",
                "suggest",
                "swear",
                "thank",
                "thirdParty",
                "unclassifiable",
                "uninterpretable",
                "silence"]
        n = randint(1,5)

        def recurs(liste, nbr, new_l=[]):
            if nbr == 0:
                return new_l
            else:
                nbis = randint(0, len(liste) - 1)
                new_l.append(liste[nbis])
                liste.pop(nbis)
                return recurs(liste, nbr - 1, new_l)
        new_l = recurs(l, n)

        # return new_l

        return ['silence']
class UserSatisfactionModel:
    """
        Gets user satisfaction according to his/her utterance
    """

    def transform(self, sent):

        n = randint(0,1)

        return []

class SuccessModel:
    """
        Says if conversation is a success
    """

    def transform(self, sent):

        n = randint(0,1)

        return []

class ResponsePertinenceModel:
    """
        Says if conversation is a success
    """

    def transform(self, sent):

        n = randint(0,1)

        return ['Y']


class IntentUnderstandingModel:
    """
        Says if conversation is a success
    """

    def transform(self, sent):

        n = randint(0,1)

        return []

class PreviousModel:
    """
        Says if the intention is the same as previous one
    """

    def transform(self, sent):

        n = randint(0,1)

        return ['no']

class IntentDetectionModel :
    """
                 Emulates the Intention detector
                 random function

                     "labels"    : [

                "delivery",
                "product",
                "payment",
                "purchase",
                "website",
                "customer_service",
                "store",
                "fidelity",
                "autre"]

    """
    def transform(self, sent) :

        l = [

                "delivery",
                "product",
                "payment",
                "purchase",
                "website",
                "customer_service",
                "store",
                "fidelity",
                "autre",
                "rien"

        ]

        return ["rien"]


class OrderStateModel :

    """

            Belief state tracker for delivery

    """
    def transform(self, sent) :

        l =  ['date', 'number', 'location']
        # return [()]
        # subtask = l[randint(0, len(l)-1)]
        #
        # if subtask == 'data' :
        #     return [('Order date', randint(1, 15))]
        #
        # elif subtask == 'name' :
        #     return [('Order name', randint(1, 300))]
        #
        # elif subtask == 'location' :
        #     loc = ['home', 'pointrelais', 'surplace']
        #     return [('Order location', loc[randint(0, len(loc)-1)])]
        #

class PaymentStateModel :
    """

            Belief state tracker for payment

    """
    
    def transform(self, sent) :
        return [()]
        # l = ['tool', 'code']
        #
        # subtask = l[randint(0, len(l)-1)]
        #
        # if subtask == 'tool' :
        #     tools = ['cb', 'check', 'paypal', 'bons', 'instalment', 'gift']
        #     return [('Payment tool', tools[randint(0, len(tools)-1)])]
        #
        # elif subtask == 'code' :
        #     return [('Payment code', 'CODE'+str(randint(0,100)))]


class ProductStateModel :

    """

            Belief state tracker for product

    """

    def transform(self, sent) :

        return [()]
        # return [("Product info", "Parfum Chanel 5")]


class WebsiteStateModel :
    """

            Belief state tracker for website

    """

    def transform(self, sent) :

        return [()]
        # l = ['account', 'device', 'data']
        #
        # subtask = l[randint(0, len(l) - 1)]
        #
        # if subtask == 'account':
        #     accounts = ['password', 'id', 'email', 'creation']
        #     return [('Customer account', accounts[randint(0, len(accounts) - 1)])]
        #
        # elif subtask == 'device':
        #     devices = ['mobile', 'pc', 'tablet']
        #     return [('Website device', devices[randint(0, len(devices) - 1)])]
        #
        # elif subtask == 'data' :
        #     datas = ['protect', 'remove', 'check', 'change']
        #     return [('Customer data', datas[randint(0, len(datas) - 1)])]

class StoreStateModel :

    """

            Belief state tracker for store

    """

    def transform(self, sent) :

        return [('Store name', "Parfum moins cher")]




class PolicyModel:
    """
        Defining basic policies for dialog management. Empirically, a subdialogue has at most 3 different policies

    """
    def transform(self, sent):

        pol =  [

                'Say Goodbye',
                'Find And Offer Booking',
                'Ask For Missing Slots',
                'Provide Info',
                'Try Book',
                'Search order',
                'Say Hello',
                'Proceed to checkpoint',
                'Ask for waiting',
                'Apologize',
                'Advise to look elsewhere',
                'Look for customer file',
                'Reset working memory',
                'Do nothing',
                'Repeat previous'
        ]
        n = randint(1, 3)

        def recurs(liste, nbr, new_l=[]):
            if nbr == 0:
                return new_l
            else:
                nbis = randint(0, len(liste) - 1)
                new_l.append(liste[nbis])
                liste.pop(nbis)
                return recurs(liste, nbr - 1, new_l)

        new_l = recurs(pol, n)
        # return new_l
        return ['Say Hello','Ask For Missing Slots']


class ResponseTypeModel:
    """

            What kind of response is provided by the system
    """

    def transform(self, sent):

        l = [

                "careful",
                "dauntless",
                "kind",
                "neutral"
            ]
        return ["neutral"]