---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocstyle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocstyle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocstyle/container.yaml"
updated_at: "2023-03-21 02:52:05.026982"
latest: "2.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocstyle"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
versions:
 - "2.8.2--r351_0"
 - "2.26.0--r42hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r41hdfd78af_0"
 - "2.18.1--r40hdfd78af_0"
 - "2.16.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocstyle"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocstyle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocstyle", "latest": {"2.26.0--r42hdfd78af_0": "sha256:ed999a43963363b739f0eadb763ba42b7326d56c5302f424aada5d7513f07d11"}, "tags": {"2.8.2--r351_0": "sha256:91de1ad44045dd5e3dbe52072f58f544f58ae6c2eacda2a148b7360e22ff0d28", "2.26.0--r42hdfd78af_0": "sha256:ed999a43963363b739f0eadb763ba42b7326d56c5302f424aada5d7513f07d11", "2.22.0--r41hdfd78af_0": "sha256:27281d0b23a6c35e976e2b0d2bb250550103a7589c0a1cba4621252f950a7d3e", "2.20.0--r41hdfd78af_0": "sha256:d6ea9af5a166cc41268fdbb7da4af36eced63268be58408a81c89649e5e1d67d", "2.18.1--r40hdfd78af_0": "sha256:0ca9ad198e5b1c18e96fbfcd980f9301df1592570c4b58159f3f9f791fd3faf9", "2.16.0--r40_0": "sha256:5e21ce186f94a445931f8cc5ac474dc684ec7b10963a1da00f8a700107d0eb20"}, "docker": "quay.io/biocontainers/bioconductor-biocstyle", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocstyle.
shpc-registry automated BioContainers addition for bioconductor-biocstyle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocstyle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocstyle:2.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocstyle/2.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocstyle/2.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocstyle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocstyle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocstyle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocstyle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocstyle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocstyle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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