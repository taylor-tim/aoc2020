#!/usr/bin/env python3.8

import cProfile

import first_one
import second_one
import one_efficient
import efficient_solution


print('\nProfiling first_one')
cProfile.run('first_one.get_answer()')

print('Profiling efficient_solition with 2 nums')
cProfile.run('efficient_solution.get_answer(2020, 2)')

print('Profiling second one')
cProfile.run('second_one.get_answer()')

print('Profiling efficient_solition with 3 nums')
cProfile.run('efficient_solution.get_answer(2020, 3)')

