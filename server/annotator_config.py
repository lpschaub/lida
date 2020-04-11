##############################################
#  IMPORT STATEMENTS
##############################################

# >>>> Native <<<<
from typing import Dict, List, Any, Tuple, Hashable, Iterable, Union
from collections import defaultdict

# >>>> Local <<<<
from server.dummy_models import RedirectionModel, EmotionalStateModel, SystemDialogActModel, UserDialogActModel, IntentDetectionModel, OrderStateModel, PaymentStateModel, ProductStateModel, WebsiteStateModel, StoreStateModel, PolicyModel, ResponseTypeModel, UsrModel, UserSatisfactionModel, PreviousModel, SuccessModel, IntentUnderstandingModel, ResponsePertinenceModel


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
            "required"  : False,
            "labels"    : [

                "happy",
                "worried",
                "angry",
                "sceptical",
                "unhappy",
                "neutre",
                "disappointed",
                "sad"
            ]
        },
        "user satisfaction": {

            "description": "Rating user satisfaction at current turn",
            "label_type" : "multilabel_classification",
            "model"      : UserSatisfactionModel(),
            "required"   : False,
            "labels"     : [
                "satisfied",
                "not satisfied"
            ]

        },

        "system_dialog_act": {

            "description": "Whether the query was request / inform / farewell",
            "label_type": "multilabel_classification",
            "required": True,
            "model": SystemDialogActModel(),
            "labels": ['Silence', 'Ask', 'Morn', 'Request', 'Inform', 'Farewell', 'Abandon', 'Accept', 'AcknowledgeThanks', 'Agree', 'Answer', 'Apologise', 'Attribute', 'Bye', 'Clarify', 'Complete', 'Confirm', 'Contradict', 'Disagree', 'Disapprove', 'DisConfirm', 'Emphatic', 'Enumerate', 'Exclaim', 'Explain', 'Greet', 'Hesitate', 'IdentifySelf', 'Insult', 'Negate', 'Nominate', 'Offer', 'Pardon', 'Phatic', 'Predict', 'Refer', 'Refuse', 'RejectSelf', 'Report', 'Retract', 'SelfTalk', 'State', 'Suggest', 'Swear', 'Thank', 'ThirdParty', 'Unclassifiable', 'Uninterpretable']


        },
        "user_dialog_act": {

            "description": "Whether the query was request / inform / farewell",
            "label_type" : "multilabel_classification",
            "required"   : True,
            "model"      : UserDialogActModel(),
            "labels"     : [
                "ask",
                "morn",
                "request",
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
                "none",
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
                "silence",
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
            "labels"    : ["delivery",
            "product",
            "payment",
            "purchase",
            "website",
            "customer_service",
            "store",
            "fidelity",
            "autre",
            "rien",
            "saluer",
            "goodbye",
            "deliveryTime",
            "deliveryCost",
            "deliveryPlace",
            "deliveryNews",
            "damagedPackage",
            "deliveryCountry",
            "InvalidOrder",
            "missingItem",
            "CancelOrder",
            "ConfirmationOrder",
            "WrongItem",
            "ArticleExchange",
            "ProductAvailable",
            "ProductPrice",
            "ProductQuality",
            "productSize",
            "ProductTarget",
            "PaymentTool",
            "PaymentRefused",
            "DoublePayment",
            "Discount",
            "Refund",
            "Compensation",
            "MultipleAccount",
            "ChangeData",
            "Login",
            "AccountCreation",
            "GDPR",
            "WebsiteBug",
            "WebsiteDevice",
            "CustomerComplaint",
            "StoreHours",
            "StoreLocation"
            ]
        },

        "previous": {

            "description": "whether the intention is the same than previous one",
            "label_type" : "multilabel_classification",
            "required"   : False,
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

        "Order_belief_state": {

            "description": "Slot-value pairs for order  belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : OrderStateModel(),
            "labels"     : [

                "Order number",
                "Order Location",
                "Order date"

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

            ]

        },
        "Product_belief_state": {

            "description": "Slot-value pairs for product belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : ProductStateModel(),
            "labels"     : [

                "Product Name",
                "Product target"

            ]

        },
        "Website_belief_state": {

            "description": "Slot-value pairs for website belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : WebsiteStateModel(),
            "labels"     : [

                "Website device",
                "Customer account",
                "Customer Data",
                "Customer action"

            ]

        },

        "Store_belief_state": {

            "description": "Slot-value pairs for store belief state tracking",
            "label_type" : "multilabel_classification_string",
            "required"   : False,
            "model"      : StoreStateModel(),
            "labels"     : [

                "Store name"

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
                'Advise to look elsewhere',
                'Look for customer file',
                'Reset working memory',
                'Do nothing',
                'Repeat previous',
                'Negate request',
                'Ask for another question'
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
            "required"   : False,
            "model"      : IntentUnderstandingModel(),
            "labels"     : [

                "True",
                "False"
            ]
        },


        "response pertinence": {

            "description": "whether or not the system provided a relevant response",
            "label_type" : "multilabel_classification",
            "required"   : False,
            "model"      : ResponsePertinenceModel(),
            "labels"     : [

                "Y",
                "N"
            ]
        },

        "response type": {

            "description": "the type of dialogic answer the system provides",
            "label_type" : "multilabel_classification",
            "required"   : False,
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
            "label_type" : "multilabel_classification",
            "required"   : False,
            "model"      : RedirectionModel(),
            "labels"     : [
                    "Redirection",
                    "No redirection"
            ]

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

            else:

                raise ValueError("The label type, {}, is not supported"
                                 .format(labelType))

        return out

    ##############################################
    #  MAIN
    ##############################################


    # EOF
