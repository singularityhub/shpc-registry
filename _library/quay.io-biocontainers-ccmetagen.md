---
layout: container
name:  "quay.io/biocontainers/ccmetagen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ccmetagen/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ccmetagen/container.yaml"
updated_at: "2022-10-27 00:32:51.812979"
latest: "1.4.0--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/ccmetagen"
aliases:
 - "CCMetagen.py"
 - "CCMetagen_extract_seqs.py"
 - "CCMetagen_merge.py"
versions:
 - "1.4.0--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for ccmetagen"
config: {"url": "https://biocontainers.pro/tools/ccmetagen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ccmetagen", "latest": {"1.4.0--pyh5e36f6f_0": "sha256:32a2c8f007b83e50e3e428683eabf083623dd33f7bef88c61f811dc777c9cdb1"}, "tags": {"1.4.0--pyh5e36f6f_0": "sha256:32a2c8f007b83e50e3e428683eabf083623dd33f7bef88c61f811dc777c9cdb1"}, "docker": "quay.io/biocontainers/ccmetagen", "aliases": {"CCMetagen.py": "/usr/local/bin/CCMetagen.py", "CCMetagen_extract_seqs.py": "/usr/local/bin/CCMetagen_extract_seqs.py", "CCMetagen_merge.py": "/usr/local/bin/CCMetagen_merge.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ccmetagen.
shpc-registry automated BioContainers addition for ccmetagen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ccmetagen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ccmetagen:1.4.0--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ccmetagen/1.4.0--pyh5e36f6f_0
$ module help quay.io/biocontainers/ccmetagen/1.4.0--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ccmetagen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ccmetagen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ccmetagen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ccmetagen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ccmetagen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ccmetagen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CCMetagen.py

```bash
$ singularity exec <container> /usr/local/bin/CCMetagen.py
$ podman run --it --rm --entrypoint /usr/local/bin/CCMetagen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CCMetagen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CCMetagen_extract_seqs.py

```bash
$ singularity exec <container> /usr/local/bin/CCMetagen_extract_seqs.py
$ podman run --it --rm --entrypoint /usr/local/bin/CCMetagen_extract_seqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CCMetagen_extract_seqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CCMetagen_merge.py

```bash
$ singularity exec <container> /usr/local/bin/CCMetagen_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/CCMetagen_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CCMetagen_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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