from enum import  Enum

from 五行 import 五行
class 陰陽(Enum):
    陰=0
    陽=1
class 干(Enum):
    甲=0
    乙=1
    丙=2
    丁=3
    戊=4
    己=5
    庚=6
    辛=7
    壬=8
    癸=9
    def 陰陽(self):
        if self.value%2 != 0:
            return 陰陽.陰
        else:
            return 陰陽.陽
    def 五行(self):
        if self.陰陽()==陰陽.陽:
            return 五行(self.value/2)
        else:
            return 五行((self.value-1)/2)
    def 五合(self,other):
        num =self.value-other.value
        return abs(num) == 5
    def 六親(self,other):
        return 六親(self.五行().關係(other.五行()).value)
    def 十神(self,other):
        liuqin=self.六親(other).value
        if self.陰陽() is not other.陰陽():
            return 十神(liuqin*2)
        return 十神(liuqin*2+1)
class 支(Enum):
    子=0
    丑=1
    寅=2
    卯=3
    辰=4
    巳=5
    午=6
    未=7
    申=8
    酉=9
    戌=10
    亥=11
    def 陰陽(self):
        if self.value%2!=0:
            return 陰陽.陰
        else:
            return 陰陽.陽
    def 五行(self):
        if self in [支.子,支.亥]:
            return 五行.水
        if self in [支.辰,支.戌,支.丑,支.未]:
            return 五行.土
        if self in [支.寅,支.卯]:
            return 五行.木
        if self in [支.巳,支.午]:
            return 五行.火
        if self in [支.申,支.酉]:
            return 五行.金
    def 三合(self,other):
        if self.value==other.value:
            return False
        return (self.value-other.value)%4==0
    def 六合(self,other):
        return (self.value+other.value-15+2)%12==0
    def 六冲(self,other):
        if self.value==other.value:
            return False
        return (self.value-other.value)%6==0
    def 刑(self,other):
        group=(
            (支.寅,支.巳),(支.巳,支.申),(支.申,支.寅),
            (支.丑,支.未),(支.未,支.戌),(支.戌,支.丑),
            (支.子,支.卯),(支.卯,支.子),
            (支.辰,支.辰),(支.午,支.午),(支.酉,支.酉),(支.亥,支.亥))

        return (self,other) in group
    def 破(self,other):
            if self.陰陽()==陰陽.陽:
                return other.value==(self.value+12-3)%12
            else:
                return other.value==(self.value+3)%12
    def 害(self,other):
        sum=self.value+other.value
        return sum==7 or sum ==19
    def 三會(self,other):
        group=(
            (支.寅,支.卯,支.辰),
            (支.巳,支.午,支.未),
            (支.申,支.酉,支.戌),
            (支.亥,支.子,支.丑)
        )
        if self is not other:
            for item in group:
                if self in item and other in item:
                    return True
        return False
    def 暗合(self,other):
        group=(
            (支.子,支.巳),
            (支.寅,支.午),
            (支.巳,支.酉),
            (支.卯,支.申),
            (支.亥,支.午)
        )
        if self is not other:
            for item in group:
                if self in item and other in item:
                    return True
        return False
    def 藏干(self):
        group={
            支.子:(干.癸),
            支.丑:(干.己,干.辛,干.癸,),
            支.寅:(干.甲,干.丙,干.戊),
            支.卯:(干.乙),
            支.辰:(干.戊,干.乙,干.癸),
            支.巳:(干.丙,干.戊,干.庚),
            支.午:(干.丁,干.己),
            支.未:(干.己,干.乙,干.丁),
            支.申:(干.庚,干.壬,干.戊),
            支.酉:(干.辛),
            支.戌:(干.戊,干.丁,干.辛),
            支.亥:(干.壬,干.甲)
        }
        return group[self]
    def 六親(self,other):
        return 六親(self.五行().關係(other.五行()))
class 六親(Enum):
    父母=0
    兄弟=1
    子孙=2
    妻财=3
    官鬼=4

class 十神(Enum):
    正印=0
    偏印=1
    劫财=2
    比肩=3
    伤官=4
    食神=5
    正财=6
    偏财=7
    正官=8
    七杀=9


