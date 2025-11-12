---
layout: container
name:  "quay.io/biocontainers/bioconductor-pi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pi/container.yaml"
updated_at: "2025-11-12 03:27:19.353783"
latest: "2.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pi"

versions:
 - "2.6.0--r41hdfd78af_0"
 - "2.10.0--r42hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
 - "2.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pi", "latest": {"2.14.0--r43hdfd78af_0": "sha256:d826341665b5f93c2008863f3968200b79b6a9e19e9e661863f3f472cc092ebf"}, "tags": {"2.6.0--r41hdfd78af_0": "sha256:8daecc7bc02198e662ce6dff95324b2e453a72e54d03795948c478ebac0ff343", "2.10.0--r42hdfd78af_0": "sha256:aeb07918cfec0d1dbb3eb903cf77a6242a66e23c3ee840330f85c9891c9319ab", "2.12.0--r43hdfd78af_0": "sha256:95e52f9ab7c94835c31db14bd9b29110ed55bd50c098669721b36fb2fa6239f4", "2.14.0--r43hdfd78af_0": "sha256:d826341665b5f93c2008863f3968200b79b6a9e19e9e661863f3f472cc092ebf"}, "docker": "quay.io/biocontainers/bioconductor-pi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pi.
shpc-registry automated BioContainers addition for bioconductor-pi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pi:2.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pi/2.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pi/2.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pi

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