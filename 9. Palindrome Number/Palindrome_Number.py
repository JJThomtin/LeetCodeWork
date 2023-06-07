
class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(x)
        print("".join([*str(x)][::-1]))
        
        return "".join([*str(x)][::-1])==str(x)
    
def main():
    answer = Solution()
    
if __name__ == "__main__":
    main()