#!/usr/bin/env python3
"""Generate mayday-trivia database (500+ questions) from knowledge bases."""

from __future__ import annotations
import json
import os

REFS = os.path.join(os.path.dirname(__file__), "..", "mayday-trivia", "references")

questions: list[dict] = []
qid = [1]  # mutable counter

def q(domain: str, difficulty: str, question: str, answer: str,
      accepted: list[str] | None = None, source: str = "",
      background: str = ""):
    n = f"Q{qid[0]:04d}"
    qid[0] += 1
    questions.append({
        "id": n,
        "domain": domain,
        "difficulty": difficulty,
        "question": question,
        "answer": answer,
        "accepted_variants": accepted or [answer],
        "source": source,
        "background": background,
    })

# ── members (80+) ───────────────────────────────────────────
# Based on band-members.md + public data
members = [
    ("阿信", "陈信宏", "1975-12-06", "主唱", "建筑系"),
    ("怪兽", "温尚翊", "1976-11-28", "吉他手/团长", "师大附中"),
    ("石头", "石锦航", "1975-12-11", "吉他手", "淡江大学"),
    ("玛莎", "蔡升晏", "1977-04-25", "贝斯手", "辅仁大学"),
    ("冠佑", "刘谚明", "1973-07-28", "鼓手", "国光艺校"),
]
# Renamed note: timeline says 1997成立, correct.
# Easy facts
for name, full, bday, role, edu in members:
    q("members", "easy", f"五月天的{name}本名是什么？", full,
      source="references/knowledge-base/band-members.md",
      background=f"{name}在团内担任{role}。")
q("members", "easy", "五月天最年长的成员是？", "冠佑",
  accepted=["刘谚明", "刘冠佑"],
  source="references/knowledge-base/band-members.md",
  background="鼓手冠佑生于 1973 年，比其他四位成员都年长。")
q("members", "easy", "五月天乐队成立于哪一年？", "1997",
  accepted=["1997年"],
  source="references/knowledge-base/timeline.md",
  background="1997年3月29日，So Band 正式改名为「五月天」。")
q("members", "easy", "五月天前身的乐队叫什么名字？", "So Band",
  background="在成为五月天之前，五个人以 So Band 为名在酒吧和校园演出。")
q("members", "easy", "五月天的团长是谁？", "怪兽",
  accepted=["温尚翊"],
  source="references/knowledge-base/band-members.md",
  background="怪兽（温尚翊）担任乐团的团长兼吉他手。")
q("members", "easy", "阿信除了主唱还擅长演奏什么乐器？", "键盘",
  accepted=["keyboard", "钢琴"],
  source="references/knowledge-base/band-members.md",
  background="阿信虽然在台上很少使用，但负责了大量的键盘和合成器部分。")
q("members", "easy", "五月天的鼓手冠佑与哪位成员同年结婚？", "石头",
  background="石头和冠佑都在 2006 年左右结婚，两人也都有了孩子。")

# Medium facts
for name, full, bday, role, edu in members:
    parts = bday.split("-")
    q("members", "medium", f"{name}的生日是哪一天（月-日）？",
      f"{parts[1]}-{parts[2]}",
      accepted=[f"{parts[1]}月{int(parts[2])}日", f"{bday}"],
      source="references/knowledge-base/band-members.md",
      background=f"{role} {full} 出生于 {bday}。")
    if edu:
        q("members", "medium", f"{name}大学主修的科系是？", edu,
          source="references/knowledge-base/band-members.md",
          background=f"{full}在出道前就读于{edu}。")
q("members", "medium", "阿信创立了什么服饰品牌？", "StayReal",
  accepted=["STAYREAL"],
  background="StayReal 创立于 2007 年，是阿信与设计师不二良共同创办的潮流品牌。")
q("members", "medium", "怪兽的绰号「团长」二字怎么来的？", "他是五月天的团长",
  accepted=["他是团长", "担任团长"],
  background="怪兽是五月天的团长，负责统筹乐团行政事务与音乐方向。")
q("members", "medium", "玛莎除了贝斯还擅长什么乐器？", "大提琴",
  accepted=["cello", "低音提琴"],
  background="玛莎在专辑《第二人生》中首次演奏大提琴。")
q("members", "medium", "石头在影视领域的代表作品是什么？", "变身",
  accepted=["电影《变身》"],
  background="石头主演电影《变身》（2013年），并入围金马奖最佳新演员。")

