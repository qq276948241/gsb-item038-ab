import subprocess
import tempfile
from pathlib import Path

根 = Path(__file__).resolve().parent


def 跑(文本, 有文件=True):
    夹 = Path(tempfile.mkdtemp())
    (夹 / "换算.py").write_text((根 / "换算.py").read_text(encoding="utf-8"), encoding="utf-8")
    if 有文件:
        (夹 / "层号").write_text(文本, encoding="utf-8")
    结果 = subprocess.run(["python3", "换算.py"], cwd=夹, capture_output=True)
    return 结果.returncode, 结果.stdout.decode(), 结果.stderr.decode()


def 核对(名字, 得到, 码, 出, 错):
    if 得到 != (码, 出, 错):
        raise SystemExit(名字 + "没对上")


核对("第一格", 跑("1\n"), 0, "第1排第1格\n", "")
核对("次排首格", 跑("7\n"), 0, "第2排第1格\n", "")
print("对照通过")
