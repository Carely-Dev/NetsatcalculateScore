Thai_score = 36 
Eng_score = 33
math_score = 40 
sci_score = 47.5 

class Netsat:
    def __init__(self,major, thai_score, eng_score, math_score, sci_score, thai_percent, eng_percent, math_percent, sci_percent,scoreMin):
        self.Thai_score = thai_score
        self.Eng_score = eng_score
        self.math_score = math_score
        self.sci_score = sci_score
        self.thai_percent = thai_percent
        self.eng_percent = eng_percent
        self.math_percent = math_percent
        self.sci_percent = sci_percent
        self.major = major
        self.scoreMin = scoreMin
    
    def averageMath (self):
        return (self.math_score / 100) * float(self.math_percent)

    def averageEng (self):
        return (self.Eng_score / 100) * float(self.eng_percent)
    
    def averageThai (self):
        return (self.Thai_score / 100) * float (self.thai_percent)
    
    def averageSci (self):
        return (self.sci_score / 100) * float(self.sci_percent)
    def totalScore(self):
        return format(self.averageThai() + self.averageEng() + self.averageMath() + self.averageSci(),'0.2f')
    def __str__(self):
        return f"\n------------------------------------------------------\n\nMAJOR: {self.major} \nThai score: {self.Thai_score} ThaitotalScore : {format(self.averageThai(),'.2f')} \n English score: {self.Eng_score} EngtotalScore : {format(self.averageEng(),'.2f')} \n Math score: {self.math_score} MathtotalScore : {format(self.averageMath(),'.2f')} \n Science score: {self.sci_score} ScitotalScore : {format(self.averageSci(),'.2f')} \n scoreMin : {self.scoreMin} \nTotal score: {self.totalScore()}"

major = input("Enter major: ")  
scoreMin = input("Enter minimum score: ")  
thai_percent = input("Enter Thai percent: ")
eng_percent = input("Enter English percent: ")
math_percent = input("Enter Math percent: ")
sci_percent = input("Enter Science percent: ")


Netsat1 = Netsat(major,Thai_score, Eng_score, math_score, sci_score, thai_percent, eng_percent, math_percent, sci_percent,scoreMin)
with open('Netsat_data.txt', 'a+', encoding='utf-8') as file:
    # Write the string representation of Netsat1 to the file
    file.write(str(Netsat1))
print(Netsat1)
print("Data has been written to Netsat_data.txt file successfully!")
