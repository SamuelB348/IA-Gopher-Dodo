import cProfile
import pstats

import numpy as np
from testing_dodo import *
from other import *
import time


def main():

    ##########################
    # DODO
    ##########################
    d = EngineDodo(start_board_dodo(6), 6, 100)

    # match(4, 100, 5.50613098, 2.9965201, -1.01483344, 0, 0.1, 1.26463952, -1.02441619, 0)
    match_vsrandom(4, 100, 1.25002444, 0.26184217, 0.14314292, -0.17516003)
    # tuning_dodo(4, 10, 0.01)
    #test_strategies(4, 100)

    # a = d.iterative_deepening(16, 1, R, d.legals(R), 1.25002444, 0.26184217, 0.14314292, -0.17516003)
    # print(a)
    # a = dodo_vsrandom(1.25002444, 0.26184217, 0.14314292, -0.17516003, 4, R)
    ##########################
    # GOPHER
    ##########################

    # g: Environment = initialize("gopher", start_board_gopher(4), R, 4, 100)
    # g.pplot()


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats()
