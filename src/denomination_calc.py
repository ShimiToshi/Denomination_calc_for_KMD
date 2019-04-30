
JPY = "JPY"
USD = "USD"

ops = {
        JPY :
            {
                "name":JPY,
                "coin":[1, 5, 10, 50, 100, 1000, 10000],
                "main": "Yen",
                "subrate": 0,
                "sub" : None,
            },
        USD :
            {
                "name": USD,
                "coin":[0.01, 0.05, 0.1, 0.25, 0.5, 1, 5, 10, 20, 50, 100],
                "main": "Doll",
                "subrate": 100,
                "sub" : "Cent",
            },


      }

class Worker:

    def __init__(self, workerinfo=None):
        if workerinfo:
            self.set_name(workerinfo[0])
            self.set_wags(workerinfo[1])
            self.set_op(workerinfo[2])

    def set_name(self, name):
        self.name = name

    def set_wags(self, wags):
        self.wags = wags

    def set_op(self, op):
        self.op = op

    def run(self):
        self.ret = all_coin_calc(self.wags, self.op)

    def display_result(self):

        for ret in self.ret:
            print(ret, ops[self.op]["main"])


def all_coin_calc(wags, ope=JPY):

    # まず、ope によって、効果の変換レートに対応したものを選定

    wag = wags

    print(ops[ope]["name"], wags, wag)

    rets = []
    for op in reversed(ops[ope]["coin"]):
        wag , ret = coin_calc(wag, op)
        rets.append(ret)

    return rets, ope_info(ope)

def coin_calc(wag, value):
    return wag%value, [value, int(wag/value), wag%value]

def ope_info(ope):
    return ops[ope]
