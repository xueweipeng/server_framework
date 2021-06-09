class User:
    avatar = ''  # 头像链接
    nick_name = ''  # 用户昵称
    signature = ''  # 签名
    sex = ''  # 性别
    birthday = ''  # 生日
    education = ''  # 学历
    industry = ''  # 行业

    def __init__(self, avatar, nick_name, signature, sex, birthday, education, industry):
        self.avatar = avatar
        self.nick_name = nick_name
        self.signature = signature
        self.sex = sex
        self.birthday = birthday
        self.education = education
        self.industry = industry

    def getAvatar(self):
        return self.avatar

    def getNickName(self):
        return self.nick_name

    def getSignature(self):
        return self.signature

    def getSex(self):
        return self.sex

    def getBirthday(self):
        return self.birthday

    def getEducation(self):
        return self.education

    def getIndustry(self):
        return self.industry
