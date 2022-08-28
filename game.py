
class Game:

    def select_winner(self,p,a):
        if p=='Rock' and a=='Scissor':
            return 1
        elif p =='Rock' and a=='Paper' :
            return -1
        elif p=='Scissor' and a=='Rock' :
            return -1
        elif p=='Scissor' and a=='Paper':
            return 1
        elif p=='Paper' and a=='Rock':
            return 1
        elif p=='Paper' and a=='Scissor':
            return -1;
        else:
            return 0
                                  