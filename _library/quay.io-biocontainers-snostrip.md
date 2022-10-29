---
layout: container
name:  "quay.io/biocontainers/snostrip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snostrip/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/snostrip/container.yaml"
updated_at: "2022-10-29 05:40:14.740081"
latest: "2.0.2--pl5321h87f3376_4"
container_url: "https://biocontainers.pro/tools/snostrip"
aliases:
 - "snoStrip.pl"
 - "2to3-3.9"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "Kinfold"
 - "RNA2Dfold"
 - "RNALalifold"
 - "RNALfold"
 - "RNAPKplex"
 - "RNAaliduplex"
 - "RNAalifold"
versions:
 - "2.0.2--pl5321h87f3376_4"
description: "shpc-registry automated BioContainers addition for snostrip"
config: {"url": "https://biocontainers.pro/tools/snostrip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snostrip", "latest": {"2.0.2--pl5321h87f3376_4": "sha256:a105846a2ce12c8bc07be7c3ca2925fa577ae281c5d5b20df440a6bb5f2623bb"}, "tags": {"2.0.2--pl5321h87f3376_4": "sha256:a105846a2ce12c8bc07be7c3ca2925fa577ae281c5d5b20df440a6bb5f2623bb"}, "docker": "quay.io/biocontainers/snostrip", "aliases": {"snoStrip.pl": "/usr/local/bin/snoStrip.pl", "2to3-3.9": "/usr/local/bin/2to3-3.9", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "Kinfold": "/usr/local/bin/Kinfold", "RNA2Dfold": "/usr/local/bin/RNA2Dfold", "RNALalifold": "/usr/local/bin/RNALalifold", "RNALfold": "/usr/local/bin/RNALfold", "RNAPKplex": "/usr/local/bin/RNAPKplex", "RNAaliduplex": "/usr/local/bin/RNAaliduplex", "RNAalifold": "/usr/local/bin/RNAalifold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snostrip.
shpc-registry automated BioContainers addition for snostrip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snostrip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snostrip:2.0.2--pl5321h87f3376_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snostrip/2.0.2--pl5321h87f3376_4
$ module help quay.io/biocontainers/snostrip/2.0.2--pl5321h87f3376_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snostrip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snostrip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snostrip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snostrip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snostrip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snostrip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snoStrip.pl

```bash
$ singularity exec <container> /usr/local/bin/snoStrip.pl
$ podman run --it --rm --entrypoint /usr/local/bin/snoStrip.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snoStrip.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### Kinfold

```bash
$ singularity exec <container> /usr/local/bin/Kinfold
$ podman run --it --rm --entrypoint /usr/local/bin/Kinfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Kinfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNA2Dfold

```bash
$ singularity exec <container> /usr/local/bin/RNA2Dfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNALalifold

```bash
$ singularity exec <container> /usr/local/bin/RNALalifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNALfold

```bash
$ singularity exec <container> /usr/local/bin/RNALfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNALfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNALfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAPKplex

```bash
$ singularity exec <container> /usr/local/bin/RNAPKplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAPKplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAPKplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAaliduplex

```bash
$ singularity exec <container> /usr/local/bin/RNAaliduplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAaliduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAaliduplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAalifold

```bash
$ singularity exec <container> /usr/local/bin/RNAalifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
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