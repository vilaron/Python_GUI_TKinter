from random import random, randint, shuffle, getrandbits, random

class GeneticWordBreak:

    def __init__(self, s: str, dic: set, p_mutation: float = 0.20):
        self.s = s
        self.dic = dic
        self.n = len(s)
        self.p_mutation = p_mutation

    def fitness(self, partitions: list):
        good, bad, pos = 0, 0, 0
        for i, x in enumerate(partitions):
            if x:  #
                ok = self.s[pos:i + 1] in self.dic
                good += ok
                bad += not ok
                pos = i + 1
        ok = self.s[pos:self.n] in self.dic
        good += ok
        bad += not ok
        ret = good / bad if bad > 0 else float('inf')
        return ret

    def tournament(self, pop: list):
        shuffle(pop)
        m = len(pop) // 2
        return [max(pop[i], pop[i + m], key=self.fitness) for i in range(m)] * 2

    def cross(self, pop: list):
        shuffle(pop)
        m = len(pop) // 2
        splits = [randint(0, self.n - 1) for _ in range(m)]
        return [pop[i][0:mid] + pop[i + m][mid:self.n - 1] for i, mid in enumerate(splits)] + \
               [pop[i + m][0:mid] + pop[i][mid:self.n - 1] for i, mid in enumerate(splits)]

    def mutate(self, pop: list):
        def random_flip(partitions: list):
            if random() <= self.p_mutation:
                partitions[randint(0, self.n - 2)] ^= True
            return partitions

        return [random_flip(x) for x in pop]

    def generate_population(self, n):
        n += n & 1  # para que n sea par siempre
        return [[not getrandbits(1) for _ in range(self.n - 1)] for _ in range(n)]

    def iterate(self, pop):
        return self.mutate(self.cross(self.tournament(pop)))

    @staticmethod
    def show(pop):
        for a in pop:
            print(a)

    def getPartition(self, partitions: list):
        words = []
        pos = 0
        for i, x in enumerate(partitions):
            if x:
                word = self.s[pos:i + 1]
                pos = i + 1
                words.append(word)
        word = self.s[pos:self.n]
        words.append(word)
        return words

    def solve(self, iterations: int = 10 ** 3, pop_size: int = 100):
        pop = self.generate_population(pop_size)
        cur = 1
        ans = max(pop, key=self.fitness)
        while cur <= iterations:
            pop = self.iterate(pop)
            best = max(pop, key=self.fitness)
            ans = max(ans, best, key=self.fitness)
            print(f'Iteracion #{cur}')
            print(f'Mejor respuesta en esta iteracion: Fitness = {self.fitness(best)}',
                  ' '.join(self.getPartition(best)), sep='\n')
            print(f'Mejor respuesta hasta el momento: Fitness = {self.fitness(ans)}',
                  ' '.join(self.getPartition(ans)), sep='\n')
            print()
            cur += 1

        pass


# string = 'Wordbreakproblem'
# string = 'Wordbreakproblem'
# dic = { 'this', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r', 'e','a', 'k','br', 'bre', 'brea', 'ak', 'problem' }

string = "JonathanVillegasOscarBurgaMarceloMartinezInteligenciaArtificial"
dic = {'Jonathan', 'Villegas', 'Oscar', 'Burga', 'Marcelo', 'Martinez',
       'Inteligencia', 'Artificial', 'VillegasOscar', 'celoMar'}
solver = GeneticWordBreak(string, dic)

solver.solve()