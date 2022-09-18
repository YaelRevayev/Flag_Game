import consts
import GridMatrix
from GridMatrix import GridMatrix


class Player():

    def __init__(self):
        #player indexes left up corner
        # initializing (0,0)
        self.row_index = 0
        self.col_index = 0

    def get_i_leftcorner(self):
        return self.row_index

    def get_j_leftcorner(self):
        return self.col_index

    def set_i_leftcorner(self,num):
        self.row_index=num

    def set_j_leftcorner(self,num):
        self.col_index=num

    def cald_legs_area(self):
        list_body_tuples=calc_body_indexes(self.row_index,self.col_index)
        return (list_body_tuples[len(list_body_tuples)-2]
                ,list_body_tuples[len(list_body_tuples)-1])

    def check_touch_trap(self,grid_matrix):
        # מיתר
        # הפעולה מקבלת את מיקום המשבצת השמאלית העליונה של השחקן במטריצה
        # הפעולה צריכה לבדוק האם השחקן נוגע ברגליו (2 המשבצות התחתונות שלו) במוקש
        # מוקש מתפרס על 1*3
        # שחקן מתפרס על 2*4
        pass

    def check_touch_flag(self,grid_matrix):
        # מיתר
        # הפעולה מקבלת את מיקום המשבצת השמאלית העליונה של השחקן במטריצה
        # הפעולה צריכה לבדוק האם השחקן נוגע בחלק הגוף (שמוגדר בהוראות) באובייקט הדגל
        # המיקום של המשבצת המשאלית העליונה של הדגל שמור במודול קבועים
        pass


def calc_body_indexes(i_leftcorner,j_leftcorner):
        list_of_tuples=[]
        for i in range(i_leftcorner,consts.SOLDIER_LENGTH+i_leftcorner):
            for j in range(j_leftcorner,consts.SOLDIER_WIDTH+j_leftcorner):
                list_of_tuples.append((i,j))
        return list_of_tuples

def tuples_in_borders(list_of_tuples):
    for tuple in list_of_tuples:
            if tuple[0]>24 or tuple[0]<0:
                return False
            elif tuple[1]>49 or tuple[1]<0:
                return False
    return True





