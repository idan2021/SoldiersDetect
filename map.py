import figmapy
import pprint

token = 'figd_7HSUewq63aMivKOxxg3TEKHhzkVRhkEks1efByaN'  # can be found in your figma user profile page
file_key = 'UL63FTDcNng8ismP3nfp58'  # can be found in the URL of the file
figmaPy = figmapy.FigmaPy(token=token)
file = figmaPy.get_file(key=file_key)