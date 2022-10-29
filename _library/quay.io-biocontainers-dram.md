---
layout: container
name:  "quay.io/biocontainers/dram"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dram/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dram/container.yaml"
updated_at: "2022-10-29 05:39:23.819063"
latest: "1.3.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/dram"
aliases:
 - "DRAM-setup.py"
 - "DRAM-v.py"
 - "DRAM.py"
 - "2to3-3.10"
 - "EukHighConfidenceFilter"
 - "alimask"
 - "annotateBed"
 - "awk"
 - "bamToBed"
 - "bamToFastq"
 - "barrnap"
 - "bed12ToBed6"
 - "bedToBam"
versions:
 - "1.3.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for dram"
config: {"url": "https://biocontainers.pro/tools/dram", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dram", "latest": {"1.3.5--pyhdfd78af_0": "sha256:b5abb14e7b0ded7a36cbd2458c256bdf9344618fe7781d37222bb01fa36ba85e"}, "tags": {"1.3.5--pyhdfd78af_0": "sha256:b5abb14e7b0ded7a36cbd2458c256bdf9344618fe7781d37222bb01fa36ba85e"}, "docker": "quay.io/biocontainers/dram", "aliases": {"DRAM-setup.py": "/usr/local/bin/DRAM-setup.py", "DRAM-v.py": "/usr/local/bin/DRAM-v.py", "DRAM.py": "/usr/local/bin/DRAM.py", "2to3-3.10": "/usr/local/bin/2to3-3.10", "EukHighConfidenceFilter": "/usr/local/bin/EukHighConfidenceFilter", "alimask": "/usr/local/bin/alimask", "annotateBed": "/usr/local/bin/annotateBed", "awk": "/usr/local/bin/awk", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "barrnap": "/usr/local/bin/barrnap", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dram.
shpc-registry automated BioContainers addition for dram
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dram
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dram:1.3.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dram/1.3.5--pyhdfd78af_0
$ module help quay.io/biocontainers/dram/1.3.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dram-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dram-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dram-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dram-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dram-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dram-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DRAM-setup.py

```bash
$ singularity exec <container> /usr/local/bin/DRAM-setup.py
$ podman run --it --rm --entrypoint /usr/local/bin/DRAM-setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DRAM-setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DRAM-v.py

```bash
$ singularity exec <container> /usr/local/bin/DRAM-v.py
$ podman run --it --rm --entrypoint /usr/local/bin/DRAM-v.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DRAM-v.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DRAM.py

```bash
$ singularity exec <container> /usr/local/bin/DRAM.py
$ podman run --it --rm --entrypoint /usr/local/bin/DRAM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DRAM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EukHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/EukHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barrnap

```bash
$ singularity exec <container> /usr/local/bin/barrnap
$ podman run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
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