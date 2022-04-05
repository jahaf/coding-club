MIN_LOGIN_LENGTH = 3
MAX_LOGIN_LENGTH = 31
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 255
PASSWORD_ALLOWED_CHAR = '!@#$%^&*()-_=+'

import re

class LoginAssessment():
    
    def __init__(self, username, password):
        self.errorText = []
        self.username = username
        self.password = password
        self.__UsernameBadCharacter()
        self.__UsernameTooLong()
        self.__UsernameTooShort()
        self.__UsernameStartsWithANumber() 
        self.__PasswordTooShort()
        self.__PasswordTooLong()
        self.__PasswordNoDigit()
        self.__PasswordContainsUsername()
        self.__findIllPassword()
        self.__PasswordBadCharacters()
        self.__PasswordNoLowerAlpha()
        self.__PasswordNoSpecialChar()
        self.__PasswordNoUpperAlpha()
    
    # Private methods
    def __UsernameTooShort(self):
        if len(self.username) < MIN_LOGIN_LENGTH:
            self.errorText.append('Username too short!')
        
    def __UsernameTooLong(self):
        if len(self.username) > MAX_LOGIN_LENGTH:
            self.errorText.append('Username too long!')
        
    def __UsernameBadCharacter(self):
        match = re.search('[^a-zA-Z0-9]', self.username)
        if match:
            self.errorText.append('Username has bad character!')

    def __UsernameStartsWithANumber(self):
        match = re.search('[0-9]', self.username[0])
        if match:
            self.errorText.append('Username starts with a number!')
    
    def __PasswordTooShort(self):    
        if len(self.password) < MIN_PASSWORD_LENGTH:
            self.errorText.append('Password too short!')
        
    def __PasswordTooLong(self):
        if len(self.password) > MAX_PASSWORD_LENGTH:
            self.errorText.append('Password too long!')
     
    def __PasswordNoDigit(self):
        match = re.search('[0-9]', self.password)
        if not match:
            self.errorText.append('Password does not include a digit!')
    
    def __PasswordContainsUsername(self):
       if self.password.lower().find(self.username.lower()) >= 0:
           self.errorText.append('Password contains username!')
   
    def __findIllPassword(self):  
        self.foundLower = False
        self.foundUpper = False
        self.foundSpecialChar = False
        self.foundBadCharacter = False
        for ch in self.password:
            if ch.isalnum():
                self.foundSpecialChar = True
            if ch.isalnum() and PASSWORD_ALLOWED_CHAR.find(ch) >= 0:
                self.foundBadCharacter = True
            if ch.islower():
                self.foundLower = True
            if ch.isupper():
                self.foundUpper = True
        
    def __PasswordBadCharacters(self):
        if self.foundBadCharacter:
            self.errorText.append('Password includes bad character!')
    
    def __PasswordNoLowerAlpha(self):
        if not self.foundLower:
            self.errorText.append('Password does not include any lower alpha!')
            
    def __PasswordNoUpperAlpha(self):
        if not self.foundUpper:
            self.errorText.append('Password does not include any upper alpha!')
            
    def __PasswordNoSpecialChar(self):
        if not self.foundSpecialChar:
            self.errorText.append('Password does not include any special character!')
             
             
            