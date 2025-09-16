---
layout: container
name:  "quay.io/biocontainers/bioconductor-screpertoire"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-screpertoire/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-screpertoire/container.yaml"
updated_at: "2025-09-16 03:39:30.635859"
latest: "2.2.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-screpertoire"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "2.2.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-screpertoire"
config: {"url": "https://biocontainers.pro/tools/bioconductor-screpertoire", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-screpertoire", "latest": {"2.2.0--r44he5774e6_0": "sha256:b775b5cde5d4dd2119703e4a78a1b8ecd3097c10cabb62a2eb12075d6da283ab"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:cea0fd8c6f3618cbfc24cd1d3f6971dbf51b59e32ea8c716728e3f5f4372a4dd", "1.8.0--r42hdfd78af_0": "sha256:a196af18e3bf0bf7a40dfda4fccb96baf44ce3a8406b6315dc1235f6b51088df", "1.10.0--r43hdfd78af_0": "sha256:05f431ebc7cf8cd984104645b506c352aaca3bd228112eb65bb64aebf31a4906", "1.12.0--r43hdfd78af_0": "sha256:d25ebd0044a23bf8df5fe34200934036b4bfb15076654c6532328bfc35589495", "2.2.0--r44he5774e6_0": "sha256:b775b5cde5d4dd2119703e4a78a1b8ecd3097c10cabb62a2eb12075d6da283ab"}, "docker": "quay.io/biocontainers/bioconductor-screpertoire"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-screpertoire.
shpc-registry automated BioContainers addition for bioconductor-screpertoire
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-screpertoire
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-screpertoire:2.2.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-screpertoire/2.2.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-screpertoire/2.2.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-screpertoire-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-screpertoire-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-screpertoire-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-screpertoire-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-screpertoire-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-screpertoire-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-screpertoire

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