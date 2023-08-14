---
layout: container
name:  "quay.io/biocontainers/pycoqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pycoqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pycoqc/container.yaml"
updated_at: "2023-08-14 03:17:04.692751"
latest: "2.5.2--py_0"
container_url: "https://biocontainers.pro/tools/pycoqc"
aliases:
 - "Barcode_split"
 - "Fast5_to_seq_summary"
 - "pycoQC"
 - "jupyter-trust"
 - "jupyter"
 - "jupyter-migrate"
 - "jupyter-troubleshoot"
 - "jsonschema"
 - "tqdm"
 - "f2py3.7"
 - "chardetect"
 - "2to3-3.7"
 - "idle3.7"
versions:
 - "2.5.2--py_0"
description: "shpc-registry automated BioContainers addition for pycoqc"
config: {"url": "https://biocontainers.pro/tools/pycoqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pycoqc", "latest": {"2.5.2--py_0": "sha256:ea0a084751a0b48b5ffe90e9d3adfa8f57473709a1b0a95c9cb38d434ee3a9a2"}, "tags": {"2.5.2--py_0": "sha256:ea0a084751a0b48b5ffe90e9d3adfa8f57473709a1b0a95c9cb38d434ee3a9a2"}, "docker": "quay.io/biocontainers/pycoqc", "aliases": {"Barcode_split": "/usr/local/bin/Barcode_split", "Fast5_to_seq_summary": "/usr/local/bin/Fast5_to_seq_summary", "pycoQC": "/usr/local/bin/pycoQC", "jupyter-trust": "/usr/local/bin/jupyter-trust", "jupyter": "/usr/local/bin/jupyter", "jupyter-migrate": "/usr/local/bin/jupyter-migrate", "jupyter-troubleshoot": "/usr/local/bin/jupyter-troubleshoot", "jsonschema": "/usr/local/bin/jsonschema", "tqdm": "/usr/local/bin/tqdm", "f2py3.7": "/usr/local/bin/f2py3.7", "chardetect": "/usr/local/bin/chardetect", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pycoqc.
shpc-registry automated BioContainers addition for pycoqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pycoqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pycoqc:2.5.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pycoqc/2.5.2--py_0
$ module help quay.io/biocontainers/pycoqc/2.5.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pycoqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pycoqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pycoqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pycoqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pycoqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pycoqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Barcode_split

```bash
$ singularity exec <container> /usr/local/bin/Barcode_split
$ podman run --it --rm --entrypoint /usr/local/bin/Barcode_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Barcode_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fast5_to_seq_summary

```bash
$ singularity exec <container> /usr/local/bin/Fast5_to_seq_summary
$ podman run --it --rm --entrypoint /usr/local/bin/Fast5_to_seq_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fast5_to_seq_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycoQC

```bash
$ singularity exec <container> /usr/local/bin/pycoQC
$ podman run --it --rm --entrypoint /usr/local/bin/pycoQC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycoQC   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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