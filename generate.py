import random
import string
import os

# 乱数のシードを設定する関数
def set_seed(seed):
    random.seed(seed)

# ------------------------------------------------------------
# 文字列
# rnd_char(S): S の中の文字をランダムに 1 つ選ぶ
# rnd_str(S, N): S の中の文字をランダムに 1 つ選んでつなげるのを繰り返す
# ------------------------------------------------------------

ALPHABET_SMALL = string.ascii_lowercase
ALPHABET_LARGE = string.ascii_uppercase
NUMBER = string.digits

def rnd_char(S):
    return random.choice(S)

def rnd_str(S, N):
    return ''.join(rnd_char(S) for _ in range(N))

# ------------------------------------------------------------
# 整数
# rnd_ll(from_, to): [from_, to) の整数をランダムに 1 つ選ぶ
# rnd_disjoint_integer(N, K, initvec): [0,N) の範囲の整数を重複なしで K 個選ぶ。 initvec は絶対選ぶ
# ------------------------------------------------------------

def rnd_ll(from_, to):
    return random.randint(from_, to - 1)

def rnd_disjoint_integer(N, K, initvec=[]):
    assert len(initvec) <= K
    result = set(initvec)
    while len(result) != K:
        result.add(rnd_ll(0, N))
    result = list(result)
    random.shuffle(result)
    return result


def generate_input() -> None:

    # inputディレクトリ

    directory = f"./Problem/{User}/{ProblemSlug}/in"

    # ディレクトリが存在しない場合に作成
    os.makedirs(directory, exist_ok=True)

    # 制約などはここに書く
    N = 1000

    for case in range(1, TestCase + 1):
        with open(f"{directory}/{case:02}.txt", 'w') as f: # 入力テストケースの .txt を作成する
            for i in range(N):
                if i != N - 1:
                    f.write(f"{rnd_ll(0, N)}\n") # 0 以上 N 未満の整数をランダムで出力する
                else:
                    f.write(f"{rnd_ll(0, N)}") # 末尾には改行を入れない方が便利


def generate_output() -> None:

    # outputディレクトリ
    directory = f"./Problem/{User}/{ProblemSlug}/out"

    # ディレクトリが存在しない場合に作成
    os.makedirs(directory, exist_ok=True)

    for case in range(1, TestCase + 1):
        with open(f"./Problem/{User}/{ProblemSlug}/in/{case:02}.txt", 'r') as f_in: # 入力テストケースの .txt を作成する
            input_data = f_in.read()
            with open(f"./Problem/{User}/{ProblemSlug}/out/{case:02}.txt", 'w') as f_out: # 出力テストケースの .txt を作成する

                # ここで入力を受け取って実装をしていく
                A = [int(i) for i in input_data.split("\n")]
                for i in A:
                    f_out.write(f"{2*i}\n")


def main() -> None:
    
    global sd, User, ProblemSlug, TestCase

    sd = 920 # 乱数
    set_seed(sd)

    User = "RIN0SU_1856" # ユーザー名
    ProblemSlug = "houzin" # 問題名
    TestCase = 10 # テストケース数

    generate_input()
    generate_output()


if __name__ == "__main__":
    main()