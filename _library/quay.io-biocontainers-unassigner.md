---
layout: container
name:  "quay.io/biocontainers/unassigner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unassigner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unassigner/container.yaml"
updated_at: "2024-06-19 02:40:40.185961"
latest: "1.0.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/unassigner"
aliases:
 - "count_mismatches"
 - "pctid_ani_sample"
 - "trimragged"
 - "unassign"
 - "unassigner"
 - "vsearch"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "1.0.0--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for unassigner"
config: {"url": "https://biocontainers.pro/tools/unassigner", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for unassigner", "latest": {"1.0.0--pyh7cba7a3_0": "sha256:d706fb0fbd1f1c06161f3a1b1b090a701795c4af214ffe452ae3ed74a98a9b26"}, "tags": {"1.0.0--pyh7cba7a3_0": "sha256:d706fb0fbd1f1c06161f3a1b1b090a701795c4af214ffe452ae3ed74a98a9b26"}, "docker": "quay.io/biocontainers/unassigner", "aliases": {"count_mismatches": "/usr/local/bin/count_mismatches", "pctid_ani_sample": "/usr/local/bin/pctid_ani_sample", "trimragged": "/usr/local/bin/trimragged", "unassign": "/usr/local/bin/unassign", "unassigner": "/usr/local/bin/unassigner", "vsearch": "/usr/local/bin/vsearch", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unassigner.
singularity registry hpc automated addition for unassigner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unassigner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unassigner:1.0.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unassigner/1.0.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/unassigner/1.0.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unassigner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unassigner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unassigner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unassigner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unassigner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unassigner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### count_mismatches

```bash
$ singularity exec <container> /usr/local/bin/count_mismatches
$ podman run --it --rm --entrypoint /usr/local/bin/count_mismatches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count_mismatches   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pctid_ani_sample

```bash
$ singularity exec <container> /usr/local/bin/pctid_ani_sample
$ podman run --it --rm --entrypoint /usr/local/bin/pctid_ani_sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pctid_ani_sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimragged

```bash
$ singularity exec <container> /usr/local/bin/trimragged
$ podman run --it --rm --entrypoint /usr/local/bin/trimragged   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimragged   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unassign

```bash
$ singularity exec <container> /usr/local/bin/unassign
$ podman run --it --rm --entrypoint /usr/local/bin/unassign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unassign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unassigner

```bash
$ singularity exec <container> /usr/local/bin/unassigner
$ podman run --it --rm --entrypoint /usr/local/bin/unassigner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unassigner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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