import math
sad_sum=0
party_sum=0
romantic_sum=0
bhakti_sum=0
sad_tempo=[103.36,129.2,152,161.5,103.36,161.5,161.5,107.67,123.05,198.77,143.55,80.75,136,152]
party_tempo=[ 89.1,152,129.2,123.05,136,107.67,129.2,89.1,99.38,68,123.05,61.52,129.2,95.7,129.2]
sad_beat=[201,196,216,201,159,246,153,208,197,191,180,199,145,142]
party_beat=[106,93,124,139,127,124,130,136,114,131,89,129,143,104,136]
romantic_tempo=[86.13,89.1,89.1,161.5,143.55,99.38,103.36,123.05,83.35]
romantic_beat=[136,196,221,221,177,151,129,152,257]
bhakti_tempo=[117.45,86.13,92.29,184.57,152,184.57,95.70]
bhakti_beat=[207,188,165,90,367,130,199]

xin=float(input('tempo' ))
yin=float(input('beats '))

for i in range (len(sad_tempo)):
    d=math.exp(-((yin-sad_beat[i])**2+(xin-sad_tempo[i])**2)/100)
    sad_sum=sad_sum+d
print(sad_sum)

for i in range (len(party_tempo)):
    d=math.exp(-((yin-party_beat[i])**2+(xin-party_tempo[i])**2)/100)
    party_sum=sad_sum+d
print(party_sum)

for i in range (len(romantic_tempo)):
    d=math.exp(-((yin-romantic_beat[i])**2+(xin-romantic_tempo[i])**2)/100)
    romantic_sum=romantic_sum+d
print(romantic_sum)

for i in range (len(bhakti_tempo)):
    d=math.exp(-((yin-bhakti_beat[i])**2+(xin-bhakti_tempo[i])**2)/100)
    bhakti_sum=bhakti_sum+d
print(bhakti_sum)

prediction=max(sad_sum,party_sum,romantic_sum,bhakti_sum)
if(prediction==sad_sum):
    print ('this song is a sad song')
if(prediction==party_sum):
    print ('this song is a party song')
if(prediction==romantic_sum):
    print ('this song is a romantic song')
if(prediction==bhakti_sum):
    print ('this song is a bhajan song')
    
