import os, sys
import numpy as np

if __name__ == "__main__":
	datContent = [i.strip().split() for i in open("/Users/nmg5038/SiB4/trunk/input/params/sib_phen.dat").readlines()]
	
	
	text_file = open("phenHelper.txt", "w")
	text_file.write('vegetationInfo=[]\n')
	text_file.write('allocationInfo=[]\n')
	text_file.write('growingSeasonStartInfo=[]\n')
	text_file.write('phenoStageFactInfo=[]\n')
	
	text_file.write('phenoStageThreshInfo=[]\n')
	text_file.write('livePoolTurnoverInfo=[]\n')
	text_file.write('livePoolGrowthRespInfo=[]\n')
	text_file.write('livePoolRespTransInfo=[]\n')
	
	
	text_file.write('livePoolRespInfo=[]\n')
	text_file.write('livePoolTransInfo=[]\n')
	text_file.write('deadPoolTurnoverInfo=[]\n')
	text_file.write('deadPoolTempRespInfo=[]\n')
	print datContent[148]
	print datContent[149]
	print datContent[150]
	for i in np.arange(1,25):
		text_file.write('vegetationInfo.append(['+', '.join(datContent[150+i][2:])+'])\n')
	
	print datContent[180-3]
	for i in np.arange(1,25):
		text_file.write('allocationInfo.append(['+', '.join(datContent[180+i][2:])+'])\n')
	
	print datContent[209-2]
	for i in np.arange(1,25):
		text_file.write('growingSeasonStartInfo.append(['+', '.join(datContent[209+i][2:])+'])\n')
	
	print datContent[237-2]
	for i in np.arange(1,25):
		text_file.write('phenoStageFactInfo.append(['+', '.join(datContent[237+i][2:])+'])\n')
	
	print datContent[266-2]
	for i in np.arange(1,25):
		text_file.write('phenoStageThreshInfo.append(['+', '.join(datContent[266+i][2:])+'])\n')
	
	print datContent[297-2]
	for i in np.arange(1,25):
		text_file.write('livePoolTurnoverInfo.append(['+', '.join(datContent[297+i][2:])+'])\n')

	print datContent[325-2]
	for i in np.arange(1,25):
		text_file.write('livePoolGrowthRespInfo.append(['+', '.join(datContent[325+i][2:])+'])\n')
	
	print datContent[353-2]
	for i in np.arange(1,25):
		text_file.write('livePoolRespTransInfo.append(['+', '.join(datContent[353+i][2:])+'])\n')
	
	print datContent[382-2]
	for i in np.arange(1,25):
		text_file.write('livePoolRespInfo.append(['+', '.join(datContent[382+i][2:])+'])\n')
	
	print datContent[411-2]
	for i in np.arange(1,25):
		text_file.write('livePoolTransInfo.append(['+', '.join(datContent[411+i][2:])+'])\n')
	
	print datContent[442-2]
	for i in np.arange(1,25):
		text_file.write('deadPoolTurnoverInfo.append(['+', '.join(datContent[442+i][2:])+'])\n')
	
	print datContent[470-2]
	for i in np.arange(1,25):
		text_file.write('deadPoolTempRespInfo.append(['+', '.join(datContent[470+i][2:])+'])\n')

	text_file.close()