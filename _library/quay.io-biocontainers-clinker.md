---
layout: container
name:  "quay.io/biocontainers/clinker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clinker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clinker/container.yaml"
updated_at: "2024-07-16 02:55:54.084097"
latest: "1.33--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/clinker"

versions:
 - "1.32--hdfd78af_2"
 - "1.33--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for clinker"
config: {"url": "https://biocontainers.pro/tools/clinker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clinker", "latest": {"1.33--hdfd78af_0": "sha256:665356100d94244dfe9de83178540649132b873aead17a9bcc88ced676b6951e"}, "tags": {"1.32--hdfd78af_2": "sha256:9d04b168a684388faf9e666a721269eb2aee71979f51a09a5b0b31de56ecbbfe", "1.33--hdfd78af_0": "sha256:665356100d94244dfe9de83178540649132b873aead17a9bcc88ced676b6951e"}, "docker": "quay.io/biocontainers/clinker"}
---

This module is a singularity container wrapper for quay.io/biocontainers/clinker.
shpc-registry automated BioContainers addition for clinker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clinker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clinker:1.33--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clinker/1.33--hdfd78af_0
$ module help quay.io/biocontainers/clinker/1.33--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clinker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clinker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clinker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clinker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clinker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clinker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### clinker

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