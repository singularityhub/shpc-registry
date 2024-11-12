---
layout: container
name:  "quay.io/biocontainers/dbcanlight"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dbcanlight/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dbcanlight/container.yaml"
updated_at: "2024-11-12 03:11:59.441508"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/dbcanlight"
aliases:
 - "dbcanLight"
 - "dbcanLight-hmmparser"
 - "dbcanLight-subparser"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "1.0.0--pyh7cba7a3_0"
 - "1.0.1--pyh7cba7a3_0"
 - "1.0.2--pyh7cba7a3_0"
 - "1.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for dbcanlight"
config: {"url": "https://biocontainers.pro/tools/dbcanlight", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dbcanlight", "latest": {"1.1.0--pyhdfd78af_0": "sha256:a8b0da21fe5d70a669151b7636e66fa8f0a08fa0ded15a90098c4c9be34337f3"}, "tags": {"1.0.0--pyh7cba7a3_0": "sha256:8cc910f8687f27de48da644fefeaa80c0be5355a1885c47ca8a90ac6fc40aa18", "1.0.1--pyh7cba7a3_0": "sha256:bccf0799623d185dd1f4679ce9e31ac54998b72edc1806c36b6da7d6971aa474", "1.0.2--pyh7cba7a3_0": "sha256:cf12ca9d485fd317e746eab9a9c4d86fb45ece13637fee9b59d9f6b14326cc4e", "1.1.0--pyhdfd78af_0": "sha256:a8b0da21fe5d70a669151b7636e66fa8f0a08fa0ded15a90098c4c9be34337f3"}, "docker": "quay.io/biocontainers/dbcanlight", "aliases": {"dbcanLight": "/usr/local/bin/dbcanLight", "dbcanLight-hmmparser": "/usr/local/bin/dbcanLight-hmmparser", "dbcanLight-subparser": "/usr/local/bin/dbcanLight-subparser", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dbcanlight.
singularity registry hpc automated addition for dbcanlight
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dbcanlight
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dbcanlight:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dbcanlight/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/dbcanlight/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dbcanlight-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dbcanlight-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dbcanlight-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dbcanlight-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dbcanlight-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dbcanlight-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dbcanLight

```bash
$ singularity exec <container> /usr/local/bin/dbcanLight
$ podman run --it --rm --entrypoint /usr/local/bin/dbcanLight   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbcanLight   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbcanLight-hmmparser

```bash
$ singularity exec <container> /usr/local/bin/dbcanLight-hmmparser
$ podman run --it --rm --entrypoint /usr/local/bin/dbcanLight-hmmparser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbcanLight-hmmparser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbcanLight-subparser

```bash
$ singularity exec <container> /usr/local/bin/dbcanLight-subparser
$ podman run --it --rm --entrypoint /usr/local/bin/dbcanLight-subparser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbcanLight-subparser   -v ${PWD} -w ${PWD} <container> -c " $@"
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