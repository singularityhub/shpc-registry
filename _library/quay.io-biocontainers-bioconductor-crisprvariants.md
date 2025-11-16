---
layout: container
name:  "quay.io/biocontainers/bioconductor-crisprvariants"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-crisprvariants/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-crisprvariants/container.yaml"
updated_at: "2025-11-16 03:46:23.284899"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-crisprvariants"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.14.0--r36_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-crisprvariants"
config: {"url": "https://biocontainers.pro/tools/bioconductor-crisprvariants", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-crisprvariants", "latest": {"1.30.0--r43hdfd78af_0": "sha256:17aaed2410fa5931a707fc2615b2bd3336e35a58d23a04ce2098160b5bea83ec"}, "tags": {"1.8.0--r351_0": "sha256:57d93e2b3196b6f7a6c735e66d7f3712faedba78f39de35d78129acbd074be87", "1.22.0--r41hdfd78af_0": "sha256:f94d00a99af7c1fd9df61122dd2533a5b4529f6af31ff684cea17497cca3b4af", "1.20.0--r41hdfd78af_0": "sha256:92fcb92c61e633bba3cec28a34364ff53967e8478c5c8d33d945f287dd162992", "1.18.0--r40hdfd78af_1": "sha256:477abec3a093da1a79c05f3fc52fcacebbace914c9ff21a54e409074e612f4bd", "1.16.0--r40_0": "sha256:b1950667ebf895c6ed415396cd2d5d1a5e0b4a1a4c6a9f77b03f6f38a513cbd9", "1.14.0--r36_0": "sha256:e09d390dbd0e132a9059843e768893cf3a05c2d5ab83d6c238cbcc069f9bb130", "1.26.0--r42hdfd78af_0": "sha256:d4b262dec283b2c470a6ee1e9b62a3ecbc289dd0aeed91bd8b0d884347b28083", "1.28.0--r43hdfd78af_0": "sha256:b4bd1d1a6a37c03f5e99aa578f1b7d2831b1d2d8445141edbfe8add19af631e4", "1.30.0--r43hdfd78af_0": "sha256:17aaed2410fa5931a707fc2615b2bd3336e35a58d23a04ce2098160b5bea83ec"}, "docker": "quay.io/biocontainers/bioconductor-crisprvariants", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-crisprvariants.
shpc-registry automated BioContainers addition for bioconductor-crisprvariants
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-crisprvariants
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-crisprvariants:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-crisprvariants/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-crisprvariants/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-crisprvariants-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-crisprvariants-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-crisprvariants-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-crisprvariants-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-crisprvariants-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-crisprvariants-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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