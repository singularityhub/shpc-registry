---
layout: container
name:  "quay.io/biocontainers/ntjoin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ntjoin/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ntjoin/container.yaml"
updated_at: "2022-10-27 01:11:07.639065"
latest: "1.1.1--py39h6935b12_0"
container_url: "https://biocontainers.pro/tools/ntjoin"
aliases:
 - "indexlr"
 - "lrunzip"
 - "lrzcat"
 - "lrzip"
 - "lrztar"
 - "lrzuntar"
 - "ntJoin"
 - "ntjoin_assemble.py"
 - "ntjoin_overlap.py"
 - "ntjoin_utils.py"
 - "read_fasta.py"
versions:
 - "1.1.1--py39h6935b12_0"
description: "shpc-registry automated BioContainers addition for ntjoin"
config: {"url": "https://biocontainers.pro/tools/ntjoin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ntjoin", "latest": {"1.1.1--py39h6935b12_0": "sha256:c575f6cb1507232dfc6fa7e37ed579ff4a8625e2bfd11c980042588aebc43d2b"}, "tags": {"1.1.1--py39h6935b12_0": "sha256:c575f6cb1507232dfc6fa7e37ed579ff4a8625e2bfd11c980042588aebc43d2b"}, "docker": "quay.io/biocontainers/ntjoin", "aliases": {"indexlr": "/usr/local/bin/indexlr", "lrunzip": "/usr/local/bin/lrunzip", "lrzcat": "/usr/local/bin/lrzcat", "lrzip": "/usr/local/bin/lrzip", "lrztar": "/usr/local/bin/lrztar", "lrzuntar": "/usr/local/bin/lrzuntar", "ntJoin": "/usr/local/bin/ntJoin", "ntjoin_assemble.py": "/usr/local/bin/ntjoin_assemble.py", "ntjoin_overlap.py": "/usr/local/bin/ntjoin_overlap.py", "ntjoin_utils.py": "/usr/local/bin/ntjoin_utils.py", "read_fasta.py": "/usr/local/bin/read_fasta.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ntjoin.
shpc-registry automated BioContainers addition for ntjoin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ntjoin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ntjoin:1.1.1--py39h6935b12_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ntjoin/1.1.1--py39h6935b12_0
$ module help quay.io/biocontainers/ntjoin/1.1.1--py39h6935b12_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ntjoin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ntjoin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ntjoin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ntjoin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ntjoin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ntjoin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### indexlr

```bash
$ singularity exec <container> /usr/local/bin/indexlr
$ podman run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrunzip

```bash
$ singularity exec <container> /usr/local/bin/lrunzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzcat

```bash
$ singularity exec <container> /usr/local/bin/lrzcat
$ podman run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzip

```bash
$ singularity exec <container> /usr/local/bin/lrzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrztar

```bash
$ singularity exec <container> /usr/local/bin/lrztar
$ podman run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzuntar

```bash
$ singularity exec <container> /usr/local/bin/lrzuntar
$ podman run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntJoin

```bash
$ singularity exec <container> /usr/local/bin/ntJoin
$ podman run --it --rm --entrypoint /usr/local/bin/ntJoin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntJoin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntjoin_assemble.py

```bash
$ singularity exec <container> /usr/local/bin/ntjoin_assemble.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntjoin_assemble.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntjoin_assemble.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntjoin_overlap.py

```bash
$ singularity exec <container> /usr/local/bin/ntjoin_overlap.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntjoin_overlap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntjoin_overlap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntjoin_utils.py

```bash
$ singularity exec <container> /usr/local/bin/ntjoin_utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntjoin_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntjoin_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/read_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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