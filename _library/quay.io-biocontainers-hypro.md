---
layout: container
name:  "quay.io/biocontainers/hypro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hypro/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hypro/container.yaml"
updated_at: "2022-10-29 05:46:14.787219"
latest: "0.1--py_0"
container_url: "https://biocontainers.pro/tools/hypro"
aliases:
 - "hypro.py"
 - "mmseqs2.sh"
 - "2to3-3.7"
 - "SOAPsh.pl"
 - "ace.pl"
 - "acyclic"
 - "alimask"
 - "amino-acid-composition"
 - "annotate"
 - "annotateBed"
 - "aragorn"
 - "archive-pubmed"
versions:
 - "0.1--py_0"
description: "shpc-registry automated BioContainers addition for hypro"
config: {"url": "https://biocontainers.pro/tools/hypro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hypro", "latest": {"0.1--py_0": "sha256:22ca9b67892d4b173666a4819253d34a068dbea4cc601bc702d3cbb52496bca8"}, "tags": {"0.1--py_0": "sha256:22ca9b67892d4b173666a4819253d34a068dbea4cc601bc702d3cbb52496bca8"}, "docker": "quay.io/biocontainers/hypro", "aliases": {"hypro.py": "/usr/local/bin/hypro.py", "mmseqs2.sh": "/usr/local/bin/mmseqs2.sh", "2to3-3.7": "/usr/local/bin/2to3-3.7", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "ace.pl": "/usr/local/bin/ace.pl", "acyclic": "/usr/local/bin/acyclic", "alimask": "/usr/local/bin/alimask", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "annotate": "/usr/local/bin/annotate", "annotateBed": "/usr/local/bin/annotateBed", "aragorn": "/usr/local/bin/aragorn", "archive-pubmed": "/usr/local/bin/archive-pubmed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hypro.
shpc-registry automated BioContainers addition for hypro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hypro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hypro:0.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hypro/0.1--py_0
$ module help quay.io/biocontainers/hypro/0.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hypro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hypro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hypro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hypro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hypro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hypro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hypro.py

```bash
$ singularity exec <container> /usr/local/bin/hypro.py
$ podman run --it --rm --entrypoint /usr/local/bin/hypro.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hypro.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs2.sh

```bash
$ singularity exec <container> /usr/local/bin/mmseqs2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aragorn

```bash
$ singularity exec <container> /usr/local/bin/aragorn
$ podman run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
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