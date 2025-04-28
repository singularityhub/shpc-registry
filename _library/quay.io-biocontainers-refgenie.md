---
layout: container
name:  "quay.io/biocontainers/refgenie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/refgenie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/refgenie/container.yaml"
updated_at: "2025-04-28 04:02:44.989716"
latest: "0.12.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/refgenie"
aliases:
 - "import_igenome"
 - "refgenie"
 - "py.test"
 - "pytest"
 - "faidx"
 - "tqdm"
 - "futurize"
 - "pasteurize"
 - "f2py3.8"
 - "chardetect"
 - "2to3-3.8"
 - "idle3.8"
versions:
 - "0.9.3--py_0"
 - "0.12.1--pyhdfd78af_0"
 - "0.11.0--pyhdfd78af_0"
 - "0.10.0--py_0"
description: "shpc-registry automated BioContainers addition for refgenie"
config: {"url": "https://biocontainers.pro/tools/refgenie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for refgenie", "latest": {"0.12.1--pyhdfd78af_0": "sha256:02aff229054b149ba6062349fa95e0fd3f71998899ce551306fe81f2b120f0a2"}, "tags": {"0.9.3--py_0": "sha256:2738ae3a3dd8e3163c4c9e39349e1eb26954639c05de55b8d4df8dde5a2df78d", "0.12.1--pyhdfd78af_0": "sha256:02aff229054b149ba6062349fa95e0fd3f71998899ce551306fe81f2b120f0a2", "0.11.0--pyhdfd78af_0": "sha256:07962ae5df1c752bff11dd84f6233dd2170829e57c3f3b63c6f3b057cef13b83", "0.10.0--py_0": "sha256:8515215e5487f615fa3142536339d5b7725b21586cc7ae380e432e96d021e2a2"}, "docker": "quay.io/biocontainers/refgenie", "aliases": {"import_igenome": "/usr/local/bin/import_igenome", "refgenie": "/usr/local/bin/refgenie", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "faidx": "/usr/local/bin/faidx", "tqdm": "/usr/local/bin/tqdm", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "f2py3.8": "/usr/local/bin/f2py3.8", "chardetect": "/usr/local/bin/chardetect", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/refgenie.
shpc-registry automated BioContainers addition for refgenie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/refgenie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/refgenie:0.12.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/refgenie/0.12.1--pyhdfd78af_0
$ module help quay.io/biocontainers/refgenie/0.12.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### refgenie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### refgenie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### refgenie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### refgenie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### refgenie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### refgenie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### import_igenome

```bash
$ singularity exec <container> /usr/local/bin/import_igenome
$ podman run --it --rm --entrypoint /usr/local/bin/import_igenome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_igenome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refgenie

```bash
$ singularity exec <container> /usr/local/bin/refgenie
$ podman run --it --rm --entrypoint /usr/local/bin/refgenie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refgenie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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