---
name: Release
title: "[RELEASE] Release version {{ env.VERSION }}"
labels: untriaged, release, v{{ env.VERSION }}
---

## Release OpenSearch and OpenSearch Dashboards {{ env.VERSION }}

I noticed that a manifest was automatically created in [manifests/{{ env.VERSION }}](/opensearch-project/opensearch-build/tree/main/manifests/{{ env.VERSION }}). Please follow the following checklist to make a release.

<details><summary>How to use this issue</summary>
<p>

## This Release Issue

This issue captures the state of the OpenSearch release, its assignee (Release Manager) is responsible for driving the release. Please contact them or @mention them on this issue for help. There are linked issues on components of the release where individual components can be tracked. For more information check the the [Release Process OpenSearch Guide](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution).

</p>
</details>

Please refer to the following link for the release version dates: [Release Schedule and Maintenance Policy](https://opensearch.org/releases.html).

### [Entrance Criteria](https://github.com/opensearch-project/.github/blob/main/RELEASING.md#entrance-criteria-to-start-release-window)
Criteria | Status | Description  | Comments
-- | -- | -- | --
Each component release issue has an assigned owner | :red_circle: |   |
Documentation draft PRs are up and in tech review for all component changes | :red_circle: |   |
Sanity testing is done for all components | :red_circle: |   |
Code coverage has not decreased (all new code has tests) | :red_circle: |   |
Release notes are ready and available for all components | :red_circle: |   |
Roadmap is up-to-date (information is available to create release highlights) | :red_circle: |   |
Release ticket is cut, and there's a forum post announcing the start of the window | :red_circle: |   |
[Any necessary security reviews](https://github.com/opensearch-project/.github/blob/main/RELEASING.md#security-reviews) are complete | :red_circle: |   |

### OpenSearch {{ env.VERSION }} [exit criteria](https://github.com/opensearch-project/.github/blob/main/RELEASING.md#exit-criteria-to-close-release-window) status:
Criteria | Status | Description  | Comments
-- | -- | -- | --
Performance tests are run, results are posted to the release ticket and there no unexpected regressions | :red_circle: |   |
No unpatched vulnerabilities of medium or higher severity that have been publicly known for more than 60 days | :red_circle: |   |
Documentation has been fully reviewed and   signed off by the documentation community. | :red_circle: |   |
All integration tests are passing |  :red_circle: |   |
Release blog is ready | :red_circle: |   |

### OpenSearch-Dashboards {{ env.VERSION }} [exit criteria](https://github.com/opensearch-project/.github/blob/main/RELEASING.md#exit-criteria-to-close-release-window) status:
Criteria | Status | Description  | Comments
-- | -- | -- | --
Documentation has been fully reviewed and   signed off by the documentation community | :red_circle: |   |
No unpatched vulnerabilities of medium or higher severity that have been publicly known for more than 60 days | :red_circle: |   |
All integration tests are passing | :red_circle: |   |
Release blog is ready | :red_circle: |   |

### [Preparation](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#preparation)

- [ ] [Release manager](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-manager) assigned.
- [ ] Update [release page](https://opensearch.org/releases.html) on the website with release manager and release issue details. [Sample PR](https://github.com/opensearch-project/project-website/pull/2642)
- [ ] Existence of label in each component repo. For more information check the [release-label](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-label) section.
- [ ] [Increase the build frequency](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#increase-the-build-frequency).
- [ ] [Release Issue](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-issue).

### [Campaigns](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#campaigns)

- [ ] [Component Release Issue](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#component-release-issues).
- [ ] [Release Campaigns](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-campaigns).

### [Version Increment](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#version-increment) - _Ends __REPLACE_RELEASE-minus-10-days__

- [ ] [Core Version Increment](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#core-version-increment).
- [ ] [Components Version Increment](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#components-version-increment).

### [Feature Freeze](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#code-complete-and-feature-freeze) - _Ends __REPLACE_RELEASE-minus-12-days__

- [ ] OpenSearch / OpenSearch-Dashboards core and components teams finalize their features.

### [Code Complete](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#code-complete-and-feature-freeze) - _Ends __REPLACE_RELEASE-minus-10-days___

- [ ] Mark this as done once the [Code Complete](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#code-complete-and-feature-freeze) is reviewed.
- [ ] Create/Verify pull requests to add each component to relase input [manifests/{{ env.VERSION }}/opensearch-{{ env.VERSION }}.yml](/opensearch-project/opensearch-build/tree/main/manifests/{{ env.VERSION }}/opensearch-{{ env.VERSION }}.yml) and [manifests/{{ env.VERSION }}/opensearch-dashboards-{{ env.VERSION }}.yml](/opensearch-project/opensearch-build/tree/main/manifests/{{ env.VERSION }}/opensearch-dashboards-{{ env.VERSION }}.yml).

### [Release Branch, Release Candidate Creation and Testing](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-candidate-creation-and-testing) - _Ends __REPLACE_RELEASE-minus-6-days___

- [ ] [Core Release Branch](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#core).
- [ ] [Components Release Branch](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#components).
- [ ] [Generate Release Candidate](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-candidate).
- [ ] [Docker Scan](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#docker-scan).
- [ ] [Integ Test](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#integration-test).
   - [ ] TAR
   - [ ] RPM
   - [ ] DEB
   - [ ] Windows
- [ ] [Backwards Compatibility Tests](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#backwards-compatibility-tests).
- [ ] [Broadcast and Communication](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#broadcast-and-communication).
- [ ] [Release Candidate Lock](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-candidate-lock).
- [ ] [Stop Release Candidate periodic auto builds](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#stop-periodic-auto-builds)
### [Performance testing validation](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#benchmark-tests) - _Ends __REPLACE_RELEASE-minus-6-days___

- [ ] Post the benchmark-tests
- [ ] Longevity tests do not show any issues.

### [Pre Release](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#pre-release) - _Ends __REPLACE_RELEASE-minus-1-days___

- [ ] [Release Labeled Issues](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-labeled-issues).
- [ ] [Go or No-Go](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#go-or-no-go).
- [ ] [Release Notes](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-notes).

### [Release](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#main-release) - _Ends {__REPLACE_RELEASE-day}_

- [ ] [Central Promotion Workflow](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#central-release-promotion-workflow).
- [ ] [Collaboration with the Project Management Team](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#collaboration-with-the-project-management-team).

### [Release Checklist](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-checklist).

<br>
<details><summary>Release Checklist</summary>
<p>

### Pre-Release activities
- [ ] Promote Repos.
   - - [ ] OS
   - - [ ] OSD
- [ ] Promote Artifacts.
   - - [ ] Windows
   - - [ ] Linux Debian
   - - [ ] Linux RPM
   - - [ ] Linux TAR
- [ ] Consolidated Release Notes.

### Release activities
- [ ] Docker Promotion.
- [ ] Release Validation part 1.
     -  - [ ] OpenSearch and OpenSearch Dashboard Validation.
     -  - [ ] Validate the native plugin installation.
- [ ] Merge consolidated release notes PR.
- [ ] Website and Documentation Changes.
    - - [ ] Merge staging website PR.
    - - [ ] Promote the website changes to prod.
    - - [ ] Add website alert.
- [ ] Release Validation part 2.
    -  - [ ] Validate the artifact download URL's and signatures. 
- [ ] Release Validation part 3.
    -  - [ ] Trigger the validation build (Search for `Completed validation for <>` in the logs).
- [ ] Maven Promotion.
- [ ] Publish blog posts.
- [ ] Advertise on Social Media.
- [ ]  Post on public slack and Github Release issue.

</p>
</details>
<br>

### [Post Release](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#post-release)

- [ ] [Release Tags](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#release-tags).
- [ ] [Input Manifest Update](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#input-manifest-update).
- [ ] [OpenSearch Build Release notes](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#opensearch-build-release-notes).
- [ ] [Decrease the Build Frequency](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#decrease-the-build-frequency).
- [ ] [Retrospective Issue](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#retrospective-issue).
- [ ] [Helm and Ansible Playbook release](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#helm-and-ansible-playbook-release).
- [ ] [Upcoming Release Preparation](https://github.com/opensearch-project/opensearch-build/wiki/Releasing-the-Distribution#upcoming-release-preparation).

### Components

__Replace with links to all component tracking issues.__

| Component | On track | Release Notes |
| --------- | -------- | ----- |
| {COMPONENT_ISSUE_LINK} | {INDICATOR} | {STATUS} |

<details><summary>Legend</summary>
<p>

| Symbol | Meaning |
| -------- | ---------- |
| :green_circle: | On track with overall release |
| :yellow_circle: | Missed last milestone |
| :red_circle: | Missed multiple milestones |

</p>
</details>
