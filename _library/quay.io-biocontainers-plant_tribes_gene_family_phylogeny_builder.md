---
layout: container
name:  "quay.io/biocontainers/plant_tribes_gene_family_phylogeny_builder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plant_tribes_gene_family_phylogeny_builder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plant_tribes_gene_family_phylogeny_builder/container.yaml"
updated_at: "2025-11-26 03:22:45.578239"
latest: "1.0.4--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/plant_tribes_gene_family_phylogeny_builder"
aliases:
 - "GeneFamilyPhylogenyBuilder"
 - "raxmlHPC"
 - "raxmlHPC-AVX2"
 - "raxmlHPC-PTHREADS"
 - "raxmlHPC-PTHREADS-AVX2"
 - "raxmlHPC-PTHREADS-SSE3"
 - "raxmlHPC-SSE3"
 - "FastTree-2.1.10.c"
 - "FastTreeMP"
 - "FastTree"
 - "fasttree"
versions:
 - "1.0.4--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for plant_tribes_gene_family_phylogeny_builder"
config: {"url": "https://biocontainers.pro/tools/plant_tribes_gene_family_phylogeny_builder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plant_tribes_gene_family_phylogeny_builder", "latest": {"1.0.4--hdfd78af_1": "sha256:83ce23d027f4e039eef1d4b20e09ff8bce696a882f523f828dde982b2117b52c"}, "tags": {"1.0.4--hdfd78af_1": "sha256:83ce23d027f4e039eef1d4b20e09ff8bce696a882f523f828dde982b2117b52c"}, "docker": "quay.io/biocontainers/plant_tribes_gene_family_phylogeny_builder", "aliases": {"GeneFamilyPhylogenyBuilder": "/usr/local/bin/GeneFamilyPhylogenyBuilder", "raxmlHPC": "/usr/local/bin/raxmlHPC", "raxmlHPC-AVX2": "/usr/local/bin/raxmlHPC-AVX2", "raxmlHPC-PTHREADS": "/usr/local/bin/raxmlHPC-PTHREADS", "raxmlHPC-PTHREADS-AVX2": "/usr/local/bin/raxmlHPC-PTHREADS-AVX2", "raxmlHPC-PTHREADS-SSE3": "/usr/local/bin/raxmlHPC-PTHREADS-SSE3", "raxmlHPC-SSE3": "/usr/local/bin/raxmlHPC-SSE3", "FastTree-2.1.10.c": "/usr/local/bin/FastTree-2.1.10.c", "FastTreeMP": "/usr/local/bin/FastTreeMP", "FastTree": "/usr/local/bin/FastTree", "fasttree": "/usr/local/bin/fasttree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plant_tribes_gene_family_phylogeny_builder.
shpc-registry automated BioContainers addition for plant_tribes_gene_family_phylogeny_builder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plant_tribes_gene_family_phylogeny_builder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plant_tribes_gene_family_phylogeny_builder:1.0.4--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plant_tribes_gene_family_phylogeny_builder/1.0.4--hdfd78af_1
$ module help quay.io/biocontainers/plant_tribes_gene_family_phylogeny_builder/1.0.4--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plant_tribes_gene_family_phylogeny_builder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_gene_family_phylogeny_builder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_gene_family_phylogeny_builder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plant_tribes_gene_family_phylogeny_builder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plant_tribes_gene_family_phylogeny_builder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plant_tribes_gene_family_phylogeny_builder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GeneFamilyPhylogenyBuilder

```bash
$ singularity exec <container> /usr/local/bin/GeneFamilyPhylogenyBuilder
$ podman run --it --rm --entrypoint /usr/local/bin/GeneFamilyPhylogenyBuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeneFamilyPhylogenyBuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree-2.1.10.c

```bash
$ singularity exec <container> /usr/local/bin/FastTree-2.1.10.c
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
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