if __name__=='__main__':
    # for item in 干:
        # print(item,item.陰陽())
        # print(item,item.五行())
        # print(item,item.五合())
    # for item in 干:
    #     for item_1 in 干:
        # print(item,item.陰陽())
        # print(item,item.五行())
        #     print(item,item_1,item.六親(item_1))
        #     if item.五合(item_1):
        #         print(item,item_1,item.五合(item_1))
        # if item.五合(item_1):

    for item in 支:

        # print(item,item.陰陽())
        # print(item,item.五行())
        for item_1 in 支:

            # if item.三合(item_1):
                # print(item,item_1,item.三合(item_1))
            # if item.六合(item_1):
            #     print(item,item_1,item.六合(item_1))
            # if item.六冲(item_1):
            #     print(item,item_1,item.六冲(item_1))
            # if item.破(item_1):
            #     print(item,item_1,item.破(item_1))from enum import  Enum
            #
            # from 五行 import 五行
            # class 陰陽(Enum):
            #     陰=0
            #     陽=1
            # class 干(Enum):
            #     甲=0
            #     乙=1
            #     丙=2
            #     丁=3
            #     戊=4
            #     己=5
            #     庚=6
            #     辛=7
            #     壬=8
            #     癸=9
            #     def 陰陽(self):
            #         if self.value%2 != 0:
            #             return 陰陽.陰
            #         else:
            #             return 陰陽.陽
            #     def 五行(self):
            #         if self.陰陽()==陰陽.陽:
            #             return 五行(self.value/2)
            #         else:
            #             return 五行((self.value-1)/2)
            #     def 五合(self,other):
            #         num =self.value-other.value
            #         return abs(num) == 5
            #     def 六親(self,other):
            #         return 六親(self.五行().關係(other.五行()).value)
            #     def 十神(self,other):
            #         liuqin=self.六親(other).value
            #         if self.陰陽() is not other.陰陽():
            #             return 十神(liuqin*2)
            #         return 十神(liuqin*2+1)
            # class 支(Enum):
            #     子=0
            #     丑=1
            #     寅=2
            #     卯=3
            #     辰=4
            #     巳=5
            #     午=6
            #     未=7
            #     申=8
            #     酉=9
            #     戌=10
            #     亥=11
            #     def 陰陽(self):
            #         if self.value%2!=0:
            #             return 陰陽.陰
            #         else:
            #             return 陰陽.陽
            #     def 五行(self):
            #         if self in [支.子,支.亥]:
            #             return 五行.水
            #         if self in [支.辰,支.戌,支.丑,支.未]:
            #             return 五行.土
            #         if self in [支.寅,支.卯]:
            #             return 五行.木
            #         if self in [支.巳,支.午]:
            #             return 五行.火
            #         if self in [支.申,支.酉]:
            #             return 五行.金
            #     def 三合(self,other):
            #         if self.value==other.value:
            #             return False
            #         return (self.value-other.value)%4==0
            #     def 六合(self,other):
            #         return (self.value+other.value-15+2)%12==0
            #     def 六冲(self,other):
            #         if self.value==other.value:
            #             return False
            #         return (self.value-other.value)%6==0
            #     def 刑(self,other):
            #         group=(
            #             (支.寅,支.巳),(支.巳,支.申),(支.申,支.寅),
            #             (支.丑,支.未),(支.未,支.戌),(支.戌,支.丑),
            #             (支.子,支.卯),(支.卯,支.子),
            #             (支.辰,支.辰),(支.午,支.午),(支.酉,支.酉),(支.亥,支.亥))
            #
            #         return (self,other) in group
            #     def 破(self,other):
            #             if self.陰陽()==陰陽.陽:
            #                 return other.value==(self.value+12-3)%12
            #             else:
            #                 return other.value==(self.value+3)%12
            #     def 害(self,other):
            #         sum=self.value+other.value
            #         return sum==7 or sum ==19
            #     def 三會(self,other):
            #         group=(
            #             (支.寅,支.卯,支.辰),
            #             (支.巳,支.午,支.未),
            #             (支.申,支.酉,支.戌),
            #             (支.亥,支.子,支.丑)
            #         )
            #         if self is not other:
            #             for item in group:
            #                 if self in item and other in item:
            #                     return True
            #         return False
            #     def 暗合(self,other):
            #         group=(
            #             (支.子,支.巳),
            #             (支.寅,支.午),
            #             (支.巳,支.酉),
            #             (支.卯,支.申),
            #             (支.亥,支.午)
            #         )
            #         if self is not other:
            #             for item in group:
            #                 if self in item and other in item:
            #                     return True
            #         return False
            #     def 藏干(self):
            #         group={
            #             支.子:(干.癸),
            #             支.丑:(干.己,干.辛,干.癸,),
            #             支.寅:(干.甲,干.丙,干.戊),
            #             支.卯:(干.乙),
            #             支.辰:(干.戊,干.乙,干.癸),
            #             支.巳:(干.丙,干.戊,干.庚),
            #             支.午:(干.丁,干.己),
            #             支.未:(干.己,干.乙,干.丁),
            #             支.申:(干.庚,干.壬,干.戊),
            #             支.酉:(干.辛),
            #             支.戌:(干.戊,干.丁,干.辛),
            #             支.亥:(干.壬,干.甲)
            #         }
            #         return group[self]
            #     def 六親(self,other):
            #         return 六親(self.五行().關係(other.五行()))
            # class 六親(Enum):
            #     父母=0
            #     兄弟=1
            #     子孙=2
            #     妻财=3
            #     官鬼=4
            #
            # class 十神(Enum):
            #     正印=0
            #     偏印=1
            #     劫财=2
            #     比肩=3
            #     伤官=4
            #     食神=5
            #     正财=6
            #     偏财=7
            #     正官=8
            #     七杀=9
            #
            #
            # if __name__=='__main__':
            #     # for item in 干:
            #         # print(item,item.陰陽())
            #         # print(item,item.五行())
            #         # print(item,item.五合())
            #     # for item in 干:
            #     #     for item_1 in 干:
            #         # print(item,item.陰陽())
            #         # print(item,item.五行())
            #         #     print(item,item_1,item.六親(item_1))
            #         #     if item.五合(item_1):
            #         #         print(item,item_1,item.五合(item_1))
            #         # if item.五合(item_1):
            #
            #     for item in 支:
            #
            #         # print(item,item.陰陽())
            #         # print(item,item.五行())
            #         for item_1 in 支:
            #
            #             # if item.三合(item_1):
            #                 # print(item,item_1,item.三合(item_1))
            #             # if item.六合(item_1):
            #             #     print(item,item_1,item.六合(item_1))
            #             # if item.六冲(item_1):
            #             #     print(item,item_1,item.六冲(item_1))
            #             # if item.破(item_1):
            #             #     print(item,item_1,item.破(item_1))
            #             if item.害(item_1):
            #                 print(item,item_1,item.害(item_1))
            if item.害(item_1):
                print(item,item_1,item.害(item_1))