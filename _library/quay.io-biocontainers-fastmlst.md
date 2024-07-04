---
layout: container
name:  "quay.io/biocontainers/fastmlst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastmlst/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastmlst/container.yaml"
updated_at: "2024-07-04 02:55:59.906319"
latest: "0.0.16--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/fastmlst"
aliases:
 - "fastmlst"
 - "test_pcre"
 - "blastdbcp"
 - "gene_info_reader"
 - "seqdb_demo"
 - "seqdb_perf"
 - "seedtop"
 - "tqdm"
 - "run_with_lock"
 - "f2py3.8"
 - "blast_formatter"
versions:
 - "0.0.9--py_0"
 - "0.0.15--pyhdfd78af_0"
 - "0.0.16--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for fastmlst"
config: {"url": "https://biocontainers.pro/tools/fastmlst", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastmlst", "latest": {"0.0.16--pyhdfd78af_0": "sha256:8076534b31ab83e74719dedda686cc65b35b038a18e92d0a386394192135a17d"}, "tags": {"0.0.9--py_0": "sha256:cc131ee6bc0b619e22e8ceb8bef435cf764a29f07751726b5db3f83e618cbdbf", "0.0.15--pyhdfd78af_0": "sha256:a4e3fafe0b295e9e6dcabb60a2ad9e22b38a2476502a8f20735333a6f5cc7595", "0.0.16--pyhdfd78af_0": "sha256:8076534b31ab83e74719dedda686cc65b35b038a18e92d0a386394192135a17d"}, "docker": "quay.io/biocontainers/fastmlst", "aliases": {"fastmlst": "/usr/local/bin/fastmlst", "test_pcre": "/usr/local/bin/test_pcre", "blastdbcp": "/usr/local/bin/blastdbcp", "gene_info_reader": "/usr/local/bin/gene_info_reader", "seqdb_demo": "/usr/local/bin/seqdb_demo", "seqdb_perf": "/usr/local/bin/seqdb_perf", "seedtop": "/usr/local/bin/seedtop", "tqdm": "/usr/local/bin/tqdm", "run_with_lock": "/usr/local/bin/run_with_lock", "f2py3.8": "/usr/local/bin/f2py3.8", "blast_formatter": "/usr/local/bin/blast_formatter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastmlst.
shpc-registry automated BioContainers addition for fastmlst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastmlst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastmlst:0.0.16--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastmlst/0.0.16--pyhdfd78af_0
$ module help quay.io/biocontainers/fastmlst/0.0.16--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastmlst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastmlst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastmlst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastmlst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastmlst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastmlst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastmlst

```bash
$ singularity exec <container> /usr/local/bin/fastmlst
$ podman run --it --rm --entrypoint /usr/local/bin/fastmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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