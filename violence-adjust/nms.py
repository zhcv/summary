import numpy as np


def nms(dets, TH_IOU, TH_IOM):

    if len(dets) == 0:
        return []

    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]

    scores = dets[:, -1]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    # order = areas.argsort()
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        iou = inter / (areas[i] + areas[order[1:]] - inter)
        iom = inter / areas[i]

        inds = np.where((iou <= TH_IOU) & (iom <= TH_IOM))[0]
        order = order[inds + 1]

    return keep


def filter_bboxes(dets, TH_SCORE, TH_IOU, TH_IOM):
    new_dets = []
    ddets = [det for det in dets if det[-1] >= TH_SCORE]
    keep = nms(np.array(ddets), TH_IOU, TH_IOM)
    for j in keep:
        new_dets.append(_dets[j])
    return sorted(new_dets, key=lambda d: d[-1], reverse=True)


def processing_bboxes(bboxes_dict, TH_SCORE, TH_IOU, TH_IOM):
    # bboxes_dict: {filename: [[x1, x2, y1, y2, score], ...]}
    nms_bboxes = {}
    for patientId, dets in bboxes_dict.items():
        if dets:
            nms_bboxes[patientId] = filter_bboxes(dets, TH_SCORE, TH_IOU, TH_IOM)
        else:
            nms_bboxes[patientId] = []
    return nms_bboxes

