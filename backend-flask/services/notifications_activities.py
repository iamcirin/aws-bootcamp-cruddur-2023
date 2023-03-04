# added for x-eay segment
# from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.core import patch_all
from datetime import datetime, timedelta, timezone
# patch_all()


# added for x-ray segment
# xray_recorder.begin_segment('notification-activities')

class NotificationsActivities:
  def run():
  # added this line for x-ray sbsegment
    # with xray_recorder.in_subsegment('notification-activities-subsegment'):
      now = datetime.now(timezone.utc).astimezone()
      results = [{
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Channel',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 1,
        'reposts_count': 0,
        'replies': [{
          'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
          'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
          'handle':  'Worf',
          'message': 'This post has no honor!',
          'likes_count': 0,
          'replies_count': 0,
          'reposts_count': 0,
          'created_at': (now - timedelta(days=2)).isoformat()
        }],
      }
      ]
      # xray_recorder.put_metadata('results', len(results))
      # xray_recorder.put_annotation('handle', results[0]['handle'])
      # xray_recorder.end_subsegment()
      return results


# xray_recorder.end_segment()