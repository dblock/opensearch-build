/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * The OpenSearch Contributors require contributions made to
 * this file be licensed under the Apache-2.0 license or a
 * compatible open source license.
 */

package jenkins

class ManifestBuilder implements Serializable {
    def steps

    ManifestBuilder(steps) {
        this.steps = steps
    }

    /**@
     * Invokes build.sh and returns the YAML from builds/manifest.yml.
     */
    def build(Map args = [:], String inputManifest) {
        this.steps.sh([
            "./build.sh",
            "\"${inputManifest}\"",
            toKeyValue(args)
        ].minus(null).join(" "))

        return this.steps.readYaml(file: "builds/manifest.yml")
    }

    /**@
     * Invokes assemble.sh and returns the YAML from dist/manifest.yml.
     */
    def assemble(Map args = [:], String buildManifest) {
        this.steps.sh([
            "./assemble.sh",
            "\"${buildManifest}\"",
            toKeyValue(args)
        ].minus(null).join(" "))

        return this.steps.readYaml(file: "dist/manifest.yml")
    }

    def toKeyValue = { 
        it.collect({ item -> 
            def key = item.key.replace('_', '-')
            return "--${key} \"${item.value}\"" 
        }).join(" ")
    }
}