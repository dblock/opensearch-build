/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * The OpenSearch Contributors require contributions made to
 * this file be licensed under the Apache-2.0 license or a
 * compatible open source license.
 */

package jenkins

class Manifest implements Serializable {
    def steps
    def filename
    def data

    Manifest(steps, filename, data) {
        this.steps = steps
        this.filename = filename
        // BUGBUG: calling this.steps.readYaml bails without error
        this.data = data
    }
}