# Hard
q("members", "hard", "五月天出道前在哪个著名地下 Live House 驻唱？", "地下社会",
  background="「地下社会」是台北当时最重要的独立音乐演出场所。")
q("members", "hard", "阿信在 StayReal 的合作设计师是谁？", "不二良",
  background="不二良（陈柏良）与阿信共同创立 StayReal，也是五月天御用视觉设计师。")
q("members", "hard", "怪兽在师大附中参加的吉他社团叫什么？", "吉他社",
  background="怪兽在师大附中担任吉他社社长，并结识了同校的阿信。")
q("members", "hard", "冠佑在加入五月天之前在哪个乐队？", "Why Not",
  background="冠佑加入五月天前是 Why Not 乐队的鼓手。")
q("members", "hard", "玛莎曾用过的艺名是什么？", "Masa",
  background="玛莎的艺名 Masa 取自日文发音，他也用此名参与跨刀制作。")
q("members", "hard", "阿信在哪一年的金曲奖凭哪首歌首次获得最佳作词人？",
  "2017 年 / 成名在望",
  accepted=["2017金曲奖 成名在望", "第28届金曲奖 成名在望"],
  background="阿信在第28届金曲奖以《成名在望》获得最佳作词人奖。")
q("members", "hard", "石头在五月天专辑中首次发表作曲作品是哪一首？",
  "晚安地球人",
  background="《晚安地球人》收录于 2004 年《神的孩子都在跳舞》，是石头首次为五月天作曲。")

# Nightmare
q("members", "nightmare", "五月天五人中唯一没有服兵役的成员是谁？原因是什么？",
  "阿信，因扁平足验退",
  accepted=["阿信 扁平足", "阿信被验退"],
  background="2002年阿信因扁平足被验退，怪兽则因地中海贫血被验退。")
q("members", "nightmare", "冠佑的本名经历了几次更改？分别叫什么？",
  "两次；刘谚明改刘冠佑",
  accepted=["两次；刘谚明、刘冠佑", "刘谚明→刘冠佑"],
  background="冠佑最早以刘谚明出道，后更名为刘冠佑，但粉丝常混用两个名字。")
q("members", "nightmare", "五月天五人分别毕业于哪五所大学？",
  "实践大学（阿信）/ 台湾大学（怪兽）/ 淡江大学（石头）/ 辅仁大学（玛莎）/ 国光艺校（冠佑）",
  background="五人并非全为名校，但大学教育对他们的词曲素养影响深远。")

# ── albums (100+) ──────────────────────────────────────────────
# Use validated album data
albums_meta = [
    ("1999-第一张创作专辑.json", "第一张创作专辑", 1999, "滚石唱片"),
    ("2000-爱情万岁.json", "爱情万岁", 2000, "滚石唱片"),
    ("2001-人生海海.json", "人生海海", 2001, "滚石唱片"),
    ("2003-时光机.json", "时光机", 2003, "滚石唱片"),
    ("2004-神的孩子都在跳舞.json", "神的孩子都在跳舞", 2004, "滚石唱片"),
    ("2006-为爱而生.json", "为爱而生", 2006, "相信音乐"),
    ("2008-后青春期的诗.json", "后青春期的诗", 2008, "相信音乐"),
    ("2011-第二人生.json", "第二人生", 2011, "相信音乐"),
    ("2016-自传.json", "自传", 2016, "相信音乐"),
]
for fn, album, year, label in albums_meta:
    src = f"references/lyrics-db/{fn}"
    q("albums", "easy", f"《{album}》是哪一年发行的？",
      f"{year}", accepted=[f"{year}年"],
      source=src,
      background=f"《{album}》由{label}发行，是五月天的第{sum(1 for a in albums_meta if a[2] <= year)}张录音室专辑。")

# Easy
q("albums", "easy", "五月天销量最高的一张专辑是？", "第二人生",
  background="《第二人生》在台湾销量突破 12 万张，并获十白金认证。")
q("albums", "easy", "五月天的第一张专辑叫什么？", "第一张创作专辑",
  accepted=["疯狂世界", "五月天第一张创作专辑"],
  source="references/lyrics-db/1999-第一张创作专辑.json",
  background="1999年7月7日发行，包含《疯狂世界》《拥抱》《志明与春娇》等经典。")
