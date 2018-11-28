import numpy as np
from mysql import connector
from ops import map_iou
from nms import processing_bboxes

def prepared_bboxes():
    gt_bboxes = {}
    pb_bboxes = {}
    cnx = connector.connect(host='180.167.46.105', user='ai', passwd='hangzhou', db='qa_rsna')

    cursor1 = cnx.cursor(buffered=True)
    cursor2 = cnx.cursor(buffered=True)
    cursor3 = cnx.cursor()


    cursor1.execute("SELECT DISTINCT patientId FROM `kaggle_pneumonia_fp_1`.`test_annotation` ")
    for (patientId, ) in cursor1:
        gt_bboxes[patientId] = []
        pb_bboxes[patientId] = []


    cursor2.execute("SELECT patientId, x, y, width, height, Target FROM \
                    `kaggle_pneumonia_fp_1`.`test_annotation` ")
    for (patientId, x, y, width, height, Target) in cursor2:
        if Target == 2:
            continue
        gt_bboxes[patientId].append([x, y, x + width, y + height)


    cursor3.execute("SELECT patientId, xmin, ymin, xmax, ymax, score FROM \
                    `qa_rsna`.`model_255634` where category = 1")
    for (patientId, x1, y1, x2, y2, score) in cursor3:
        pb_bboxes[patientId].append([x1, y1, x2, y2, score)


    cursor1.close()
    cursor2.close()
    cursor3.close()
    cnx.close()
    
    return gt_bboxes, pb_bboxes



def search_max(gt_bboxes, pt_bboxes, TH_SCORE, TH_IOU, TH_IOM):
    toc_score = 0
    toc_num = 0
    nt_bboxes = processing_bboxes(pt_bboxes, TH_SCORE, TH_IOU, TH_IOM)
    for patientId, boxes_pred in nt_bboxes.items():
        boxes_true = gt_bboxes.get(patientId)

        if not boxes_pred and not boxes_true:
            pass
        elif boxes_pred and not boxes_true:
            toc_num += 1
        elif not boxes_pred and boxes_true:
            toc_num += 1
        # elif boxes_pred and boxes_true:
        else:
            image_score = map_iou(np.array(boxes_true), np.array(boxes_pred))
            toc_score += image_score
            toc_num += 1


    return toc_score / float(toc_num)


# TH_SCORE = 0.4
# TH_IOU = 0.4
# TH_IOM = 0.9
#
# nt_bboxes = processing_bboxes(pb_bboxes, TH_SCORE, TH_IOU, TH_IOM)
#
# _THRESHOLDS = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
# toc_score = 0
# toc_num = 0
# # for patientId, boxes_pred in nt_bboxes.items():
# for patientId in sorted(nt_bboxes.keys()):
#     boxes_pred = nt_bboxes[patientId]
#     boxes_true = gt_bboxes.get(patientId)
#
#     if not boxes_pred and not boxes_true:
#         pass
#     elif boxes_pred and not boxes_true:
#         toc_num += 1
#     elif not boxes_pred and boxes_true:
#         toc_num += 1
#     # elif boxes_pred and boxes_true:
#     else:
#         image_score = map_iou(np.array(boxes_true), np.array(boxes_pred), thresholds=_THRESHOLDS)
#         print patientId, boxes_pred
#         toc_score += image_score
#         toc_num += 1
#
#     # if toc_num > 5:
#     #     break
#
# print "total number:", toc_num
# print "total score:", toc_score
# print "Evaluation score:", toc_score / float(toc_num)


if __name__ == '__main__':
    _SCORES = np.linspace(0.1, 0.7, 7)
    _TH_IOUS = np.linspace(0.3, 0.8, 6)
    _TH_IOMS = np.linspace(0.5, 1, 6)

    score_list = []
    for s in _SCORES:
        for u in _TH_IOUS:
            for m in _TH_IOMS:
                kaggle_score = search_max(gt_bboxes, pb_bboxes, s, u, m)
                score_list.append(kaggle_score)
                print "score = %s, iou = %.3f, iom = %.3f ---> %s" % (s, u, m, kaggle_score)

    print "Max Score:", max(score_list)
