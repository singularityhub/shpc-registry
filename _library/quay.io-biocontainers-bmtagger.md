---
layout: container
name:  "quay.io/biocontainers/bmtagger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bmtagger/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bmtagger/container.yaml"
updated_at: "2024-11-24 03:07:22.569927"
latest: "3.101--h470a237_4"
container_url: "https://biocontainers.pro/tools/bmtagger"
aliases:
 - "bmfilter"
 - "bmtagger.sh"
 - "bmtool"
 - "extract_fullseq"
 - "srprism"
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
 - "3.101--h470a237_4"
description: "shpc-registry automated BioContainers addition for bmtagger"
config: {"url": "https://biocontainers.pro/tools/bmtagger", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bmtagger", "latest": {"3.101--h470a237_4": "sha256:e836ced6978a0a5d2192e878c3643de96027d68add069370a161284c7f8e98d0"}, "tags": {"3.101--h470a237_4": "sha256:e836ced6978a0a5d2192e878c3643de96027d68add069370a161284c7f8e98d0"}, "docker": "quay.io/biocontainers/bmtagger", "aliases": {"bmfilter": "/usr/local/bin/bmfilter", "bmtagger.sh": "/usr/local/bin/bmtagger.sh", "bmtool": "/usr/local/bin/bmtool", "extract_fullseq": "/usr/local/bin/extract_fullseq", "srprism": "/usr/local/bin/srprism", "test_pcre": "/usr/local/bin/test_pcre", "blastdbcp": "/usr/local/bin/blastdbcp", "gene_info_reader": "/usr/local/bin/gene_info_reader", "seqdb_demo": "/usr/local/bin/seqdb_demo", "seqdb_perf": "/usr/local/bin/seqdb_perf", "seedtop": "/usr/local/bin/seedtop", "run_with_lock": "/usr/local/bin/run_with_lock", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdbcheck": "/usr/local/bin/blastdbcheck"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bmtagger.
shpc-registry automated BioContainers addition for bmtagger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bmtagger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bmtagger:3.101--h470a237_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bmtagger/3.101--h470a237_4
$ module help quay.io/biocontainers/bmtagger/3.101--h470a237_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bmtagger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bmtagger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bmtagger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bmtagger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bmtagger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bmtagger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bmfilter

```bash
$ singularity exec <container> /usr/local/bin/bmfilter
$ podman run --it --rm --entrypoint /usr/local/bin/bmfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bmtagger.sh

```bash
$ singularity exec <container> /usr/local/bin/bmtagger.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bmtagger.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmtagger.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bmtool

```bash
$ singularity exec <container> /usr/local/bin/bmtool
$ podman run --it --rm --entrypoint /usr/local/bin/bmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_fullseq

```bash
$ singularity exec <container> /usr/local/bin/extract_fullseq
$ podman run --it --rm --entrypoint /usr/local/bin/extract_fullseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_fullseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srprism

```bash
$ singularity exec <container> /usr/local/bin/srprism
$ podman run --it --rm --entrypoint /usr/local/bin/srprism   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srprism   -v ${PWD} -w ${PWD} <container> -c " $@"
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