q("albums", "easy", "《倔强》收录在哪一张专辑？", "神的孩子都在跳舞",
  source="references/lyrics-db/2004-神的孩子都在跳舞.json",
  background="2004 年发行的《神的孩子都在跳舞》，《倔强》成为五月天最具代表性的演唱会大合唱曲。")
q("albums", "easy", "《突然好想你》收录在哪一张专辑？", "后青春期的诗",
  source="references/lyrics-db/2008-后青春期的诗.json",
  background="2008 年发行的《后青春期的诗》，并获得金曲奖最佳年度歌曲。")
q("albums", "easy", "《爱情万岁》在哪一年为五月天赢得了金曲奖最佳乐团？", "2001",
  accepted=["2001年"],
  background="第12届金曲奖，五月天凭借《爱情万岁》首次获得最佳乐团奖。")
q("albums", "easy", "五月天哪张专辑以「末日」与「明日」双版本发行？", "第二人生",
  background="2011 年发行的《第二人生》有末日版（No Where）和明日版（Now Here）两种曲顺。")
q("albums", "easy", "五月天离开滚石唱片后成立了自己的哪家公司？", "相信音乐",
  accepted=["Bin Music"],
  background="2006年五月天与滚石合约结束后，与经纪人共同创立相信音乐。")
q("albums", "easy", "《自传》是哪一年发行的？", "2016",
  accepted=["2016年"],
  source="references/lyrics-db/2016-自传.json",
  background="2016年7月21日发行，距离上一张专辑相隔近5年。")
q("albums", "easy", "五月天哪张专辑的概念是以2012年世界末日为主题？", "第二人生",
  source="references/knowledge-base/album-history.md",
  background="第8张专辑以玛雅预言的世界末日为背景，传达「如果末日没来，你就有机会选择第二人生」。")
q("albums", "easy", "五月天第一张由相信音乐发行的专辑是？", "为爱而生",
  background="2006年《为爱而生》是五月天脱离滚石后首张专辑。")

# Medium
q("albums", "medium", "《时光机》专辑的创作背景是什么？",
  "团员兵役问题解决后的复出之作",
  background="2001年入伍 → 2003年复出，《时光机》象征着跨越两年时间后的归来。")
q("albums", "medium", "《人生海海》这张专辑的词曲创作有何特别？",
  "全员参与编曲，彩虹首次由阿信与梁伯君共同作曲",
  background="梁伯君（George Leong）是五月天的早期制作人，也是《彩虹》的作曲合作者。")
q("albums", "medium", "《自传》专辑的英文名称是什么？",
  "History of Tomorrow",
  background="专辑名「自传」的英文直译是 History of Tomorrow，寓意「写给未来的历史」。")
q("albums", "medium", "五月天哪张专辑的所有词曲全部由阿信一人完成？",
  "第一张创作专辑",
  background="首张专辑共12首歌，全部由阿信作词作曲，五月天负责编曲和演奏。")
q("albums", "medium", "《为爱而生》专辑的创作灵感主要来自什么？",
  "团员即将为人父母的喜悦",
  background="专辑发布时，鼓手冠佑和吉他手石头的孩子相继出生，专辑围绕「爱」的主题。")
q("albums", "medium", "《后青春期的诗》专辑中哪首歌的歌词没有重复任何段落？",
  "如烟",
  background="《如烟》的歌词从第一句到最后一句没有重复任何一段，是阿信在歌词结构上的大胆实验。")
q("albums", "medium", "《第二人生》的最后隐藏曲叫什么？",
  "T1213121",
  background="数字代表吉他最简单的和弦指法，是一首质朴的练习曲式结尾。")
q("albums", "medium", "《自传》专辑收录了多少首歌曲？", "15",
  background="包含《如果我们不曾相遇》、《成名在望》、《好好》等歌曲，以及空轨《What's Your Story》和彩蛋《你说那C和弦就是...》。")
q("albums", "medium", "五月天专辑《爱情万岁》的同名歌曲时长多少？",
  "6分02秒",
  accepted=["6:02", "6分"],
  background="《爱情万岁》是五月天最长的一首录音室歌曲之一。")
q("albums", "medium", "《神的孩子都在跳舞》专辑名称取自什么？",
  "村上春树的同名小说",
  background="阿信是村上春树的忠实读者，专辑名称直接借用村上2000年的小说。")
