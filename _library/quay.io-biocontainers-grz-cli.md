---
layout: container
name:  "quay.io/biocontainers/grz-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grz-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grz-cli/container.yaml"
updated_at: "2025-01-09 13:35:54.396842"
latest: "0.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/grz-cli"
aliases:
 - "crypt4gh"
 - "crypt4gh-keygen"
 - "grz-cli"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "jp.py"
 - "jsonschema"
 - "tqdm"
versions:
 - "0.1.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for grz-cli"
config: {"url": "https://biocontainers.pro/tools/grz-cli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grz-cli", "latest": {"0.1.1--pyhdfd78af_0": "sha256:3d1d63ab7ff383a0cb440daa3f861042eb043745416cf1caeef8ee06cede240c"}, "tags": {"0.1.1--pyhdfd78af_0": "sha256:3d1d63ab7ff383a0cb440daa3f861042eb043745416cf1caeef8ee06cede240c"}, "docker": "quay.io/biocontainers/grz-cli", "aliases": {"crypt4gh": "/usr/local/bin/crypt4gh", "crypt4gh-keygen": "/usr/local/bin/crypt4gh-keygen", "grz-cli": "/usr/local/bin/grz-cli", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "jp.py": "/usr/local/bin/jp.py", "jsonschema": "/usr/local/bin/jsonschema", "tqdm": "/usr/local/bin/tqdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grz-cli.
singularity registry hpc automated addition for grz-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grz-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grz-cli:0.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grz-cli/0.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/grz-cli/0.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grz-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grz-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grz-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grz-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grz-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grz-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crypt4gh

```bash
$ singularity exec <container> /usr/local/bin/crypt4gh
$ podman run --it --rm --entrypoint /usr/local/bin/crypt4gh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crypt4gh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crypt4gh-keygen

```bash
$ singularity exec <container> /usr/local/bin/crypt4gh-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/crypt4gh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crypt4gh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grz-cli

```bash
$ singularity exec <container> /usr/local/bin/grz-cli
$ podman run --it --rm --entrypoint /usr/local/bin/grz-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grz-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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