---
layout: container
name:  "quay.io/biocontainers/degenotate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/degenotate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/degenotate/container.yaml"
updated_at: "2024-09-05 04:32:01.697808"
latest: "1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/degenotate"
aliases:
 - "degenotate.py"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "1.1.2--pyhdfd78af_0"
 - "1.1.3--pyhdfd78af_0"
 - "1.2.1--pyhdfd78af_0"
 - "1.2.2--pyhdfd78af_0"
 - "1.2.4--pyhdfd78af_0"
 - "1.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for degenotate"
config: {"url": "https://biocontainers.pro/tools/degenotate", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for degenotate", "latest": {"1.3--pyhdfd78af_0": "sha256:53c02a44a74e03b2c2a75250d5dd2bc436e58d6720d73a5ef24951f84a4a889b"}, "tags": {"1.1.2--pyhdfd78af_0": "sha256:3feb46e6814af282497e051be937b075ed742cafeb64e51f72a3a265d203c447", "1.1.3--pyhdfd78af_0": "sha256:2994dbbddf9b7e0a454e26c3da599db8fd4e8e5285b097042086de71bc8240a9", "1.2.1--pyhdfd78af_0": "sha256:88ca3292b59de074d75c8aecba5dff3e64471f04863d92dc2ecc1ab061d96b08", "1.2.2--pyhdfd78af_0": "sha256:08293c27b0bdcde75dfa5b5a8d194593740b316dee8f91626161e2816c37eaab", "1.2.4--pyhdfd78af_0": "sha256:be9ae0fc37ba1c15002bd9bf61e826a95fda996a4c3909eded30b1e5425be3c5", "1.3--pyhdfd78af_0": "sha256:53c02a44a74e03b2c2a75250d5dd2bc436e58d6720d73a5ef24951f84a4a889b"}, "docker": "quay.io/biocontainers/degenotate", "aliases": {"degenotate.py": "/usr/local/bin/degenotate.py", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/degenotate.
singularity registry hpc automated addition for degenotate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/degenotate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/degenotate:1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/degenotate/1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/degenotate/1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### degenotate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### degenotate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### degenotate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### degenotate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### degenotate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### degenotate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### degenotate.py

```bash
$ singularity exec <container> /usr/local/bin/degenotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/degenotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/degenotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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