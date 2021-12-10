class String:
    def __init__(self,n):
        self.n = n
    s1 = "aeiouAEIOU"
    s2 = ",.@#$-"
    def Vowel(string,s1):
        res = set([i for i in string if i in s1])
        print("The vowels present in the string:\n ", res)
    def Constraints(string,s2):
        res1 = set([i for i in string if i in s2])
        print("The constraints present in the string:\n ", res1)
    def display(self):
        Str = (self.n)
        print("isspace(): ",Str.isspace())
        print("isupper(): ",Str.isupper())
        String.Vowel(self.n,self.s1)
        String.Constraints(self.n, self.s2)
obj = String("QWERTY UIOPas dfghj kl1234567890-@.,")
obj.display()
