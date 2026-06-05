# Mayday Radio · AI 电台 DJ

按主题和时长编排一档完整的五月天主题广播节目，含 DJ 串场、情绪曲线和开场/收尾。

## 功能

- **主题电台**：失恋治愈 / 通勤励志 / 深夜疗愈 / 演唱会倒计时
- **自定义情绪曲线**：描述你想要的情绪旅程
- **排除曲目**：不想听的歌可以跳过
- **DJ 串场**：按风格指南生成的自然过渡文本

## 使用

```
# 用 build-program.py 编排曲目
python scripts/build-program.py --theme 失恋治愈 --duration 30

# 带排除列表
python scripts/build-program.py --theme 通勤励志 --duration 45 --skip 派对动物,轧车

# 自定义情绪曲线
python scripts/build-program.py --theme 自定义 --duration 60 --arc 3,2,5,4,8,7
```

## 依赖

- lyrics-db（通过 `scripts/sync-lyrics-db.sh` 同步）
- Python 3.12+（stdlib only）
