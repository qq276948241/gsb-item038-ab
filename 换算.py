import sys
from pathlib import Path

每排 = 6


def 失败(消息):
    sys.stderr.write(消息 + "\n")
    raise SystemExit(1)


def 主():
    路径 = Path("层号")
    if not 路径.is_file():
        失败("找不到层号")
    原文 = 路径.read_text(encoding="utf-8")
    if 原文 == "":
        失败("层号不对")
    行 = 原文.split("\n")
    if 行 and 行[-1] == "":
        行.pop()
    if len(行) != 1:
        失败("层号不对")
    文本 = 行[0]
    if 文本 == "0":
        失败("层号为零")
    if not 文本.isdigit() or (len(文本) > 1 and 文本[0] == "0"):
        失败("层号不对")
    层 = int(文本)
    if 层 < 1 or 层 > 999:
        失败("层号不对")
    排 = (层 - 1) // 每排 + 1
    格 = (层 - 1) % 每排 + 1
    sys.stdout.write("第%s排第%s格\n" % (排, 格))


if __name__ == "__main__":
    主()
