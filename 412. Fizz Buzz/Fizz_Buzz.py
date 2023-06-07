


from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n):
            if (i%5==0) and (i%3==0):
                answer.append("FizzBuzz")
            elif (i%3==0):
                answer.append("Fizz")
            elif (i%5 == 0):
                answer.append("Buzz")
            else:
                answer.append(f"{i}")
        return answer
    
def main():
    number = Solution()
    print(number.fizzBuzz(300))
    
if __name__ == "__main__":
    main()