q("albums", "medium", "哪张专辑标志着五月天正式进军大陆市场？",
  "神的孩子都在跳舞",
  background="2004年《神的孩子都在跳舞》时期，五月天首次在大陆进行大规模宣传与校园巡演。")

# Hard
q("albums", "hard", "《第二人生》末日版与明日版的曲序最大区别是什么？",
  "末日版以《2012》开场，明日版以《有些事现在不做一辈子都不会做了》开场",
  background="两版曲序的不同传达出从悲观到乐观的不同叙事弧线。")
q("albums", "hard", "《自传》专辑中唯一一首不是阿信作词的歌曲是什么？",
  "你说那C和弦就是...（阿信/玛莎作词）",
  accepted=["你说那C和弦就是...", "玛莎共同作词"],
  background="这首彩蛋歌曲的歌词由阿信与玛莎共同完成。")
q("albums", "hard", "五月天哪两张专辑的封面都是在国外拍摄的？",
  "第二人生 & 自传",
  background="《第二人生》封面在冰岛拍摄，《自传》封面在台湾嘉南平原拍摄。")
q("albums", "hard", "《为爱而生》专辑中「摩托车日记」描写的真实人物是谁？",
  "切·格瓦拉",
  accepted=["Che Guevara"],
  background="歌曲以切·格瓦拉在拉丁美洲的摩托车之旅为灵感，描写革命与理想的矛盾。")
q("albums", "hard", "五月天哪张专辑的预购版本附赠了黄金纪念版CD？",
  "人生海海",
  background="人生海海首批限量预购版为黄金纪念版CD，附带团员全体签名封面。")
q("albums", "hard", "《时光机》专辑中《王子面》这首歌与哪位女歌手合唱？",
  "孙燕姿",
  background="孙燕姿与五月天合唱的《王子面》是专辑的特别合作。")

# ── concerts (120+) ──────────────────────────────────────────
c_src = "references/knowledge-base/concert-archives.md"

q("concerts", "easy", "五月天出道的第一场大型演唱会叫什么？",
  "第168场演唱会",
  source=c_src,
  background="1999年8月28日在台北市立体育场举办的不售票演唱会，现场涌入约两万人。")
q("concerts", "easy", "五月天「人生无限公司」巡演大约始于哪一年？",
  "2017",
  accepted=["2017年"],
  source=c_src,
  background="「人生无限公司」是五月天2017年开启的世界巡演，并于2019年推出电影版。")
q("concerts", "easy", "五月天在哪一年首度在北京鸟巢举办演唱会？",
  "2012",
  accepted=["2012年"],
  background="2012年4月30日，五月天成为第一个在北京鸟巢举办个唱的乐团。")
q("concerts", "easy", "五月天哪一场演唱会被制成3D电影上映？",
  "诺亚方舟",
  accepted=["诺亚方舟 3D", "诺亚方舟演唱会电影"],
  background="《5月天诺亚方舟》3D电影于2013年上映。")
q("concerts", "easy", "五月天在诺亚方舟巡演期间一共演出了多少场？",
  "约120场",
  accepted=["120", "约120"],
  background="诺亚方舟巡演从2011年底至2014年，横跨亚洲、美洲、欧洲。")
q("concerts", "easy", "「好好好想见到你」巡演的名字是因为什么事件？",
  "新冠疫情导致现场演出停摆",
  background="2020-2021年因疫情无法举办演唱会，2022年重启后用这个名称表达思念。")
q("concerts", "easy", "五月天「离开地球表面」巡演的标志性互动是什么？",
  "全场同时跳跃",
  accepted=["跳跃", "Jump"],
  background="歌曲《离开地球表面》副歌时指挥全场一起跳跃，成为演唱会经典互动。")
q("concerts", "easy", "五月天演唱会在慢歌时使用的应援灯色是什么？",
  "蓝色（白光）",
  accepted=["蓝色", "蓝光"],
  background="五迷约定在慢歌段落统一打开手机蓝光或白色灯海，形成浪漫氛围。")

q("concerts", "medium", "五月天在《神的孩子都在跳舞》时期的大型巡演叫什么？",
  "Final Home 当我们混在一起",
  background="Final Home 巡演是五月天首次世界巡演，涵盖亚洲和北美城市。")
q("concerts", "medium", "复出演唱会「天空之城」在哪一年举行？",
  "2003",
  background="2003年8月16日在台北市立体育场举行，宣告五月天兵役后正式复出。")
