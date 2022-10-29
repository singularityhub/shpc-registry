---
layout: container
name:  "quay.io/biocontainers/r-acidsinglecell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidsinglecell/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidsinglecell/container.yaml"
updated_at: "2022-10-29 05:47:13.963628"
latest: "0.2.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-acidsinglecell"
aliases:
 - "R"
 - "Rscript"
 - "acountry"
 - "adig"
 - "ahost"
 - "autopoint"
 - "bunzip2"
 - "bzcat"
 - "bzcmp"
 - "bzdiff"
versions:
 - "0.2.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidsinglecell"
config: {"url": "https://biocontainers.pro/tools/r-acidsinglecell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidsinglecell", "latest": {"0.2.0--r41hdfd78af_0": "sha256:28547717f9ab2bbce71036b8347db6a2b766d568fd75f4cc4b865cdfa5f3b1f9"}, "tags": {"0.2.0--r41hdfd78af_0": "sha256:28547717f9ab2bbce71036b8347db6a2b766d568fd75f4cc4b865cdfa5f3b1f9"}, "docker": "quay.io/biocontainers/r-acidsinglecell", "aliases": {"R": "/usr/local/bin/R", "Rscript": "/usr/local/bin/Rscript", "acountry": "/usr/local/bin/acountry", "adig": "/usr/local/bin/adig", "ahost": "/usr/local/bin/ahost", "autopoint": "/usr/local/bin/autopoint", "bunzip2": "/usr/local/bin/bunzip2", "bzcat": "/usr/local/bin/bzcat", "bzcmp": "/usr/local/bin/bzcmp", "bzdiff": "/usr/local/bin/bzdiff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidsinglecell.
shpc-registry automated BioContainers addition for r-acidsinglecell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidsinglecell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidsinglecell:0.2.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidsinglecell/0.2.0--r41hdfd78af_0
$ module help quay.io/biocontainers/r-acidsinglecell/0.2.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidsinglecell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidsinglecell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidsinglecell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidsinglecell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidsinglecell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidsinglecell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R

```bash
$ singularity exec <container> /usr/local/bin/R
$ podman run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rscript

```bash
$ singularity exec <container> /usr/local/bin/Rscript
$ podman run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acountry

```bash
$ singularity exec <container> /usr/local/bin/acountry
$ podman run --it --rm --entrypoint /usr/local/bin/acountry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acountry   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adig

```bash
$ singularity exec <container> /usr/local/bin/adig
$ podman run --it --rm --entrypoint /usr/local/bin/adig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ahost

```bash
$ singularity exec <container> /usr/local/bin/ahost
$ podman run --it --rm --entrypoint /usr/local/bin/ahost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ahost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autopoint

```bash
$ singularity exec <container> /usr/local/bin/autopoint
$ podman run --it --rm --entrypoint /usr/local/bin/autopoint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autopoint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bunzip2

```bash
$ singularity exec <container> /usr/local/bin/bunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/bunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bzcat

```bash
$ singularity exec <container> /usr/local/bin/bzcat
$ podman run --it --rm --entrypoint /usr/local/bin/bzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bzcmp

```bash
$ singularity exec <container> /usr/local/bin/bzcmp
$ podman run --it --rm --entrypoint /usr/local/bin/bzcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bzcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bzdiff

```bash
$ singularity exec <container> /usr/local/bin/bzdiff
$ podman run --it --rm --entrypoint /usr/local/bin/bzdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bzdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
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