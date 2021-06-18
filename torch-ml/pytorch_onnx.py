num_classes = 21
net = build_ssd('test', 300, num_classes) # from https://github.com/amdegroot/ssd.pytorch/blob/master/ssd.py
dummy_input = Variable(torch.randn(1, 3, 300, 300))
model = torch.load('weights/ssd300_mAP_77.43_v2.pth')
net.load_state_dict(model)
torch.onnx.export(net, dummy_input, "ssd.onnx")
