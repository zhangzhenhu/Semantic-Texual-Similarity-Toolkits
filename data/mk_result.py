#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2014 Hal.com, Inc. All Rights Reserved
#
"""
模块用途描述

Authors: zhangzhenhu(zhangzhenhu1@100tal.com)
Date:    2018/2/1 11:27
"""
import sys
import argparse

__version__ = 1.0


def init_option():
    """
    初始化命令行参数项
    Returns:
        OptionParser 的parser对象
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input",
                        help=u"输入文件；默认标准输入设备")
    parser.add_argument("-o", "--output", dest="output",
                        help=u"输出文件；默认标准输出设备")
    return parser


def main(options):
    db = []
    with open('../data/test_ai-lab.txt') as fh:
        for line in fh:
            line = line.strip().split('\t')
            key = line[1].strip() + line[2].strip()
            # db[key] = line[0]
            db.append(line[0])
    out_file = open('submission_sample', 'w')
    with open('outputs/S1-gb/test_ai-lab.csv') as fh:
        index = 0
        for line in fh:
            line = line.strip().split('\t')
            # key = line[3].strip() + line[4].strip()
            score = line[0]
            out_file.write('%s\t%s\n' % (db[index], score))
            index += 1
    out_file.close()


if __name__ == "__main__":

    parser = init_option()
    options = parser.parse_args()

    if options.input:

        options.input = open(options.input)
    else:
        options.input = sys.stdin
    main(options)
