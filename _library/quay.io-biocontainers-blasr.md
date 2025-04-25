---
layout: container
name:  "quay.io/biocontainers/blasr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blasr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blasr/container.yaml"
updated_at: "2025-04-25 02:53:28.521733"
latest: "5.3.9c6f0a5--0"
container_url: "https://biocontainers.pro/tools/blasr"
aliases:
 - "bam2sam"
 - "blasr"
 - "loadPulses"
 - "pbindex"
 - "pbindexdump"
 - "pbmerge"
 - "pls2fasta"
 - "samFilter"
 - "samtoh5"
 - "samtom4"
 - "sawriter"
 - "sdpMatcher"
 - "easy_install-3.6"
 - "uconv"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
versions:
 - "5.3.f8bfa9c--0"
 - "5.3.9c6f0a5--0"
description: "shpc-registry automated BioContainers addition for blasr"
config: {"url": "https://biocontainers.pro/tools/blasr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for blasr", "latest": {"5.3.9c6f0a5--0": "sha256:468c306f0186016051b5451687e3e04e19033e135e98d8a2d1b82366c556e0aa"}, "tags": {"5.3.f8bfa9c--0": "sha256:8526342becc0d68a4b65c36cbdefac086bb11179066122354c94ded59175c08c", "5.3.9c6f0a5--0": "sha256:468c306f0186016051b5451687e3e04e19033e135e98d8a2d1b82366c556e0aa"}, "docker": "quay.io/biocontainers/blasr", "aliases": {"bam2sam": "/usr/local/bin/bam2sam", "blasr": "/usr/local/bin/blasr", "loadPulses": "/usr/local/bin/loadPulses", "pbindex": "/usr/local/bin/pbindex", "pbindexdump": "/usr/local/bin/pbindexdump", "pbmerge": "/usr/local/bin/pbmerge", "pls2fasta": "/usr/local/bin/pls2fasta", "samFilter": "/usr/local/bin/samFilter", "samtoh5": "/usr/local/bin/samtoh5", "samtom4": "/usr/local/bin/samtom4", "sawriter": "/usr/local/bin/sawriter", "sdpMatcher": "/usr/local/bin/sdpMatcher", "easy_install-3.6": "/usr/local/bin/easy_install-3.6", "uconv": "/usr/local/bin/uconv", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blasr.
shpc-registry automated BioContainers addition for blasr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blasr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blasr:5.3.9c6f0a5--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blasr/5.3.9c6f0a5--0
$ module help quay.io/biocontainers/blasr/5.3.9c6f0a5--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blasr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blasr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blasr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blasr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blasr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blasr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2sam

```bash
$ singularity exec <container> /usr/local/bin/bam2sam
$ podman run --it --rm --entrypoint /usr/local/bin/bam2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blasr

```bash
$ singularity exec <container> /usr/local/bin/blasr
$ podman run --it --rm --entrypoint /usr/local/bin/blasr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blasr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loadPulses

```bash
$ singularity exec <container> /usr/local/bin/loadPulses
$ podman run --it --rm --entrypoint /usr/local/bin/loadPulses   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loadPulses   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindex

```bash
$ singularity exec <container> /usr/local/bin/pbindex
$ podman run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindexdump

```bash
$ singularity exec <container> /usr/local/bin/pbindexdump
$ podman run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbmerge

```bash
$ singularity exec <container> /usr/local/bin/pbmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pls2fasta

```bash
$ singularity exec <container> /usr/local/bin/pls2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/pls2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pls2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samFilter

```bash
$ singularity exec <container> /usr/local/bin/samFilter
$ podman run --it --rm --entrypoint /usr/local/bin/samFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtoh5

```bash
$ singularity exec <container> /usr/local/bin/samtoh5
$ podman run --it --rm --entrypoint /usr/local/bin/samtoh5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtoh5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtom4

```bash
$ singularity exec <container> /usr/local/bin/samtom4
$ podman run --it --rm --entrypoint /usr/local/bin/samtom4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtom4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sawriter

```bash
$ singularity exec <container> /usr/local/bin/sawriter
$ podman run --it --rm --entrypoint /usr/local/bin/sawriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sawriter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdpMatcher

```bash
$ singularity exec <container> /usr/local/bin/sdpMatcher
$ podman run --it --rm --entrypoint /usr/local/bin/sdpMatcher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdpMatcher   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.6

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uconv

```bash
$ singularity exec <container> /usr/local/bin/uconv
$ podman run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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