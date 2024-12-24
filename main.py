from pkg.plugin.context import APIHost, BasePlugin, EventContext, handler, register
from pkg.plugin.events import (
    GroupNormalMessageReceived,
    PersonNormalMessageReceived,
)

# 还没有提供内置持久化库，所以这里先不写

# 注册插件
@register(name="Analysis", description="null", version="0.1", author="Constellation39")
class AnalysisPlugin(BasePlugin):
    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        match event := ctx.event:
            case PersonNormalMessageReceived():
                msg = (
                    event.text_message
                )  # 这里的 event 即为 PersonNormalMessageReceived 的对象
                if msg == "hello":  # 如果消息为hello
                    # 输出调试信息
                    self.ap.logger.info("hello, {}".format(event.sender_id))

                    # 回复消息 "hello, <发送者id>!"
                    ctx.add_return("reply", ["hello, {}!".format(event.sender_id)])

                    # 阻止该事件默认行为（向接口获取回复）
                    ctx.prevent_default()
            case _:
                self.ap.logger.debug("unknown event: {}".format(event))
                pass

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        match event := ctx.event:
            case GroupNormalMessageReceived():
                msg = event.text_message
                if msg == "hello":  # 如果消息为hello
                    # 输出调试信息
                    self.ap.logger.debug("hello, {}".format(event.sender_id))

                    # 回复消息 "hello, everyone!"
                    ctx.add_return("reply", ["hello, everyone!"])

                    # 阻止该事件默认行为（向接口获取回复）
                    ctx.prevent_default()

            case _:
                self.ap.logger.debug("unknown event: {}".format(event))
                pass

    # 插件卸载时触发
    def __del__(self):
        pass
