##############################################
#  IMPORT STATEMENTS
##############################################

# >>>> Native <<<<
from typing import Dict, List, Any, Tuple, Hashable, Iterable, Union
from collections import defaultdict

# >>>> Local <<<<
from server.dummy_models import RedirectionModel, EmotionalStateModel, DialogActModel, IntentDetectionModel, DeliveryStateModel, PurchaseStateModel, PaymentStateModel, ProductStateModel, WebsiteStateModel, CustomerStateModel, StoreStateModel, PolicyModel, ResponseTypeModel, UsrModel, UserSatisfactionModel, PreviousModel, SuccessModel, IntentUnderstandingModel, ResponsePertinenceModel


##############################################
#                  CONFIG Dict
#
# The config dict describes all the data fields.
# This is also the place to specify models and label types.
#
# Available label types:
#
#     => "multilabel_classification":: displays as checkboxes in front end
#
#     => "multilabel_classification_string":: displays as a checkbox and text input for string value. Used for
#                                              slot-value pairs.
#
#     => "string":: displays underneath the user utterance (indicated by label_type of "data")
#
#############################################

##############################################
#  CODE
##############################################


class Configuration(object):
    """
    class responsible for configuration and valid annotation structure
    """


    configDict = {

        "usr": {
            "description": "The user's query",
            "label_type" : "data",
            "required"   : True
        },

        "emotional_state": {

            "description": "The user's emotional state",
            "label_type": "multilabel_classification",
            "model"     : EmotionalStateModel(),
            "required"  : True,
            "labels"    : [

                "satisfied",
                "worried",
                "angry",
                "sceptical",
                "unhappy",
                "neutre"
            ]
        },
        "user satisfaction": {

            "description": "Rating user satisfaction at current turn",
            "label_type" : "string",
            "model"      : UserSatisfactionModel(),
            "required"   : False,
            "labels"     : [
                "satisfied",
                "not satisfied"
            ]

        },

        "dialog_act": {

            "description": "Whether the query was request / inform / farewell",
            "label_type" : "multilabel_classification",
            "required"   : True,
            "model"      : DialogActModel(),
            "labels"     : [

                "request",
                "inform",
                "farewell",
                "hello",
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

        },

        "intent": {

            "description": "User intention",
            "label_type": "multilabel_classification",
            "model"     : IntentDetectionModel(),
            "required"  : True,
            "labels"    : [

                "delivery",
                "product",
                "payment",
                "purchase",
                "website",
                "customer_service",
                "store",
                "fidelity",
                "autre"

            ]

        },

        "previous": {

            "description": "whether the intention is the same than previous one",
            "label_type" : "multilabel_classification",
            "required"   : True,
            "model"      : PreviousModel(),
            "labels"     : [

                "yes",
                "no"
            ]
        },

        "success": {

            "description": "wheter the dialogue is a success",
            "label_type" : "multilabel_classification",
            "required"   : False,
            "model": SuccessModel(),
            "labels"     : [

                "success",
                "fail"
            ]

        },

        "Delivery_belief_state": {

            "description": "Slot-value pairs for delivery  belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : DeliveryStateModel(),
            "labels"     : [

                "Order number",
                "Delivery Location",
                "Order date",

            ]

        },
        "Purchase_belief_state": {

            "description": "Slot-value pair for purchase belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : PurchaseStateModel(),
            "labels"     : [

                "Order process",
                "Order issue",

            ]

        },
        "Payment_belief_state": {

            "description": "Slot-value pairs for payment belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : PaymentStateModel(),
            "labels"     : [

                "Payment tool",
                "Payment code",
                "Payment request"

            ]

        },
        "Product_belief_state": {

            "description": "Slot-value pairs for product belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : ProductStateModel(),
            "labels"     : [

                "Product available",
                "Product Quality",
                "Product Name",
                "Product target",
                "Product Origin",

            ]

        },
        "Website_belief_state": {

            "description": "Slot-value pairs for website belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : WebsiteStateModel(),
            "labels"     : [

                "Website bug",
                "Website device"

            ]

        },
        "Customer_belief_state": {

            "description": "Slot-value pairs for customer belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : CustomerStateModel(),
            "labels"     : [

                "Customer complaint",
                "Customer account",
                "Custommer Data",

            ]

        },
        "Store_belief_state": {

            "description": "Slot-value pairs for store belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : StoreStateModel(),
            "labels"     : [

                "Store name",
                "Store location ",
                "Store hour",

            ]

        },

        "policy_funcs": {

            "description": "Policy functions called for this query",
            "label_type" : "multilabel_classification",
            "required"   : False,
            "model"      : PolicyModel(),
            "labels"     : [

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

        },

        "sys": {

            "description": "The system's response",
            "label_type" : "data",
            "required"   : True
        },

        "intent understanding": {

            "description": "whether or not the system got the user's intention",
            "label_type" : "multilabel_classification",
            "required"   : True,
            "model"      : IntentUnderstandingModel(),
            "labels"     : [

                "True",
                "False"
            ]
        },

        "response pertinence": {

            "description": "whether or not the system provided a relevant response",
            "label_type" : "multilabel_classification",
            "required"   : True,
            "model"      : ResponsePertinenceModel(),
            "labels"     : [

                "Y",
                "N"
            ]
        },

        "response type": {

            "description": "the type of dialogic answer the system provides",
            "label_type" : "multilabel_classification",
            "required"   : True,
            "model"      : ResponseTypeModel(),
            "labels"     : [

                "careful",
                "dauntless",
                "kind",
                "neutral"
            ]
        },

        "redirection": {

            "description": "the system redirects the user",
            "label_type" : "string",
            "required"   : False,
            "model"      : RedirectionModel()

        }
    }


    @staticmethod
    def validate_dialogue(dialogue: List[Dict[str, Any]]) -> Union[str, List[Dict]]:
        """
        validates the dialogue and makes sure it conforms to the configDict
        """

        for i, turn in enumerate(dialogue):

            for labelName, info in Configuration.configDict.items():

                try:
                    turn[labelName]
                except KeyError:
                    if info["required"]:
                        return "ERROR1: Label \'{}\' is listed as \"required\" in the " \
                               "config.py file, but is missing from the provided " \
                               "dialogue in turn {}.".format(labelName, i)

                if info["required"] and not turn[labelName]:
                    return "ERROR2: Required label, \'{}\', does not have a value " \
                           "provided in the dialogue in turn {}".format(labelName, i)

                if "multilabel_classification" == info["label_type"]:
                    print(turn)
                    providedLabels = turn[labelName]

                    if not all(x in info["labels"] for x in providedLabels):
                        return "ERROR3: One of the provided labels in the list: " \
                               "\'{}\' is not in allowed list according to " \
                               "config.py in turn {}".format(providedLabels, i)

        return dialogue

    @staticmethod
    def create_annotation_dict():
        """
        Generates a dictionary mapping label names to a dictionary of their description, label types
        and, if applicable, the possible values the label can take.
        """
        out = {}

        for key, value in Configuration.configDict.items():
            temp = list(value["labels"]) if value.get("labels") else ""

            out[key] = {
                "label_type": value["label_type"],
                "labels": temp,
                "info": value["description"]
            }

        return out

    @staticmethod
    def create_empty_turn():
        """
        creates an empty turn based on the configuration dictionary
        """
        out = {}

        for key, value in Configuration.configDict.items():

            labelType = value["label_type"]

            if labelType == "data":
                out[key] = "query"

            elif labelType == "multilabel_classification" or \
                    labelType == "multilabel_classification_string":

                out[key] = []

            elif labelType == "string":

                out[key] = ""
            elif labelType == "bool":
                out[key] = bool

            else:

                raise ValueError("The label type, {}, is not supported"
                                 .format(labelType))

        return out

    ##############################################
    #  MAIN
    ##############################################


    # EOF
