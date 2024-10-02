---
layout: container
name:  "quay.io/biocontainers/bioconductor-hyperdraw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hyperdraw/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hyperdraw/container.yaml"
updated_at: "2024-10-02 02:57:52.526130"
latest: "1.54.0--r43h92b7604_1"
container_url: "https://biocontainers.pro/tools/bioconductor-hyperdraw"
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
 - "1.46.0--r41hcb05c77_1"
 - "1.50.0--r42hcb05c77_0"
 - "1.50.0--r42hba55f59_1"
 - "1.52.0--r43hba55f59_0"
 - "1.54.0--r43hba55f59_0"
 - "1.54.0--r43h92b7604_1"
description: "shpc-registry automated BioContainers addition for bioconductor-hyperdraw"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hyperdraw", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hyperdraw", "latest": {"1.54.0--r43h92b7604_1": "sha256:7f190d1321e4741748461cc9dbc3b4793132d9267a2c5fe33df6e1312912262b"}, "tags": {"1.46.0--r41hcb05c77_1": "sha256:a818c82afe8b9caa7dd679092ca377994d540831d66b96c249b607b061753c45", "1.50.0--r42hcb05c77_0": "sha256:b155cdc0a592b91a3168ec51246a1bad5b203d050d0fe5697e3a809152a6b3f1", "1.50.0--r42hba55f59_1": "sha256:be500c65487a7c46f7d58ba4212ba6e07daf7aba4ec9974e3b52dc3a2bf0c100", "1.52.0--r43hba55f59_0": "sha256:eb09d64f08e8f75dac52a7ccec55635e454bca38cf6672dd579ac95f511b5282", "1.54.0--r43hba55f59_0": "sha256:80c08594b871466f2a7e68b58d9f880601a18db4305e0b92215741393ea97622", "1.54.0--r43h92b7604_1": "sha256:7f190d1321e4741748461cc9dbc3b4793132d9267a2c5fe33df6e1312912262b"}, "docker": "quay.io/biocontainers/bioconductor-hyperdraw", "aliases": {"diffimg": "/usr/local/bin/diffimg", "delaunay": "/usr/local/bin/delaunay", "gts-config": "/usr/local/bin/gts-config", "gts2dxf": "/usr/local/bin/gts2dxf", "gts2oogl": "/usr/local/bin/gts2oogl", "gts2stl": "/usr/local/bin/gts2stl", "gtscheck": "/usr/local/bin/gtscheck", "gtscompare": "/usr/local/bin/gtscompare", "gtstemplate": "/usr/local/bin/gtstemplate", "stl2gts": "/usr/local/bin/stl2gts"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hyperdraw.
shpc-registry automated BioContainers addition for bioconductor-hyperdraw
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hyperdraw
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hyperdraw:1.54.0--r43h92b7604_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hyperdraw/1.54.0--r43h92b7604_1
$ module help quay.io/biocontainers/bioconductor-hyperdraw/1.54.0--r43h92b7604_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hyperdraw-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hyperdraw-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hyperdraw-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hyperdraw-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hyperdraw-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hyperdraw-inspect-deffile:

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