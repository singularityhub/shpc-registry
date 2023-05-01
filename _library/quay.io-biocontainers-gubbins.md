---
layout: container
name:  "quay.io/biocontainers/gubbins"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gubbins/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gubbins/container.yaml"
updated_at: "2023-05-01 03:10:12.023505"
latest: "3.2.1--py39pl5321h87d955d_0"
container_url: "https://biocontainers.pro/tools/gubbins"
aliases:
 - "extract_gubbins_clade.py"
 - "generate_ska_alignment.py"
 - "gubbins"
 - "gubbins_alignment_checker.py"
 - "mask_gubbins_aln.py"
 - "rapidnj"
 - "raxml-ng"
 - "raxml-ng-mpi"
 - "run_gubbins.py"
 - "ska"
 - "iqtree"
 - "raxmlHPC"
 - "raxmlHPC-AVX2"
 - "raxmlHPC-PTHREADS"
 - "raxmlHPC-PTHREADS-AVX2"
 - "raxmlHPC-PTHREADS-SSE3"
 - "raxmlHPC-SSE3"
 - "dendropy-format"
 - "get_objgraph"
 - "undill"
versions:
 - "3.2.1--py39pl5321h87d955d_0"
description: "shpc-registry automated BioContainers addition for gubbins"
config: {"url": "https://biocontainers.pro/tools/gubbins", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gubbins", "latest": {"3.2.1--py39pl5321h87d955d_0": "sha256:18221405d72b5ba7ca93aa9098cb99b73cc290ef0c1f60104ac29a40dc9d1cff"}, "tags": {"3.2.1--py39pl5321h87d955d_0": "sha256:18221405d72b5ba7ca93aa9098cb99b73cc290ef0c1f60104ac29a40dc9d1cff"}, "docker": "quay.io/biocontainers/gubbins", "aliases": {"extract_gubbins_clade.py": "/usr/local/bin/extract_gubbins_clade.py", "generate_ska_alignment.py": "/usr/local/bin/generate_ska_alignment.py", "gubbins": "/usr/local/bin/gubbins", "gubbins_alignment_checker.py": "/usr/local/bin/gubbins_alignment_checker.py", "mask_gubbins_aln.py": "/usr/local/bin/mask_gubbins_aln.py", "rapidnj": "/usr/local/bin/rapidnj", "raxml-ng": "/usr/local/bin/raxml-ng", "raxml-ng-mpi": "/usr/local/bin/raxml-ng-mpi", "run_gubbins.py": "/usr/local/bin/run_gubbins.py", "ska": "/usr/local/bin/ska", "iqtree": "/usr/local/bin/iqtree", "raxmlHPC": "/usr/local/bin/raxmlHPC", "raxmlHPC-AVX2": "/usr/local/bin/raxmlHPC-AVX2", "raxmlHPC-PTHREADS": "/usr/local/bin/raxmlHPC-PTHREADS", "raxmlHPC-PTHREADS-AVX2": "/usr/local/bin/raxmlHPC-PTHREADS-AVX2", "raxmlHPC-PTHREADS-SSE3": "/usr/local/bin/raxmlHPC-PTHREADS-SSE3", "raxmlHPC-SSE3": "/usr/local/bin/raxmlHPC-SSE3", "dendropy-format": "/usr/local/bin/dendropy-format", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gubbins.
shpc-registry automated BioContainers addition for gubbins
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gubbins
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gubbins:3.2.1--py39pl5321h87d955d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gubbins/3.2.1--py39pl5321h87d955d_0
$ module help quay.io/biocontainers/gubbins/3.2.1--py39pl5321h87d955d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gubbins-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gubbins-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gubbins-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gubbins-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gubbins-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gubbins-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### extract_gubbins_clade.py

```bash
$ singularity exec <container> /usr/local/bin/extract_gubbins_clade.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_gubbins_clade.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_gubbins_clade.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_ska_alignment.py

```bash
$ singularity exec <container> /usr/local/bin/generate_ska_alignment.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_ska_alignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_ska_alignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gubbins

```bash
$ singularity exec <container> /usr/local/bin/gubbins
$ podman run --it --rm --entrypoint /usr/local/bin/gubbins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gubbins   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gubbins_alignment_checker.py

```bash
$ singularity exec <container> /usr/local/bin/gubbins_alignment_checker.py
$ podman run --it --rm --entrypoint /usr/local/bin/gubbins_alignment_checker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gubbins_alignment_checker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mask_gubbins_aln.py

```bash
$ singularity exec <container> /usr/local/bin/mask_gubbins_aln.py
$ podman run --it --rm --entrypoint /usr/local/bin/mask_gubbins_aln.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mask_gubbins_aln.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidnj

```bash
$ singularity exec <container> /usr/local/bin/rapidnj
$ podman run --it --rm --entrypoint /usr/local/bin/rapidnj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidnj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng-mpi

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_gubbins.py

```bash
$ singularity exec <container> /usr/local/bin/run_gubbins.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_gubbins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_gubbins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ska

```bash
$ singularity exec <container> /usr/local/bin/ska
$ podman run --it --rm --entrypoint /usr/local/bin/ska   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ska   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
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