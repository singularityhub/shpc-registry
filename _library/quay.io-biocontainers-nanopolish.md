---
layout: container
name:  "quay.io/biocontainers/nanopolish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanopolish/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nanopolish/container.yaml"
updated_at: "2022-10-27 00:59:46.828329"
latest: "0.9.2--py35_ncurses5.9_4"
container_url: "https://biocontainers.pro/tools/nanopolish"
aliases:
 - "gost-hash"
 - "nanopolish"
 - "nanopolish_makerange.py"
 - "nanopolish_merge.py"
versions:
 - "0.9.2--py35_ncurses5.9_4"
description: "shpc-registry automated BioContainers addition for nanopolish"
config: {"url": "https://biocontainers.pro/tools/nanopolish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanopolish", "latest": {"0.9.2--py35_ncurses5.9_4": "sha256:7ebca1ed0119f110c84c02de5910f874d9345bb4087c6b0763c2102e09607310"}, "tags": {"0.9.2--py35_ncurses5.9_4": "sha256:7ebca1ed0119f110c84c02de5910f874d9345bb4087c6b0763c2102e09607310"}, "docker": "quay.io/biocontainers/nanopolish", "aliases": {"gost-hash": "/usr/local/bin/gost-hash", "nanopolish": "/usr/local/bin/nanopolish", "nanopolish_makerange.py": "/usr/local/bin/nanopolish_makerange.py", "nanopolish_merge.py": "/usr/local/bin/nanopolish_merge.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanopolish.
shpc-registry automated BioContainers addition for nanopolish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanopolish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanopolish:0.9.2--py35_ncurses5.9_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanopolish/0.9.2--py35_ncurses5.9_4
$ module help quay.io/biocontainers/nanopolish/0.9.2--py35_ncurses5.9_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanopolish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanopolish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanopolish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanopolish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanopolish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanopolish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gost-hash

```bash
$ singularity exec <container> /usr/local/bin/gost-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanopolish

```bash
$ singularity exec <container> /usr/local/bin/nanopolish
$ podman run --it --rm --entrypoint /usr/local/bin/nanopolish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanopolish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanopolish_makerange.py

```bash
$ singularity exec <container> /usr/local/bin/nanopolish_makerange.py
$ podman run --it --rm --entrypoint /usr/local/bin/nanopolish_makerange.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanopolish_makerange.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanopolish_merge.py

```bash
$ singularity exec <container> /usr/local/bin/nanopolish_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/nanopolish_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanopolish_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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