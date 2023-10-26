---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqc/container.yaml"
updated_at: "2023-10-26 03:17:10.389922"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqc"

versions:
 - "1.28.0--r41hdfd78af_1"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqc", "latest": {"1.34.0--r43hdfd78af_0": "sha256:1b92eaafa386219187409a1075d7b64deba6c7a02b2163ccc88bacb54d586a6a"}, "tags": {"1.28.0--r41hdfd78af_1": "sha256:92de73d6081bf69cf0dcf89318590a7fed87f607f1d47a15effe352fd8427331", "1.32.0--r42hdfd78af_0": "sha256:bf46ec5a23271971cc7723f8752894ae964c91ceb578fbc69ef7456efe65d5a6", "1.34.0--r43hdfd78af_0": "sha256:1b92eaafa386219187409a1075d7b64deba6c7a02b2163ccc88bacb54d586a6a"}, "docker": "quay.io/biocontainers/bioconductor-seqc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqc.
shpc-registry automated BioContainers addition for bioconductor-seqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqc:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqc/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seqc/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seqc

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