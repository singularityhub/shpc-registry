---
layout: container
name:  "quay.io/biocontainers/bioconductor-simlr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-simlr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-simlr/container.yaml"
updated_at: "2025-11-15 03:55:46.947357"
latest: "1.32.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-simlr"
aliases:
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "pyvenv"
 - "c89"
versions:
 - "1.8.1--r351hf484d3e_0"
 - "1.24.0--r42hc247a5b_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.16.0--r40h399db7b_1"
 - "1.14.0--r40h5f743cb_0"
 - "1.24.0--r42hf17093f_1"
 - "1.26.1--r43hf17093f_0"
 - "1.28.0--r43hf17093f_0"
 - "1.32.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-simlr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-simlr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-simlr", "latest": {"1.32.0--r44he5774e6_0": "sha256:d7a007c1324552c5a87ad36f6c67731bc0b50e2b2365f9119f7dcef21f94f8d1"}, "tags": {"1.8.1--r351hf484d3e_0": "sha256:acbe102efede6cb527b4fe0473ed667356ed8630c8b64bc43c4bd46b665834d3", "1.24.0--r42hc247a5b_0": "sha256:80daf9ac9dc0515cbca25085943edf9c65e496bacc512fa6d812745fe9c67a43", "1.20.0--r41hc247a5b_2": "sha256:85a4990aba7475386676dd91e200a7a0887cffa8466a7d118dfe06dcd118a22d", "1.18.0--r41h399db7b_0": "sha256:f1b8656c8fca04ebdc62a13cdcce5864d4e097b56b2fca232ab35d3a36cd46db", "1.16.0--r40h399db7b_1": "sha256:6c2a37dceb9a8699c1a99339bb1bfa18db782f54ef1e6e2e337dd95a0da340ff", "1.14.0--r40h5f743cb_0": "sha256:f0d8b8141fc85a05cc5c6cf6f8983cd004d7346fd5e33296591b377548347348", "1.24.0--r42hf17093f_1": "sha256:5b298e576a8243643308d8974aff85b799cc2485c65cb758a068f135f23e8442", "1.26.1--r43hf17093f_0": "sha256:5e74af4bc64e471d383a2c399bfe7a199162682ce2ce4f5ea6f28eddeecd253c", "1.28.0--r43hf17093f_0": "sha256:6234b16d46ae0507441a473451318b8ea8f4833dd72383de4d629a57222321ef", "1.32.0--r44he5774e6_0": "sha256:d7a007c1324552c5a87ad36f6c67731bc0b50e2b2365f9119f7dcef21f94f8d1"}, "docker": "quay.io/biocontainers/bioconductor-simlr", "aliases": {"2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv", "c89": "/usr/local/bin/c89"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-simlr.
shpc-registry automated BioContainers addition for bioconductor-simlr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-simlr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-simlr:1.32.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-simlr/1.32.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-simlr/1.32.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-simlr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simlr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simlr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-simlr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-simlr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-simlr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
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