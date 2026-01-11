---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminahumanv2beadid.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminahumanv2beadid.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminahumanv2beadid.db/container.yaml"
updated_at: "2026-01-11 04:26:24.135087"
latest: "1.8.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminahumanv2beadid.db"

versions:
 - "1.8.0--r41hdfd78af_9"
 - "1.8.0--r42hdfd78af_10"
 - "1.8.0--r43hdfd78af_11"
 - "1.8.0--r43hdfd78af_12"
 - "1.8.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminahumanv2beadid.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminahumanv2beadid.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminahumanv2beadid.db", "latest": {"1.8.0--r44hdfd78af_13": "sha256:4b1a72d0b3d4be269d387e9a8e00abf1622cf20510e7cd76e972fced9e3f29e0"}, "tags": {"1.8.0--r41hdfd78af_9": "sha256:d2b82954b1ea50861a1207d1ce379c0fb0253c2488577b515837c2518031d0b8", "1.8.0--r42hdfd78af_10": "sha256:f268e23c549a6902be70b6f2e0eb3b7e1cdbc8f95c65f763cb350299bff37dcf", "1.8.0--r43hdfd78af_11": "sha256:8f2eaf8ce10ec3a9931faf5664bd7a4b897e5893dec4c895727df56177267690", "1.8.0--r43hdfd78af_12": "sha256:190ea831deb1eeaa2c3e64047a162143f61ffef5831e276261938b2c053d840f", "1.8.0--r44hdfd78af_13": "sha256:4b1a72d0b3d4be269d387e9a8e00abf1622cf20510e7cd76e972fced9e3f29e0"}, "docker": "quay.io/biocontainers/bioconductor-illuminahumanv2beadid.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminahumanv2beadid.db.
shpc-registry automated BioContainers addition for bioconductor-illuminahumanv2beadid.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanv2beadid.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanv2beadid.db:1.8.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminahumanv2beadid.db/1.8.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-illuminahumanv2beadid.db/1.8.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminahumanv2beadid.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanv2beadid.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanv2beadid.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminahumanv2beadid.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminahumanv2beadid.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminahumanv2beadid.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminahumanv2beadid.db

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