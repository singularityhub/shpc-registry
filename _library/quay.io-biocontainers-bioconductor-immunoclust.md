---
layout: container
name:  "quay.io/biocontainers/bioconductor-immunoclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-immunoclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-immunoclust/container.yaml"
updated_at: "2025-08-24 04:08:01.749661"
latest: "1.38.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-immunoclust"

versions:
 - "1.26.0--r41hc247a5b_2"
 - "1.30.0--r42hc247a5b_0"
 - "1.30.0--r42hf17093f_1"
 - "1.32.0--r43hf17093f_0"
 - "1.34.0--r43h7c4fd5e_0"
 - "1.38.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-immunoclust"
config: {"url": "https://biocontainers.pro/tools/bioconductor-immunoclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-immunoclust", "latest": {"1.38.0--r44he5774e6_0": "sha256:328bb2820dec250142a95381f16aac6681c1a9eab8fbf27c8c72d3263bb4ba48"}, "tags": {"1.26.0--r41hc247a5b_2": "sha256:53b106d3c9868a067915272d4243761cc4074b55b28b64b66e69abd17e5da214", "1.30.0--r42hc247a5b_0": "sha256:84f76f9817191130abc4e60c0aa17401d5703fd7cdef2b3b2c529239e66011cd", "1.30.0--r42hf17093f_1": "sha256:089af7987c6d9c4fb2b60013f3ae772994c8805b4a09901ccf35c8fb57157b40", "1.32.0--r43hf17093f_0": "sha256:982e7312918dcda251b2a667f55bded9f45c9e77e9bfd12dc516b13ad9961d0a", "1.34.0--r43h7c4fd5e_0": "sha256:6407840be16b43d386062f348fd4c4a199f7adb2d4762119ccf8ad5656777178", "1.38.0--r44he5774e6_0": "sha256:328bb2820dec250142a95381f16aac6681c1a9eab8fbf27c8c72d3263bb4ba48"}, "docker": "quay.io/biocontainers/bioconductor-immunoclust"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-immunoclust.
shpc-registry automated BioContainers addition for bioconductor-immunoclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-immunoclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-immunoclust:1.38.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-immunoclust/1.38.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-immunoclust/1.38.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-immunoclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-immunoclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-immunoclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-immunoclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-immunoclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-immunoclust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-immunoclust

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