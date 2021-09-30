class shark:
    def __init__(self, phylum, facts, species):
        self.phylum  = phylum
        self.facts   = facts
        self.species = species

    def desc(self):
        print("Phylum          :", self.phylum)
        print("Name of species :", self.species)
        print("Fun facts about", self.species, ":", self.facts)
        print("===============================================================================================================")

class jellyfish:
    def __init__(self, phylum, facts, species):
        self.phylum  = phylum
        self.facts   = facts
        self.species = species

    def desc(self):
        print("Phylum          :", self.phylum)
        print("Name of species :", self.species)
        print("Fun facts about", self.species, ":", self.facts)
        print("===============================================================================================================")

class sponge:
    def __init__(self, phylum, facts, species):
        self.phylum  = phylum
        self.facts   = facts
        self.species = species

    def desc(self):
        print("Phylum          :", self.phylum)
        print("Name of species :", self.species)
        print("Fun facts about", self.species, ":", self.facts)
        print("===============================================================================================================")

shark = shark("Chordata", "Each whale shark’s spot pattern is unique as a fingerprint", "Whale Shark")
jellyfish = jellyfish("Cnidaria", "The lion's mane jellyfish is one of the largest jelly species in the world", "Lion's Mane Jellyfish")
sponge = sponge("Porifera", "Commonly called the “Venus flower basket,” this sponge builds its skeleton in a way that entraps a certain species of crustacean inside for life", "Glass Sponge")

for animal in (shark, jellyfish, sponge):
    animal.desc()