import queue
# 큐 객체 선언
q = queue.Queue()

q.put(12) # put=enque
q.put(21)
q.put(5)
q.put(67)
q.put(38)
q.put(11)
# print(q.qsize()) # size=6
#
# print(q.get()) # get=deque /value=12
# print(q.get()) # 21

# print(q.empty()) # False
#
# print(q.queue[0]) # front /value=5
# print(q.queue[-1]) # rear /value=11
# print(q.queue) # deque([5, 67, 38, 11])

# 스택 -> 따로 라이브러리 없이 리스트로 구현가능
stack = []
stack.append(12) # push
stack.append(21)
stack.append(5)
stack.append(67)
stack.append(38)
stack.append(11)
# print(stack) # [12, 21, 5, 67, 38, 11]
#
# print(stack.pop()) # 11
# print(stack.pop()) # 38

# Deque :덱
from collections import deque
dq = deque()

dq.append(12)
dq.append(21)
dq.append(5)
dq.append(67)
dq.append(38)
dq.append(11)

print(dq) # deque([12, 21, 5, 67, 38, 11])
print(dq.pop()) # 11
print(dq.pop()) # 38
print(dq.popleft()) # 12
print(dq[0]) # front=21
print(dq[-1]) # rear=67