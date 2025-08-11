---
layout: container
name:  "quay.io/biocontainers/dendropy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dendropy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dendropy/container.yaml"
updated_at: "2025-08-11 04:02:51.109496"
latest: "5.0.8--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/dendropy"
aliases:
 - "dendropy-format"
 - "sumlabels.py"
 - "sumtrees.py"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "4.5.2--pyh3252c3a_0"
 - "4.6.0--pyh7cba7a3_0"
 - "4.6.1--pyhdfd78af_0"
 - "5.0.1--pyhdfd78af_0"
 - "5.0.6--pyhdfd78af_0"
 - "5.0.8--pyhdfd78af_0"
 - "5.0.8--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for dendropy"
config: {"url": "https://biocontainers.pro/tools/dendropy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dendropy", "latest": {"5.0.8--pyhdfd78af_1": "sha256:2860ea1b4b318105da63eb6107a5d58a21c9a057447a59f581ae7e4573b2f413"}, "tags": {"4.5.2--pyh3252c3a_0": "sha256:1c6595b3af0f838931fda400b692afe39373703c2dac6522c8ecc0d431aea6b0", "4.6.0--pyh7cba7a3_0": "sha256:1778413bbf7b564ce868a80e0af58ab32b93c8b23efe6539fe3000a6ca1ff099", "4.6.1--pyhdfd78af_0": "sha256:f1312713487965ae3470c0ebb6d4e8d0617e55837be3adc8f29aca45a22f5469", "5.0.1--pyhdfd78af_0": "sha256:744606432b791823e9f71bd8a1b5520e29385775f8812051106de9b8039afdae", "5.0.6--pyhdfd78af_0": "sha256:96c391d7e2bbd464406d63d9edbb66bc16e6f96a1ad433981761efa5994c29a9", "5.0.8--pyhdfd78af_0": "sha256:67527f4adba0657b6ce7cdbcccde3f7e8d0891eeddcbd280f58c2a7bec6f950a", "5.0.8--pyhdfd78af_1": "sha256:2860ea1b4b318105da63eb6107a5d58a21c9a057447a59f581ae7e4573b2f413"}, "docker": "quay.io/biocontainers/dendropy", "aliases": {"dendropy-format": "/usr/local/bin/dendropy-format", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dendropy.
shpc-registry automated BioContainers addition for dendropy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dendropy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dendropy:5.0.8--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dendropy/5.0.8--pyhdfd78af_1
$ module help quay.io/biocontainers/dendropy/5.0.8--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dendropy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dendropy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dendropy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dendropy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dendropy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dendropy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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