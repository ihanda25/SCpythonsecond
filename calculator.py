import time
first_num = float(raw_input("Enter first num: "))
operater = str(raw_input("Enter operater (plus,minus,multiply,divide, exponents,): "))
second_num = float(raw_input("Enter second num: "))
print(first_num , operater , second_num, "=")
answer = 0 
if operater == "plus" :
    answer = first_num + second_num
    time.sleep(0.5)
    print(answer)
    print ("Created By Ishaan")
else:
    if operater == "minus":
        time.sleep(0.5)
        print(first_num - second_num)
        print ("Created By Ishaan")
    else:
        if operater == "multiply":
            answer = first_num * second_num
            time.sleep(0.5)
            print(answer)
            print ("Created By Ishaan")
        else:
            if operater == "divide":
                remainder = str(raw_input("Should I leave a remainder? "))
                if remainder == "yes":
                    answer = first_num // second_num
                    remainder = first_num%second_num
                    time.sleep(0.5)
                    print(answer, " remainder ", remainder)
                    print ("Created By Ishaan")
                else:
                    answer = first_num / second_num
                    time.sleep(0.5)
                    print answer
                    print ("Created By Ishaan")
                    
            else:
                answer = first_num ** second_num
                time.sleep(0.5)
                print answer
                print ("Created By Ishaan")
                
