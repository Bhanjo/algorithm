from collections import deque

def solution(order):
    answer = 0

    order = deque(order)
    box = [i+1 for i in range(len(order))]
    box = deque(box)
    st = deque()
    
    while(order):
        if box:
            if order[0] > box[0]:
                st.append(box.popleft())
            elif order[0] == box[0]:
                order.popleft()
                box.popleft()
                answer += 1
            elif order[0] < box[0]:
                if st[-1] == order[0]:
                    st.pop()
                    order.popleft()
                    answer += 1
                else:
                    break
        else:
            if st[-1] == order[0]:
                st.pop()
                order.popleft()
                answer += 1
            else:
                break

    return answer