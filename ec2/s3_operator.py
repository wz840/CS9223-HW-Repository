#!/usr/bin/python

import boto
import boto.s3
import sys


# go through all regions
for region in boto.s3.regions():
  try:
    conn=boto.s3.connect_to_region(region.name)
    bucket = conn.get_bucket(sys.argv[1])
    file = '/home/ec2-user/ec2_status_logging.log'
    key = boto.s3.key.Key(bucket, file)
    with oper(file) as f:
      key.send_file(f)


  # most likely will get exception on new beta region and gov cloud
  except Exception as e:
    print 'Exception error in %s: %s' % (region.name, e.message)
