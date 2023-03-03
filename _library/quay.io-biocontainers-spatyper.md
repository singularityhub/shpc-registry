---
layout: container
name:  "quay.io/biocontainers/spatyper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spatyper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spatyper/container.yaml"
updated_at: "2023-03-03 04:40:04.843292"
latest: "0.3.3--pyhdfd78af_3"
container_url: "https://biocontainers.pro/tools/spatyper"
aliases:
 - "download-spatypes.sh"
 - "spaTyper"
 - "sparepeats.fasta"
 - "spatypes.txt"
 - "idn2"
 - "wget"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.3.3--pyhdfd78af_3"
description: "shpc-registry automated BioContainers addition for spatyper"
config: {"url": "https://biocontainers.pro/tools/spatyper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spatyper", "latest": {"0.3.3--pyhdfd78af_3": "sha256:8c29abb04a86643c36a7bc46e08141b4c181e1ea25bfd90e9b43f22f0940bc82"}, "tags": {"0.3.3--pyhdfd78af_3": "sha256:8c29abb04a86643c36a7bc46e08141b4c181e1ea25bfd90e9b43f22f0940bc82"}, "docker": "quay.io/biocontainers/spatyper", "aliases": {"download-spatypes.sh": "/usr/local/bin/download-spatypes.sh", "spaTyper": "/usr/local/bin/spaTyper", "sparepeats.fasta": "/usr/local/bin/sparepeats.fasta", "spatypes.txt": "/usr/local/bin/spatypes.txt", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spatyper.
shpc-registry automated BioContainers addition for spatyper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spatyper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spatyper:0.3.3--pyhdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spatyper/0.3.3--pyhdfd78af_3
$ module help quay.io/biocontainers/spatyper/0.3.3--pyhdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spatyper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spatyper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spatyper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spatyper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spatyper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spatyper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### download-spatypes.sh

```bash
$ singularity exec <container> /usr/local/bin/download-spatypes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download-spatypes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-spatypes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaTyper

```bash
$ singularity exec <container> /usr/local/bin/spaTyper
$ podman run --it --rm --entrypoint /usr/local/bin/spaTyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaTyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sparepeats.fasta

```bash
$ singularity exec <container> /usr/local/bin/sparepeats.fasta
$ podman run --it --rm --entrypoint /usr/local/bin/sparepeats.fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sparepeats.fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spatypes.txt

```bash
$ singularity exec <container> /usr/local/bin/spatypes.txt
$ podman run --it --rm --entrypoint /usr/local/bin/spatypes.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spatypes.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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