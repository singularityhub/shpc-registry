---
layout: container
name:  "quay.io/biocontainers/bioconductor-multigsea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multigsea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multigsea/container.yaml"
updated_at: "2025-08-25 03:26:13.050544"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multigsea"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multigsea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multigsea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multigsea", "latest": {"1.16.0--r44hdfd78af_0": "sha256:c17b1391a4089905eac3496bf17fd79875021a6a8080b7208dfce0eff4e7dc77"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:c48d4d33bedb3cb204b65077ef465a804f193e42786ac976bf233ec2f1f8b468", "1.8.0--r42hdfd78af_0": "sha256:a3d30038b3a0ab33fcaac879232e877940047f96cd97caa680704e07c3313330", "1.10.0--r43hdfd78af_0": "sha256:5bdaec756f16035bc6aea10721036d5bb9977b1041cd05204b3d6f6f5fe28bd8", "1.12.0--r43hdfd78af_0": "sha256:f95096582f2237f1199c5503b226b694189760a63e01f50f02e24b0fc2947f12", "1.16.0--r44hdfd78af_0": "sha256:c17b1391a4089905eac3496bf17fd79875021a6a8080b7208dfce0eff4e7dc77"}, "docker": "quay.io/biocontainers/bioconductor-multigsea"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multigsea.
shpc-registry automated BioContainers addition for bioconductor-multigsea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multigsea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multigsea:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multigsea/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multigsea/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multigsea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multigsea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multigsea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multigsea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multigsea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multigsea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-multigsea

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