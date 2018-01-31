#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2014 Hal.com, Inc. All Rights Reserved
#
"""
模块用途描述

Authors: zhangzhenhu(zhangzhenhu1@100tal.com)
Date:    2018/1/31 19:45
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
    db = {}
    for fname in ['stsbenchmark/sts-train.csv', 'stsbenchmark/sts-dev.csv', 'stsbenchmark/sts-test.csv']:
        with open(fname) as fh:
            for line in fh:
                line = line.strip().split('\t')
                key = line[5] + line[6]
                db[key] = line[4]

    total_count = 0
    hit_count = 0
    with open('test_ai-lab.txt') as fh:
        for line in fh:
            total_count += 1
            line = line.strip().split('\t')
            key = line[1] + line[2]
            score = db.get(key, None)
            if score is not None:
                hit_count += 1
            else:
                score = '0'
            line = ['ai-lab', 'test', '2017', line[0], score, line[1], line[2]]
            print('\t'.join(line))


if __name__ == "__main__":

    parser = init_option()
    options = parser.parse_args()

    if options.input:

        options.input = open(options.input)
    else:
        options.input = sys.stdin
    main(options)
