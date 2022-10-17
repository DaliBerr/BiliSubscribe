from bilibili_api import user,sync,Credential
from bilibili_api.user import RelationType
import asyncio

#用于登录你的账号，f12可以看到
bili_jct = " "
sessdata = " "
buvid3 = " "

#你的账号ID 和 想要克隆的账号ID
MyUserID = 1342286038
TargetUserID = 30312113

credential = Credential(sessdata=sessdata, bili_jct=bili_jct,buvid3=buvid3)
MyUser = user.User(uid=MyUserID,credential=credential)
TargetUser = user.User(uid=TargetUserID, credential=credential)
Fo = TargetUser.get_all_followings()
ListFo = sync(Fo)
async def Subscribe():
    for i in ListFo:
        u = user.User(uid=int(i),credential=credential)
        await u.modify_relation(relation=RelationType.SUBSCRIBE)
        print(f"Subscribing {int(i)}")
        await asyncio.sleep(1)


sync(Subscribe())