class myclass:


    __privatevar= 27


    def __privmeth(self):
        print("I'm inside myclass")



    def hello(self):
        print("Private Variable value:",myclass.__privatevar)


foo=myclass()
foo.hello()
foo.__privmeth