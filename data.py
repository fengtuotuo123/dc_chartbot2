# 账号认证列表，多账号一起开的时候，可在列表中追加
authorization_list = [""]

# 账号认证,从指定频道text_chanel_id 随机获取聊天内容时使用
authorization = ""

# 获取聊天信息的频道id
# 频道id获取方式: 打开开发者模式（用户设置-高级设置-开发者模式）,右键点击想要聊天的频道，再点击复制频道ID
text_channel_id = ""

# 需要自动聊天的频道id，同时刷多个服务器，可在列表中追加
channel_id_list = [""]

# Ture：脚本模式， False：从指定频道text_chanel_id 随机获取聊天内容
script_mode_flg = False

# 聊天脚本，script_mode_flg=Ture时使用
script_text_list = [
    "新来的朋友要关注以下几点1.好好聊天 不要FUD 认真解答问题 2.不准发Galaxy Quiz的答案 3.不要谈ZZ 树就会有!4.角色获取和加入时间没有关系 只跟你贡献和活跃程度有关！5.有了角色还是可能被回收的！",
    "友情提醒大家一下，领水的任务可以每天都可以做，准确的说是八小时!",
    "再提示下新盆友，SWAP ERROR报错社区给出的解决方案是1.加大Gas 2.如果还是不行，最好就等人少时候交互3.或者等待RPC完全修复4.术大牛可以自己搭个RPC!",
    "祝愿项目越来越好吧",
    "说实话，这个社区的氛围我感觉是我接触到社区里面已经算是很好的了",
    "还有没有需要帮助的新朋友啊，社区老人都很热心呢",
    "银河只有几个简单的任务，但是目前项目的任务都在银河，没有在zealy，大家注意分别",
    "任务里面有不明白的，新人可以问哈",
    "多回答大家的问题也是有帮助的",
    "这个项目的三币模型非常有创意，大家可以去读一下他的白皮书",
    "感觉交互起来越来越流畅了，项目方在做事啊",
    "熊弟们，你们仔细看过白皮书和经济模型吗，我感觉挺有创意的",
    "你们组池子在哪个网站上，我还没找到",
    "我想把里面的应用都体验下，找BUG出来是不是就能长树了哈",
    "项目方是懂营销的，产品也不错",
    "现在感觉流畅多了~",
    "新来的熊弟们可以先看下置顶留言",
    "你们今天又领水了吗，可以每天领取的",
    "兄弟们，有个问题，BGT是不是无法空投获得，只能组池子",
    "新来的朋友要注意不要FUD，认真解答问题  不要发Galaxy Quiz的答案 认真回答问题会有惊喜哈",
    "今天程序很丝滑，大家可以去感受下",
    "今天你们领水了没，现在能领到",
    "领不到水的多试几次，一般都能成，我刚才就是",
    "在提示下，前两天交互失败的现在可以去试试，丝滑了不少，项目方在做事哦",
    "我看还有问总是聊天怎么还没得到树这个问题的，大家放平心态，有时间就说几句，主要是活跃氛围，能给新人解决问题",
    "社区氛围很好，这在其他项目不多见啊，看好这个项目，带社区成员起飞",
    "如果领水报错，可以尝试换个节点，我试了，很好用",
    "继续努力",
]

# 信息发送的间隔时间
chat_sleep_time_min = 50
chat_sleep_time_max = 60

# 多频道一起刷的间隔时间
channel_sleep_time_min = 10
channel_sleep_time_max = 20

# 多账号一起刷的间隔时间
ac_sleep_time_min = 10
ac_sleep_time_max = 20


# 是否检测mod说话
check_mod_flg = True

# dc服务器id，check_mod_flg=True时需要设置
# 服务器id获取方式：打开开发者模式（用户设置-高级设置-开发者模式），右键点击想要聊天的服务器，再点击复制服务器ID
guild_id = ""

# mod角色列表（包括mod，管理员等），check_mod_flg=True时需要设置
# mod角色ID获取方式：打开开发者模式（用户设置-高级设置-开发者模式），点击mod头像，右键点击该mod的mod身份组，点击复制身份组ID，如果有多个管理身份组，都复制添加到列表中
mod_role_id_list = [""]
