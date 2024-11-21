class Krug:
    r = 0

    def __init__(self, r):
        self.r = r

    def opseg(self):
        return (2 * 3.14159 * self.r)

    def povrsina(self):
        return (3.14159 * self.r * self.r)


krug = Krug(4)
print(krug.opseg())
print(krug.povrsina())
