#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import uuid
from datetime import datetime
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):

    @task(1)
    def getMinVersion(self):
        self.client.headers.update(
            {'Authorization': 'Basic MjA0Mjk3Nzg4ODo1OGJhMWU2MC0xMjhlLTQyNTAtYTk3Mi05MzFkYTJlM2RmZjQ=', 'User-Agent': 'com.razor.razor'})
        self.client.get('/api/v1/min_version/android')

    @task(2)
    def login(self):
        self.client.headers.update(
            {'content-type': 'application/json', 'User-Agent': 'com.razor.razor'})
        self.client.post(
            '/api/v1/login', json={"phone": "2042977888", "password": "58ba1e60-128e-4250-a972-931da2e3dff4"})


class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet
    min_wait = 500
    max_wait = 1500
