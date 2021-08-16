dictionary = {"멋사":"멋쟁이 사자처럼", "파이썬":"지금 배우는 언어"}

def create_word() :
    keyWord = input("Enter word :")
    valueWord = input("Enter meaning :")
    dictionary[keyWord] = valueWord
    print("성공적으로 등록되었습니다!")

def read_dictionary() :
    Dlist = dictionary.keys()
    for item in Dlist :
        print(item,":",dictionary.get(item))

def update_word() :
    updateWord = input("Enter word :")
    if(updateWord in dictionary) :
        updateValue = input("Enter meaning :")
        dictionary[updateWord] = updateValue
        print("성공적으로 업데이트되었습니다!")
    else :
        print("업데이트 실패")

def delete_word() :
    delWord = input("Enter word :")
    if(delWord in dictionary) :
        del dictionary[delWord]
        print("성공적으로 삭제되었습니다!")
    else:
        print("삭제 실패")

def console_help() :
    print("Command List")
    print("-----")
    print("C for create")
    print("R for read")
    print("U for update")
    print("D for delete")
    print("Q for quit")

def receive_input() :
    command = input("Input command: ")
    if command == 'c' or command == 'C' :
        create_word()
        return True
    if command == 'r' or command == 'R':
        read_dictionary()
        return True
    if command == 'u' or command == 'U':
        update_word()
        return True
    if command == 'd' or command == 'D':
        delete_word()
        return True
    if command == 'q' or command == 'Q':
        return False
    else:
        print("Please enter one of the letters above.")
        return True


def main():
    console_help()
    while receive_input():
        pass


if __name__ == "__main__":
    main()