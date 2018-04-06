#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def calMoney():
    rate = 0.93
    firstin = int(input('请输入初始投入金额:'))
    earn = float(input('请输入每比想赚取的金额:'))
    sumin = firstin
    needin = 0
    count = 1
    print('如果中奖，按Y，否则，按N键继续投入')
    command = input('请选择:(Y N)')

    while (command.upper() != 'Y'):
        if (command.upper() == "N"):
            count = count + 1
            print('\n\n继续努力,这是你第 %d 次投注:' % count)
            needin = math.ceil((sumin + earn * count) / rate)
            print('至少需要投入:%d' % needin)
            actualin = int(input('请输入实际投入金额:'))
            sumin = sumin + actualin
            print('实际已投入:%d' % sumin)
            possibleEarn = actualin * (1 + rate)
            print('实际投入可能中奖金额:%.2f' % possibleEarn)
            actualEarn = possibleEarn - sumin
            print('如果中奖,收益为:%.2f' % actualEarn)

            print('\n******  如果中奖，按Y，否则，按N键继续投入.  ******')
            command = input('请选择:(Y N)')
    if (count == 1):
        print('\n\n一拉就响! 共投入:%d,盈利:%.2f.' % (sumin, firstin*rate))
    else:
        print('\n\n共投注:%d次,动用本金%d,盈利:%.2f. 不容易啊!' % (count, sumin, actualEarn))


if __name__ == '__main__':
    calMoney()
