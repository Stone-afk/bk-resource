# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - Resource SDK (BlueKing - Resource SDK) available.
Copyright (C) 2023 THL A29 Limited,
a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the
specific language governing permissions and limitations under the License.
We undertake not to change the open source license (MIT license) applicable
to the current version of the project delivered to anyone in the future.
"""

from bk_resource import BkApiResource


class MockApiResource(BkApiResource):
    base_url = "https://bk.tencent.com"
    method = "GET"
    action = "/"
    platform_authorization = False


class MockPlatformAuth(MockApiResource):
    platform_authorization = True


class MockHeaderInject(MockApiResource):
    bkapi_header_authorization = True


class MockRequest:
    COOKIES = {"username": "admin"}

    class User:
        bk_username = "admin"

    @property
    def user(self):
        return self.User()