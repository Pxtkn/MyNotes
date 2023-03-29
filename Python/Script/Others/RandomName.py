import random
import json

pinyin = [
    "a", "ai",  "an", "ang", "ao", "ba", "bai", "ban",
    "bang", "bao", "bei", "ben", "beng", "bi", "bian", "biao",
    "bie", "bin", "bing", "bo", "bu", "ca", "cai", "can",
    "cang", "cao", "ce", "cen", "ceng", "cha", "chai", "chan",
    "chang", "chao", "che", "chen", "cheng", "chi", "chong", "chou",
    "chu", "chua", "chuai", "chuan", "chuang", "chui", "chun", "chuo",
    "ci", "cong", "cou", "cu", "cuan", "cui", "cun", "cuo",
    "da", "dai", "dan", "dang", "dao", "de", "dei", "den",
    "deng", "di", "dia", "dian", "diao", "die", "ding", "diu",
    "dong", "dou", "du", "duan", "dui", "dun", "duo", "e",
    "ei", "en", "eng", "er", "fa", "fan", "fang", "fei",
    "fen", "feng", "fo", "fou", "fu", "ga", "gai", "gan",
    "gang", "gao", "ge", "gei", "gen", "geng", "gong", "gou",
    "gu", "gua", "guai", "guan", "guang", "gui", "gun", "guo",
    "ha", "hai", "han", "hang", "hao", "he", "hei", "hen",
    "heng", "hm", "hng", "hong", "hou", "hu", "hua", "huai",
    "huan", "huang", "hui", "hun", "huo", "ji", "jia", "jian",
    "jiang", "jiao", "jie", "jin", "jing", "jiong", "jiu", "ju",
    "juan", "jue", "jun", "ka", "kai", "kan", "kang", "kao",
    "ke", "kei", "ken", "keng", "kong", "kou", "ku", "kua",
    "kuai", "kuan", "kuang", "kui", "kun", "kuo", "la", "lai",
    "lan", "lang", "lao", "le", "lei", "leng", "li", "lia",
    "lian", "liang", "liao", "lie", "lin", "ling", "liu", "lo",
    "long", "lou", "lu", "lü", "luan", "lüe", "lun", "luo",
    "m", "ma", "mai", "man", "mang", "mao", "me", "mei",
    "men", "meng", "mi", "mian", "miao", "mie", "min", "ming",
    "miu", "mo", "mou", "mu", "n", "na", "nai", "nan",
    "nang", "nao", "ne", "nei", "nen", "neng", "ng", "ni",
    "nian", "niang", "niao", "nie", "nin", "ning", "niu", "nong",
    "nou", "nu", "nü", "nuan", "nüe", "nuo", "o", "ou",
    "pa", "pai", "pan", "pang", "pao", "pei", "pen", "peng",
    "pi", "pian", "piao", "pie", "pin", "ping", "po", "pou",
    "pu", "qi", "qia", "qian", "qiang", "qiao", "qie", "qin",
    "qing", "qiong", "qiu", "qu", "quan", "que", "qun", "ran",
    "rang", "rao", "re", "ren", "reng", "ri", "rong", "rou",
    "ru", "rua", "ruan", "rui", "run", "ruo", "sa", "sai",
    "san", "sang", "sao", "se", "sen", "seng", "sha", "shai",
    "shan", "shang", "shao", "she", "shei", "shen", "sheng", "shi",
    "shou", "shu", "shua", "shuai", "shuan", "shuang", "shui", "shun",
    "shuo", "si", "song", "sou", "su", "suan", "sui", "sun",
    "suo", "ta", "tai", "tan", "tang", "tao", "te", "teng",
    "ti", "tian", "tiao", "tie", "ting", "tong", "tou", "tu",
    "tuan", "tui", "tun", "tuo", "wa", "wai", "wan", "wang",
    "wei", "wen", "weng", "wo", "wu", "xi", "xia", "xian",
    "xiang", "xiao", "xie", "xin", "xing", "xiong", "xiu", "xu",
    "xuan", "xue", "xun", "ya", "yan", "yang", "yao", "ye",
    "yi", "yin", "ying", "yo", "yong", "you", "yu", "yuan",
    "yue", "yun", "za", "zai", "zan", "zang", "zao", "ze",
    "zei", "zen", "zeng", "zha", "zhai", "zhan", "zhang", "zhao",
    "zhe", "zhei", "zhen", "zheng", "zhi", "zhong", "zhou", "zhu",
    "zhua", "zhuai", "zhuan", "zhuang", "zhui", "zhun", "zhuo", "zi",
    "zong", "zou", "zu", "zuan", "zui", "zun", "zuo",
]
ch_char_fp = open(
    "D:/repositories/chinese-dictionary/data/character/char_base.json",
    encoding="utf-8")
ch_char = json.load(ch_char_fp)
frequent_ch_char = [i["char"] for i in ch_char if i["frequency"] < 4]


def random_en_letter(n, min_letter_num, max_letter_num):
    for i in range(n):
        letter_num = random.randint(min_letter_num, max_letter_num)
        for j in range(letter_num):
            print(chr(random.randint(97, 122)), end="")
        print("  ", end="")



# random_english_letter(100, 4, 5)
for i in range(10):
    print(random.choice(frequent_ch_char))


