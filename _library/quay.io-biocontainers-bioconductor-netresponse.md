---
layout: container
name:  "quay.io/biocontainers/bioconductor-netresponse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-netresponse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-netresponse/container.yaml"
updated_at: "2024-03-04 04:53:43.789784"
latest: "1.62.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-netresponse"
aliases:
 - "pandoc-server"
 - "glpsol"
 - "pandoc"
versions:
 - "1.54.0--r41hc0cfd56_2"
 - "1.58.0--r42hc0cfd56_0"
 - "1.58.0--r42ha9d7317_1"
 - "1.60.0--r43ha9d7317_0"
 - "1.62.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-netresponse"
config: {"url": "https://biocontainers.pro/tools/bioconductor-netresponse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-netresponse", "latest": {"1.62.0--r43ha9d7317_0": "sha256:8bec218adf1bcc6088d1ca6fb9ed032e0232c26e1e76802c5e5bb9064c630e35"}, "tags": {"1.54.0--r41hc0cfd56_2": "sha256:bf4efbf2697e6dad1d7f1d263d14fae9dbd374f96369867fef1840962d2e3f20", "1.58.0--r42hc0cfd56_0": "sha256:97264e6f2101467af00754e6f4d231b7bceb8d56035063e66e83360cda199424", "1.58.0--r42ha9d7317_1": "sha256:06fc0f339f7bf89dc5751cfb5ff561e4086abc0eeebc17565871f70083b00188", "1.60.0--r43ha9d7317_0": "sha256:eacc6f27ee0eb07314357f558c377c89e7206835bb0accd97893c983f829e6a7", "1.62.0--r43ha9d7317_0": "sha256:8bec218adf1bcc6088d1ca6fb9ed032e0232c26e1e76802c5e5bb9064c630e35"}, "docker": "quay.io/biocontainers/bioconductor-netresponse", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "glpsol": "/usr/local/bin/glpsol", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-netresponse.
shpc-registry automated BioContainers addition for bioconductor-netresponse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-netresponse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-netresponse:1.62.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-netresponse/1.62.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-netresponse/1.62.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-netresponse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netresponse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netresponse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-netresponse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-netresponse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-netresponse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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