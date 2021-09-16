# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import logging
import re

from ci_workflow.ci_check import CiCheck
from system.properties_file import PropertiesFile


class CiCheckMavenDependencies(CiCheck):
    def __init__(self, component, git_repo, target, args):
        super().__init__(component, git_repo, target, args)
        self.dependencies = self.__get_dependencies()

    def __get_dependencies(self):
        cmd = " ".join(
            [
                "mvn dependency:tree",
                "| grep INFO",
                "| cut -d] -f2",
            ]
        )

        lines = self.__extract_dependencies__(self.git_repo.output(cmd))
        stack = [lines.pop()] if lines else []
        props = PropertiesFile("")
        for line in lines:
            # e.g. "|    +- org.opensearch:opensearch-core:1.1.0-SNAPSHOT"
            # see security_dependencies.txt in tests for an example
            match = re.search(r"-\s(.*):([0-9,\w,.-]*):([0-9,\w,.-]*)[\s]*", line)
            if match:
                levels = line.count(" ")
                while levels < len(stack):
                    del stack[-1]

                if levels == len(stack):
                    stack[-1] = match.group(1).strip()
                elif levels > len(stack):
                    stack.append(match.group(1).strip())

                key = "/".join(stack)
                value = match.group(2).strip()
                logging.debug(f"{key}={value}")
                props[key] = value

        return props

    def __extract_dependencies__(self, output):
        lines = []
        tree = False
        for line in output.split("\n"):
            line = line.strip()
            if "maven-dependency-plugin:" in line:
                tree = True
            elif "----" in line:
                tree = False
            elif tree:
                lines.append(line)
        return lines

class CiCheckMavenDependenciesOpenSearchVersion(CiCheckMavenDependencies):
    def check(self):
        self.dependencies.check_value(
            "org.opensearch:opensearch", self.target.opensearch_version
        )
        logging.info(
            f"Checked {self.component.name} OpenSearch dependency ({self.target.opensearch_version})."
        )
