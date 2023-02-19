---
layout: container
name:  "quay.io/biocontainers/ditasic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ditasic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ditasic/container.yaml"
updated_at: "2023-02-19 03:27:42.363487"
latest: "0.2--h9ee0642_2"
container_url: "https://biocontainers.pro/tools/ditasic"
aliases:
 - "ditasic"
 - "ditasic_mapping.py"
 - "ditasic_matrix.py"
 - "kallisto"
 - "mason_frag_sequencing"
 - "mason_genome"
 - "mason_materializer"
 - "mason_methylation"
 - "mason_simulator"
 - "mason_splicing"
 - "mason_variator"
 - "f2py3.9"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5copy"
 - "h5debug"
versions:
 - "0.2--h9ee0642_2"
description: "shpc-registry automated BioContainers addition for ditasic"
config: {"url": "https://biocontainers.pro/tools/ditasic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ditasic", "latest": {"0.2--h9ee0642_2": "sha256:2e1db75a4a134cfdb572aa7abc44be10bb4945bf7269b71f0bfc18d4a4adf7e5"}, "tags": {"0.2--h9ee0642_2": "sha256:2e1db75a4a134cfdb572aa7abc44be10bb4945bf7269b71f0bfc18d4a4adf7e5"}, "docker": "quay.io/biocontainers/ditasic", "aliases": {"ditasic": "/usr/local/bin/ditasic", "ditasic_mapping.py": "/usr/local/bin/ditasic_mapping.py", "ditasic_matrix.py": "/usr/local/bin/ditasic_matrix.py", "kallisto": "/usr/local/bin/kallisto", "mason_frag_sequencing": "/usr/local/bin/mason_frag_sequencing", "mason_genome": "/usr/local/bin/mason_genome", "mason_materializer": "/usr/local/bin/mason_materializer", "mason_methylation": "/usr/local/bin/mason_methylation", "mason_simulator": "/usr/local/bin/mason_simulator", "mason_splicing": "/usr/local/bin/mason_splicing", "mason_variator": "/usr/local/bin/mason_variator", "f2py3.9": "/usr/local/bin/f2py3.9", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ditasic.
shpc-registry automated BioContainers addition for ditasic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ditasic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ditasic:0.2--h9ee0642_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ditasic/0.2--h9ee0642_2
$ module help quay.io/biocontainers/ditasic/0.2--h9ee0642_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ditasic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ditasic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ditasic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ditasic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ditasic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ditasic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ditasic

```bash
$ singularity exec <container> /usr/local/bin/ditasic
$ podman run --it --rm --entrypoint /usr/local/bin/ditasic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ditasic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ditasic_mapping.py

```bash
$ singularity exec <container> /usr/local/bin/ditasic_mapping.py
$ podman run --it --rm --entrypoint /usr/local/bin/ditasic_mapping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ditasic_mapping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ditasic_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/ditasic_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/ditasic_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ditasic_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_frag_sequencing

```bash
$ singularity exec <container> /usr/local/bin/mason_frag_sequencing
$ podman run --it --rm --entrypoint /usr/local/bin/mason_frag_sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_frag_sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_genome

```bash
$ singularity exec <container> /usr/local/bin/mason_genome
$ podman run --it --rm --entrypoint /usr/local/bin/mason_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_materializer

```bash
$ singularity exec <container> /usr/local/bin/mason_materializer
$ podman run --it --rm --entrypoint /usr/local/bin/mason_materializer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_materializer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_methylation

```bash
$ singularity exec <container> /usr/local/bin/mason_methylation
$ podman run --it --rm --entrypoint /usr/local/bin/mason_methylation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_methylation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_simulator

```bash
$ singularity exec <container> /usr/local/bin/mason_simulator
$ podman run --it --rm --entrypoint /usr/local/bin/mason_simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_splicing

```bash
$ singularity exec <container> /usr/local/bin/mason_splicing
$ podman run --it --rm --entrypoint /usr/local/bin/mason_splicing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_splicing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_variator

```bash
$ singularity exec <container> /usr/local/bin/mason_variator
$ podman run --it --rm --entrypoint /usr/local/bin/mason_variator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_variator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /usr/local/bin/h5debug
$ podman run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
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