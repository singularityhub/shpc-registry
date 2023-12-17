---
layout: container
name:  "quay.io/biocontainers/cosi2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cosi2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cosi2/container.yaml"
updated_at: "2023-12-17 03:11:08.341091"
latest: "2.3.0rc4--py27h2d50403_1"
container_url: "https://biocontainers.pro/tools/cosi2"
aliases:
 - "coalescent"
 - "get_recomap"
 - "recomap_hapmap2"
 - "recosimulate"
 - "sample_stats_extra"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.3.0rc4--py27h2d50403_1"
description: "shpc-registry automated BioContainers addition for cosi2"
config: {"url": "https://biocontainers.pro/tools/cosi2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cosi2", "latest": {"2.3.0rc4--py27h2d50403_1": "sha256:b8372c183135e0549f4f17aa2f7f546b58493236f0ac6352d6f7cfe57b4a9779"}, "tags": {"2.3.0rc4--py27h2d50403_1": "sha256:b8372c183135e0549f4f17aa2f7f546b58493236f0ac6352d6f7cfe57b4a9779"}, "docker": "quay.io/biocontainers/cosi2", "aliases": {"coalescent": "/usr/local/bin/coalescent", "get_recomap": "/usr/local/bin/get_recomap", "recomap_hapmap2": "/usr/local/bin/recomap_hapmap2", "recosimulate": "/usr/local/bin/recosimulate", "sample_stats_extra": "/usr/local/bin/sample_stats_extra", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cosi2.
shpc-registry automated BioContainers addition for cosi2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cosi2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cosi2:2.3.0rc4--py27h2d50403_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cosi2/2.3.0rc4--py27h2d50403_1
$ module help quay.io/biocontainers/cosi2/2.3.0rc4--py27h2d50403_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cosi2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cosi2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cosi2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cosi2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cosi2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cosi2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coalescent

```bash
$ singularity exec <container> /usr/local/bin/coalescent
$ podman run --it --rm --entrypoint /usr/local/bin/coalescent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coalescent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_recomap

```bash
$ singularity exec <container> /usr/local/bin/get_recomap
$ podman run --it --rm --entrypoint /usr/local/bin/get_recomap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_recomap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### recomap_hapmap2

```bash
$ singularity exec <container> /usr/local/bin/recomap_hapmap2
$ podman run --it --rm --entrypoint /usr/local/bin/recomap_hapmap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recomap_hapmap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### recosimulate

```bash
$ singularity exec <container> /usr/local/bin/recosimulate
$ podman run --it --rm --entrypoint /usr/local/bin/recosimulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recosimulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sample_stats_extra

```bash
$ singularity exec <container> /usr/local/bin/sample_stats_extra
$ podman run --it --rm --entrypoint /usr/local/bin/sample_stats_extra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sample_stats_extra   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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