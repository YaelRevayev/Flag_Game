import consts
class GridMatrix:

    def __init__(self):
        self.grid_matrix = []
        #initializing a matrix
        for i in range(consts.ROWS_MATRIX):
            inner_list=[]
            for j in range(consts.COLUMNS_MATRIX):
                inner_list.append("free")
            self.grid_matrix.append(inner_list)

        for insert_try in range(3):
            self.grid_matrix[0][insert_try]="trap"

    def get_matrix(self):
        return self.grid_matrix

    def insert_random_traps(self):
        #מיתר
        #הפעולה מכניסה כ20 מוקשים בשורות המטריצה כל מוקש תופס שורה אחת ו3 עמודות
        # בשביל לגשת למטריצה תכתבי self.grid_matrix
        pass

    def check_touch_flag(self,i_player,j_player):
        #מיתר
        # הפעולה מקבלת את מיקום המשבצת השמאלית העליונה של השחקן במטריצה
        # הפעולה צריכה לבדוק האם השחקן נוגע בחלק הגוף (שמוגדר בהוראות) באובייקט הדגל
        # המיקום של המשבצת המשאלית העליונה של הדגל שמור במודול קבועים
        pass

    def check_touch_trap(self,i_player,j_player):
        #מיתר
        #הפעולה מקבלת את מיקום המשבצת השמאלית העליונה של השחקן במטריצה
        #הפעולה צריכה לבדוק האם השחקן נוגע ברגליו (2 המשבצות התחתונות שלו) במוקש
        # מוקש מתפרס על 1*3
        # שחקן מתפרס על 2*4
        pass
