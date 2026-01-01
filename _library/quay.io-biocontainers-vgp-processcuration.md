---
layout: container
name:  "quay.io/biocontainers/vgp-processcuration"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vgp-processcuration/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vgp-processcuration/container.yaml"
updated_at: "2026-01-01 07:03:12.318201"
latest: "1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/vgp-processcuration"
aliases:
 - "chromosome_assignment"
 - "chromosome_assignment.py"
 - "sak_generation"
 - "sak_generation.py"
 - "split_agp"
 - "split_agp.py"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "natsort"
 - "numpy-config"
versions:
 - "1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for vgp-processcuration"
config: {"url": "https://biocontainers.pro/tools/vgp-processcuration", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vgp-processcuration", "latest": {"1.0--pyhdfd78af_0": "sha256:7ec76f6fff97e40ff3d656c7454f45f8a684e058a961c7009c414819ee29d0df"}, "tags": {"1.0--pyhdfd78af_0": "sha256:7ec76f6fff97e40ff3d656c7454f45f8a684e058a961c7009c414819ee29d0df"}, "docker": "quay.io/biocontainers/vgp-processcuration", "aliases": {"chromosome_assignment": "/usr/local/bin/chromosome_assignment", "chromosome_assignment.py": "/usr/local/bin/chromosome_assignment.py", "sak_generation": "/usr/local/bin/sak_generation", "sak_generation.py": "/usr/local/bin/sak_generation.py", "split_agp": "/usr/local/bin/split_agp", "split_agp.py": "/usr/local/bin/split_agp.py", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "natsort": "/usr/local/bin/natsort", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vgp-processcuration.
singularity registry hpc automated addition for vgp-processcuration
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vgp-processcuration
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vgp-processcuration:1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vgp-processcuration/1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/vgp-processcuration/1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vgp-processcuration-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vgp-processcuration-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vgp-processcuration-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vgp-processcuration-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vgp-processcuration-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vgp-processcuration-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chromosome_assignment

```bash
$ singularity exec <container> /usr/local/bin/chromosome_assignment
$ podman run --it --rm --entrypoint /usr/local/bin/chromosome_assignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chromosome_assignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chromosome_assignment.py

```bash
$ singularity exec <container> /usr/local/bin/chromosome_assignment.py
$ podman run --it --rm --entrypoint /usr/local/bin/chromosome_assignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chromosome_assignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sak_generation

```bash
$ singularity exec <container> /usr/local/bin/sak_generation
$ podman run --it --rm --entrypoint /usr/local/bin/sak_generation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sak_generation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sak_generation.py

```bash
$ singularity exec <container> /usr/local/bin/sak_generation.py
$ podman run --it --rm --entrypoint /usr/local/bin/sak_generation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sak_generation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_agp

```bash
$ singularity exec <container> /usr/local/bin/split_agp
$ podman run --it --rm --entrypoint /usr/local/bin/split_agp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_agp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_agp.py

```bash
$ singularity exec <container> /usr/local/bin/split_agp.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_agp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_agp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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