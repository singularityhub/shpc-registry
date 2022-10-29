---
layout: container
name:  "quay.io/biocontainers/rgi_conda_dev"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rgi_conda_dev/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rgi_conda_dev/container.yaml"
updated_at: "2022-10-29 05:33:24.372470"
latest: "3.1.2--py27_1"
container_url: "https://biocontainers.pro/tools/rgi_conda_dev"
aliases:
 - "rgi"
 - "rgi_clean"
 - "rgi_jsonformat"
 - "rgi_jsontab"
 - "rgi_load"
 - "blast_formatter"
 - "blastdb_aliastool"
 - "blastdbcheck"
 - "blastdbcmd"
 - "blastdbcp"
 - "blastn"
 - "blastp"
 - "blastx"
 - "bmp2tiff"
 - "convert2blastmask"
versions:
 - "3.1.2--py27_1"
description: "shpc-registry automated BioContainers addition for rgi_conda_dev"
config: {"url": "https://biocontainers.pro/tools/rgi_conda_dev", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rgi_conda_dev", "latest": {"3.1.2--py27_1": "sha256:a8ad5c6a105f9b5b730b4608255cfe3d3eba0c2f4cf6c9fc47784a6468c11e12"}, "tags": {"3.1.2--py27_1": "sha256:a8ad5c6a105f9b5b730b4608255cfe3d3eba0c2f4cf6c9fc47784a6468c11e12"}, "docker": "quay.io/biocontainers/rgi_conda_dev", "aliases": {"rgi": "/usr/local/bin/rgi", "rgi_clean": "/usr/local/bin/rgi_clean", "rgi_jsonformat": "/usr/local/bin/rgi_jsonformat", "rgi_jsontab": "/usr/local/bin/rgi_jsontab", "rgi_load": "/usr/local/bin/rgi_load", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdbcheck": "/usr/local/bin/blastdbcheck", "blastdbcmd": "/usr/local/bin/blastdbcmd", "blastdbcp": "/usr/local/bin/blastdbcp", "blastn": "/usr/local/bin/blastn", "blastp": "/usr/local/bin/blastp", "blastx": "/usr/local/bin/blastx", "bmp2tiff": "/usr/local/bin/bmp2tiff", "convert2blastmask": "/usr/local/bin/convert2blastmask"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rgi_conda_dev.
shpc-registry automated BioContainers addition for rgi_conda_dev
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rgi_conda_dev
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rgi_conda_dev:3.1.2--py27_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rgi_conda_dev/3.1.2--py27_1
$ module help quay.io/biocontainers/rgi_conda_dev/3.1.2--py27_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rgi_conda_dev-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rgi_conda_dev-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rgi_conda_dev-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rgi_conda_dev-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rgi_conda_dev-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rgi_conda_dev-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rgi

```bash
$ singularity exec <container> /usr/local/bin/rgi
$ podman run --it --rm --entrypoint /usr/local/bin/rgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgi_clean

```bash
$ singularity exec <container> /usr/local/bin/rgi_clean
$ podman run --it --rm --entrypoint /usr/local/bin/rgi_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgi_jsonformat

```bash
$ singularity exec <container> /usr/local/bin/rgi_jsonformat
$ podman run --it --rm --entrypoint /usr/local/bin/rgi_jsonformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi_jsonformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgi_jsontab

```bash
$ singularity exec <container> /usr/local/bin/rgi_jsontab
$ podman run --it --rm --entrypoint /usr/local/bin/rgi_jsontab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi_jsontab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgi_load

```bash
$ singularity exec <container> /usr/local/bin/rgi_load
$ podman run --it --rm --entrypoint /usr/local/bin/rgi_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi_load   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bmp2tiff

```bash
$ singularity exec <container> /usr/local/bin/bmp2tiff
$ podman run --it --rm --entrypoint /usr/local/bin/bmp2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmp2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert2blastmask

```bash
$ singularity exec <container> /usr/local/bin/convert2blastmask
$ podman run --it --rm --entrypoint /usr/local/bin/convert2blastmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert2blastmask   -v ${PWD} -w ${PWD} <container> -c " $@"
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