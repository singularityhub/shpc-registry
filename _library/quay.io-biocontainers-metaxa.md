---
layout: container
name:  "quay.io/biocontainers/metaxa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaxa/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metaxa/container.yaml"
updated_at: "2022-10-29 05:42:00.205793"
latest: "2.2.3--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/metaxa"
aliases:
 - "metaxa2"
 - "metaxa2_c"
 - "metaxa2_dbb"
 - "metaxa2_dc"
 - "metaxa2_install_database"
 - "metaxa2_rf"
 - "metaxa2_si"
 - "metaxa2_ttt"
 - "metaxa2_uc"
 - "metaxa2_x"
 - "2to3-3.10"
 - "alimask"
 - "blast_formatter"
 - "blastdb_aliastool"
 - "blastdbcheck"
 - "blastdbcmd"
 - "blastdbcp"
 - "blastn"
 - "blastp"
 - "blastx"
versions:
 - "2.2.3--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for metaxa"
config: {"url": "https://biocontainers.pro/tools/metaxa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaxa", "latest": {"2.2.3--pl5321hdfd78af_1": "sha256:9bfaf876eef8986005b96d84b6f6745caaaedf539991f0eb1f69d51f6da1167e"}, "tags": {"2.2.3--pl5321hdfd78af_1": "sha256:9bfaf876eef8986005b96d84b6f6745caaaedf539991f0eb1f69d51f6da1167e"}, "docker": "quay.io/biocontainers/metaxa", "aliases": {"metaxa2": "/usr/local/bin/metaxa2", "metaxa2_c": "/usr/local/bin/metaxa2_c", "metaxa2_dbb": "/usr/local/bin/metaxa2_dbb", "metaxa2_dc": "/usr/local/bin/metaxa2_dc", "metaxa2_install_database": "/usr/local/bin/metaxa2_install_database", "metaxa2_rf": "/usr/local/bin/metaxa2_rf", "metaxa2_si": "/usr/local/bin/metaxa2_si", "metaxa2_ttt": "/usr/local/bin/metaxa2_ttt", "metaxa2_uc": "/usr/local/bin/metaxa2_uc", "metaxa2_x": "/usr/local/bin/metaxa2_x", "2to3-3.10": "/usr/local/bin/2to3-3.10", "alimask": "/usr/local/bin/alimask", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdbcheck": "/usr/local/bin/blastdbcheck", "blastdbcmd": "/usr/local/bin/blastdbcmd", "blastdbcp": "/usr/local/bin/blastdbcp", "blastn": "/usr/local/bin/blastn", "blastp": "/usr/local/bin/blastp", "blastx": "/usr/local/bin/blastx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaxa.
shpc-registry automated BioContainers addition for metaxa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaxa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaxa:2.2.3--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaxa/2.2.3--pl5321hdfd78af_1
$ module help quay.io/biocontainers/metaxa/2.2.3--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaxa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaxa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaxa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaxa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaxa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaxa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metaxa2

```bash
$ singularity exec <container> /usr/local/bin/metaxa2
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_c

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_c
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_dbb

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_dbb
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_dbb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_dbb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_dc

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_dc
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_install_database

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_install_database
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_install_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_install_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_rf

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_rf
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_rf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_rf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_si

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_si
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_si   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_si   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_ttt

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_ttt
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_ttt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_ttt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_uc

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_uc
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_uc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_uc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_x

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_x
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_formatter

```bash
$ singularity exec <container> /usr/local/bin/blast_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_aliastool

```bash
$ singularity exec <container> /usr/local/bin/blastdb_aliastool
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcheck

```bash
$ singularity exec <container> /usr/local/bin/blastdbcheck
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcmd

```bash
$ singularity exec <container> /usr/local/bin/blastdbcmd
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcp

```bash
$ singularity exec <container> /usr/local/bin/blastdbcp
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastn

```bash
$ singularity exec <container> /usr/local/bin/blastn
$ podman run --it --rm --entrypoint /usr/local/bin/blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastp

```bash
$ singularity exec <container> /usr/local/bin/blastp
$ podman run --it --rm --entrypoint /usr/local/bin/blastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastx

```bash
$ singularity exec <container> /usr/local/bin/blastx
$ podman run --it --rm --entrypoint /usr/local/bin/blastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastx   -v ${PWD} -w ${PWD} <container> -c " $@"
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