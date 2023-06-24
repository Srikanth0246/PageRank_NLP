from src.Service.LoadInput import LoadInput
from src.Service.ConversationForest import ConversationForest
from src.Service.InteractionNetwork import InteractionNetwork


filePath="C:/Users/91897/Downloads/MajorProject-feature-standard/input/createdebate_released_no_parse.xlsx"

loadInput=LoadInput(filePath)
loadInput.loadDataFromAllSheets()
conversationForest=ConversationForest(loadInput)
conversationForest.buildConversationTrees()
trees=conversationForest.getAllConversationTrees()

for key in trees.keys():
    tree=trees[key]
    tree.showConversationTree()
    iNetwork=InteractionNetwork(tree,[])
    iNetwork.showInteractionNetwork()



