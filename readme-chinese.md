# 构建 Frida Manager 版本变体

> 状态：**draft-inactive（草稿，未激活）**。已有静态验证能力；激活前仍需完成代表性新版本接入和
> 经过授权的真实兼容性验证。

这个 Skill 为 Frida Manager 获取或编译、锁定、打包并验证一个精确 Frida 版本，使
`frida-server`、基于 frida-core 的 Device Engine、类型化 Server Adapter、Root 模块产物和发布证据
保持一致，同时明确区分“构建成功”和“运行时兼容”。

它会严格区分下载 Frida 官方预编译 Server 与从源码编译 Frida。

Skill 现已加入一份仅从实际读取的“熟悉并调整 Frida UI 管理器”会话提取的资格验证经验，涵盖候选哈希
变化、安装文件比对、Android/Root Manager 矩阵差异、Boot readiness、blocked 版本处理、原生构建
入口以及 GitHub Release 产物完整性。

## 安装到 Codex

草稿激活前不要安装。激活后，把完整的 `build-frida-manager-variants/` 源码目录链接到用户 Skill
目录；链接目标顶层必须直接包含 `SKILL.md`，不要复制可编辑源码。

Windows PowerShell：

```powershell
$skillsRoot = Join-Path $HOME ".agents\skills"
$source = (Resolve-Path "<仓库根目录>\build-frida-manager-variants").Path
$link = Join-Path $skillsRoot "build-frida-manager-variants"
New-Item -ItemType Directory -Force -Path $skillsRoot | Out-Null
if (Test-Path -LiteralPath $link) { throw "目标已存在：$link" }
New-Item -ItemType Junction -Path $link -Target $source | Out-Null
```

macOS：

```bash
skills_root="$HOME/.agents/skills"
source_dir="$(cd "<仓库根目录>/build-frida-manager-variants" && pwd)"
link_path="$skills_root/build-frida-manager-variants"
mkdir -p "$skills_root"
if [ -e "$link_path" ] || [ -L "$link_path" ]; then echo "目标已存在：$link_path" >&2; exit 1; fi
ln -s "$source_dir" "$link_path"
```

激活后可用 `$build-frida-manager-variants` 调用。需要跨 Agent 复用时，CC Switch v3.13 或更高版本可
从 `~/.agents/skills` 扫描/导入并同步到兼容目标；导入后仍需检查各 Agent 的格式、工具和权限。

## 文件说明

- `SKILL.md`：身份、获取/编译、打包、资格验证与发布关卡。
- `references/`：产物合同、兼容性矩阵和发布证据。
- `references/verified-history-qualification-lessons.md`：实际会话中的版本故障与晋级关卡。
- `scripts/check_variant_readiness.py`：只读检查 Manager 变体锁、哈希和目录结构。
