#!/usr/bin/env python

import boto3
import argparse

# Use AWS reko API to detect image mood and prints a positivity shout-out
# Inputs
#   image       --- image name that is uploaded on AWS S3 bucket (required)
#   bucket      --- AWS S3 bucket name
#   attributes  --- to pass to rekognition.detect_faces
#   region      ---  AWS region
def detect_faces_and_send_postivity(image, bucket, attributes=['ALL'], region="us-east-1"):
    try:
        rekognition = boto3.client("rekognition", region)

        face = rekognition.detect_faces(
            Image={
 #          'Bytes': b'bytes',
                'S3Object': {
                    'Bucket': bucket,
                    'Name': image,
#                   'Version': 'string'
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

    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(image, bucket) +
              "Make sure your object and bucket exist and your bucket is in the us-east-1.")
        raise e


if __name__ == '__main__':

    # Let's use Amazon S3
    s3 = boto3.resource('s3')

    # Print out AWS S3bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)

    # Get user's input for the bucket and image name
    parser = argparse.ArgumentParser(description='Process image and send positivity')
    parser.add_argument('-i', '--image', help='Image in S3 to process', required=True)
    parser.add_argument('-b', '--S3bucket', help='AWS S3 bucket', required=True)
    args = parser.parse_args()

    # print input values #
    print ("Image: %s  S3bucket: %s" % (args.image, args.S3bucket))
#    print ("S3 bucket: %s" % args.S3bucket)

    # Use AWS reko API to detect image mode and send a positivity shout-out
    detect_faces_and_send_postivity(args.image, args.S3bucket)



