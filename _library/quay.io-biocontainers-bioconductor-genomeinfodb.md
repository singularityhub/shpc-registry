---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomeinfodb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomeinfodb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomeinfodb/container.yaml"
updated_at: "2024-12-30 03:09:10.246495"
latest: "1.38.1--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-genomeinfodb"
aliases:
 - "pngcp"
 - "bmp2tiff"
 - "gif2tiff"
 - "ras2tiff"
 - "rgb2ycbcr"
 - "thumbnail"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.6.3--0"
 - "1.30.1--r41hdfd78af_0"
 - "1.28.0--r41hdfd78af_0"
 - "1.26.4--r40hdfd78af_0"
 - "1.24.0--r40_0"
 - "1.22.0--r36_0"
 - "1.34.1--r42hdfd78af_0"
 - "1.34.8--r42hdfd78af_0"
 - "1.34.9--r42hdfd78af_0"
 - "1.36.1--r43hdfd78af_0"
 - "1.38.1--r43hdfd78af_0"
 - "1.38.1--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-genomeinfodb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomeinfodb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomeinfodb", "latest": {"1.38.1--r43hdfd78af_1": "sha256:711b902761edfb784e60fc1458698e40ecd7da7662022e7c75731b2d53fa5a0b"}, "tags": {"1.6.3--0": "sha256:f91c7100a5d1768f09ce49379090b1d4eb043049e82275090074dc621fc476d2", "1.30.1--r41hdfd78af_0": "sha256:173b560b5f8730d04152db395330519788912523cbc9687a370d7de365e18d90", "1.28.0--r41hdfd78af_0": "sha256:da7973f70f0706e9a8d14fb3c758b51440b742e21a17e639f212bd46c73da3f5", "1.26.4--r40hdfd78af_0": "sha256:f874f96ccaa3c846b65bd93a8a17aa3253e7df93f6b3ea4a490fa945e5a14a76", "1.24.0--r40_0": "sha256:8f77d6ba37835fba755e6e746499d93fbd6253ea9a167accf2024a14b2388a1b", "1.22.0--r36_0": "sha256:5858e06c9f7df9583971b9e6292292db6ef633e52cc11e7809f81a060859e923", "1.34.1--r42hdfd78af_0": "sha256:38abc0379485a93cba5d9ac00a01ad96049b6c2a6d18c9493e9dcda2af3f2685", "1.34.8--r42hdfd78af_0": "sha256:771935f27f47f186d4b4d95b5b85bcbae16005217b1ca65ba73359b7749492a9", "1.34.9--r42hdfd78af_0": "sha256:c83760f6e56db9a04f3223712fe8aa67c02cf1f4373c077e6fe13fd517b3693a", "1.36.1--r43hdfd78af_0": "sha256:ff0ea747da822ed74df6a4d535c27e4019421ac5d829b8862f383227f44d294a", "1.38.1--r43hdfd78af_0": "sha256:de06fc3aac6cbebbab38ed502fd3b5838da212cc43114fe57e8c5678befd750c", "1.38.1--r43hdfd78af_1": "sha256:711b902761edfb784e60fc1458698e40ecd7da7662022e7c75731b2d53fa5a0b"}, "docker": "quay.io/biocontainers/bioconductor-genomeinfodb", "aliases": {"pngcp": "/usr/local/bin/pngcp", "bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomeinfodb.
shpc-registry automated BioContainers addition for bioconductor-genomeinfodb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomeinfodb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomeinfodb:1.38.1--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomeinfodb/1.38.1--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-genomeinfodb/1.38.1--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomeinfodb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomeinfodb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomeinfodb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomeinfodb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomeinfodb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomeinfodb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pngcp

```bash
$ singularity exec <container> /usr/local/bin/pngcp
$ podman run --it --rm --entrypoint /usr/local/bin/pngcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pngcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bmp2tiff

```bash
$ singularity exec <container> /usr/local/bin/bmp2tiff
$ podman run --it --rm --entrypoint /usr/local/bin/bmp2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmp2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2tiff

```bash
$ singularity exec <container> /usr/local/bin/gif2tiff
$ podman run --it --rm --entrypoint /usr/local/bin/gif2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ras2tiff

```bash
$ singularity exec <container> /usr/local/bin/ras2tiff
$ podman run --it --rm --entrypoint /usr/local/bin/ras2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ras2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgb2ycbcr

```bash
$ singularity exec <container> /usr/local/bin/rgb2ycbcr
$ podman run --it --rm --entrypoint /usr/local/bin/rgb2ycbcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgb2ycbcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thumbnail

```bash
$ singularity exec <container> /usr/local/bin/thumbnail
$ podman run --it --rm --entrypoint /usr/local/bin/thumbnail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thumbnail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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