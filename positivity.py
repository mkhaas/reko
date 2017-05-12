#!/usr/bin/env python

import boto3
import argparse


def detect_faces_and_send_postivity(image, bucket, attributes=['ALL'], region="us-east-1"):
    rekognition = boto3.client("rekognition", region)
    face = rekognition.detect_faces(
        Image={
 #       'Bytes': b'bytes',
            'S3Object': {
                'Bucket': bucket,
                'Name': image,
#               'Version': 'string'
            }
        },
        Attributes=['ALL'],
    )

#   print(face, "\n")
#    print(face["FaceDetails"], "\n")
#    print(face["FaceDetails"][0], "\n")
#    print(face["FaceDetails"][0]["Emotions"], "\n")
#    print(face["FaceDetails"][0]["Smile"], "\n")
    print ("Smiling: %s" % face["FaceDetails"][0]["Smile"]["Value"])


    inspirationquotes = {
        "smile" : "Chill the champagne; more good news is on your way :) :)",
        "not_smile" : "Keep your chin up, universe is sending good news your way :) :)"
    }

#  print(inspirationquotes, "\n\n")

    smilevalue = face["FaceDetails"][0]["Smile"]["Value"]

    if (smilevalue == True):
#        print (inspirationquotes["smile"])
        print ('\x1b[1;31m'+ inspirationquotes["smile"] + '\x1b[0m')
    else:
        print('\x1b[1;31m'+ inspirationquotes["not_smile"] + '\x1b[0m')



if __name__ == '__main__':

    # Let's use Amazon S3
    s3 = boto3.resource('s3')

    # Print out bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)

    # Find the bucket and image name
    parser = argparse.ArgumentParser(description='Process image and send positivity')
    parser.add_argument('-i', '--image', help='Image in S3 to process', required=True)
    parser.add_argument('-b', '--S3bucket', help='AWS S3 bucket', required=True)
    args = parser.parse_args()

    ## show values ##
    print ("Image: %s  S3bucket: %s" % (args.image, args.S3bucket))
#    print ("S3 bucket: %s" % args.S3bucket)

    detect_faces_and_send_postivity(args.image, args.S3bucket)



