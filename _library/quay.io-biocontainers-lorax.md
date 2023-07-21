---
layout: container
name:  "quay.io/biocontainers/lorax"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lorax/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lorax/container.yaml"
updated_at: "2023-07-21 03:05:30.073826"
latest: "0.3.7--h6b1aa3f_2"
container_url: "https://biocontainers.pro/tools/lorax"
aliases:
 - "lorax"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.7--ha41ced6_0"
 - "0.3.7--h2af1cb8_1"
 - "0.3.7--h6b1aa3f_2"
description: "singularity registry hpc automated addition for lorax"
config: {"url": "https://biocontainers.pro/tools/lorax", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lorax", "latest": {"0.3.7--h6b1aa3f_2": "sha256:82794481e34d5f1b0093198a0302e92cf41bc03c24b2c1f542f84477b2c570d7"}, "tags": {"0.3.7--ha41ced6_0": "sha256:e80e4088b20acddfb1ba595746d8917ca17664fab8ae16e5840961c8a6203140", "0.3.7--h2af1cb8_1": "sha256:0b4dfc4699abf80e94f12eeebaf1fdb312f0fed542522b2977f9b277d6eb0021", "0.3.7--h6b1aa3f_2": "sha256:82794481e34d5f1b0093198a0302e92cf41bc03c24b2c1f542f84477b2c570d7"}, "docker": "quay.io/biocontainers/lorax", "aliases": {"lorax": "/usr/local/bin/lorax", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lorax.
singularity registry hpc automated addition for lorax
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lorax
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lorax:0.3.7--h6b1aa3f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lorax/0.3.7--h6b1aa3f_2
$ module help quay.io/biocontainers/lorax/0.3.7--h6b1aa3f_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lorax-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lorax-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lorax-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lorax-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lorax-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lorax-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lorax

```bash
$ singularity exec <container> /usr/local/bin/lorax
$ podman run --it --rm --entrypoint /usr/local/bin/lorax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lorax   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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