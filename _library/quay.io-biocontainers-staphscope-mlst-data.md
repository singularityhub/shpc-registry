---
layout: container
name:  "quay.io/biocontainers/staphscope-mlst-data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/staphscope-mlst-data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/staphscope-mlst-data/container.yaml"
updated_at: "2026-07-01 07:04:54.618080"
latest: "1.2.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/staphscope-mlst-data"

versions:
 - "1.2.0--hdfd78af_1"
description: "singularity registry hpc automated addition for staphscope-mlst-data"
config: {"url": "https://biocontainers.pro/tools/staphscope-mlst-data", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for staphscope-mlst-data", "latest": {"1.2.0--hdfd78af_1": "sha256:34ad4590c17de910eaa085cab51fff3599ca18bcac730a6099757ba7470c72f0"}, "tags": {"1.2.0--hdfd78af_1": "sha256:34ad4590c17de910eaa085cab51fff3599ca18bcac730a6099757ba7470c72f0"}, "docker": "quay.io/biocontainers/staphscope-mlst-data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/staphscope-mlst-data.
singularity registry hpc automated addition for staphscope-mlst-data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/staphscope-mlst-data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/staphscope-mlst-data:1.2.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/staphscope-mlst-data/1.2.0--hdfd78af_1
$ module help quay.io/biocontainers/staphscope-mlst-data/1.2.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### staphscope-mlst-data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### staphscope-mlst-data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### staphscope-mlst-data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### staphscope-mlst-data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### staphscope-mlst-data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### staphscope-mlst-data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### staphscope-mlst-data

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