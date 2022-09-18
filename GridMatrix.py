import consts
import random
class GridMatrix:

    def __init__(self):
        self.grid_matrix = []
        #initializing a matrix
        for i in range(consts.ROWS_MATRIX):
            inner_list=[]
            for j in range(consts.COLUMNS_MATRIX):
                inner_list.append("free")
            self.grid_matrix.append(inner_list)

        self.insert_random_traps()

    def get_matrix(self):
        return self.grid_matrix

    def check_empty_trio_in_grid(self,i_check,j_check):
        for j in range(j_check,j_check+3):
            if self.grid_matrix[i_check][j]== "trap":
                return False
        return True

    def add_trap_trio(self,i_check,j_check):
        for j in range(j_check,j_check+3):
            self.grid_matrix[i_check][j] = "trap"

    def insert_random_traps(self):
        #generate 20 trios of mines in grid
        for count in range(20):
            flag_next = True
            random_start_i=random.randint(0,consts.ROWS_MATRIX-3)
            random_start_j=random.randint(0,consts.COLUMNS_MATRIX-3)
            if self.check_empty_trio_in_grid(random_start_i, random_start_j):
                self.add_trap_trio(random_start_i,random_start_j)
            else:
                flag_next=False
                while flag_next is False:
                    random_start_i = random.randint(0, consts.ROWS_MATRIX - 3)
                    random_start_j = random.randint(0, consts.COLUMNS_MATRIX - 3)
                    if self.check_empty_trio_in_grid(random_start_i, random_start_j):
                        flag_next=True
                        self.add_trap_trio(random_start_i, random_start_j)

    def secdlist_tuples_traps_sequances(self):
        secd_list_of_traps=[]
        for i in range(len(self.grid_matrix)):
            j = 0
            inner_list=[]
            while j < (consts.COLUMNS_MATRIX - 3):
                if self.grid_matrix[i][j] == "trap":
                    for j in range(j, j+3):
                        inner_list.append((i,j))
                    j += 3
                else:
                    j += 1
            secd_list_of_traps.append(inner_list)
        return secd_list_of_traps
