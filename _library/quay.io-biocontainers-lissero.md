---
layout: container
name:  "quay.io/biocontainers/lissero"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lissero/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/lissero/container.yaml"
updated_at: "2022-10-29 05:31:08.395973"
latest: "0.4.9--py_0"
container_url: "https://biocontainers.pro/tools/lissero"
aliases:
 - "gfPcr"
 - "isPcr"
 - "lissero"
 - "2to3-3.9"
 - "CA.pm"
 - "accn-at-a-time"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "asp-cp"
 - "asp-ls"
 - "between-two-genes"
 - "blast_formatter"
 - "blastdb_aliastool"
versions:
 - "0.4.9--py_0"
description: "shpc-registry automated BioContainers addition for lissero"
config: {"url": "https://biocontainers.pro/tools/lissero", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lissero", "latest": {"0.4.9--py_0": "sha256:d209fcec504828bfb4338764d476032d9d7fa213fbeaf3d6c8656f25532abf3d"}, "tags": {"0.4.9--py_0": "sha256:d209fcec504828bfb4338764d476032d9d7fa213fbeaf3d6c8656f25532abf3d"}, "docker": "quay.io/biocontainers/lissero", "aliases": {"gfPcr": "/usr/local/bin/gfPcr", "isPcr": "/usr/local/bin/isPcr", "lissero": "/usr/local/bin/lissero", "2to3-3.9": "/usr/local/bin/2to3-3.9", "CA.pm": "/usr/local/bin/CA.pm", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asp-cp": "/usr/local/bin/asp-cp", "asp-ls": "/usr/local/bin/asp-ls", "between-two-genes": "/usr/local/bin/between-two-genes", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lissero.
shpc-registry automated BioContainers addition for lissero
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lissero
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lissero:0.4.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lissero/0.4.9--py_0
$ module help quay.io/biocontainers/lissero/0.4.9--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lissero-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lissero-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lissero-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lissero-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lissero-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lissero-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfPcr

```bash
$ singularity exec <container> /usr/local/bin/gfPcr
$ podman run --it --rm --entrypoint /usr/local/bin/gfPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isPcr

```bash
$ singularity exec <container> /usr/local/bin/isPcr
$ podman run --it --rm --entrypoint /usr/local/bin/isPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lissero

```bash
$ singularity exec <container> /usr/local/bin/lissero
$ podman run --it --rm --entrypoint /usr/local/bin/lissero   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lissero   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-cp

```bash
$ singularity exec <container> /usr/local/bin/asp-cp
$ podman run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-ls

```bash
$ singularity exec <container> /usr/local/bin/asp-ls
$ podman run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### between-two-genes

```bash
$ singularity exec <container> /usr/local/bin/between-two-genes
$ podman run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
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