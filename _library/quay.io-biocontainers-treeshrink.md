---
layout: container
name:  "quay.io/biocontainers/treeshrink"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treeshrink/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treeshrink/container.yaml"
updated_at: "2025-02-13 03:06:08.239688"
latest: "1.3.9--py39r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/treeshrink"
aliases:
 - "decompose.py"
 - "make_gene_folder.py"
 - "run_treeshrink"
 - "run_treeshrink.py"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.3.9--py39r42hdfd78af_0"
description: "singularity registry hpc automated addition for treeshrink"
config: {"url": "https://biocontainers.pro/tools/treeshrink", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for treeshrink", "latest": {"1.3.9--py39r42hdfd78af_0": "sha256:19f5a8c600594bbbc36735fc5aaabfe50e41d417faaa8d14787524aa2f741aba"}, "tags": {"1.3.9--py39r42hdfd78af_0": "sha256:19f5a8c600594bbbc36735fc5aaabfe50e41d417faaa8d14787524aa2f741aba"}, "docker": "quay.io/biocontainers/treeshrink", "aliases": {"decompose.py": "/usr/local/bin/decompose.py", "make_gene_folder.py": "/usr/local/bin/make_gene_folder.py", "run_treeshrink": "/usr/local/bin/run_treeshrink", "run_treeshrink.py": "/usr/local/bin/run_treeshrink.py", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treeshrink.
singularity registry hpc automated addition for treeshrink
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treeshrink
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treeshrink:1.3.9--py39r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treeshrink/1.3.9--py39r42hdfd78af_0
$ module help quay.io/biocontainers/treeshrink/1.3.9--py39r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treeshrink-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treeshrink-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treeshrink-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treeshrink-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treeshrink-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treeshrink-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### decompose.py

```bash
$ singularity exec <container> /usr/local/bin/decompose.py
$ podman run --it --rm --entrypoint /usr/local/bin/decompose.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/decompose.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_gene_folder.py

```bash
$ singularity exec <container> /usr/local/bin/make_gene_folder.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_gene_folder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_gene_folder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_treeshrink

```bash
$ singularity exec <container> /usr/local/bin/run_treeshrink
$ podman run --it --rm --entrypoint /usr/local/bin/run_treeshrink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_treeshrink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_treeshrink.py

```bash
$ singularity exec <container> /usr/local/bin/run_treeshrink.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_treeshrink.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_treeshrink.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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