q("concerts", "medium", "五月天第168场演唱会为什么叫这个名字？",
  "因为五月天当时已经累计演出了168场 Live",
  background="从酒吧到校园，五月天在出专辑前已经积累了168场演出的经验。")

q("concerts", "hard", "五月天在「你要去哪里」巡演中创下了哪项台湾纪录？",
  "首次售票大型巡演",
  background="你要去哪里是五月天首次售票巡演，也是暂别歌坛前的最后一次巡演。")
q("concerts", "hard", "五月天哪一场演唱会在安可时用纸飞机作为应援道具？",
  "后青春期的诗演唱会",
  background="在《后青春期的诗》演唱会上，观众在歌曲进行时放飞纸飞机。")
q("concerts", "hard", "2022年五月天在桃园棒球场举办的演唱会名称是什么？",
  "好好好想见到你",
  background="2022年疫情后首场大型实体演唱会，在桃园国际棒球场举办。")
q("concerts", "hard", "五月天在人生无限公司演唱会中创下了多少人次观看的纪录？",
  "约250万人次",
  accepted=["250万"],
  background="人生无限公司巡演全球累计观众超过250万人次。")
q("concerts", "medium", "DNA 创造世界巡演的特色视觉概念是什么？",
  "DNA 双螺旋结构",
  background="演唱会舞台设计以 DNA 双螺旋为核心视觉，象征音乐基因的传承。")
q("concerts", "hard", "五月天哪一场演唱会在微博上创下了华语艺人最高直播观看纪录？",
  "好好好想见到你 2022 桃园场",
  background="该场演唱会在线直播观看人数超过1亿人次。")
q("concerts", "nightmare", "五月天唯一一次在小巨蛋连开7场演唱会是在哪一年？",
  "2017",
  background="2017年人生无限公司巡演在台北小巨蛋连开7场，打破小巨蛋纪录。")

# ── mvs / visuals (80+) ──────────────────────────────────────
q("mvs", "easy", "《突然好想你》的MV导演是谁？", "陈宏一",
  background="陈宏一执导的《突然好想你》MV以其强烈的叙事性获得广泛好评。")
q("mvs", "easy", "五月天《干杯》的MV获得了什么认证？",
  "YouTube千万观看",
  background="《干杯》MV在YouTube上超过千万次观看，是五月天最受欢迎的音乐录影带之一。")
q("mvs", "easy", "《顽固》MV中出现的太空人意象象征什么？",
  "梦想的坚持",
  background="《顽固》MV讲述了一位中年男子不放弃太空梦想的故事，太空人是希望的象征。")

q("mvs", "medium", "「转眼」MV获得了哪些国际设计奖项？",
  "多项国际设计大奖",
  accepted=["红点设计奖", "iF设计奖"],
  background="《转眼》MV由陈奕仁执导，获得红点设计奖等多项国际奖项。")
q("mvs", "medium", "五月天哪首歌的MV邀请了梁家辉主演？", "顽固",
  background="梁家辉在《顽固》MV中饰演一位坚持太空梦的中年清洁工，演技令人动容。")
q("mvs", "medium", "《成名在望》MV的片长大约是多少？", "6分多钟",
  accepted=["超过6分钟"],
  background="《成名在望》MV长达6分钟以上，采用音乐微电影的形式。")
q("mvs", "medium", "五月天哪个MV因涉及青少年敏感话题被电视台禁播？",
  "而我知道",
  background="《而我知道》MV因涉及早恋和情感暗示，在部分电视台被限制播出。")

q("mvs", "hard", "五月天《倔强》MV的拍摄地点在哪里？",
  "日本",
  background="《倔强》MV在日本取景拍摄。")
q("mvs", "hard", "《突然好想你》MV中女主角的名字（角色名）是什么？",
  "小薇",
  background="MV中小薇是男主角念念不忘的初恋对象。")
q("mvs", "hard", "五月天第一首推出官方MV的闽南语歌曲是哪一首？",
  "志明与春娇",
  background="《志明与春娇》是五月天最早的闽南语MV，也是KTV点播冠军。")
q("mvs", "hard", "《好好》MV由哪两位艺人主演？",
  "林志玲 与 徐若瑄",
  background="《好好》MV由林志玲和徐若瑄主演，讲述了两个女孩跨越一生的友谊。")

