from .Ernie import Ernie,FastErnie

BDUSS_BFESS='pkUDVrTjdmY3NFY0x2SDNrflZRdnJ5SUx3eXlDZ3JGVzFoQ0dRQVNRaGZEZlJrSVFBQUFBJCQAAAAAAQAAAAEAAAALZWR9bHdtYW50AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF-AzGRfgMxkcE'
BAIDUID='3E533140D1AEDD31474BE5D9A3935DE1:FG=1'
# i=str(0x0000026FF2A193C0)
# ernie=Ernie(BAIDUID,BDUSS_BFESS)
# ernie.deleteConversation(sessionId=i)

class erniebot:
    def __init__(self, BAIDUID: str, BDUSS_BFESS: str):
        self.ernie = Ernie(BAIDUID, BDUSS_BFESS)
        self.sessionId = ''
        self.parentChatId = '0'

    def ask(self,question:str,sessionId='',parentChatId='0'):
        if  sessionId=='':
            self.sessionId = self.ernie.newConversation(question)
        else:
            self.sessionId=sessionId
            self.parentChatId=parentChatId
        result = {}
        urls=[]
        for data in self.ernie.askStream(question, self.sessionId,self.parentChatId):
            if data['urls']:
                for url in data['urls']:
                    if url not in urls:
                        urls.append(url)
        self.parentChatId = data['botChatId']
        result = data
        result['urls']=urls
        result['sessionId']=self.sessionId
        return result

