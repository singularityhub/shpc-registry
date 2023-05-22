---
layout: container
name:  "quay.io/biocontainers/augur"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/augur/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/augur/container.yaml"
updated_at: "2023-05-22 02:43:55.399147"
latest: "13.1.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/augur"
aliases:
 - "augur"
 - "dsdp5"
 - "treetime"
 - "vcftools"
 - "iqtree"
 - "raxmlHPC"
 - "raxmlHPC-AVX2"
 - "raxmlHPC-PTHREADS"
 - "raxmlHPC-PTHREADS-AVX2"
 - "raxmlHPC-PTHREADS-SSE3"
 - "raxmlHPC-SSE3"
 - "FastTree-2.1.10.c"
 - "FastTreeMP"
 - "cmpfillin"
versions:
 - "9.0.0--py_1"
 - "13.1.2--pyhdfd78af_0"
 - "13.0.4--pyhdfd78af_0"
 - "12.1.1--pyhdfd78af_0"
 - "12.0.0--pyhdfd78af_0"
 - "11.3.0--py_0"
description: "shpc-registry automated BioContainers addition for augur"
config: {"url": "https://biocontainers.pro/tools/augur", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for augur", "latest": {"13.1.2--pyhdfd78af_0": "sha256:d9fb311e25b0bfd52ec109aed76f270d428f7098cdc719d05796132fae3df3db"}, "tags": {"9.0.0--py_1": "sha256:b50216d6d9feda2fa8e54fd976d596c5b58410b98aede1419fe54525203a337b", "13.1.2--pyhdfd78af_0": "sha256:d9fb311e25b0bfd52ec109aed76f270d428f7098cdc719d05796132fae3df3db", "13.0.4--pyhdfd78af_0": "sha256:fbbff4860cde5d4ca8c9977b8b902d288ea8d529a63aa3a15327f89b8d7779f6", "12.1.1--pyhdfd78af_0": "sha256:548eabeaee28da804021d0f68e2fdbcf9202f6c0f0790def57ab84149b7bf3ac", "12.0.0--pyhdfd78af_0": "sha256:558b1eeb992284f3cb35f3d461ad03ef8471deb95c2065df65a9016d29c3f6af", "11.3.0--py_0": "sha256:7185216d958d3f06355eda046e50b3bf8620fc142bb8acca30f2c56fabfddff6"}, "docker": "quay.io/biocontainers/augur", "aliases": {"augur": "/usr/local/bin/augur", "dsdp5": "/usr/local/bin/dsdp5", "treetime": "/usr/local/bin/treetime", "vcftools": "/usr/local/bin/vcftools", "iqtree": "/usr/local/bin/iqtree", "raxmlHPC": "/usr/local/bin/raxmlHPC", "raxmlHPC-AVX2": "/usr/local/bin/raxmlHPC-AVX2", "raxmlHPC-PTHREADS": "/usr/local/bin/raxmlHPC-PTHREADS", "raxmlHPC-PTHREADS-AVX2": "/usr/local/bin/raxmlHPC-PTHREADS-AVX2", "raxmlHPC-PTHREADS-SSE3": "/usr/local/bin/raxmlHPC-PTHREADS-SSE3", "raxmlHPC-SSE3": "/usr/local/bin/raxmlHPC-SSE3", "FastTree-2.1.10.c": "/usr/local/bin/FastTree-2.1.10.c", "FastTreeMP": "/usr/local/bin/FastTreeMP", "cmpfillin": "/usr/local/bin/cmpfillin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/augur.
shpc-registry automated BioContainers addition for augur
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/augur
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/augur:13.1.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/augur/13.1.2--pyhdfd78af_0
$ module help quay.io/biocontainers/augur/13.1.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### augur-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### augur-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### augur-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### augur-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### augur-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### augur-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### augur

```bash
$ singularity exec <container> /usr/local/bin/augur
$ podman run --it --rm --entrypoint /usr/local/bin/augur   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/augur   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsdp5

```bash
$ singularity exec <container> /usr/local/bin/dsdp5
$ podman run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treetime

```bash
$ singularity exec <container> /usr/local/bin/treetime
$ podman run --it --rm --entrypoint /usr/local/bin/treetime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treetime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcftools

```bash
$ singularity exec <container> /usr/local/bin/vcftools
$ podman run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree

```bash
$ singularity exec <container> /usr/local/bin/iqtree
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
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