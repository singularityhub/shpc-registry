---
layout: container
name:  "quay.io/biocontainers/staphscope-mge-data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/staphscope-mge-data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/staphscope-mge-data/container.yaml"
updated_at: "2026-10-11 09:13:45.497689"
latest: "2.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/staphscope-mge-data"

versions:
 - "2.0.0--hdfd78af_0"
description: "singularity registry hpc automated addition for staphscope-mge-data"
config: {"url": "https://biocontainers.pro/tools/staphscope-mge-data", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for staphscope-mge-data", "latest": {"2.0.0--hdfd78af_0": "sha256:b527acad47e25d6c1d5141b5faa4e1eae2c727987be681e32e6e90a57b7d676f"}, "tags": {"2.0.0--hdfd78af_0": "sha256:b527acad47e25d6c1d5141b5faa4e1eae2c727987be681e32e6e90a57b7d676f"}, "docker": "quay.io/biocontainers/staphscope-mge-data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/staphscope-mge-data.
singularity registry hpc automated addition for staphscope-mge-data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/staphscope-mge-data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/staphscope-mge-data:2.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/staphscope-mge-data/2.0.0--hdfd78af_0
$ module help quay.io/biocontainers/staphscope-mge-data/2.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### staphscope-mge-data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### staphscope-mge-data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### staphscope-mge-data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### staphscope-mge-data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### staphscope-mge-data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### staphscope-mge-data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### staphscope-mge-data

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