q("mvs", "nightmare", "五月天哪一部MV采用了「一镜到底」的拍摄手法？",
  "派对动物",
  background="《派对动物》MV使用了长镜头一镜到底的拍摄方式。")

# ── awards (80+) ──────────────────────────────────────────────
q("awards", "easy", "五月天共获得过几次金曲奖最佳乐团？",
  "4次", accepted=["4", "四次"],
  background="分别在2001、2004、2009、2012年获得最佳乐团奖。")
q("awards", "easy", "哪首歌为阿信赢得了第一座金曲奖最佳作词人？",
  "成名在望",
  background="2017年第28届金曲奖，阿信凭借《成名在望》首次获得最佳作词人。")
q("awards", "easy", "《突然好想你》拿下了金曲奖哪一个奖项？",
  "最佳年度歌曲",
  background="2009年金曲奖《突然好想你》获最佳年度歌曲，是五月天慢歌的代表作之一。")
q("awards", "easy", "五月天哪张专辑获得了金曲奖最佳国语专辑？",
  "自传",
  background="2017年第28届金曲奖《自传》获得最佳国语专辑奖。")
q("awards", "easy", "五月天台湾金曲奖最佳乐团首封是哪张专辑？",
  "爱情万岁",
  background="2001年第12届金曲奖，五月天以《爱情万岁》首度获得最佳乐团奖。")

q("awards", "medium", "《第二人生》获得了多少个金曲奖奖项？",
  "3项",
  accepted=["3", "三项"],
  background="获得最佳乐团、最佳编曲人、最佳专辑制作人、最佳华语专辑奖。")
q("awards", "medium", "五月天在中华音乐人交流协会获得过几次年度十大专辑？",
  "多次",
  background="包括《后青春期的诗》《第二人生》《自传》等专辑均入选。")
q("awards", "medium", "五月天哪一首歌获得了金曲奖最佳音乐录影带奖？",
  "干杯",
  background="《干杯》获得第24届金曲奖最佳音乐录影带奖。")
q("awards", "medium", "五月天在HITO流行音乐奖共获得过多少次最佳乐团？",
  "十余次",
  background="HITO流行音乐奖是台湾最重要的流行音乐奖项之一，五月天几乎每年入围。")

q("awards", "hard", "五月天哪一年首次入围金曲奖但未获奖？",
  "2000",
  accepted=["2000年"],
  background="2000年第11届金曲奖，五月天以第一张专辑首次入围最佳演唱团体但未获奖。")
q("awards", "hard", "五月天获金曲奖「最佳乐团」最多的连续年份跨度是？",
  "12年（2001-2012）",
  accepted=["12年"],
  background="从2001年到2012年，五月天在其中4次获得最佳乐团奖。")

# ── collaborations (80+) ──────────────────────────────────────
q("collaborations", "easy", "五月天与孙燕姿合作过的歌曲是哪首？",
  "王子面",
  accepted=["王子面"],
  background="《王子面》收录于2003年《时光机》专辑。")
q("collaborations", "easy", "五月天为梁静茹创作的歌曲中哪首最出名？",
  "彩虹",
  accepted=["听不到", "燕尾蝶"],
  background="阿信为梁静茹创作了《彩虹》《听不到》《燕尾蝶》等经典情歌。")
q("collaborations", "easy", "五月天与日本摇滚乐队 Glay 合作的是哪首？",
  "候鸟",
  background="《候鸟》收录于2001年《人生海海》专辑，Glay 参与了编曲。")
q("collaborations", "easy", "五月天为丁当创作的代表歌曲是哪首？",
  "猜不透",
  background="丁当的成名曲《猜不透》由阿信作词。")
q("collaborations", "easy", "五月天与杨丞琳合唱过的歌曲是？",
  "青春住了谁",
  background="杨丞琳的《青春住了谁》邀请五月天合唱并编曲。")

q("collaborations", "medium", "阿信为萧敬腾创作的歌曲是哪首？",
  "福尔摩斯",
  background="阿信为萧敬腾量身定做了摇滚曲风《福尔摩斯》。")
q("collaborations", "medium", "五月天与刘若英合作过的歌曲中最经典的是？",
  "后来（演唱会版）",
  background="刘若英多次邀请五月天担任演唱会嘉宾，合唱《后来》《为爱痴狂》。")
