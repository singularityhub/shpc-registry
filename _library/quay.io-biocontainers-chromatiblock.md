---
layout: container
name:  "quay.io/biocontainers/chromatiblock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chromatiblock/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chromatiblock/container.yaml"
updated_at: "2024-09-20 03:03:42.245764"
latest: "1.0.0--py_0"
container_url: "https://biocontainers.pro/tools/chromatiblock"
aliases:
 - "C-Sibelia.py"
 - "Sibelia"
 - "cairosvg"
 - "chromatiblock"
 - "snpEffAnnotate.py"
 - "test_pcre"
 - "blastdbcp"
 - "gene_info_reader"
 - "seqdb_demo"
 - "seqdb_perf"
 - "seedtop"
 - "run_with_lock"
 - "f2py3.8"
 - "blast_formatter"
 - "blastdb_aliastool"
versions:
 - "1.0.0--py_0"
description: "shpc-registry automated BioContainers addition for chromatiblock"
config: {"url": "https://biocontainers.pro/tools/chromatiblock", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chromatiblock", "latest": {"1.0.0--py_0": "sha256:fce5317ca2a8159debfe7f1aa57cf173602b7b58aa01897f5c746a07e5fb1f9d"}, "tags": {"1.0.0--py_0": "sha256:fce5317ca2a8159debfe7f1aa57cf173602b7b58aa01897f5c746a07e5fb1f9d"}, "docker": "quay.io/biocontainers/chromatiblock", "aliases": {"C-Sibelia.py": "/usr/local/bin/C-Sibelia.py", "Sibelia": "/usr/local/bin/Sibelia", "cairosvg": "/usr/local/bin/cairosvg", "chromatiblock": "/usr/local/bin/chromatiblock", "snpEffAnnotate.py": "/usr/local/bin/snpEffAnnotate.py", "test_pcre": "/usr/local/bin/test_pcre", "blastdbcp": "/usr/local/bin/blastdbcp", "gene_info_reader": "/usr/local/bin/gene_info_reader", "seqdb_demo": "/usr/local/bin/seqdb_demo", "seqdb_perf": "/usr/local/bin/seqdb_perf", "seedtop": "/usr/local/bin/seedtop", "run_with_lock": "/usr/local/bin/run_with_lock", "f2py3.8": "/usr/local/bin/f2py3.8", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chromatiblock.
shpc-registry automated BioContainers addition for chromatiblock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chromatiblock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chromatiblock:1.0.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chromatiblock/1.0.0--py_0
$ module help quay.io/biocontainers/chromatiblock/1.0.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chromatiblock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chromatiblock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chromatiblock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chromatiblock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chromatiblock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chromatiblock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### C-Sibelia.py

```bash
$ singularity exec <container> /usr/local/bin/C-Sibelia.py
$ podman run --it --rm --entrypoint /usr/local/bin/C-Sibelia.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/C-Sibelia.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Sibelia

```bash
$ singularity exec <container> /usr/local/bin/Sibelia
$ podman run --it --rm --entrypoint /usr/local/bin/Sibelia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Sibelia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cairosvg

```bash
$ singularity exec <container> /usr/local/bin/cairosvg
$ podman run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chromatiblock

```bash
$ singularity exec <container> /usr/local/bin/chromatiblock
$ podman run --it --rm --entrypoint /usr/local/bin/chromatiblock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chromatiblock   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpEffAnnotate.py

```bash
$ singularity exec <container> /usr/local/bin/snpEffAnnotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/snpEffAnnotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpEffAnnotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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