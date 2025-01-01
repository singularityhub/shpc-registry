---
layout: container
name:  "quay.io/biocontainers/fusioncatcher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fusioncatcher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fusioncatcher/container.yaml"
updated_at: "2025-01-01 02:58:50.542976"
latest: "1.33--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/fusioncatcher"

versions:
 - "1.33--hdfd78af_3"
 - "1.33--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for fusioncatcher"
config: {"url": "https://biocontainers.pro/tools/fusioncatcher", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fusioncatcher", "latest": {"1.33--hdfd78af_4": "sha256:15a5b28a4f8e51bec6f2ec9038c3d22cf18263349de495bb24faf14ace488c1c"}, "tags": {"1.33--hdfd78af_3": "sha256:4dbd6ada2dd9f971182b9eb620ce7e936b7f459cbf59c57cb03cdbba1b95d376", "1.33--hdfd78af_4": "sha256:15a5b28a4f8e51bec6f2ec9038c3d22cf18263349de495bb24faf14ace488c1c"}, "docker": "quay.io/biocontainers/fusioncatcher"}
---

This module is a singularity container wrapper for quay.io/biocontainers/fusioncatcher.
shpc-registry automated BioContainers addition for fusioncatcher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fusioncatcher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fusioncatcher:1.33--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fusioncatcher/1.33--hdfd78af_4
$ module help quay.io/biocontainers/fusioncatcher/1.33--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fusioncatcher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fusioncatcher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fusioncatcher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fusioncatcher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fusioncatcher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fusioncatcher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### fusioncatcher

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