---
layout: container
name:  "quay.io/biocontainers/blast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blast/container.yaml"
updated_at: "2024-08-04 03:01:44.698353"
latest: "2.15.0--pl5321h6f7f691_1"
container_url: "https://biocontainers.pro/tools/blast"
aliases:
 - "blast_formatter"
 - "blastdb_aliastool"
 - "blastdbcheck"
 - "blastdbcmd"
 - "blastn"
 - "blastp"
 - "blastx"
 - "cleanup-blastdb-volumes.py"
 - "convert2blastmask"
 - "deltablast"
 - "eblast"
 - "makeblastdb"
 - "psiblast"
 - "rpsblast"
 - "rpstblastn"
 - "tblastn"
 - "tblastx"
 - "update_blastdb.pl"
versions:
 - "2.10.1--pl526he19e7b1_3"
 - "2.11.0--pl5262h3289130_1"
 - "2.12.0--pl5262h3289130_0"
 - "2.12.0--hf3cf87c_4"
 - "2.13.0--hf3cf87c_0"
 - "2.14.0--hf3cf87c_0"
 - "2.13.0--hf3cf87c_1"
 - "2.14.0--h7d5a4b4_1"
 - "2.14.0--pl5321h6f7f691_2"
 - "2.14.1--pl5321h6f7f691_0"
 - "2.15.0--pl5321h6f7f691_1"
description: "shpc-registry automated BioContainers addition for blast"
config: {"url": "https://biocontainers.pro/tools/blast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for blast", "latest": {"2.15.0--pl5321h6f7f691_1": "sha256:0a9a03dc0e7c4a68caabe5077ef5ce9bd9852604f7090a144fcbe338ffea079f"}, "tags": {"2.10.1--pl526he19e7b1_3": "sha256:f12a5a35a0e6645134fcfe8650b0d1b5ff1f486430828a4ec3c4c9bfe35a5d78", "2.11.0--pl5262h3289130_1": "sha256:52e8e0ed12a0fe8854681dadb600e1d5599e04b960b01034cb53812fad944c3d", "2.12.0--pl5262h3289130_0": "sha256:a7eb056f5ca6a32551bf9f87b6b15acc45598cfef39bffdd672f59da3847cd18", "2.12.0--hf3cf87c_4": "sha256:9df91dee10f97405384734f964021feae38fcf68a721315f706be99be9366d86", "2.13.0--hf3cf87c_0": "sha256:221b0ab5540cf7c4013b51b60b2c66113104a5b700611d411ae25eb5904f78d8", "2.14.0--hf3cf87c_0": "sha256:294286c40fce6e281d09853d9e650520df160ee0398bc7afc78587ab2c1e8ca3", "2.13.0--hf3cf87c_1": "sha256:64f77cdca6492aefc381cf5415a78ee16d6a3fd1eb6b6babd4c2a456bfd721b3", "2.14.0--h7d5a4b4_1": "sha256:8a077ba3916a3078a9cb442ba31138292bb869116347d86ba0dc3b3554f21255", "2.14.0--pl5321h6f7f691_2": "sha256:e7398357b102f3cb4462ea28c705745c05b43c2910e7ca61b23c2bdddea93a65", "2.14.1--pl5321h6f7f691_0": "sha256:0fa116b90c6411d5b09cdda5ca81a857167d218c49915104e7e1588b16baedf7", "2.15.0--pl5321h6f7f691_1": "sha256:0a9a03dc0e7c4a68caabe5077ef5ce9bd9852604f7090a144fcbe338ffea079f"}, "docker": "quay.io/biocontainers/blast", "aliases": {"blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdbcheck": "/usr/local/bin/blastdbcheck", "blastdbcmd": "/usr/local/bin/blastdbcmd", "blastn": "/usr/local/bin/blastn", "blastp": "/usr/local/bin/blastp", "blastx": "/usr/local/bin/blastx", "cleanup-blastdb-volumes.py": "/usr/local/bin/cleanup-blastdb-volumes.py", "convert2blastmask": "/usr/local/bin/convert2blastmask", "deltablast": "/usr/local/bin/deltablast", "eblast": "/usr/local/bin/eblast", "makeblastdb": "/usr/local/bin/makeblastdb", "psiblast": "/usr/local/bin/psiblast", "rpsblast": "/usr/local/bin/rpsblast", "rpstblastn": "/usr/local/bin/rpstblastn", "tblastn": "/usr/local/bin/tblastn", "tblastx": "/usr/local/bin/tblastx", "update_blastdb.pl": "/usr/local/bin/update_blastdb.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blast.
shpc-registry automated BioContainers addition for blast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blast:2.15.0--pl5321h6f7f691_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blast/2.15.0--pl5321h6f7f691_1
$ module help quay.io/biocontainers/blast/2.15.0--pl5321h6f7f691_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blast-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### cleanup-blastdb-volumes.py

```bash
$ singularity exec <container> /usr/local/bin/cleanup-blastdb-volumes.py
$ podman run --it --rm --entrypoint /usr/local/bin/cleanup-blastdb-volumes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleanup-blastdb-volumes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert2blastmask

```bash
$ singularity exec <container> /usr/local/bin/convert2blastmask
$ podman run --it --rm --entrypoint /usr/local/bin/convert2blastmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert2blastmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deltablast

```bash
$ singularity exec <container> /usr/local/bin/deltablast
$ podman run --it --rm --entrypoint /usr/local/bin/deltablast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deltablast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eblast

```bash
$ singularity exec <container> /usr/local/bin/eblast
$ podman run --it --rm --entrypoint /usr/local/bin/eblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeblastdb

```bash
$ singularity exec <container> /usr/local/bin/makeblastdb
$ podman run --it --rm --entrypoint /usr/local/bin/makeblastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeblastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psiblast

```bash
$ singularity exec <container> /usr/local/bin/psiblast
$ podman run --it --rm --entrypoint /usr/local/bin/psiblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psiblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rpsblast

```bash
$ singularity exec <container> /usr/local/bin/rpsblast
$ podman run --it --rm --entrypoint /usr/local/bin/rpsblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rpsblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rpstblastn

```bash
$ singularity exec <container> /usr/local/bin/rpstblastn
$ podman run --it --rm --entrypoint /usr/local/bin/rpstblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rpstblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn

```bash
$ singularity exec <container> /usr/local/bin/tblastn
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastx

```bash
$ singularity exec <container> /usr/local/bin/tblastx
$ podman run --it --rm --entrypoint /usr/local/bin/tblastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_blastdb.pl

```bash
$ singularity exec <container> /usr/local/bin/update_blastdb.pl
$ podman run --it --rm --entrypoint /usr/local/bin/update_blastdb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_blastdb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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