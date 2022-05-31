# coding:utf-8
import os
from pathlib import Path
from typing import Callable
import pickle
import json
import os
import tempfile
# CURR_PATH = Path(__file__).absolute().parent
# SETTING_STORE_FILE = CURR_PATH.joinpath("setting_store.json")
TMP_DIR = tempfile.gettempdir()
SETTING_STORE_FILE = Path(TMP_DIR).joinpath("drink_notify.json")


class SettingClass:
    # 设置类
    title = "丹丹喝水提醒"
    min_notified = False
    drink_open = False  # 是否开启喝水提醒
    drink_words = ["该喝水啦", "喝水时间到!"]  # 喝水提醒词
    drink_notify_interval = 3600  # 提醒喝水间隔

    class_on_open = False  # 是否开启上课提醒
    class_off_open = False  # 是否开启下课提醒
    class_notify_before = 600  # 上下课提前提醒时间
    class_store = []  # 存储课程
    icon = ""

    @staticmethod
    def save():
        save_setting(SettingClass)

    @staticmethod
    def to_dict():
        res = {}
        for k in dir(SettingClass):
            v = getattr(SettingClass, k)
            if not isinstance(v, Callable) and not k.startswith("__"):
                res[k] = v
        return res


def load_setting():
    # 将配置文件中的配置添加到设置类中
    if SETTING_STORE_FILE.exists():
        with open(SETTING_STORE_FILE, "r") as f:
            _setting = json.load(f)
        for k, v in _setting.items():
            setattr(SettingClass, k, v)


def save_setting(setting):
    print("save setting")
    with open(SETTING_STORE_FILE, "w") as f:
        json.dump(setting.to_dict(), f, ensure_ascii=False, indent=4)


class Constant:
    icon = b'iVBORw0KGgoAAAANSUhEUgAAALcAAAC3CAYAAABQbs+fAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAACvpSURBVHhe7d0HmCxFFQXgRsw554SKWTGhYoQnimAAFUVEgSeioqKoGEFARcWAoBLEiBjQh1nBCCIqJsxixoA5P3MW+Yu9z3pNz0zP7OyyU1Pn+/rb3ZlOs3Pq1qlzb1VvsHbt2rOaiooCcb6FnxUVxaGSu6JYVHJXFItK7opiUcldUSwquSuKRSV3RbGo5K4oFpXcFcWikruiWFRyVxSLSu6KYlHJXVEsKrkrikUld0WxqOSuKBaV3BXFopK7olhUci8TzjrrrOa///3vwl8Vy4E6h3KJgMw2ON/5zokh/v7HP/7R/OEPf2jO/r83f/nLX5q//vWvzb/+9a+0z0UvetHmUpe6VNoufelLNxe60IXScRWToZJ7iYG8X/jCF5o3v/nNzYc//OHmd7/7XXOBC1ygueIVr9hc/epXby55yUumv0X13//+9833v//95te//nU6FsG33HLL5u53v3tz+9vfvrnGNa6xrqFUjEYl9xLhT3/6U/PWt761edGLXtRc+MIXbh7/+Mcnkl7pSldqLnKRiyzs1Q0RXqP42c9+1nz5y19OjeLEE09s/v3vf6dz7LjjjonsF7/4xdftH70E1AZwDiq5pwwE/NznPtc85SlPSYQ78sgjm5vd7GbrSZMg4iASxj75+6TLT3/60+YjH/lI8/a3v7350pe+1GyyySbNox71qGaLLbZoLne5yy3sWRGo5F4EgoQbbLBB+vm3v/2tOeqoo5rXv/71zbOf/exmu+22W5Io6lp//vOfm8985jPNq1/96hTZr3Od6zTPf/7zE9GrVj8HldyLQJAbgX/72982Bx98cHPqqacmcm+00UYLey09DEw/9rGPNa94xSuaH/3oR81ee+3V7LLLLkkOuT9Yika20lHJPQUEsT//+c83b3rTm9JgcTlIFY0LXId0Of3001ME/8EPftAceuihzR3veMf0/jyiknuRMHB85StfmaQBYhswttEmYSB/PaTNNBrD3//+9+b4449Pg9nNNtused7znpdsxmmdf1ZQyb0IiJRr1qxJupcUufa1rz2UQOw+Wlmkp89ZgJe5zGWS5Xf+859/Ya/FIRqMezjzzDObZz7zmc1PfvKTZZdKKwGV3BMCgT7+8Y+nqHjAAQek7j+IFUCw//znP4lcBprHHXdc8rAveMELpkQNu49eBn73ne50p2bTTTdNNt/1r3/9RPoNN9wwvd917mGI/TWmww8/vHn3u9+dNLnze30eIngl94SgaV/60pc2V73qVZtnPOMZC6+uT0JEPvDAA5NE2GGHHZqdd945uRq5myGaI/kvf/nL5jvf+U6yEQ0O+dvIvdVWWzX3u9/9EikntfvIlGOOOSbZki984Qube9zjHgvvlI1K7gkQOvsTn/hEkiUicR4JEfa0005LXjcyv+QlL1lHzJz8w6InyfPzn/88Ef0tb3lLOt+Nb3zjJDM233zzkYmgNvjv73znO5sXvOAFc0PwSu6eCFLaPvjBDyaCvPa1r2023njj9QgLJ510UpIqu+22W7LkFisBnFuDcl7R97vf/W7qBfbYY4/OAewgBMFf/OIXJyflDne4Qzp3qRKlfOE1Zfzwhz9M5N5+++0TsYHTEW7HySef3Oy///4p3b569er0+mKrAZ2DJpcU+sAHPpBS8VLzt7vd7Zr99tsv1aT0gUEricMH32effdJnKVl7F/XJkAuRYsv/XiwQjHY94YQTEil23333hXfOgfe/9rWvNYcddljzsIc9rHnQgx607vVpEsi5uB4GqKecckrzi1/8ornLXe7SvOMd70iD12Gf2XsGqPe+972bu93tbonk//znP9cdUxqKIncQKbb872ngW9/6VkrUPP3pT0/Zv5wQBoQq/y572cumeo+lJovPds1rXrM54ogjmte85jXJCUFYDc97w3CJS1wiFV+pMnzd61638Gp5KIbcoha34aEPfWhyGWy+/Ec/+tHJefD+YkDzkgOsuzzrh8Qi+vvf//7mG9/4RtKy047WgyDiug558p73vCeRe+utt26OPvrohT3WR97YRX/7i/i/+tWvluV+lxsz/YmiO/3jH/+YsnH3ve99m1vd6lbNV7/61WTVcTNuetObNg9/+MObbbbZJiVPxkVc45vf/GZqJPQ0IIrN+673oQ99KDkZUYa6HMgbEd/c9WVJuStk0TAtTp5opJwXg9QSMdPk9uXSjJIjyGWw9aQnPSlFbJm/a13rWs3jHve4VCZ661vfOjkXkTTpC9eQTfzkJz+Z/Gh2XEgO761duzYNMA34uA9LLUeGAWFv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'
    RUN_PATH = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"