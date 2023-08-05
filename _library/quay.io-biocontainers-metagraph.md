---
layout: container
name:  "quay.io/biocontainers/metagraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metagraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metagraph/container.yaml"
updated_at: "2023-08-05 03:04:45.197104"
latest: "0.3.6--hf159946_3"
container_url: "https://biocontainers.pro/tools/metagraph"
aliases:
 - "metagraph"
 - "metagraph_DNA"
 - "metagraph_Protein"
 - "jemalloc-config"
 - "jeprof"
 - "jemalloc.sh"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.6--h15c59b9_1"
 - "0.3.6--ha1a87e0_2"
 - "0.3.6--hf159946_3"
description: "shpc-registry automated BioContainers addition for metagraph"
config: {"url": "https://biocontainers.pro/tools/metagraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metagraph", "latest": {"0.3.6--hf159946_3": "sha256:c6e02d79938a7397ded44be9e39242f85164ae6aef08c87eeac5e609c1e677d6"}, "tags": {"0.3.6--h15c59b9_1": "sha256:38e254af4c68bf6d0a68b45f198e813d3fa2182c870a569631fc5c7912f50914", "0.3.6--ha1a87e0_2": "sha256:542ff7cf6cb69599cddfc7e86c8cd7c44d854dbe07d152b77626f16c40404799", "0.3.6--hf159946_3": "sha256:c6e02d79938a7397ded44be9e39242f85164ae6aef08c87eeac5e609c1e677d6"}, "docker": "quay.io/biocontainers/metagraph", "aliases": {"metagraph": "/usr/local/bin/metagraph", "metagraph_DNA": "/usr/local/bin/metagraph_DNA", "metagraph_Protein": "/usr/local/bin/metagraph_Protein", "jemalloc-config": "/usr/local/bin/jemalloc-config", "jeprof": "/usr/local/bin/jeprof", "jemalloc.sh": "/usr/local/bin/jemalloc.sh", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metagraph.
shpc-registry automated BioContainers addition for metagraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metagraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metagraph:0.3.6--hf159946_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metagraph/0.3.6--hf159946_3
$ module help quay.io/biocontainers/metagraph/0.3.6--hf159946_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metagraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metagraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metagraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metagraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metagraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metagraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metagraph

```bash
$ singularity exec <container> /usr/local/bin/metagraph
$ podman run --it --rm --entrypoint /usr/local/bin/metagraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metagraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metagraph_DNA

```bash
$ singularity exec <container> /usr/local/bin/metagraph_DNA
$ podman run --it --rm --entrypoint /usr/local/bin/metagraph_DNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metagraph_DNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metagraph_Protein

```bash
$ singularity exec <container> /usr/local/bin/metagraph_Protein
$ podman run --it --rm --entrypoint /usr/local/bin/metagraph_Protein   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metagraph_Protein   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc-config

```bash
$ singularity exec <container> /usr/local/bin/jemalloc-config
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jeprof

```bash
$ singularity exec <container> /usr/local/bin/jeprof
$ podman run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc.sh

```bash
$ singularity exec <container> /usr/local/bin/jemalloc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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