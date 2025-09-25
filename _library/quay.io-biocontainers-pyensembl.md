---
layout: container
name:  "quay.io/biocontainers/pyensembl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyensembl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyensembl/container.yaml"
updated_at: "2025-09-25 03:43:42.153704"
latest: "2.3.13--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/pyensembl"
aliases:
 - "epylint"
 - "isort"
 - "isort-identify-imports"
 - "pyensembl"
 - "pylint"
 - "pylint-config"
 - "pyreverse"
 - "symilar"
 - "get_objgraph"
 - "undill"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "2.0.1--pyh5e36f6f_0"
 - "2.1.0--pyh7cba7a3_0"
 - "2.2.9--pyh7cba7a3_0"
 - "2.3.4--pyh7cba7a3_0"
 - "2.3.9--pyh7cba7a3_0"
 - "2.3.11--pyh7cba7a3_0"
 - "2.3.12--pyh7cba7a3_0"
 - "2.3.13--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for pyensembl"
config: {"url": "https://biocontainers.pro/tools/pyensembl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyensembl", "latest": {"2.3.13--pyh7cba7a3_0": "sha256:cbf2504de640ce0acf14cb3da52f721b1acb1f178f679bdde0c61939d01ef00b"}, "tags": {"2.0.1--pyh5e36f6f_0": "sha256:c35a3a654e49c7b48485c0d0904d24f814daa9c678d1c7ce9b52f2a853e707c7", "2.1.0--pyh7cba7a3_0": "sha256:5fb67d92074158b3461248af76573ba3d3cbd080c77bb682b7dcac779f5ac464", "2.2.9--pyh7cba7a3_0": "sha256:b1273d266bfa8204bdc8a5a683305a3b2c0a6282a19f52d51c3ac13d94125061", "2.3.4--pyh7cba7a3_0": "sha256:d8702fe569f5f6569f6e63714cc54fb476038c111b7669260f110b9de5955352", "2.3.9--pyh7cba7a3_0": "sha256:bf1e32313961f5e3d721265bccf20cfeb7a5163676fdae9239bd643435f3c9fd", "2.3.11--pyh7cba7a3_0": "sha256:7fbe9627b07f4e3df32028f105e656d88fd4be836a58fb0ff02c07be60c56725", "2.3.12--pyh7cba7a3_0": "sha256:dd9381682c6e189cad85c2dc955c12f276872f0c29e8fc10d0352f5466d18bcd", "2.3.13--pyh7cba7a3_0": "sha256:cbf2504de640ce0acf14cb3da52f721b1acb1f178f679bdde0c61939d01ef00b"}, "docker": "quay.io/biocontainers/pyensembl", "aliases": {"epylint": "/usr/local/bin/epylint", "isort": "/usr/local/bin/isort", "isort-identify-imports": "/usr/local/bin/isort-identify-imports", "pyensembl": "/usr/local/bin/pyensembl", "pylint": "/usr/local/bin/pylint", "pylint-config": "/usr/local/bin/pylint-config", "pyreverse": "/usr/local/bin/pyreverse", "symilar": "/usr/local/bin/symilar", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyensembl.
shpc-registry automated BioContainers addition for pyensembl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyensembl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyensembl:2.3.13--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyensembl/2.3.13--pyh7cba7a3_0
$ module help quay.io/biocontainers/pyensembl/2.3.13--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyensembl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyensembl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyensembl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyensembl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyensembl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyensembl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### epylint

```bash
$ singularity exec <container> /usr/local/bin/epylint
$ podman run --it --rm --entrypoint /usr/local/bin/epylint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epylint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort

```bash
$ singularity exec <container> /usr/local/bin/isort
$ podman run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort-identify-imports

```bash
$ singularity exec <container> /usr/local/bin/isort-identify-imports
$ podman run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyensembl

```bash
$ singularity exec <container> /usr/local/bin/pyensembl
$ podman run --it --rm --entrypoint /usr/local/bin/pyensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylint

```bash
$ singularity exec <container> /usr/local/bin/pylint
$ podman run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylint-config

```bash
$ singularity exec <container> /usr/local/bin/pylint-config
$ podman run --it --rm --entrypoint /usr/local/bin/pylint-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylint-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyreverse

```bash
$ singularity exec <container> /usr/local/bin/pyreverse
$ podman run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### symilar

```bash
$ singularity exec <container> /usr/local/bin/symilar
$ podman run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
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