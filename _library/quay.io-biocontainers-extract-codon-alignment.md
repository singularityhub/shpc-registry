---
layout: container
name:  "quay.io/biocontainers/extract-codon-alignment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/extract-codon-alignment/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/extract-codon-alignment/container.yaml"
updated_at: "2022-10-27 00:55:41.069484"
latest: "0.0.1--py_0"
container_url: "https://biocontainers.pro/tools/extract-codon-alignment"
aliases:
 - "extract_codon_alignment"
versions:
 - "0.0.1--py_0"
description: "shpc-registry automated BioContainers addition for extract-codon-alignment"
config: {"url": "https://biocontainers.pro/tools/extract-codon-alignment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for extract-codon-alignment", "latest": {"0.0.1--py_0": "sha256:b7c2568a3db0e603987d01f0b5d1e1bb2474cbb409767d9cca51963bc5caa3cc"}, "tags": {"0.0.1--py_0": "sha256:b7c2568a3db0e603987d01f0b5d1e1bb2474cbb409767d9cca51963bc5caa3cc"}, "docker": "quay.io/biocontainers/extract-codon-alignment", "aliases": {"extract_codon_alignment": "/usr/local/bin/extract_codon_alignment"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/extract-codon-alignment.
shpc-registry automated BioContainers addition for extract-codon-alignment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/extract-codon-alignment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/extract-codon-alignment:0.0.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/extract-codon-alignment/0.0.1--py_0
$ module help quay.io/biocontainers/extract-codon-alignment/0.0.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### extract-codon-alignment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### extract-codon-alignment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### extract-codon-alignment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### extract-codon-alignment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### extract-codon-alignment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### extract-codon-alignment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### extract_codon_alignment

```bash
$ singularity exec <container> /usr/local/bin/extract_codon_alignment
$ podman run --it --rm --entrypoint /usr/local/bin/extract_codon_alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_codon_alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
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