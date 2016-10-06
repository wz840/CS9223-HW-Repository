#!/usr/bin/python

import boto
import boto.s3
import sys


# go through all regions
for region in boto.s3.regions():
  try:
    conn=boto.s3.connect_to_region(region.name)
    bucket = conn.get_bucket(sys.argv[1])
    file = 'ec2_status_logging.log'
    key = boto.s3.key.Key(bucket, file)
    with oper(file) as f:
      key.send_file(f)

    # reservations = conn.get_all_instances()
    # start_list = []
    # stop_list = []
    # for res in reservations:
    #   for inst in res.instances:
    #     name = inst.tags['Name'] if 'Name' in inst.tags else 'Unknown'
    #     state = inst.state

    #     # check auto:start and auto:stop tags
    #     start_sched = inst.tags['auto:start'] if 'auto:start' in inst.tags else None
    #     stop_sched = inst.tags['auto:stop'] if 'auto:stop' in inst.tags else None

    #     print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (region.name, name, inst.id, inst.instance_type, inst.launch_time, state, start_sched, stop_sched, inst.tags)

    #     # queue up instances that have the start time falls between now and the next 30 minutes
    #     if start_sched != None and state == "stopped" and time_to_action(start_sched, now, 31 * 60):
    #       start_list.append(inst.id)

    #     # queue up instances that have the stop time falls between 30 minutes ago and now
    #     if stop_sched != None and state == "running" and time_to_action(stop_sched, now, 31 * -60):
    #       stop_list.append(inst.id)

    # # start instances
    # if len(start_list) > 0:
    #   ret = conn.start_instances(instance_ids=start_list, dry_run=False)
    #   print "start_instances %s" % ret

    # # stop instances
    # if len(stop_list) > 0:
    #   ret = conn.stop_instances(instance_ids=stop_list, dry_run=False)
    #   print "stop_instances %s" % ret

  # most likely will get exception on new beta region and gov cloud
  except Exception as e:
    print 'Exception error in %s: %s' % (region.name, e.message)
