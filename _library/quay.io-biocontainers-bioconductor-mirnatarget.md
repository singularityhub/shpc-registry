---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirnatarget"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirnatarget/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirnatarget/container.yaml"
updated_at: "2025-01-22 03:08:39.077143"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirnatarget"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirnatarget"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirnatarget", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirnatarget", "latest": {"1.44.0--r44hdfd78af_0": "sha256:4abbb0e62e94ead6a8aa7a6f77ac4038c7e10662a7a5742d86bf9f6c5bbf1f89"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:cb998ec3f37e130bc747848606eadf41356bc87042ec2653b2e9f771dc32d29e", "1.35.0--r42hdfd78af_0": "sha256:9ac39028ee82ca57c3a7a56fe019bd64a455f25222685b7a673e83cfa0c968df", "1.38.0--r43hdfd78af_0": "sha256:056e3e70fdb46210a4ee398edb310eefe5e2cb8bc6005fcdcae6cf6c53cf1e0c", "1.40.0--r43hdfd78af_0": "sha256:15c5996bf4f20e8c905227e46c4a129a0d50abdf598309ca905ed8b2b3c119b4", "1.44.0--r44hdfd78af_0": "sha256:4abbb0e62e94ead6a8aa7a6f77ac4038c7e10662a7a5742d86bf9f6c5bbf1f89"}, "docker": "quay.io/biocontainers/bioconductor-mirnatarget"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirnatarget.
shpc-registry automated BioContainers addition for bioconductor-mirnatarget
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirnatarget
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirnatarget:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirnatarget/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirnatarget/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirnatarget-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirnatarget-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirnatarget-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirnatarget-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirnatarget-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirnatarget-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirnatarget

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