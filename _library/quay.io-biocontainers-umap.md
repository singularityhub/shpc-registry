---
layout: container
name:  "quay.io/biocontainers/umap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/umap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/umap/container.yaml"
updated_at: "2024-04-14 03:58:45.188776"
latest: "1.1.1--pyh1687a27_0"
container_url: "https://biocontainers.pro/tools/umap"
aliases:
 - "__init__.py"
 - "combine_umaps.py"
 - "get_kmers.py"
 - "handle_fasta.py"
 - "map_bed.py"
 - "run_bowtie.py"
 - "ubismap.py"
 - "uint8_to_bed.py"
 - "uint8_to_bed_parallel.py"
 - "unify_bowtie.py"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
 - "f2py2"
versions:
 - "1.1.1--pyh1687a27_0"
description: "shpc-registry automated BioContainers addition for umap"
config: {"url": "https://biocontainers.pro/tools/umap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for umap", "latest": {"1.1.1--pyh1687a27_0": "sha256:33d464374871b19aa35abb1964593708aa68c83690f6096fb98930bef956674a"}, "tags": {"1.1.1--pyh1687a27_0": "sha256:33d464374871b19aa35abb1964593708aa68c83690f6096fb98930bef956674a"}, "docker": "quay.io/biocontainers/umap", "aliases": {"__init__.py": "/usr/local/bin/__init__.py", "combine_umaps.py": "/usr/local/bin/combine_umaps.py", "get_kmers.py": "/usr/local/bin/get_kmers.py", "handle_fasta.py": "/usr/local/bin/handle_fasta.py", "map_bed.py": "/usr/local/bin/map_bed.py", "run_bowtie.py": "/usr/local/bin/run_bowtie.py", "ubismap.py": "/usr/local/bin/ubismap.py", "uint8_to_bed.py": "/usr/local/bin/uint8_to_bed.py", "uint8_to_bed_parallel.py": "/usr/local/bin/uint8_to_bed_parallel.py", "unify_bowtie.py": "/usr/local/bin/unify_bowtie.py", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect", "f2py2": "/usr/local/bin/f2py2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/umap.
shpc-registry automated BioContainers addition for umap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/umap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/umap:1.1.1--pyh1687a27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/umap/1.1.1--pyh1687a27_0
$ module help quay.io/biocontainers/umap/1.1.1--pyh1687a27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### umap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### umap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### umap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### umap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### umap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### umap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### __init__.py

```bash
$ singularity exec <container> /usr/local/bin/__init__.py
$ podman run --it --rm --entrypoint /usr/local/bin/__init__.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/__init__.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_umaps.py

```bash
$ singularity exec <container> /usr/local/bin/combine_umaps.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_umaps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_umaps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_kmers.py

```bash
$ singularity exec <container> /usr/local/bin/get_kmers.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_kmers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_kmers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### handle_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/handle_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/handle_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/handle_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_bed.py

```bash
$ singularity exec <container> /usr/local/bin/map_bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_bowtie.py

```bash
$ singularity exec <container> /usr/local/bin/run_bowtie.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_bowtie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_bowtie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ubismap.py

```bash
$ singularity exec <container> /usr/local/bin/ubismap.py
$ podman run --it --rm --entrypoint /usr/local/bin/ubismap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ubismap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uint8_to_bed.py

```bash
$ singularity exec <container> /usr/local/bin/uint8_to_bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/uint8_to_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uint8_to_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uint8_to_bed_parallel.py

```bash
$ singularity exec <container> /usr/local/bin/uint8_to_bed_parallel.py
$ podman run --it --rm --entrypoint /usr/local/bin/uint8_to_bed_parallel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uint8_to_bed_parallel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unify_bowtie.py

```bash
$ singularity exec <container> /usr/local/bin/unify_bowtie.py
$ podman run --it --rm --entrypoint /usr/local/bin/unify_bowtie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unify_bowtie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
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