from datetime import datetime
import json
import time

import requests


def post_message_slack(text):
    url = 'https://hooks.slack.com/services/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'
    headers = {'Content-Type': 'application/json'}
    data = {
        "attachments": [
            {
                "mrkdwn_in": ["text", "pretext"],
                "color": "danger" if 'FAILED' in text else "good",
                "pretext": "Automation Tests Alerts: *Test Reports*",
                "text": text,
                "footer": "Automation Tests",
                "footer_icon": "https://s3-us-west-2.amazonaws.com/slack-files2/avatar-temp/2018-07-09/395140071906_09e99d515f9632d9fb6e.png",
                "thumb_url": "https://s3-us-west-2.amazonaws.com/slack-files2/avatar-temp/2018-07-09/395140071906_09e99d515f9632d9fb6e.png",
                "ts": time.mktime(datetime.utcnow().timetuple())
            }
        ]
    }
    requests.post(url, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    outfile = r'E:\PyCharm\Workspace\StarlightGroup\AmericanScienceCBD_AutomationTest\Reports\logfile.txt'
    with open(outfile, 'r') as f:
        post_message_slack(f.read())
