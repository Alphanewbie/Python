class StackCrawling:
    def __init__(self,recruitID):
        self.recruitID = recruitID
        self.preferencelist = []
        self.requiredlist = []
        self.stacklist = []
        
    # 자격 사항 크롤링
    def crawling_requried(self, soup):
        required = soup.select(
            'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > section.section-requirements > div > div > ul > li'
        )

        for item in required:
            # print(item.get_text('li'))
            self.requiredlist.append(item.get_text('li'))

    # 우대조건 크롤링
    def crawling_preference(self, soup):
        preference = soup.select(
            'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > section.section-preference > div > div > ul > li'
        )

        for item in preference:
            # print(item.get_text('li'))
            self.preferencelist.append(item.get_text('li'))

    # 기술 스택 크롤링
    def crawling_preference(self, soup):
        stacks = soup.select(
            'section.section-stacks > table > tbody > tr > td > code'
        )

        for stack in stacks:
            # print(item.get_text('li'))
            self.stacklist.append(stack.get_text('code'))
