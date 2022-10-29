---
layout: container
name:  "quay.io/biocontainers/telr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/telr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/telr/container.yaml"
updated_at: "2022-10-29 05:58:26.466034"
latest: "0.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/telr"
aliases:
 - "queryRepeatDatabase.pl"
 - "queryTaxonomyDatabase.pl"
 - "sniffles"
 - "sniffles-debug"
 - "telr"
 - "wtdbg-cns"
 - "wtdbg2"
 - "wtpoa-cns"
 - "2to3-3.6"
 - "DateRepeats"
 - "DupMasker"
 - "ProcessRepeats"
 - "RepeatMasker"
 - "RepeatProteinMask"
 - "ace2sam"
 - "alimask"
 - "annotateBed"
 - "bamToBed"
versions:
 - "0.2--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for telr"
config: {"url": "https://biocontainers.pro/tools/telr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for telr", "latest": {"0.2--pyhdfd78af_1": "sha256:747495fb7770dff6d91720f5236ce20d1d88c9ec036728c30796b292d887a6e1"}, "tags": {"0.2--pyhdfd78af_1": "sha256:747495fb7770dff6d91720f5236ce20d1d88c9ec036728c30796b292d887a6e1"}, "docker": "quay.io/biocontainers/telr", "aliases": {"queryRepeatDatabase.pl": "/usr/local/bin/queryRepeatDatabase.pl", "queryTaxonomyDatabase.pl": "/usr/local/bin/queryTaxonomyDatabase.pl", "sniffles": "/usr/local/bin/sniffles", "sniffles-debug": "/usr/local/bin/sniffles-debug", "telr": "/usr/local/bin/telr", "wtdbg-cns": "/usr/local/bin/wtdbg-cns", "wtdbg2": "/usr/local/bin/wtdbg2", "wtpoa-cns": "/usr/local/bin/wtpoa-cns", "2to3-3.6": "/usr/local/bin/2to3-3.6", "DateRepeats": "/usr/local/bin/DateRepeats", "DupMasker": "/usr/local/bin/DupMasker", "ProcessRepeats": "/usr/local/bin/ProcessRepeats", "RepeatMasker": "/usr/local/bin/RepeatMasker", "RepeatProteinMask": "/usr/local/bin/RepeatProteinMask", "ace2sam": "/usr/local/bin/ace2sam", "alimask": "/usr/local/bin/alimask", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/telr.
shpc-registry automated BioContainers addition for telr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/telr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/telr:0.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/telr/0.2--pyhdfd78af_1
$ module help quay.io/biocontainers/telr/0.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### telr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### telr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### telr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### telr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### telr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### telr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### queryRepeatDatabase.pl

```bash
$ singularity exec <container> /usr/local/bin/queryRepeatDatabase.pl
$ podman run --it --rm --entrypoint /usr/local/bin/queryRepeatDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queryRepeatDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### queryTaxonomyDatabase.pl

```bash
$ singularity exec <container> /usr/local/bin/queryTaxonomyDatabase.pl
$ podman run --it --rm --entrypoint /usr/local/bin/queryTaxonomyDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queryTaxonomyDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sniffles

```bash
$ singularity exec <container> /usr/local/bin/sniffles
$ podman run --it --rm --entrypoint /usr/local/bin/sniffles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sniffles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sniffles-debug

```bash
$ singularity exec <container> /usr/local/bin/sniffles-debug
$ podman run --it --rm --entrypoint /usr/local/bin/sniffles-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sniffles-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### telr

```bash
$ singularity exec <container> /usr/local/bin/telr
$ podman run --it --rm --entrypoint /usr/local/bin/telr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/telr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtdbg-cns

```bash
$ singularity exec <container> /usr/local/bin/wtdbg-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtdbg2

```bash
$ singularity exec <container> /usr/local/bin/wtdbg2
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtpoa-cns

```bash
$ singularity exec <container> /usr/local/bin/wtpoa-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DateRepeats

```bash
$ singularity exec <container> /usr/local/bin/DateRepeats
$ podman run --it --rm --entrypoint /usr/local/bin/DateRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DateRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DupMasker

```bash
$ singularity exec <container> /usr/local/bin/DupMasker
$ podman run --it --rm --entrypoint /usr/local/bin/DupMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DupMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ProcessRepeats

```bash
$ singularity exec <container> /usr/local/bin/ProcessRepeats
$ podman run --it --rm --entrypoint /usr/local/bin/ProcessRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ProcessRepeats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatMasker

```bash
$ singularity exec <container> /usr/local/bin/RepeatMasker
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatMasker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatProteinMask

```bash
$ singularity exec <container> /usr/local/bin/RepeatProteinMask
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatProteinMask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatProteinMask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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