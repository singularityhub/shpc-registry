---
layout: container
name:  "quay.io/biocontainers/crypto_typer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crypto_typer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/crypto_typer/container.yaml"
updated_at: "2022-10-29 05:47:43.356433"
latest: "1.0.0--py_0"
container_url: "https://biocontainers.pro/tools/crypto_typer"
aliases:
 - "crypto_typer"
 - "2to3-3.7"
 - "blast_formatter"
 - "blast_report"
 - "blastdb_aliastool"
 - "blastdb_convert"
 - "blastdb_path"
 - "blastdbcheck"
 - "blastdbcmd"
 - "blastdbcp"
 - "blastn"
versions:
 - "1.0.0--py_0"
description: "shpc-registry automated BioContainers addition for crypto_typer"
config: {"url": "https://biocontainers.pro/tools/crypto_typer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crypto_typer", "latest": {"1.0.0--py_0": "sha256:4dd3f40653643ddfe0cd2a30c8091540628367bc19e832fd982070d297806287"}, "tags": {"1.0.0--py_0": "sha256:4dd3f40653643ddfe0cd2a30c8091540628367bc19e832fd982070d297806287"}, "docker": "quay.io/biocontainers/crypto_typer", "aliases": {"crypto_typer": "/usr/local/bin/crypto_typer", "2to3-3.7": "/usr/local/bin/2to3-3.7", "blast_formatter": "/usr/local/bin/blast_formatter", "blast_report": "/usr/local/bin/blast_report", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "blastdbcheck": "/usr/local/bin/blastdbcheck", "blastdbcmd": "/usr/local/bin/blastdbcmd", "blastdbcp": "/usr/local/bin/blastdbcp", "blastn": "/usr/local/bin/blastn"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crypto_typer.
shpc-registry automated BioContainers addition for crypto_typer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crypto_typer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crypto_typer:1.0.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crypto_typer/1.0.0--py_0
$ module help quay.io/biocontainers/crypto_typer/1.0.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crypto_typer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crypto_typer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crypto_typer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crypto_typer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crypto_typer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crypto_typer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crypto_typer

```bash
$ singularity exec <container> /usr/local/bin/crypto_typer
$ podman run --it --rm --entrypoint /usr/local/bin/crypto_typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crypto_typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_formatter

```bash
$ singularity exec <container> /usr/local/bin/blast_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_report

```bash
$ singularity exec <container> /usr/local/bin/blast_report
$ podman run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_aliastool

```bash
$ singularity exec <container> /usr/local/bin/blastdb_aliastool
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_convert

```bash
$ singularity exec <container> /usr/local/bin/blastdb_convert
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_path

```bash
$ singularity exec <container> /usr/local/bin/blastdb_path
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
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