---
layout: container
name:  "quay.io/biocontainers/bioconductor-easier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-easier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-easier/container.yaml"
updated_at: "2025-01-27 03:08:45.134973"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-easier"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.3--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-easier"
config: {"url": "https://biocontainers.pro/tools/bioconductor-easier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-easier", "latest": {"1.12.0--r44hdfd78af_0": "sha256:574f3da017185b98137a8f053a5e7da897520070ec8d168030a06ab1981107f5"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:be3cb49ef8ee1f1d4c34d9a2dd8114a92e84da2ac2ceecd566acf5a39779c650", "1.4.0--r42hdfd78af_0": "sha256:51ee752d22f6f0460d6698f4c1b650b8def64c26caf8b8301312b2f7aae54aa6", "1.6.3--r43hdfd78af_0": "sha256:89b49b334c02c5f3cb27cb5b76584583a830eee7e2451afc5eed46d861881475", "1.8.0--r43hdfd78af_0": "sha256:c3202d7f58c840d140ae769ad4641adb33f5e975d4ed1d2746b0ca7b7c3ed273", "1.12.0--r44hdfd78af_0": "sha256:574f3da017185b98137a8f053a5e7da897520070ec8d168030a06ab1981107f5"}, "docker": "quay.io/biocontainers/bioconductor-easier"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-easier.
shpc-registry automated BioContainers addition for bioconductor-easier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-easier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-easier:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-easier/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-easier/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-easier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-easier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-easier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-easier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-easier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-easier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-easier

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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