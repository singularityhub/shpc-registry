---
layout: container
name:  "quay.io/biocontainers/tandem-genotypes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tandem-genotypes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tandem-genotypes/container.yaml"
updated_at: "2024-01-11 02:50:19.029086"
latest: "1.9.1--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/tandem-genotypes"
aliases:
 - "tandem-genotypes"
 - "tandem-genotypes-join"
 - "tandem-genotypes-merge"
 - "tandem-genotypes-plot"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.9.0--pyh5e36f6f_0"
 - "1.9.1--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for tandem-genotypes"
config: {"url": "https://biocontainers.pro/tools/tandem-genotypes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tandem-genotypes", "latest": {"1.9.1--pyh7cba7a3_0": "sha256:08a23fec5aabf0d38bbb1aa1a7cf9ded74fd4d612aca5bbdf14edf387d779bbd"}, "tags": {"1.9.0--pyh5e36f6f_0": "sha256:b19f29fbaafa20ad5dcbb7982ad21ea387f489c31fa11eee17879664411ec26c", "1.9.1--pyh7cba7a3_0": "sha256:08a23fec5aabf0d38bbb1aa1a7cf9ded74fd4d612aca5bbdf14edf387d779bbd"}, "docker": "quay.io/biocontainers/tandem-genotypes", "aliases": {"tandem-genotypes": "/usr/local/bin/tandem-genotypes", "tandem-genotypes-join": "/usr/local/bin/tandem-genotypes-join", "tandem-genotypes-merge": "/usr/local/bin/tandem-genotypes-merge", "tandem-genotypes-plot": "/usr/local/bin/tandem-genotypes-plot", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tandem-genotypes.
shpc-registry automated BioContainers addition for tandem-genotypes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tandem-genotypes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tandem-genotypes:1.9.1--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tandem-genotypes/1.9.1--pyh7cba7a3_0
$ module help quay.io/biocontainers/tandem-genotypes/1.9.1--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tandem-genotypes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tandem-genotypes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tandem-genotypes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tandem-genotypes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tandem-genotypes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tandem-genotypes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tandem-genotypes

```bash
$ singularity exec <container> /usr/local/bin/tandem-genotypes
$ podman run --it --rm --entrypoint /usr/local/bin/tandem-genotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tandem-genotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tandem-genotypes-join

```bash
$ singularity exec <container> /usr/local/bin/tandem-genotypes-join
$ podman run --it --rm --entrypoint /usr/local/bin/tandem-genotypes-join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tandem-genotypes-join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tandem-genotypes-merge

```bash
$ singularity exec <container> /usr/local/bin/tandem-genotypes-merge
$ podman run --it --rm --entrypoint /usr/local/bin/tandem-genotypes-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tandem-genotypes-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tandem-genotypes-plot

```bash
$ singularity exec <container> /usr/local/bin/tandem-genotypes-plot
$ podman run --it --rm --entrypoint /usr/local/bin/tandem-genotypes-plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tandem-genotypes-plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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