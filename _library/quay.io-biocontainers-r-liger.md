---
layout: container
name:  "quay.io/biocontainers/r-liger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-liger/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-liger/container.yaml"
updated_at: "2025-07-10 03:44:43.691117"
latest: "2.2.0--r44h165a49b_2"
container_url: "https://biocontainers.pro/tools/r-liger"
aliases:
 - "numba"
 - "pycc"
 - "mirror_server"
 - "mirror_server_stop"
 - "tqdm"
 - "f2py3.10"
 - "jaotc"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
versions:
 - "1.0.0--r41h3b3379e_1"
 - "1.0.0--r42h3b3379e_2"
 - "1.0.0--r42hd0834be_4"
 - "1.0.0--r43hd0834be_5"
 - "1.0.1--r43hd0834be_0"
 - "2.0.1--r43hd0834be_0"
 - "2.1.0--r43hd0834be_0"
 - "2.1.0--r44h165a49b_2"
 - "2.2.0--r44h165a49b_2"
description: "shpc-registry automated BioContainers addition for r-liger"
config: {"url": "https://biocontainers.pro/tools/r-liger", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-liger", "latest": {"2.2.0--r44h165a49b_2": "sha256:816a44fab7438f7d5d3af26f3908e47f532fbeac97e1d4c78ffa20ed17c9abc4"}, "tags": {"1.0.0--r41h3b3379e_1": "sha256:bc852d337eac33592fb472f8609d0cc5794e94c3026bf534fab5a0453410a786", "1.0.0--r42h3b3379e_2": "sha256:caefaf04cc1bdc4aec5b0bd3569a90f2cf00dbbb58623327dc26b63fc83caae4", "1.0.0--r42hd0834be_4": "sha256:3d9f715c4c84f67d953a43612119339025506f753556082b9b0accf0c2b2694c", "1.0.0--r43hd0834be_5": "sha256:f75b13940c477b784426515501e83f5aae9645bd1f350c2ca9120ff05a523db9", "1.0.1--r43hd0834be_0": "sha256:50d99cdc48b97b4e3b1609fa71f4ad7335cd451b3d086afbdb4af9fa9d0b0b4a", "2.0.1--r43hd0834be_0": "sha256:5fc71f7bb4f1e9ec03aef973154fb3413aa692b883be42b502865580476688aa", "2.1.0--r43hd0834be_0": "sha256:c3dc25491aedb6641ad826c681ce9e4fe4bc2f9bd468718ca649ac0de1c227da", "2.1.0--r44h165a49b_2": "sha256:9ec1c6f3e58465443518fcb66e681f664a99d9d7e9260f09a1d86472c3e7b8e1", "2.2.0--r44h165a49b_2": "sha256:816a44fab7438f7d5d3af26f3908e47f532fbeac97e1d4c78ffa20ed17c9abc4"}, "docker": "quay.io/biocontainers/r-liger", "aliases": {"numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "tqdm": "/usr/local/bin/tqdm", "f2py3.10": "/usr/local/bin/f2py3.10", "jaotc": "/usr/local/bin/jaotc", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-liger.
shpc-registry automated BioContainers addition for r-liger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-liger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-liger:2.2.0--r44h165a49b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-liger/2.2.0--r44h165a49b_2
$ module help quay.io/biocontainers/r-liger/2.2.0--r44h165a49b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-liger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-liger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-liger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-liger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-liger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-liger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server_stop

```bash
$ singularity exec <container> /usr/local/bin/mirror_server_stop
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
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