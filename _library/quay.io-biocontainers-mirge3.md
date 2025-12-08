---
layout: container
name:  "quay.io/biocontainers/mirge3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirge3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mirge3/container.yaml"
updated_at: "2025-12-08 03:57:04.512464"
latest: "0.1.4--pyh7cba7a3_1"
container_url: "https://biocontainers.pro/tools/mirge3"
aliases:
 - "miRge3.0"
 - "RNAdos"
 - "x86_64-conda_cos7-linux-gnu-ld"
 - "cutadapt"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
versions:
 - "0.1.1--pyh7cba7a3_0"
 - "0.1.2--pyh7cba7a3_0"
 - "0.1.4--pyh7cba7a3_0"
 - "0.1.4--pyh7cba7a3_1"
description: "shpc-registry automated BioContainers addition for mirge3"
config: {"url": "https://biocontainers.pro/tools/mirge3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mirge3", "latest": {"0.1.4--pyh7cba7a3_1": "sha256:c78ca6e0e49c69bc3be7eacd92cf175ecac01666d5e1a3be2373a43e12372202"}, "tags": {"0.1.1--pyh7cba7a3_0": "sha256:d67c441abb353724e1496973852b3ab0b52e1965cd1067d8ee60b634b70c53e4", "0.1.2--pyh7cba7a3_0": "sha256:ce4d7749521ddb5e67814144b40c9978d23b9256f455e1025332f8c51f2ca209", "0.1.4--pyh7cba7a3_0": "sha256:0d4e8aabad71ba31a0b864c4bc13406df03d7e2175521c697f68bd08605ff80e", "0.1.4--pyh7cba7a3_1": "sha256:c78ca6e0e49c69bc3be7eacd92cf175ecac01666d5e1a3be2373a43e12372202"}, "docker": "quay.io/biocontainers/mirge3", "aliases": {"miRge3.0": "/usr/local/bin/miRge3.0", "RNAdos": "/usr/local/bin/RNAdos", "x86_64-conda_cos7-linux-gnu-ld": "/usr/local/bin/x86_64-conda_cos7-linux-gnu-ld", "cutadapt": "/usr/local/bin/cutadapt", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirge3.
shpc-registry automated BioContainers addition for mirge3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirge3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirge3:0.1.4--pyh7cba7a3_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirge3/0.1.4--pyh7cba7a3_1
$ module help quay.io/biocontainers/mirge3/0.1.4--pyh7cba7a3_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirge3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirge3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirge3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirge3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirge3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirge3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### miRge3.0

```bash
$ singularity exec <container> /usr/local/bin/miRge3.0
$ podman run --it --rm --entrypoint /usr/local/bin/miRge3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miRge3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdos

```bash
$ singularity exec <container> /usr/local/bin/RNAdos
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda_cos7-linux-gnu-ld

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseDists

```bash
$ singularity exec <container> /usr/local/bin/AnalyseDists
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseSeqs

```bash
$ singularity exec <container> /usr/local/bin/AnalyseSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAlocmin

```bash
$ singularity exec <container> /usr/local/bin/RNAlocmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNApvmin

```bash
$ singularity exec <container> /usr/local/bin/RNApvmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2ct

```bash
$ singularity exec <container> /usr/local/bin/b2ct
$ podman run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2db

```bash
$ singularity exec <container> /usr/local/bin/ct2db
$ podman run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinwalker

```bash
$ singularity exec <container> /usr/local/bin/kinwalker
$ podman run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
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