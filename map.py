import FigmaPy as figmapy
import pprint

from FigmaPy import FigmaPy

token = 'figd_7HSUewq63aMivKOxxg3TEKHhzkVRhkEks1efByaN'  # can be found in your figma user profile page
file_key = 'UL63FTDcNng8ismP3nfp58'  # can be found in the URL of the file
figmaPy = FigmaPy(token)
file = figmaPy.get_file(file_key)
print([x.get('name') for x in file.document.get('children')])
# ['Page 1', 'Page 2']

page1 = file.document.get('children')
print(page1)
print([x.get('name') for x in page1])
# ['myArrow', 'myGroup', 'myImage']

ids = [x.get('id') for x in page1]
print(ids)
# ['7:2', '7:6', '21:4']

images = figmaPy.get_file_images(file_key=file_key, ids=ids)
pprint.pprint(images.images)
# {'21:4': 'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/9bc9fdbd-REDACTED-2d1f31e9b57e',
#  '7:2': 'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/de2afe63d-REDACTED-8abc-9ca5b5f88ac8',
#  '7:6': 'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/f56d5d8dd-REDACTED-af17-461010e0af14'}
