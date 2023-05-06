---
layout: container
name:  "quay.io/biocontainers/spotyping3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spotyping3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spotyping3/container.yaml"
updated_at: "2023-05-06 02:45:50.497807"
latest: "3.0--py_0"
container_url: "https://biocontainers.pro/tools/spotyping3"
aliases:
 - "SpoTyping.py"
 - "SpoTyping_plot.r"
 - "test_pcre"
 - "blastdbcp"
 - "gene_info_reader"
 - "seqdb_demo"
 - "seqdb_perf"
 - "seedtop"
 - "run_with_lock"
 - "blast_formatter"
 - "blastdb_aliastool"
 - "blastdbcheck"
versions:
 - "3.0--py_0"
description: "shpc-registry automated BioContainers addition for spotyping3"
config: {"url": "https://biocontainers.pro/tools/spotyping3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spotyping3", "latest": {"3.0--py_0": "sha256:7180a61d05e07338b2e2726e460c5e419b8687b6db8c9871fd578fc02690ff3e"}, "tags": {"3.0--py_0": "sha256:7180a61d05e07338b2e2726e460c5e419b8687b6db8c9871fd578fc02690ff3e"}, "docker": "quay.io/biocontainers/spotyping3", "aliases": {"SpoTyping.py": "/usr/local/bin/SpoTyping.py", "SpoTyping_plot.r": "/usr/local/bin/SpoTyping_plot.r", "test_pcre": "/usr/local/bin/test_pcre", "blastdbcp": "/usr/local/bin/blastdbcp", "gene_info_reader": "/usr/local/bin/gene_info_reader", "seqdb_demo": "/usr/local/bin/seqdb_demo", "seqdb_perf": "/usr/local/bin/seqdb_perf", "seedtop": "/usr/local/bin/seedtop", "run_with_lock": "/usr/local/bin/run_with_lock", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdbcheck": "/usr/local/bin/blastdbcheck"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spotyping3.
shpc-registry automated BioContainers addition for spotyping3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spotyping3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spotyping3:3.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spotyping3/3.0--py_0
$ module help quay.io/biocontainers/spotyping3/3.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spotyping3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spotyping3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spotyping3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spotyping3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spotyping3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spotyping3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SpoTyping.py

```bash
$ singularity exec <container> /usr/local/bin/SpoTyping.py
$ podman run --it --rm --entrypoint /usr/local/bin/SpoTyping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SpoTyping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SpoTyping_plot.r

```bash
$ singularity exec <container> /usr/local/bin/SpoTyping_plot.r
$ podman run --it --rm --entrypoint /usr/local/bin/SpoTyping_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SpoTyping_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcp

```bash
$ singularity exec <container> /usr/local/bin/blastdbcp
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_info_reader

```bash
$ singularity exec <container> /usr/local/bin/gene_info_reader
$ podman run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_demo

```bash
$ singularity exec <container> /usr/local/bin/seqdb_demo
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_perf

```bash
$ singularity exec <container> /usr/local/bin/seqdb_perf
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seedtop

```bash
$ singularity exec <container> /usr/local/bin/seedtop
$ podman run --it --rm --entrypoint /usr/local/bin/seedtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seedtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_with_lock

```bash
$ singularity exec <container> /usr/local/bin/run_with_lock
$ podman run --it --rm --entrypoint /usr/local/bin/run_with_lock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_with_lock   -v ${PWD} -w ${PWD} <container> -c " $@"
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