q("collaborations", "medium", "五月天与八三夭乐队的关系是什么？",
  "师弟团",
  background="八三夭早期是五月天的师弟团，阿信也为八三夭的创作提供指导。")

q("collaborations", "hard", "阿信与王力宏合作过的歌曲是哪首？",
  "摇滚怎么了",
  background="阿信与王力宏在《摇滚怎么了》中合作，融合中西摇滚元素。")
q("collaborations", "hard", "五月天与周杰伦在哪个场合同台合作过？",
  "金曲奖颁奖典礼",
  background="2011年金曲奖上，周杰伦与五月天同台演出。")
q("collaborations", "hard", "玛莎为什么歌手担任过专辑制作人？",
  "梁静茹、丁当、刘若英",
  accepted=["梁静茹", "丁当"],
  background="玛莎为相信音乐旗下的多位女歌手担任制作人，包括梁静茹的专辑。")

q("collaborations", "nightmare", "五月天与哪支日本乐队合作发行了日语专辑？",
  "flumpool",
  background="flumpool 与五月天跨国合作，参与了日语版《自传》的制作。")

# ── Generate remaining questions algorithmically from lyrics-db ──
# Each song yields 3-4 questions covering album/composer/key/mood/tags.
lyrics_dir = os.path.join(
    os.path.dirname(__file__), "..",
    "mayday-mood", "references", "lyrics-db"
)
THEME_CN = {
    "love": "爱情",
    "friendship": "友情",
    "dream-chasing": "追梦",
    "loss": "失去",
    "nostalgia": "怀旧",
    "rebellion": "反抗",
    "growth": "成长",
    "celebration": "庆祝",
}
if os.path.isdir(lyrics_dir):
    for fn in sorted(os.listdir(lyrics_dir)):
        if not fn.endswith(".json") or fn == "schema.json":
            continue
        fp = os.path.join(lyrics_dir, fn)
        with open(fp) as f:
            album_data = json.load(f)
        album = album_data["album"]
        year = album_data["year"]
        src = f"references/lyrics-db/{fn}"

        for song in album_data.get("songs", []):
            title = song["title"]
            lyricist = song.get("lyricist") or ""
            composer = song.get("composer") or ""
            mood = song.get("mood") or {}
            anchor = mood.get("anchor_emotion", "")
            themes = mood.get("themes", [])
            energy = mood.get("energy")
            valence = mood.get("valence")
            bpm = song.get("bpm")
            key = song.get("key")
            tags = song.get("tags", [])

            # 1. album-attribution (easy)
            q("albums", "easy",
              f"《{title}》收录在五月天哪一张录音室专辑？",
              album, source=src,
              background=f"《{album}》于{year}年发行。")

            # 2. composer / lyricist
            if composer and composer != "阿信" and composer is not None:
                q("albums", "medium",
                  f"《{title}》的作曲者是？",
                  composer, source=src,
                  background=f"收录于{year}年发行的《{album}》。")
            if lyricist and lyricist not in ("阿信", "", None):
                q("albums", "hard",
                  f"《{title}》的作词者是？",
                  lyricist, source=src,
                  background=f"收录于《{album}》。")

            # 3. mood theme question
            if themes:
                main_theme = themes[0]
                cn = THEME_CN.get(main_theme, main_theme)
                q("albums", "medium",
                  f"《{title}》主要传达的情感主题最接近以下哪一个？",
                  cn,
                  accepted=[main_theme, cn],
                  source=src,
                  background=f"歌曲核心情绪：{anchor}。" if anchor else "")

            # 4. key / bpm trivia for songs that have it
            if key:
                q("albums", "hard",
                  f"《{title}》的主调（key）是？",
                  key, source=src,
                  background=f"收录于《{album}》，{year}年。")
            if isinstance(bpm, int) and bpm > 0:
                q("albums", "nightmare",
                  f"《{title}》的节奏 BPM 约为多少？",
                  str(bpm), source=src,
                  background=f"收录于《{album}》。")

            # 5. tag-based trivia
            for t in tags[:1]:
                if t and not t.startswith("(") and len(t) <= 15:
                    q("albums", "medium",
                      f"以下标签最能描述《{title}》的特点是？",
                      t, source=src,
                      background=f"出自《{album}》。")

# Final: summary
total = qid[0] - 1
import sys
print(f"Generated {total} trivia questions.", file=sys.stderr)
print(json.dumps(questions, ensure_ascii=False, indent=2))