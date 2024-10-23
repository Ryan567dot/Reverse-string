class reverse:
    def reverse_words(self,water):
        return " " .join(reversed(water.split()))

print(reverse().reverse_words("Hello world!"))
