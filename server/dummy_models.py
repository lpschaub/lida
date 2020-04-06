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
        if n == 0 :
            return "I redirect you to a competent agent"
        else :
            return ''


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


class PolicyDummyModel :
    """
        Emulates a Policy Predictor

            "labels": [
                'Say Goodbye',
                'Find And Offer Booking',
                'Ask For Missing Slots',
                'Provide Info',
                'Try Book'
            ]
    """

    def transform(self, sent) :
        return ["Find And Offer Booking", "Ask For Missing Slots"]


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
        return [l[randint(0,len(l)-1)]]


class DialogActModel :
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
        l =  ["request",
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
                "uninterpretable"]
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
        return new_l
class UserSatisfactionModel:
    """
        Gets user satisfaction according to his/her utterance
    """

    def transform(self, sent):

        n = randint(0,1)

        if n == 1:
            return ['satisfied']
        else :
            return ['not satisfied']

class SuccessModel:
    """
        Says if conversation is a success
    """

    def transform(self, sent):

        n = randint(0,1)

        if n == 0:
            return ['fail']
        else :
            return ['success']

class ResponsePertinenceModel:
    """
        Says if conversation is a success
    """

    def transform(self, sent):

        n = randint(0,1)

        if n == 0:
            return ['N']
        else :
            return ['Y']


class IntentUnderstandingModel:
    """
        Says if conversation is a success
    """

    def transform(self, sent):

        n = randint(0,1)

        if n == 0:
            return ['False']
        else :
            return ['True']

class PreviousModel:
    """
        Says if the intention is the same as previous one
    """

    def transform(self, sent):

        n = randint(0,1)

        if n == 0:
            return ['no']
        else :
            return ['yes']


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
                "autre"]
        return [l[randint(0, len(l)-1)]]


class DeliveryStateModel :

    """

            Belief state tracker for delivery

    """
    def transform(self, sent) :

        l =  ['time', 'cost', 'location']

        subtask = l[randint(0, len(l)-1)]

        if subtask == 'time' :
            return [('Order date', randint(1, 15))]

        elif subtask == 'cost' :
            return [('Delivery cost', randint(1, 300))]

        elif subtask == 'location' :
            loc = ['home', 'pointrelais', 'surplace']
            return [('Delivery location', loc[randint(0, len(loc)-1)])]


class PurchaseStateModel :
    """

         Belief state tracker for purchase

    """
    def transform(self, sent) :

        l = ['process', 'issue']

        subtask = l[randint(0, len(l) - 1)]

        if subtask == 'process' :
            process = ['change', 'cancel', 'other']
            return [('Order process', process[randint(0, len(process)-1)])]

        elif subtask == 'issue' :
            issues = ['invalid', 'wrong', 'missing', 'noConfirmation']
            return [('Order issue', issues[randint(0,len(issues)-1)])]
        
        
class PaymentStateModel :
    """

            Belief state tracker for payment

    """
    
    def transform(self, sent) :

        l = ['tool', 'code', 'request']

        subtask = l[randint(0, len(l)-1)]

        if subtask == 'tool' :
            tools = ['cb', 'check', 'paypal', 'bons', 'instalment', 'gift']
            return [('Payment tool', tools[randint(0, len(tools)-1)])]

        elif subtask == 'code' :
            return [('Payment code', 'CODE'+str(randint(0,100)))]

        elif subtask == 'request' :
            requests = ['refund', 'compensation', 'refused', 'invoice']
            return [('Payment request', requests[randint(0, len(requests) - 1)])]


class ProductStateModel :

    """

            Belief state tracker for product

    """

    def transform(self, sent) :

        return [("Product info", "Parfum Chanel 5")]


class WebsiteStateModel :
    """

            Belief state tracker for website

    """

    def transform(self, sent) :

        l = ['bug', 'device']

        subtask = l[randint(0, len(l) - 1)]

        if subtask == 'bug':
            bugs = ['account', 'homepage', 'connection', 'email', 'application']
            return [('Website bug', bugs[randint(0, len(bugs) - 1)])]

        elif subtask == 'device':
            devices = ['mobile', 'pc', 'tablet']
            return [('Website device', devices[randint(0, len(devices) - 1)])]

class CustomerStateModel :
    """

            Belief state tracker for customer

    """

    def transform(self, sent):

        l = ['account', 'complaint', 'data']

        subtask = l[randint(0, len(l) - 1)]

        if subtask == 'account':
            accounts = ['password', 'id', 'email', 'creation']
            return [('Customer account', accounts[randint(0, len(accounts) - 1)])]

        elif subtask == 'complaint':
            complaints = ['badAd', 'concurrence', 'service']
            return [('Customer complaint', complaints[randint(0, len(complaints) - 1)])]

        elif subtask == 'data' :
            datas = ['protect', 'remove', 'check', 'change']
            return [('Customer data', datas[randint(0, len(datas) - 1)])]

class StoreStateModel :

    """

            Belief state tracker for store

    """

    def transform(self, sent) :

        l = ['location', 'hours']

        subtask = l[randint(0, len(l) - 1)]

        if subtask == 'location' :
            locations = ['situé', 'France', 'magasin']
            return [('Store location', locations[randint(0, len(locations)-1)])]

        elif subtask == 'hours' :
            hours = ['PMC Lyon', 'dimanche', 'soir', 'matin']
            n = randint(1, (len(hours)))

            def recurs(liste, nbr, new_l=[]):
                if nbr == 0:
                    return new_l
                else:
                    nbis = randint(0, len(liste) - 1)
                    new_l.append(liste[nbis])
                    liste.pop(nbis)
                    return recurs(liste, nbr - 1, new_l)
            new_l = recurs(hours, n)
            return new_l


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
        return new_l


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
        return [l[randint(0, len(l)-1)]]