---
layout: container
name:  "quay.io/biocontainers/bioconductor-norce"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-norce/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-norce/container.yaml"
updated_at: "2023-05-23 02:46:09.102280"
latest: "1.10.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-norce"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-norce"
config: {"url": "https://biocontainers.pro/tools/bioconductor-norce", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-norce", "latest": {"1.10.0--r42hdfd78af_0": "sha256:69892493bbe0a8a7699b7f26e859dc7709c1972d7d73a4797a5a5695b04b0e1c"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:f68861adeda4b782b2c81a40473535d389364284093d921d346ad8e8809b9a8a", "1.10.0--r42hdfd78af_0": "sha256:69892493bbe0a8a7699b7f26e859dc7709c1972d7d73a4797a5a5695b04b0e1c"}, "docker": "quay.io/biocontainers/bioconductor-norce"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-norce.
shpc-registry automated BioContainers addition for bioconductor-norce
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-norce
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-norce:1.10.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-norce/1.10.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-norce/1.10.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-norce-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-norce-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-norce-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-norce-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-norce-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-norce-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-norce

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