---
layout: container
name:  "quay.io/biocontainers/samshee"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samshee/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/samshee/container.yaml"
updated_at: "2025-12-14 04:20:59.330844"
latest: "0.2.11--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/samshee"
aliases:
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "jsonschema"
 - "normalizer"
versions:
 - "0.2.1--pyhdfd78af_0"
 - "0.2.2--pyhdfd78af_0"
 - "0.2.3--pyhdfd78af_0"
 - "0.2.8--pyhdfd78af_0"
 - "0.2.9--pyhdfd78af_0"
 - "0.2.10--pyhdfd78af_0"
 - "0.2.11--pyhdfd78af_0"
description: "singularity registry hpc automated addition for samshee"
config: {"url": "https://biocontainers.pro/tools/samshee", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for samshee", "latest": {"0.2.11--pyhdfd78af_0": "sha256:c83aeeb28aaa92d091e02a96439ed759cdff54c550e70245fc4a79edbeb068eb"}, "tags": {"0.2.1--pyhdfd78af_0": "sha256:6c61dab83f761d86dbf4a2e7210ed44bf2b36cc79cc1b7466f14570935976454", "0.2.2--pyhdfd78af_0": "sha256:d956f97acb38825971a97224a21c33e667e8801063b7c03f93aabed846ef7bc0", "0.2.3--pyhdfd78af_0": "sha256:d3a037a0b76f3dcee60c25067e686b65c06b9bb6aa8ae7054117ac5f4598768a", "0.2.8--pyhdfd78af_0": "sha256:89ed9c72439d7db30126a31c338b1d192beb556bff47ee788a35242df58db879", "0.2.9--pyhdfd78af_0": "sha256:3fa2867a3bd47d34803af5d702c43adbb00118994b50437c70b0f91c1a42b6e7", "0.2.10--pyhdfd78af_0": "sha256:2435ecccedd930cb7d0e4e45ca6147ba5d3adb8e3f1efb06b2c1e7f7d8bc9554", "0.2.11--pyhdfd78af_0": "sha256:c83aeeb28aaa92d091e02a96439ed759cdff54c550e70245fc4a79edbeb068eb"}, "docker": "quay.io/biocontainers/samshee", "aliases": {"idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "jsonschema": "/usr/local/bin/jsonschema", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samshee.
singularity registry hpc automated addition for samshee
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samshee
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samshee:0.2.11--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samshee/0.2.11--pyhdfd78af_0
$ module help quay.io/biocontainers/samshee/0.2.11--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samshee-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samshee-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samshee-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samshee-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samshee-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samshee-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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