/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * The OpenSearch Contributors require contributions made to
 * this file be licensed under the Apache-2.0 license or a
 * compatible open source license.
 */

import org.junit.*
import java.util.*
import static com.lesfurets.jenkins.unit.global.lib.LibraryConfiguration.library
import static com.lesfurets.jenkins.unit.global.lib.ProjectSource.projectSource
import com.lesfurets.jenkins.unit.*
import com.lesfurets.jenkins.unit.declarative.*
import static org.junit.Assert.*

class TestManifestBuilder extends DeclarativePipelineTest {
    def jenkinsScript = "tests/jenkins/jobs/ManifestBuilder_Jenkinsfile"

    @Override
    @Before
    void setUp() throws Exception {
        super.setUp()

        helper.registerSharedLibrary(
            library().name('jenkins')
                .defaultVersion('<notNeeded>')
                .allowOverride(true)
                .implicit(true)
                .targetPath('<notNeeded>')
                .retriever(projectSource())
                .build()
            )
    }

    @Test
    void testBuildOpenSearch() throws Exception {
        helper.registerAllowedMethod('readYaml', [Map.class], null)
        binding.setVariable('BASE_URL', 'https://ci.opensearch.org/x/y')
        runScript(jenkinsScript)
        RegressionTestHelper.testNonRegression(helper, jenkinsScript)
        assertJobStatusSuccess()
        printCallStack()
    }
}