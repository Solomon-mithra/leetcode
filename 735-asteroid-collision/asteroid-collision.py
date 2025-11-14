class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # Try to resolve collisions while there is something on the stack
            while stack and stack[-1] > 0 and a < 0:
                top = stack[-1]
                if abs(top) == abs(a):
                    # Same size, both explode
                    stack.pop()
                    a = 0      # current also destroyed
                    break
                elif abs(top) > abs(a):
                    # Top is bigger, current is destroyed
                    a = 0
                    break
                else:
                    # Current is bigger, pop the top and continue
                    stack.pop()
                    # loop continues to check with new top

            if a != 0:
                stack.append(a)

        return stack