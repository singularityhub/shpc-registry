---
layout: container
name:  "gradle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/gradle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/gradle/container.yaml"
updated_at: "2024-06-25 03:22:50.035988"
latest: "8-jdk21"
container_url: "https://hub.docker.com/_/gradle"
aliases:
 - "gradle"
versions:
 - "7.0.0-hotspot"
 - "7.0.1-hotspot"
 - "7.0.2-hotspot"
 - "7.1.0-hotspot"
 - "7.1.1-hotspot"
 - "7.2.0"
 - "7.3.0"
 - "7.3.3"
 - "7.4.0"
 - "latest"
 - "7"
 - "7-jdk17"
 - "7-jdk16"
 - "7-jdk11"
 - "7-jdk-openj9"
 - "7-jdk18"
 - "7-jdk19"
 - "8"
 - "8-jdk19"
 - "8-jdk17"
 - "8-jdk11"
 - "8-jdk8"
 - "8-jdk21"
 - "8-jdk20"
 - "8-jdk-21-and-22"
description: "Gradle is a build tool with a focus on build automation and support for multi-language development."
config: {"docker": "gradle", "url": "https://hub.docker.com/_/gradle", "maintainer": "@vsoch", "description": "Gradle is a build tool with a focus on build automation and support for multi-language development.", "latest": {"8-jdk21": "sha256:c582bc70eb666f62d90525367974dd66122bf069c1d45a70f621b0d08bd2182c"}, "tags": {"7.0.0-hotspot": "sha256:cef49a7bdb0c53dc0d64ed24f375fb0fdd6e3489d0b4fcd393f0c8c09be11320", "7.0.1-hotspot": "sha256:f3207f774a8ceb3286e0b65ca1864cfab639797a307c3d505bc6775adfb28d66", "7.0.2-hotspot": "sha256:b36aabaa3f4b333aae071be8658ad2fa558bcaea9e31b3e8dc42f6e7846cbd01", "7.1.0-hotspot": "sha256:92c0f3381fd8db612dac10b5b584d68376c192bae6b1a11b2190780a60411fe4", "7.1.1-hotspot": "sha256:19d9bdf24a291e5d7ac758c8d0c7d8f2f5d641b130d17b556dbab2c49701bf3e", "7.2.0": "sha256:67de4380b26d2b5406077cf5439b3488d139f7fedd9bdb8ddfadbe277750ede8", "7.3.0": "sha256:1f65f4991aa496cf835cbce10290bdc71c1cb526b4df807d97c4f51b863f2399", "7.3.3": "sha256:8d037a3bd86fc48b591ad778d6eb6130e641bad1be546923e6d097a7ad7708eb", "7.4.0": "sha256:5248d0e8f7f6ad2095c3a053d5461daa17b02097410f0e9f6397f8f4dedc34bf", "latest": "sha256:c582bc70eb666f62d90525367974dd66122bf069c1d45a70f621b0d08bd2182c", "7": "sha256:d69e7e64b8b04d795cc965a9190c59179d96b7289dba8a8f2ecb2943377f9edc", "7-jdk17": "sha256:d69e7e64b8b04d795cc965a9190c59179d96b7289dba8a8f2ecb2943377f9edc", "7-jdk16": "sha256:f174c0dcf9a84b4035f1fcb62f0340ddc69c0b93320e0d35f097d20ce2ca89d5", "7-jdk11": "sha256:b89a04fbdf9493edc8986f6345bb3e02486be74b3d8a385c894873c473c0b27b", "7-jdk-openj9": "sha256:acd908af42e1bee2f841eeac031d41317ab3fddcc3ec9d0d4e1cb4b28be24f5f", "7-jdk18": "sha256:f3c6308a57fa86af3c05ed1746cd041035074ed932cb9fecc0a0efedad35955e", "7-jdk19": "sha256:71af39c788a072e2ac641a4f87fa9d2a71fc46c017a5041c7aab3ff4fd36c666", "8": "sha256:c582bc70eb666f62d90525367974dd66122bf069c1d45a70f621b0d08bd2182c", "8-jdk19": "sha256:c241e5fb467405a0388618854931d392af82cc22869e658f20a65e062a660550", "8-jdk17": "sha256:cb3b50c6d5298026e5962880469079d62389f33744af3bba90bf21175052aa91", "8-jdk11": "sha256:a379579285ffd105d4ace7a11ac4b99f08cd718894a624ff25384b7e12e0314f", "8-jdk8": "sha256:9f54260f52639a0cb3f223c1e99a907cd7191bffaa6f6c584ebfc58712e65eab", "8-jdk21": "sha256:c582bc70eb666f62d90525367974dd66122bf069c1d45a70f621b0d08bd2182c", "8-jdk20": "sha256:c4aec619101a1b52872ef6e9687797e8e36c0b44649046e95001a797bd4697c8", "8-jdk-21-and-22": "sha256:0ddfdec8ec84c266d69f37a961bedcbf95548469f1bbb19cb929c7dce7578902"}, "aliases": {"gradle": "/usr/bin/gradle"}}
---

This module is a singularity container wrapper for gradle.
Gradle is a build tool with a focus on build automation and support for multi-language development.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install gradle
```

Or a specific version:

```bash
$ shpc install gradle:8-jdk21
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load gradle/8-jdk21
$ module help gradle/8-jdk21
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gradle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gradle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gradle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gradle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gradle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gradle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gradle

```bash
$ singularity exec <container> /usr/bin/gradle
$ podman run --it --rm --entrypoint /usr/bin/gradle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/gradle   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)