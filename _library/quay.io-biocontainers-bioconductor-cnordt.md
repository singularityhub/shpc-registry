---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnordt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnordt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnordt/container.yaml"
updated_at: "2025-09-15 03:37:23.192768"
latest: "1.48.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnordt"
aliases:
 - "diffimg"
 - "delaunay"
 - "gts-config"
 - "gts2dxf"
 - "gts2oogl"
 - "gts2stl"
 - "gtscheck"
 - "gtscompare"
 - "gtstemplate"
 - "stl2gts"
versions:
 - "1.36.0--r41hc0cfd56_2"
 - "1.40.0--r42hc0cfd56_0"
 - "1.40.0--r42ha9d7317_1"
 - "1.42.0--r43ha9d7317_0"
 - "1.44.0--r43ha9d7317_0"
 - "1.48.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnordt"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnordt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnordt", "latest": {"1.48.0--r44h3df3fcb_0": "sha256:e6824cbff43bbf4b04cd1930aa9360019f06c4a5a7a8b7a6d3b856c63b31ec9e"}, "tags": {"1.36.0--r41hc0cfd56_2": "sha256:b5665dbbd4f6ed24ddaf827fcd7bee33f05d8c3cb2e9411659b8158164a86405", "1.40.0--r42hc0cfd56_0": "sha256:85d7ec446f6eadb143fe33a20d60db0b77f4bab48d991b7fcf8e85a57f9e9ece", "1.40.0--r42ha9d7317_1": "sha256:f0d4b24433e903c33ed7c56b72c364416e3b27b8f4bcea8c6b21f69311f00d5d", "1.42.0--r43ha9d7317_0": "sha256:ccb0b8d08e1b8d6e5363a252d7d1b8dda2cef1449c005311b513e9e396f1ed78", "1.44.0--r43ha9d7317_0": "sha256:0129525b35003b3146f678d0abc7c29e0c9ec90e769112fc0e2a227a4772dd71", "1.48.0--r44h3df3fcb_0": "sha256:e6824cbff43bbf4b04cd1930aa9360019f06c4a5a7a8b7a6d3b856c63b31ec9e"}, "docker": "quay.io/biocontainers/bioconductor-cnordt", "aliases": {"diffimg": "/usr/local/bin/diffimg", "delaunay": "/usr/local/bin/delaunay", "gts-config": "/usr/local/bin/gts-config", "gts2dxf": "/usr/local/bin/gts2dxf", "gts2oogl": "/usr/local/bin/gts2oogl", "gts2stl": "/usr/local/bin/gts2stl", "gtscheck": "/usr/local/bin/gtscheck", "gtscompare": "/usr/local/bin/gtscompare", "gtstemplate": "/usr/local/bin/gtstemplate", "stl2gts": "/usr/local/bin/stl2gts"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnordt.
shpc-registry automated BioContainers addition for bioconductor-cnordt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnordt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnordt:1.48.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnordt/1.48.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-cnordt/1.48.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnordt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnordt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnordt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnordt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnordt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnordt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### diffimg

```bash
$ singularity exec <container> /usr/local/bin/diffimg
$ podman run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delaunay

```bash
$ singularity exec <container> /usr/local/bin/delaunay
$ podman run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts-config

```bash
$ singularity exec <container> /usr/local/bin/gts-config
$ podman run --it --rm --entrypoint /usr/local/bin/gts-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2dxf

```bash
$ singularity exec <container> /usr/local/bin/gts2dxf
$ podman run --it --rm --entrypoint /usr/local/bin/gts2dxf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2dxf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2oogl

```bash
$ singularity exec <container> /usr/local/bin/gts2oogl
$ podman run --it --rm --entrypoint /usr/local/bin/gts2oogl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2oogl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2stl

```bash
$ singularity exec <container> /usr/local/bin/gts2stl
$ podman run --it --rm --entrypoint /usr/local/bin/gts2stl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2stl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtscheck

```bash
$ singularity exec <container> /usr/local/bin/gtscheck
$ podman run --it --rm --entrypoint /usr/local/bin/gtscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtscompare

```bash
$ singularity exec <container> /usr/local/bin/gtscompare
$ podman run --it --rm --entrypoint /usr/local/bin/gtscompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtscompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtstemplate

```bash
$ singularity exec <container> /usr/local/bin/gtstemplate
$ podman run --it --rm --entrypoint /usr/local/bin/gtstemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtstemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stl2gts

```bash
$ singularity exec <container> /usr/local/bin/stl2gts
$ podman run --it --rm --entrypoint /usr/local/bin/stl2gts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stl2gts   -v ${PWD} -w ${PWD} <container> -c " $@"
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