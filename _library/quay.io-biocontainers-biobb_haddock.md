---
layout: container
name:  "quay.io/biocontainers/biobb_haddock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_haddock/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_haddock/container.yaml"
updated_at: "2025-05-15 03:29:11.397220"
latest: "5.0.0--pyhdfd78af_4"
container_url: "https://biocontainers.pro/tools/biobb_haddock"
aliases:
 - "capri_eval"
 - "clust_fcc"
 - "em_ref"
 - "flex_ref"
 - "rigid_body"
 - "sele_top"
 - "topology"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "normalizer"
versions:
 - "4.2.1--pyhdfd78af_0"
 - "5.0.0--pyhdfd78af_0"
 - "5.0.0--pyhdfd78af_4"
description: "singularity registry hpc automated addition for biobb_haddock"
config: {"url": "https://biocontainers.pro/tools/biobb_haddock", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for biobb_haddock", "latest": {"5.0.0--pyhdfd78af_4": "sha256:02ae442526f3d5a8a7d485f166d9c37826f0fc1100f99910dd463a11b0633e44"}, "tags": {"4.2.1--pyhdfd78af_0": "sha256:f7e0fa46658ff87f63569da48104cd10a83b0ba453a950be1c6473e0ba8ab335", "5.0.0--pyhdfd78af_0": "sha256:4ecaffeddb0b949e08f23defb923b6729a82cf6912814743b77e9bc7a0ba0da2", "5.0.0--pyhdfd78af_4": "sha256:02ae442526f3d5a8a7d485f166d9c37826f0fc1100f99910dd463a11b0633e44"}, "docker": "quay.io/biocontainers/biobb_haddock", "aliases": {"capri_eval": "/usr/local/bin/capri_eval", "clust_fcc": "/usr/local/bin/clust_fcc", "em_ref": "/usr/local/bin/em_ref", "flex_ref": "/usr/local/bin/flex_ref", "rigid_body": "/usr/local/bin/rigid_body", "sele_top": "/usr/local/bin/sele_top", "topology": "/usr/local/bin/topology", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_haddock.
singularity registry hpc automated addition for biobb_haddock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_haddock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_haddock:5.0.0--pyhdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_haddock/5.0.0--pyhdfd78af_4
$ module help quay.io/biocontainers/biobb_haddock/5.0.0--pyhdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_haddock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_haddock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_haddock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_haddock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_haddock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_haddock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### capri_eval

```bash
$ singularity exec <container> /usr/local/bin/capri_eval
$ podman run --it --rm --entrypoint /usr/local/bin/capri_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capri_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clust_fcc

```bash
$ singularity exec <container> /usr/local/bin/clust_fcc
$ podman run --it --rm --entrypoint /usr/local/bin/clust_fcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clust_fcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### em_ref

```bash
$ singularity exec <container> /usr/local/bin/em_ref
$ podman run --it --rm --entrypoint /usr/local/bin/em_ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/em_ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flex_ref

```bash
$ singularity exec <container> /usr/local/bin/flex_ref
$ podman run --it --rm --entrypoint /usr/local/bin/flex_ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flex_ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rigid_body

```bash
$ singularity exec <container> /usr/local/bin/rigid_body
$ podman run --it --rm --entrypoint /usr/local/bin/rigid_body   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rigid_body   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sele_top

```bash
$ singularity exec <container> /usr/local/bin/sele_top
$ podman run --it --rm --entrypoint /usr/local/bin/sele_top   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sele_top   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### topology

```bash
$ singularity exec <container> /usr/local/bin/topology
$ podman run --it --rm --entrypoint /usr/local/bin/topology   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/topology   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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