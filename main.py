import os

def main():
    print('作成したいフォルダ名を入力して下さい')
    name = input()
    print('授業回数は何回ありますか')
    num = int(input())


    for i in range(num):
      path = f'./{name}/第{i+1}回'
      os.makedirs(path, exist_ok=True)

if __name__ == '__main__':
    main()