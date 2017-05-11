#!/usr/bin/env python

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
#data = open('/Users/mkaushik/AWS/Cisco/s2.jpg', 'rb')
#s3.Bucket('mrkrecoko').put_object(Key='s2.jpg', Body=data)

rekognition = boto3.client("rekognition", "us-east-1")
face = rekognition.detect_faces(
    Image={
 #       'Bytes': b'bytes',
        'S3Object': {
            'Bucket': 'mrkrecoko',
            'Name': 's2.jpg',
#            'Version': 'string'
        }
    },
    Attributes=['ALL'],

)

print(face)
print("\n")

FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")

print(face["FaceDetails"])
print("\n")

print(face["FaceDetails"][0])
print("\n")

print(face["FaceDetails"][0]["Emotions"])
print("\n")

print(face["FaceDetails"][0]["Smile"])
print("\n")

print(face["FaceDetails"][0]["Smile"]["Value"])
print("\n")

inspirationquotes = {
        "smile" : "Chill the champagne; more good news is on your way",
        "not_smile" : "Keep your chin up, universe is sending good news your way"
}

print(inspirationquotes, "\n\n")

smilevalue = face["FaceDetails"][0]["Smile"]["Value"]

if (smilevalue == True):
    print (inspirationquote["smile"], "\n")

else:
    print(inspirationquotes["not_smile"])

#for emotion in face[""['Emotions']:
#		print("  {Type} : {Confidence}%".format(**emotion))

#for feature, data in face.iteritems():
#    if feature not in FEATURES_BLACKLIST:
#        print(feature)
#        print data[0]
#        print data[1]
#        print "  {feature}({data[Value]}) : {data[Confidence]}%".format(feature=feature, data=data)


