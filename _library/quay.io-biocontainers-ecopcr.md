---
layout: container
name:  "quay.io/biocontainers/ecopcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ecopcr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ecopcr/container.yaml"
updated_at: "2022-10-27 00:43:46.703429"
latest: "0.5.0--py27_1"
container_url: "https://biocontainers.pro/tools/ecopcr"
aliases:
 - "ecoPCR"
 - "ecoPCRFilter.py"
 - "ecoPCRFormat.py"
 - "ecoSort.py"
 - "ecofind"
 - "ecogrep"
versions:
 - "0.5.0--py27_1"
description: "shpc-registry automated BioContainers addition for ecopcr"
config: {"url": "https://biocontainers.pro/tools/ecopcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ecopcr", "latest": {"0.5.0--py27_1": "sha256:c9b4e6a807855ed593fde9a7d40586279e7eff1e101139310790261f9bd189c1"}, "tags": {"0.5.0--py27_1": "sha256:c9b4e6a807855ed593fde9a7d40586279e7eff1e101139310790261f9bd189c1"}, "docker": "quay.io/biocontainers/ecopcr", "aliases": {"ecoPCR": "/usr/local/bin/ecoPCR", "ecoPCRFilter.py": "/usr/local/bin/ecoPCRFilter.py", "ecoPCRFormat.py": "/usr/local/bin/ecoPCRFormat.py", "ecoSort.py": "/usr/local/bin/ecoSort.py", "ecofind": "/usr/local/bin/ecofind", "ecogrep": "/usr/local/bin/ecogrep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ecopcr.
shpc-registry automated BioContainers addition for ecopcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ecopcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ecopcr:0.5.0--py27_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ecopcr/0.5.0--py27_1
$ module help quay.io/biocontainers/ecopcr/0.5.0--py27_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ecopcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ecopcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ecopcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ecopcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ecopcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ecopcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ecoPCR

```bash
$ singularity exec <container> /usr/local/bin/ecoPCR
$ podman run --it --rm --entrypoint /usr/local/bin/ecoPCR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecoPCR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecoPCRFilter.py

```bash
$ singularity exec <container> /usr/local/bin/ecoPCRFilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/ecoPCRFilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecoPCRFilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecoPCRFormat.py

```bash
$ singularity exec <container> /usr/local/bin/ecoPCRFormat.py
$ podman run --it --rm --entrypoint /usr/local/bin/ecoPCRFormat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecoPCRFormat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecoSort.py

```bash
$ singularity exec <container> /usr/local/bin/ecoSort.py
$ podman run --it --rm --entrypoint /usr/local/bin/ecoSort.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecoSort.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecofind

```bash
$ singularity exec <container> /usr/local/bin/ecofind
$ podman run --it --rm --entrypoint /usr/local/bin/ecofind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecofind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecogrep

```bash
$ singularity exec <container> /usr/local/bin/ecogrep
$ podman run --it --rm --entrypoint /usr/local/bin/ecogrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecogrep   -v ${PWD} -w ${PWD} <container> -c " $@"
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