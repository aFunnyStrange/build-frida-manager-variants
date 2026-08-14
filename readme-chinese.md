# 构建 Frida Manager 版本变体

> 状态：**draft-inactive（草稿，未激活）**。v2.0.2 仓库、授权矩阵和已完成的公开 Release 已提供
> 代表性证据；激活前仍需补齐报告与精确哈希绑定、一次独立前向使用和用户明确批准。

这个 Skill 为 Frida Manager 获取或编译、锁定、打包并验证一个精确 Frida 版本，使
`frida-server`、基于 frida-core 的 Device Engine、类型化 Server Adapter、版本兼容产物、Root 模块和
发布证据保持一致，并明确区分“构建成功”和“运行时兼容”。

它结合工作目录下两个已实际读取的历史会话，补充了 Manager 产品版本与 Frida 运行时版本的独立
维度、构建目标与工具链、依赖锁/运行时产物锁/发布清单三层契约、候选哈希变化、Android/Root
Manager 矩阵、blocked 隔离和 GitHub Release 完整性规则。
v2.0.2 的完整发布复核还补充了 Native 二进制路径脱敏和发布后平台 digest 校验。

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
- `references/build-targets-and-version-axes.md`：版本维度、构建目标、工具链、锁和复用产物语义。
- `references/`：产物合同、兼容性矩阵、发布和历史证据。
- `scripts/check_variant_readiness.py`：只读检查 Manager 变体锁、哈希和目录结构。
