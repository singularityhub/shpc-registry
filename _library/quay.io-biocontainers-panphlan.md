---
layout: container
name:  "quay.io/biocontainers/panphlan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/panphlan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/panphlan/container.yaml"
updated_at: "2024-04-04 04:12:58.683407"
latest: "3.1--py_0"
container_url: "https://biocontainers.pro/tools/panphlan"
aliases:
 - "misc.py"
 - "panphlan_download_pangenome.py"
 - "panphlan_map.py"
 - "panphlan_profiling.py"
 - "perl5.32.0"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
 - "bowtie2-inspect-s"
versions:
 - "3.1--py_0"
description: "shpc-registry automated BioContainers addition for panphlan"
config: {"url": "https://biocontainers.pro/tools/panphlan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for panphlan", "latest": {"3.1--py_0": "sha256:4fbdbf8c2c65b88ace3a165bc1c99ea5eac4799b57c5a1ad5fcb45f1dcc2a06f"}, "tags": {"3.1--py_0": "sha256:4fbdbf8c2c65b88ace3a165bc1c99ea5eac4799b57c5a1ad5fcb45f1dcc2a06f"}, "docker": "quay.io/biocontainers/panphlan", "aliases": {"misc.py": "/usr/local/bin/misc.py", "panphlan_download_pangenome.py": "/usr/local/bin/panphlan_download_pangenome.py", "panphlan_map.py": "/usr/local/bin/panphlan_map.py", "panphlan_profiling.py": "/usr/local/bin/panphlan_profiling.py", "perl5.32.0": "/usr/local/bin/perl5.32.0", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect", "bowtie2-inspect-l": "/usr/local/bin/bowtie2-inspect-l", "bowtie2-inspect-s": "/usr/local/bin/bowtie2-inspect-s"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/panphlan.
shpc-registry automated BioContainers addition for panphlan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/panphlan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/panphlan:3.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/panphlan/3.1--py_0
$ module help quay.io/biocontainers/panphlan/3.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### panphlan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### panphlan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### panphlan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### panphlan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### panphlan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### panphlan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### misc.py

```bash
$ singularity exec <container> /usr/local/bin/misc.py
$ podman run --it --rm --entrypoint /usr/local/bin/misc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/misc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panphlan_download_pangenome.py

```bash
$ singularity exec <container> /usr/local/bin/panphlan_download_pangenome.py
$ podman run --it --rm --entrypoint /usr/local/bin/panphlan_download_pangenome.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panphlan_download_pangenome.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panphlan_map.py

```bash
$ singularity exec <container> /usr/local/bin/panphlan_map.py
$ podman run --it --rm --entrypoint /usr/local/bin/panphlan_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panphlan_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panphlan_profiling.py

```bash
$ singularity exec <container> /usr/local/bin/panphlan_profiling.py
$ podman run --it --rm --entrypoint /usr/local/bin/panphlan_profiling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panphlan_profiling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
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