---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodbncbi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodbncbi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodbncbi/container.yaml"
updated_at: "2024-06-15 02:58:24.785317"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biodbncbi"

versions:
 - "1.2.0--r42hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-biodbncbi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodbncbi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-biodbncbi", "latest": {"1.6.0--r43hdfd78af_0": "sha256:de48abadc6a694694766376aa43b946a37c04aff8a987404253c667da1d54825"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:16e708bb1e2220c6c4ec0ce2ff6d65d610493f1d6735a4658307f2c62581326d", "1.4.0--r43hdfd78af_0": "sha256:e7af0953bea7aaac2a7265fe9fbbad4ddccfa58eba3ff043918cae13190cc7f0", "1.6.0--r43hdfd78af_0": "sha256:de48abadc6a694694766376aa43b946a37c04aff8a987404253c667da1d54825"}, "docker": "quay.io/biocontainers/bioconductor-biodbncbi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodbncbi.
singularity registry hpc automated addition for bioconductor-biodbncbi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbncbi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbncbi:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodbncbi/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biodbncbi/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodbncbi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbncbi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbncbi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodbncbi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodbncbi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodbncbi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodbncbi

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