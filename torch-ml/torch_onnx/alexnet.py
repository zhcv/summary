import torch
import torchvision
from torch import nn

dummy_input = torch.randn(1, 3, 224, 224, device='cuda')
model = torchvision.models.alexnet(pretrained=True).cuda()
# Providing input and output names sets the display names for values
# within the model's graph. Setting these does not change the semantics
# of the graph; it is only for readability.
#
# The inputs to the network consist of the flat list of inputs (i.e.
# the values you would pass to the forward() method) followed by the
# flat list of parameters. You can partially specify names, i.e. provide
# a list here shorter than the number of inputs to the model, and we will
# only set that subset of names, starting from the beginning.

# add softmax layer to the last layer
model = nn.Sequential(model, nn.Softmax(1))


input_names = [ "actual_input_1" ] + [ "learned_%d" % i for i in range(3) ]
print(input_names)
out = model(dummy_input)

print(out[:,:5])
output_names = [ "output1" ]
torch.onnx.export(model, dummy_input, "alexnet.onnx", verbose=True, input_names=input_names, output_names=output_names)
