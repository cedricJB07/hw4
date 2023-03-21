def double(outputMessage):
    def tryAgain():
        outputMessage()
        print("Let's try that again!")
        outputMessage()
    return tryAgain
