---
layout: container
name:  "quay.io/biocontainers/perl-velvetoptimiser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-velvetoptimiser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-velvetoptimiser/container.yaml"
updated_at: "2024-05-06 19:11:18.211152"
latest: "2.2.6--pl526_0"
container_url: "https://biocontainers.pro/tools/perl-velvetoptimiser"
aliases:
 - "VelvetOptimiser.pl"
 - "velvetg"
 - "velveth"
 - "gifecho"
 - "gifinto"
 - "gdlib-config"
 - "bam2bedgraph"
 - "bp_pairwise_kaks"
 - "bp_find-blast-matches.pl"
 - "t_coffee"
 - "baseml"
versions:
 - "2.2.6--pl526_0"
description: "shpc-registry automated BioContainers addition for perl-velvetoptimiser"
config: {"url": "https://biocontainers.pro/tools/perl-velvetoptimiser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-velvetoptimiser", "latest": {"2.2.6--pl526_0": "sha256:172b538aeeb671df7918d6f7db02f9782b4c39c7571c09a536d32098d022b231"}, "tags": {"2.2.6--pl526_0": "sha256:172b538aeeb671df7918d6f7db02f9782b4c39c7571c09a536d32098d022b231"}, "docker": "quay.io/biocontainers/perl-velvetoptimiser", "aliases": {"VelvetOptimiser.pl": "/usr/local/bin/VelvetOptimiser.pl", "velvetg": "/usr/local/bin/velvetg", "velveth": "/usr/local/bin/velveth", "gifecho": "/usr/local/bin/gifecho", "gifinto": "/usr/local/bin/gifinto", "gdlib-config": "/usr/local/bin/gdlib-config", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bp_pairwise_kaks": "/usr/local/bin/bp_pairwise_kaks", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "t_coffee": "/usr/local/bin/t_coffee", "baseml": "/usr/local/bin/baseml"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-velvetoptimiser.
shpc-registry automated BioContainers addition for perl-velvetoptimiser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-velvetoptimiser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-velvetoptimiser:2.2.6--pl526_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-velvetoptimiser/2.2.6--pl526_0
$ module help quay.io/biocontainers/perl-velvetoptimiser/2.2.6--pl526_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-velvetoptimiser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-velvetoptimiser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-velvetoptimiser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-velvetoptimiser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-velvetoptimiser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-velvetoptimiser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### VelvetOptimiser.pl

```bash
$ singularity exec <container> /usr/local/bin/VelvetOptimiser.pl
$ podman run --it --rm --entrypoint /usr/local/bin/VelvetOptimiser.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VelvetOptimiser.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velvetg

```bash
$ singularity exec <container> /usr/local/bin/velvetg
$ podman run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velveth

```bash
$ singularity exec <container> /usr/local/bin/velveth
$ podman run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifecho

```bash
$ singularity exec <container> /usr/local/bin/gifecho
$ podman run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifinto

```bash
$ singularity exec <container> /usr/local/bin/gifinto
$ podman run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t_coffee

```bash
$ singularity exec <container> /usr/local/bin/t_coffee
$ podman run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseml

```bash
$ singularity exec <container> /usr/local/bin/baseml
$ podman run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
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