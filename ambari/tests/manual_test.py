# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.ambari import AmbariCheck


def test_check(aggregator):
    instance = [{
        "url": "https://146.148.123.63",
        "port": "8443",
        "path": "/ambari-lab-2/dp-proxy/ambari",
        "username": "admin",
        "password": "admin",
        "tags": ["test:abc", "test1:xyz"],
        "services": {
            "HDFS": ["NAMENODE", "DATANODE"],
            "YARN": ["NODEMANANGER", "YARNCLIENT"]
        },
        "metric_headers": ["cpu", "jvm"],
        "collect_host_metrics": True,
        "collect_service_metrics": True,
        "timeout": 30
    }]
    check = AmbariCheck('ambari', {}, {}, instance)
    check.check(instance[0])
    # import pdb; pdb.set_trace()
    aggregator.assert_all_metrics_covered()