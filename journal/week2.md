# Week 2 — Distributed Tracing

## Instrument Honeycomb with OTEL

![](assets/week2/query.png)

![](assets/week2/query2.png)

![](assets/week2/span.png)

![](assets/week2/traces0.png)

![](assets/week2/traces2.png)

### Add instruments to display day on console:

![](assets/week2/console.png)


## Instrument AWS X-Ray

### Create x-ray group

![](assets/week2/xray-create-group.png)

### Create sampling-rule:

![](assets/week2/xray-simpling-rule.png)

### Send data to aws x-ray:

![](assets/week2/xray-data.png)

![](assets/week2/xray-data2.png)

![](assets/week2/xray-data3.png)

### Configure the X-RAY segment and subsegment for "notifications-activities.py"


![](assets/week2/xray-notifications1.png)

![](assets/week2/xray-notifications2.png)

![](assets/week2/xray-notifications3.png)


### Activities-notifications' trace row data:

![](assets/week2/traces.png)


```json
{
    "Id": "1-640358eb-2eea1239c43e50ee698d2775",
    "Duration": 0.002,
    "LimitExceeded": false,
    "Segments": [
        {
            "Id": "360c599cdf153a94",
            "Document": {
                "id": "360c599cdf153a94",
                "name": "4567-iamcirin-awsbootcampcru-6sgfhud7439.ws-eu89.gitpod.io",
                "start_time": 1677940971.414751,
                "trace_id": "1-640358eb-2eea1239c43e50ee698d2775",
                "end_time": 1677940971.4162974,
                "in_progress": false,
                "http": {
                    "request": {
                        "url": "http://4567-iamcirin-awsbootcampcru-6sgfhud7439.ws-eu89.gitpod.io/api/activities/notifications",
                        "method": "GET",
                        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                        "client_ip": "197.0.23.76",
                        "x_forwarded_for": true
                    },
                    "response": {
                        "status": 200,
                        "content_length": 679
                    }
                },
                "aws": {
                    "xray": {
                        "sdk_version": "2.11.0",
                        "sdk": "X-Ray for Python"
                    }
                },
                "service": {
                    "runtime": "CPython",
                    "runtime_version": "3.10.10"
                },
                "subsegments": [
                    {
                        "id": "cf56ed4791ab7b58",
                        "name": "notification-activities-subsegment",
                        "start_time": 1677940971.4153833,
                        "end_time": 1677940971.415471,
                        "in_progress": false,
                        "annotations": {
                            "handle": "Channel"
                        },
                        "metadata": {
                            "default": {
                                "results": 1
                            }
                        },
                        "namespace": "local"
                    }
                ]
            }
        }
    ]
}

```

	### Configure custom logger to send to CloudWatch Logs

![](assets/week2/cloudwatch1.png)
![](assets/week2/cloudwatch2.png)

