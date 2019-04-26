from src.denomination_calc import *
from src.my_csv import *

csvname = "workerinfo.csv"

def main():
    #proto_main()
    csv_main()



def proto_main():
    wk_num = int(input("Worker num :" ))

    waglis = []
    for i in range(wk_num):
        waglis.append(int(input("wag set :")))

    wks = []
    for wag in waglis:
        wk = Worker()
        wk.set_wags(wag)
        wk.run()
        wks.append(wk)

    for i in wks:
        i.display_result()

def csv_main():
    wks = [Worker(worker) for worker in read_csv(csvname)]

    for wk in wks:
        wk.run()

    for wk in wks:
        wk.display_result()


if __name__ == "__main__":
    main()
