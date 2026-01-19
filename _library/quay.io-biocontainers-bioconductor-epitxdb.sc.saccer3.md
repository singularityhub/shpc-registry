---
layout: container
name:  "quay.io/biocontainers/bioconductor-epitxdb.sc.saccer3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epitxdb.sc.saccer3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epitxdb.sc.saccer3/container.yaml"
updated_at: "2026-01-19 05:05:38.907186"
latest: "0.99.5--r44hdfd78af_6"
container_url: "https://biocontainers.pro/tools/bioconductor-epitxdb.sc.saccer3"

versions:
 - "0.99.5--r41hdfd78af_2"
 - "0.99.5--r42hdfd78af_3"
 - "0.99.5--r43hdfd78af_4"
 - "0.99.5--r43hdfd78af_5"
 - "0.99.5--r44hdfd78af_6"
description: "shpc-registry automated BioContainers addition for bioconductor-epitxdb.sc.saccer3"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epitxdb.sc.saccer3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epitxdb.sc.saccer3", "latest": {"0.99.5--r44hdfd78af_6": "sha256:5520322e398f641482afbeb87c315bd594762d7836a3be619de7267025c50f8a"}, "tags": {"0.99.5--r41hdfd78af_2": "sha256:83fbdab38edc36892dd83a3030eef3462b9e33ec28f75e7fc318edd6c18c2b4a", "0.99.5--r42hdfd78af_3": "sha256:869ffff15d91cd6a8312f74edb170a4ccd84e59eb0b57002c18a0ebc88273001", "0.99.5--r43hdfd78af_4": "sha256:b2613b813a2362d24fff42c52582eef5fff4311ffa7cb804d20c47cfdf182fb7", "0.99.5--r43hdfd78af_5": "sha256:c1c5e1a950af6be5b032234f840babba694117683f8fdada3d9042bc6826d8ec", "0.99.5--r44hdfd78af_6": "sha256:5520322e398f641482afbeb87c315bd594762d7836a3be619de7267025c50f8a"}, "docker": "quay.io/biocontainers/bioconductor-epitxdb.sc.saccer3"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epitxdb.sc.saccer3.
shpc-registry automated BioContainers addition for bioconductor-epitxdb.sc.saccer3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epitxdb.sc.saccer3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epitxdb.sc.saccer3:0.99.5--r44hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epitxdb.sc.saccer3/0.99.5--r44hdfd78af_6
$ module help quay.io/biocontainers/bioconductor-epitxdb.sc.saccer3/0.99.5--r44hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epitxdb.sc.saccer3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epitxdb.sc.saccer3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epitxdb.sc.saccer3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epitxdb.sc.saccer3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epitxdb.sc.saccer3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epitxdb.sc.saccer3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-epitxdb.sc.saccer3

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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