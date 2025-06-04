import json
from pathlib import Path
import random
from nonebot.rule import to_me
from nonebot_plugin_alconna import Alconna, Args, Arparma, on_alconna
from nonebot_plugin_uninfo import Uninfo
from nonebot.plugin import PluginMetadata

CONFIG_PATH = str(Path(__file__).parent.resolve()) + "/config.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

__plugin_meta__ = PluginMetadata(
    name="来杯咖啡",
    description="来一杯热气腾腾的咖啡吧~",
    usage="""
    指令：
        来杯咖啡
    """.strip(),
    extra={
        "author": "舰长的初号",
        "version": "1.0",
        "priority": 5,
        "plugin_type": "NORMAL",
    },
)

_matcher = on_alconna(
    Alconna(
        "来杯咖啡",
    ),
    priority=5,
    block=True,
    rule=to_me()
)

@_matcher.handle()
async def _(session: Uninfo, arparma: Arparma):
    # 从配置中随机选取
    coffee = random.choice(CONFIG["coffee_types"])
    topping = random.choice(CONFIG["toppings"])
    flavor = random.choice(CONFIG["flavors"])
    scene = random.choice(CONFIG["scenes"])
    action = random.choice(CONFIG["actions"])
    emoji = random.choice(CONFIG["emojis"])
    template = random.choice(CONFIG["templates"])

    # 替换模板变量
    reply = template.format(
        coffee=coffee,
        topping=topping,
        flavor=flavor,
        scene=scene,
        action=action,
        emoji=emoji
    )
    await _matcher.send(reply)