---
layout: container
name:  "quay.io/biocontainers/bioconductor-snagee"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snagee/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snagee/container.yaml"
updated_at: "2024-10-15 03:14:50.818671"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-snagee"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-snagee"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snagee", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snagee", "latest": {"1.42.0--r43hdfd78af_0": "sha256:59126bd5c7ea0b214cd9f375047d3887324a2f57b2d68dba4cf6c860457fa687"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:4db541f26a9b567d437068d9270e65d4924b2e5835ec7b0a73e74af85c21abaf", "1.38.0--r42hdfd78af_0": "sha256:3bbbde4c1d30801bf2b56e69c4b57ad6cf1ebe921677f1ac9c12369ee85f4b3b", "1.40.0--r43hdfd78af_0": "sha256:41b9db1b6978741c64ed440ad51030687dfea5fa6442414f35c993dc345721e0", "1.42.0--r43hdfd78af_0": "sha256:59126bd5c7ea0b214cd9f375047d3887324a2f57b2d68dba4cf6c860457fa687"}, "docker": "quay.io/biocontainers/bioconductor-snagee"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snagee.
shpc-registry automated BioContainers addition for bioconductor-snagee
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snagee
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snagee:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snagee/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-snagee/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snagee-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snagee-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snagee-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snagee-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snagee-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snagee-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-snagee

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