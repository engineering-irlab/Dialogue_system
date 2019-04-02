from Util import data_cleaning
from NLU import IntentClassification
from data.initial_data import loading_history
path="..\.\history\\"
ic=IntentClassification.IntentClassify()
historywithtime=loading_history(path)


def get_response(text):
    global historywithtime
    text=data_cleaning.remove_punctuation(text,strip_all=False)
    text=data_cleaning.get_stopwords(text)
    text=ic.Communicative_function(text)
    #text = PolicyLearning.policy(text)
    print('\033[1;32m' + "槽信息填充情况：", ic.slot, '\033[0m')
    print('\033[1;32m' + "上一轮对话意图：", ic.usr_intent[-2], '\033[0m')
    print('\033[1;32m' + "当前对话意图：", ic.usr_intent[-1], '\033[0m')

    return text



