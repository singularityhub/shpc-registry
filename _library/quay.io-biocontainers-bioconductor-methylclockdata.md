---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylclockdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylclockdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylclockdata/container.yaml"
updated_at: "2023-06-05 03:47:26.311292"
latest: "1.6.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylclockdata"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylclockdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylclockdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylclockdata", "latest": {"1.6.0--r42hdfd78af_0": "sha256:b00044a226c002ecdbbc56cc9c02a644362fe78df895ef8d15937e215a6d66e1"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:0e757a85b4daca6b197460d815eff2599186fe73ae1363f5b528fe3f3bca310a", "1.6.0--r42hdfd78af_0": "sha256:b00044a226c002ecdbbc56cc9c02a644362fe78df895ef8d15937e215a6d66e1"}, "docker": "quay.io/biocontainers/bioconductor-methylclockdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylclockdata.
shpc-registry automated BioContainers addition for bioconductor-methylclockdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylclockdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylclockdata:1.6.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylclockdata/1.6.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methylclockdata/1.6.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylclockdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylclockdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylclockdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylclockdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylclockdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylclockdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylclockdata

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