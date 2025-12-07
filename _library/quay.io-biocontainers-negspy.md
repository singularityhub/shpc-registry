---
layout: container
name:  "quay.io/biocontainers/negspy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/negspy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/negspy/container.yaml"
updated_at: "2025-12-07 04:10:59.982384"
latest: "0.2.24--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/negspy"
aliases:
 - "chr_pos_to_genome_pos.py"
 - "create_chrominfo.py"
 - "make_triangular.py"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "0.2.24--pyh7e72e81_0"
description: "singularity registry hpc automated addition for negspy"
config: {"url": "https://biocontainers.pro/tools/negspy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for negspy", "latest": {"0.2.24--pyh7e72e81_0": "sha256:2fdf7711e7e6998933a2b88346c5fe082d457af09af2070a78dba9813faed3a7"}, "tags": {"0.2.24--pyh7e72e81_0": "sha256:2fdf7711e7e6998933a2b88346c5fe082d457af09af2070a78dba9813faed3a7"}, "docker": "quay.io/biocontainers/negspy", "aliases": {"chr_pos_to_genome_pos.py": "/usr/local/bin/chr_pos_to_genome_pos.py", "create_chrominfo.py": "/usr/local/bin/create_chrominfo.py", "make_triangular.py": "/usr/local/bin/make_triangular.py", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/negspy.
singularity registry hpc automated addition for negspy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/negspy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/negspy:0.2.24--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/negspy/0.2.24--pyh7e72e81_0
$ module help quay.io/biocontainers/negspy/0.2.24--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### negspy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### negspy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### negspy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### negspy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### negspy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### negspy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chr_pos_to_genome_pos.py

```bash
$ singularity exec <container> /usr/local/bin/chr_pos_to_genome_pos.py
$ podman run --it --rm --entrypoint /usr/local/bin/chr_pos_to_genome_pos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chr_pos_to_genome_pos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_chrominfo.py

```bash
$ singularity exec <container> /usr/local/bin/create_chrominfo.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_chrominfo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_chrominfo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_triangular.py

```bash
$ singularity exec <container> /usr/local/bin/make_triangular.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_triangular.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_triangular.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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