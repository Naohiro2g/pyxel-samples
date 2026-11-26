# pyxel-samplesの環境構築

何も入っていない機械から、`uv run hello_pyxel.py`で窓を出すまでの手順です。Python本体は、uvが`.python-version`のとおりに入れるので、別に入れなくてかまいません。段ごとに「確かめ」を置きました。通らなかったら、そこで止めて「うまくいかないとき」を見てください。

確かめた範囲（2026-11-26）：Ubuntuで、「3. 取ってきて動かす」が通りました。その機械には、uv、Git、SDL2がもう入っていました。Windowsの手順は、まだ誰も通していません。

## Windows（10／11）

### 1. uv

PowerShellで、次のどちらかを打ちます。

```powershell
winget install --id astral-sh.uv -e
```

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

確かめ：新しいターミナルを開いて、`uv --version`が版を表示する。

### 2. Git

```powershell
winget install --id Git.Git -e
```

確かめ：新しいターミナルで`git --version`が版を表示する。

### 3. 取ってきて動かす

```powershell
git clone https://github.com/Naohiro2g/pyxel-samples.git
cd pyxel-samples
uv run hello_pyxel.py
```

uvが、Python 3.13を落とし、`.venv`を作り、`uv.lock`に書いたpyxel 3.0.4を入れてから動かします。

確かめ：窓に、色が変わる「Hello, Pyxel!」と、横へ動く四角が出る。Escで終わる。

### 4. pyxelのcommand

`pyxel`のcommandも、`uv run`を付けて使います。

```powershell
uv run pyxel
```

確かめ：`pyxel run`、`pyxel edit`、`pyxel copy_examples`などの一覧が出る。

公式の作例を手元へ写して動かせます。`pyxel_examples`フォルダーは、Gitの管理の外にしてあります。

```powershell
uv run pyxel copy_examples
cd pyxel_examples
uv run pyxel run 01_hello_pyxel.py
```

画像と音を作る道具は`uv run pyxel edit`です。

### 5. VS Code

1. VS Codeを入れます（`winget install --id Microsoft.VisualStudioCode -e`）
2. 拡張の「Python」（Microsoft）を入れます
3. 「フォルダーを開く」で`pyxel-samples`を開き、「Python: Select Interpreter」で`.venv`のPythonを選びます

確かめ：`hello_pyxel.py`で`pyxel.text`にマウスを乗せると、説明が出る。

拡張の「Pyxel」（作者のkitaoさんのもの）を入れると、PythonやPyxelを入れずにVS Codeの中で動かせます。このrepoでは、uvで版をそろえる上の手順を使います。

## Linux（Ubuntu）

### 1. uvとGitとSDL2

```bash
sudo apt install curl git libsdl2-2.0-0
curl -LsSf https://astral.sh/uv/install.sh | sh
```

LinuxのpyxelはSDL2を外から使います（`pyxel_binding.abi3.so`が`libSDL2-2.0.so.0`を読む）。終わったら新しいターミナルを開きます。

確かめ：`uv --version`と`git --version`が版を表示する。

### 2. 取ってきて動かす

Windowsの「3. 取ってきて動かす」から先と同じです。

## macOS

1. Linuxの`curl -LsSf https://astral.sh/uv/install.sh | sh`でuvを入れます
2. Gitは`xcode-select --install`で入ります
3. Windowsの「3. 取ってきて動かす」から先と同じです

## uvを使わないやり方

公式の手引きの方法です。Python 3.11以上を入れ、`pip install -U pyxel`を打ちます。python.orgのinstallerでは、「Add python.exe to PATH」に印を付けます。この場合、pyxelの版は`uv.lock`でそろいません。

## うまくいかないとき

- `uv`や`git`が見つからない：ターミナルを開き直します。installerがPATHを足したのは、新しいターミナルからです
- Windowsで`irm`の行が止められる：`winget`の行を使います
- Linuxで`libSDL2-2.0.so.0`が見つからない：「1. uvとGitとSDL2」の`libsdl2-2.0-0`を入れます
- 窓が開かない：GPUのdriverを新しくします

## 参考

- Pyxelのuser guide：<https://github.com/kitao/pyxel/blob/main/docs/user-guide.md>
- uvのinstall：<https://docs.astral.sh/uv/getting-started/installation/>
