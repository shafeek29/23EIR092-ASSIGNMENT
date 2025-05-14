class MyStack(object):

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        
        
        ele = self._queue.pop()
        
        return ele


    def top(self):
        """
        :rtype: int
        """
        ele = self._queue[-1]
        return ele

    def empty(self):
        """
        :rtype: bool
        """
        return not self._queue
