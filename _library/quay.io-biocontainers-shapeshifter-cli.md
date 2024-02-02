---
layout: container
name:  "quay.io/biocontainers/shapeshifter-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shapeshifter-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shapeshifter-cli/container.yaml"
updated_at: "2024-02-02 02:55:18.897773"
latest: "1.0.0--py_0"
container_url: "https://biocontainers.pro/tools/shapeshifter-cli"
aliases:
 - "plasma_store_server"
 - "pzstd"
 - "shapeshift"
 - "shapeshiftmerge"
 - "ss"
 - "ssm"
 - "thrift"
 - "plasma_store"
 - "gflags_completions.sh"
 - "runxlrd.py"
 - "vba_extract.py"
 - "jupyter-trust"
 - "jupyter"
 - "jupyter-migrate"
 - "jupyter-troubleshoot"
 - "jsonschema"
 - "protoc"
versions:
 - "1.0.0--py_0"
description: "shpc-registry automated BioContainers addition for shapeshifter-cli"
config: {"url": "https://biocontainers.pro/tools/shapeshifter-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shapeshifter-cli", "latest": {"1.0.0--py_0": "sha256:7367db6f5c4ab92446e8ba58323c13e280d8b5bec5ab1827592a6ddf77e23a10"}, "tags": {"1.0.0--py_0": "sha256:7367db6f5c4ab92446e8ba58323c13e280d8b5bec5ab1827592a6ddf77e23a10"}, "docker": "quay.io/biocontainers/shapeshifter-cli", "aliases": {"plasma_store_server": "/usr/local/bin/plasma_store_server", "pzstd": "/usr/local/bin/pzstd", "shapeshift": "/usr/local/bin/shapeshift", "shapeshiftmerge": "/usr/local/bin/shapeshiftmerge", "ss": "/usr/local/bin/ss", "ssm": "/usr/local/bin/ssm", "thrift": "/usr/local/bin/thrift", "plasma_store": "/usr/local/bin/plasma_store", "gflags_completions.sh": "/usr/local/bin/gflags_completions.sh", "runxlrd.py": "/usr/local/bin/runxlrd.py", "vba_extract.py": "/usr/local/bin/vba_extract.py", "jupyter-trust": "/usr/local/bin/jupyter-trust", "jupyter": "/usr/local/bin/jupyter", "jupyter-migrate": "/usr/local/bin/jupyter-migrate", "jupyter-troubleshoot": "/usr/local/bin/jupyter-troubleshoot", "jsonschema": "/usr/local/bin/jsonschema", "protoc": "/usr/local/bin/protoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shapeshifter-cli.
shpc-registry automated BioContainers addition for shapeshifter-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shapeshifter-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shapeshifter-cli:1.0.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shapeshifter-cli/1.0.0--py_0
$ module help quay.io/biocontainers/shapeshifter-cli/1.0.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shapeshifter-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shapeshifter-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shapeshifter-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shapeshifter-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shapeshifter-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shapeshifter-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plasma_store_server

```bash
$ singularity exec <container> /usr/local/bin/plasma_store_server
$ podman run --it --rm --entrypoint /usr/local/bin/plasma_store_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma_store_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pzstd

```bash
$ singularity exec <container> /usr/local/bin/pzstd
$ podman run --it --rm --entrypoint /usr/local/bin/pzstd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pzstd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shapeshift

```bash
$ singularity exec <container> /usr/local/bin/shapeshift
$ podman run --it --rm --entrypoint /usr/local/bin/shapeshift   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shapeshift   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shapeshiftmerge

```bash
$ singularity exec <container> /usr/local/bin/shapeshiftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/shapeshiftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shapeshiftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ss

```bash
$ singularity exec <container> /usr/local/bin/ss
$ podman run --it --rm --entrypoint /usr/local/bin/ss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssm

```bash
$ singularity exec <container> /usr/local/bin/ssm
$ podman run --it --rm --entrypoint /usr/local/bin/ssm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thrift

```bash
$ singularity exec <container> /usr/local/bin/thrift
$ podman run --it --rm --entrypoint /usr/local/bin/thrift   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thrift   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma_store

```bash
$ singularity exec <container> /usr/local/bin/plasma_store
$ podman run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags_completions.sh

```bash
$ singularity exec <container> /usr/local/bin/gflags_completions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runxlrd.py

```bash
$ singularity exec <container> /usr/local/bin/runxlrd.py
$ podman run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter

```bash
$ singularity exec <container> /usr/local/bin/jupyter
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-migrate

```bash
$ singularity exec <container> /usr/local/bin/jupyter-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-troubleshoot

```bash
$ singularity exec <container> /usr/local/bin/jupyter-troubleshoot
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc

```bash
$ singularity exec <container> /usr/local/bin/protoc
$ podman run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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