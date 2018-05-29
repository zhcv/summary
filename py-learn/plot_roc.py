#! -*- coding=utf-8 -*-

import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as pl


def plot_roc(evaluate_result):
    db = []  # [filename,score]
    pos, neg = 0, 0
    with open(evaluate_result, 'r') as fs:
        for line in fs:
            _, nonclk, clk, score = line.strip().split(' ')
            nonclk = int(nonclk)
            clk = int(clk)
            score = float(score)
            db.append([score, nonclk, clk])
            pos += clk
            neg += nonclk

    print "roc:pos: ", pos 
    db = sorted(db, key=lambda x: x[0], reverse=True)

    # calculate ROC ordinate
    xy_arr = []
    tp, fp = 0., 0.
    for i in range(len(db)):
        tp += db[i][2]
        fp += db[i][1]
        xy_arr.append([fp / neg, tp / pos])

    # calculate AUC
    auc = 0.
    prev_x = 0
    for x, y in xy_arr:
        if x != prev_x:
            auc += (x - prev_x) * y
        prev_x = x
    print "the auc is %s." % auc

    x = [_v[0] for _v in xy_arr]
    y = [_v[1] for _v in xy_arr]
    return x, y, auc


if __name__ == '__main__':

    sec_x, sec_y, sec_auc = plot_roc('dev_test.txt')
    xin_x, xin_y, xin_auc = plot_roc('xinjiang_526.txt')
    # pl.title("ROC curve of %s (AUC = %.4f)" % ('TB_MODEL', auc))
    pl.title('ROC curve of TB_MODEL')
    pl.xlabel("False Positive Rate")
    pl.ylabel("True Positive Rate")
    # use pylab to plot x and y
    pl.plot(xin_x, xin_y, 'g', label='model5 AUC:%.4f' % xin_auc)
    pl.plot(sec_x, sec_y, 'r', label='model6 AUC:%.4f' % sec_auc)
    pl.legend(bbox_to_anchor=(1.0, 0.85), loc=1, borderaxespad=0.)
    pl.show()  # show the plot on the screen
    #pl.savefig('xinjiang.png')
