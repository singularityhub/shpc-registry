---
layout: container
name:  "quay.io/biocontainers/bioconductor-rontotools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rontotools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rontotools/container.yaml"
updated_at: "2025-09-13 03:15:47.601244"
latest: "2.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rontotools"

versions:
 - "2.8.0--r351_0"
 - "2.26.0--r42hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r41hdfd78af_0"
 - "2.18.0--r40hdfd78af_1"
 - "2.16.0--r40_0"
 - "2.28.0--r43hdfd78af_0"
 - "2.30.0--r43hdfd78af_0"
 - "2.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rontotools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rontotools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rontotools", "latest": {"2.34.0--r44hdfd78af_0": "sha256:326f0aa603e441fedbbf07aa598cd4c6f1e653e40072c5c312fd5f69f5cb3da1"}, "tags": {"2.8.0--r351_0": "sha256:bf4889379a827665540cea6226fe983b6f503819a8bea26009cd4613f94b4f72", "2.26.0--r42hdfd78af_0": "sha256:f76ede169bf15720767e8a8e43d92c6462e919801d0122d306a621507ead2921", "2.22.0--r41hdfd78af_0": "sha256:eebb492b17b2d679107b9f6a0ac61cff9361533711d1ceedd08c82e5850f9d68", "2.20.0--r41hdfd78af_0": "sha256:da115cb2a17ca1f130ae96346af2bf183f08aaea8e84215c5ea2a1039e5a8585", "2.18.0--r40hdfd78af_1": "sha256:2983ddf3f9aadbec1ae3e6eaab8da363f857d61a297b132b83ad5c85eb8d31da", "2.16.0--r40_0": "sha256:71d6866c463c7d7e079a5ab3b70785c6ec7b44345e1bccf2c6880004fcfe9e22", "2.28.0--r43hdfd78af_0": "sha256:fa022149240c8dfc4e96db31ff035bb31e34792d653a9f53899a836952555bff", "2.30.0--r43hdfd78af_0": "sha256:eae37da532a4a7441a42018f4b5822bc2977011ed2fa3cc1a40f50aac602c4d4", "2.34.0--r44hdfd78af_0": "sha256:326f0aa603e441fedbbf07aa598cd4c6f1e653e40072c5c312fd5f69f5cb3da1"}, "docker": "quay.io/biocontainers/bioconductor-rontotools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rontotools.
shpc-registry automated BioContainers addition for bioconductor-rontotools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rontotools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rontotools:2.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rontotools/2.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rontotools/2.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rontotools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rontotools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rontotools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rontotools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rontotools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rontotools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rontotools

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