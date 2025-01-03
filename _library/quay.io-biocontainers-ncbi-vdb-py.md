---
layout: container
name:  "quay.io/biocontainers/ncbi-vdb-py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbi-vdb-py/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncbi-vdb-py/container.yaml"
updated_at: "2025-01-03 03:36:37.708828"
latest: "3.1.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/ncbi-vdb-py"
aliases:
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "3.0.0--hdfd78af_0"
 - "3.0.2--hdfd78af_0"
 - "3.0.5--hdfd78af_0"
 - "3.0.6--hdfd78af_0"
 - "3.0.7--hdfd78af_0"
 - "3.0.8--hdfd78af_0"
 - "3.0.9--hdfd78af_0"
 - "3.1.1--hdfd78af_0"
 - "3.0.10--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for ncbi-vdb-py"
config: {"url": "https://biocontainers.pro/tools/ncbi-vdb-py", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncbi-vdb-py", "latest": {"3.1.1--hdfd78af_0": "sha256:4f5e963924f299fbe11a92100515332f164ce98eaa51fb99175e56a99e01f848"}, "tags": {"3.0.0--hdfd78af_0": "sha256:20d4b99eb6724ef8d903aa6e28fbbe0989ad6185c57a177e30c7f191ad442b83", "3.0.2--hdfd78af_0": "sha256:46b9c36fea38d24c473c7d8da50d470c0f7d3a4993cd8c4d03787c0388abb98c", "3.0.5--hdfd78af_0": "sha256:3f7acf927be36a1e8216e60b7c240a076da7ba68707ef20387f00fde572f9f96", "3.0.6--hdfd78af_0": "sha256:5a0e99b1abaecf7b0c8d8c6f1b3b1fe9842c4a4a4aa5ebc62b58696c985b1203", "3.0.7--hdfd78af_0": "sha256:107eb1aeb7fa4c5960a3e3164f8a4d334d2cd379da01ac4c727c51a98d0d38d8", "3.0.8--hdfd78af_0": "sha256:7e03443e76d37944c4968f1d2a35fc4264f4127ccc12b137e66a20a6729b5ef1", "3.0.9--hdfd78af_0": "sha256:8deee59a75b93185ae2bfd2de39ce69765198f2a0f3dd6ee2bfa060778959a7e", "3.1.1--hdfd78af_0": "sha256:4f5e963924f299fbe11a92100515332f164ce98eaa51fb99175e56a99e01f848", "3.0.10--hdfd78af_0": "sha256:3d6b022dfcfd296a93fe67c136f419415d86f8844d704899e5ab917014fce040"}, "docker": "quay.io/biocontainers/ncbi-vdb-py", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbi-vdb-py.
shpc-registry automated BioContainers addition for ncbi-vdb-py
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbi-vdb-py
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbi-vdb-py:3.1.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbi-vdb-py/3.1.1--hdfd78af_0
$ module help quay.io/biocontainers/ncbi-vdb-py/3.1.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbi-vdb-py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-vdb-py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-vdb-py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbi-vdb-py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbi-vdb-py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-vdb-py-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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