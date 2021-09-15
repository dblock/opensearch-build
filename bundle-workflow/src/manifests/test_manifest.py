# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

from manifests.manifest import Manifest
from manifests.typechecked import dataclass_typechecked


class TestManifest(Manifest):
    """
    TestManifest contains the test support matrix for any component.

    The format for schema version 1.0 is:
        schema-version: '1.0'
        components:
          - name: index-management
            integ-test:
              dependencies:
                - job-scheduler
                - alerting
              test-configs:
                - with-security
                - without-security
                - with-less-security
            bwc-test:
              dependencies:
              test-configs:
                - with-security
                - without-security
    """

    def __init__(self, data):
        super().__init__(data)
        self.components = list(
            map(lambda entry: self.Component(entry), data["components"])
        )

    def __to_dict__(self):
        return {
            "schema-version": "1.0",
            "components": list(
                map(lambda component: component.__to_dict__(), self.components)
            ),
        }

    @dataclass_typechecked
    class Component:
        name: str
        integ_test: dict
        bwc_test: dict

        def __init__(self, data):
            self.name = data["name"]
            self.integ_test = data["integ-test"]
            self.bwc_test = data["bwc-test"]

        def __to_dict__(self):
            return {
                "name": self.name,
                "integ-test": self.integ_test,
                "bwc-test": self.bwc_test,
            }


TestManifest.__test__ = False  # type:ignore
