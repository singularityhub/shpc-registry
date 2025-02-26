---
layout: container
name:  "quay.io/biocontainers/sequenza-utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sequenza-utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sequenza-utils/container.yaml"
updated_at: "2025-02-26 02:57:40.013686"
latest: "3.0.0--py311h8ddd9a4_8"
container_url: "https://biocontainers.pro/tools/sequenza-utils"
aliases:
 - "sequenza-utils"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "ace2sam"
versions:
 - "3.0.0--py27h95a95ce_5"
 - "3.0.0--py38hcbe9525_6"
 - "3.0.0--py310h068649b_6"
 - "3.0.0--py312h719dbc0_7"
 - "3.0.0--py311h8ddd9a4_8"
description: "shpc-registry automated BioContainers addition for sequenza-utils"
config: {"url": "https://biocontainers.pro/tools/sequenza-utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sequenza-utils", "latest": {"3.0.0--py311h8ddd9a4_8": "sha256:6114c8d64cf99a3eaa250c3d9292901531277cb2fa607d269f4fc1d7a2f0d4bf"}, "tags": {"3.0.0--py27h95a95ce_5": "sha256:cd725cb5730ad0ea7536e0f5231d4462a83d4691f2c23ea63089fd9aaeaaffd2", "3.0.0--py38hcbe9525_6": "sha256:305f7f3b3093eb630b0343a4a8d5c7cb619608903455f1dfbebdc597a1443d1d", "3.0.0--py310h068649b_6": "sha256:c747e187a8eb0719abbaf979c6279e95c5f88222b5c9e3f011753a7ec98e5bdd", "3.0.0--py312h719dbc0_7": "sha256:ebd76434afe2021a677f998cc6db59cb8f79547235a0133fbdd1bda567907d2d", "3.0.0--py311h8ddd9a4_8": "sha256:6114c8d64cf99a3eaa250c3d9292901531277cb2fa607d269f4fc1d7a2f0d4bf"}, "docker": "quay.io/biocontainers/sequenza-utils", "aliases": {"sequenza-utils": "/usr/local/bin/sequenza-utils", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "ace2sam": "/usr/local/bin/ace2sam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sequenza-utils.
shpc-registry automated BioContainers addition for sequenza-utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sequenza-utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sequenza-utils:3.0.0--py311h8ddd9a4_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sequenza-utils/3.0.0--py311h8ddd9a4_8
$ module help quay.io/biocontainers/sequenza-utils/3.0.0--py311h8ddd9a4_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sequenza-utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sequenza-utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sequenza-utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sequenza-utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sequenza-utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sequenza-utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sequenza-utils

```bash
$ singularity exec <container> /usr/local/bin/sequenza-utils
$ podman run --it --rm --entrypoint /usr/local/bin/sequenza-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequenza-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
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