---
layout: container
name:  "quay.io/biocontainers/sloika"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sloika/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sloika/container.yaml"
updated_at: "2022-10-27 00:50:11.322929"
latest: "2.0.1--np112_0"
container_url: "https://biocontainers.pro/tools/sloika"
aliases:
 - "basecall_network.py"
 - "chunkify.py"
 - "dump_json.py"
 - "extract_reference.py"
 - "theano-test"
 - "train_network.py"
 - "validate_network.py"
 - "verify_network.py"
versions:
 - "2.0.1--np112_0"
description: "shpc-registry automated BioContainers addition for sloika"
config: {"url": "https://biocontainers.pro/tools/sloika", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sloika", "latest": {"2.0.1--np112_0": "sha256:d1a30f58f3e61c1e10eb4262102f01b18cd4db83e1953b148bbd9241d7188545"}, "tags": {"2.0.1--np112_0": "sha256:d1a30f58f3e61c1e10eb4262102f01b18cd4db83e1953b148bbd9241d7188545"}, "docker": "quay.io/biocontainers/sloika", "aliases": {"basecall_network.py": "/usr/local/bin/basecall_network.py", "chunkify.py": "/usr/local/bin/chunkify.py", "dump_json.py": "/usr/local/bin/dump_json.py", "extract_reference.py": "/usr/local/bin/extract_reference.py", "theano-test": "/usr/local/bin/theano-test", "train_network.py": "/usr/local/bin/train_network.py", "validate_network.py": "/usr/local/bin/validate_network.py", "verify_network.py": "/usr/local/bin/verify_network.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sloika.
shpc-registry automated BioContainers addition for sloika
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sloika
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sloika:2.0.1--np112_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sloika/2.0.1--np112_0
$ module help quay.io/biocontainers/sloika/2.0.1--np112_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sloika-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sloika-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sloika-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sloika-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sloika-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sloika-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### basecall_network.py

```bash
$ singularity exec <container> /usr/local/bin/basecall_network.py
$ podman run --it --rm --entrypoint /usr/local/bin/basecall_network.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basecall_network.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chunkify.py

```bash
$ singularity exec <container> /usr/local/bin/chunkify.py
$ podman run --it --rm --entrypoint /usr/local/bin/chunkify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chunkify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dump_json.py

```bash
$ singularity exec <container> /usr/local/bin/dump_json.py
$ podman run --it --rm --entrypoint /usr/local/bin/dump_json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dump_json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_reference.py

```bash
$ singularity exec <container> /usr/local/bin/extract_reference.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-test

```bash
$ singularity exec <container> /usr/local/bin/theano-test
$ podman run --it --rm --entrypoint /usr/local/bin/theano-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train_network.py

```bash
$ singularity exec <container> /usr/local/bin/train_network.py
$ podman run --it --rm --entrypoint /usr/local/bin/train_network.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train_network.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validate_network.py

```bash
$ singularity exec <container> /usr/local/bin/validate_network.py
$ podman run --it --rm --entrypoint /usr/local/bin/validate_network.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validate_network.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### verify_network.py

```bash
$ singularity exec <container> /usr/local/bin/verify_network.py
$ podman run --it --rm --entrypoint /usr/local/bin/verify_network.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/verify_network.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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