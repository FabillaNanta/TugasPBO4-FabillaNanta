class shark:
    def introduction(self):
        print("There are a lot of shark species in the ocean")

    def facts(self):
        print("Shark species came with many shapes and sizes")
        print("==============================================")

class WhaleShark(shark):
    def facts(self):
       print("Whale Sharks are the largest shark species")
       print("==============================================")

class DwarfLanternShark(shark):
    def facts(self):
        print("Dwarf Lantern Sharks are the smallest shark species")
        print("==============================================")

obj_shark = shark()
obj_WhaleShark = WhaleShark()
obj_DwarfLanternShark = DwarfLanternShark()

obj_shark.introduction()
obj_shark.facts()

obj_shark.introduction()
obj_WhaleShark.facts()

obj_shark.introduction()
obj_DwarfLanternShark.facts()