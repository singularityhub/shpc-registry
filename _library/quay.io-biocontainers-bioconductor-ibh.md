---
layout: container
name:  "quay.io/biocontainers/bioconductor-ibh"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ibh/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ibh/container.yaml"
updated_at: "2024-09-26 10:57:59.110305"
latest: "1.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ibh"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ibh"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ibh", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ibh", "latest": {"1.50.0--r43hdfd78af_0": "sha256:e875f3a4e4840382cafc2acb8646f3df4272af50ee61f1b502c0552a153df763"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:97c0d38b3460c4bca7e37ae16dc0341c147ba0f73a35ebdacaac9ec41dc224cc", "1.46.0--r42hdfd78af_0": "sha256:f885ba8169608676fb0e0c37de7d2399f7890956fc26e50ef000dcf603fbd89b", "1.48.0--r43hdfd78af_0": "sha256:8e405788e39a8dee5ddb56ac1a906a14e347ff341ee1d795d94a18e89f170b17", "1.50.0--r43hdfd78af_0": "sha256:e875f3a4e4840382cafc2acb8646f3df4272af50ee61f1b502c0552a153df763"}, "docker": "quay.io/biocontainers/bioconductor-ibh"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ibh.
shpc-registry automated BioContainers addition for bioconductor-ibh
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ibh
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ibh:1.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ibh/1.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ibh/1.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ibh-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ibh-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ibh-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ibh-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ibh-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ibh-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ibh

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