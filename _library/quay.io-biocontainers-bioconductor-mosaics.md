---
layout: container
name:  "quay.io/biocontainers/bioconductor-mosaics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mosaics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mosaics/container.yaml"
updated_at: "2025-07-28 04:15:46.368071"
latest: "2.44.0--pl5321r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-mosaics"
aliases:
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "pngcp"
 - "bmp2tiff"
 - "gif2tiff"
 - "ras2tiff"
 - "rgb2ycbcr"
 - "thumbnail"
 - "podselect"
versions:
 - "2.4.1--0"
 - "2.36.0--pl5321r42hc247a5b_0"
 - "2.32.0--pl5321r41hc247a5b_2"
 - "2.30.0--pl5320r41h399db7b_0"
 - "2.28.0--pl530r40h5f743cb_0"
 - "2.26.0--pl526r40h5f743cb_0"
 - "2.38.0--pl5321r43hf17093f_0"
 - "2.40.0--pl5321r43hf17093f_0"
 - "2.44.0--pl5321r44he5774e6_0"
 - "2.44.0--pl5321r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-mosaics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mosaics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mosaics", "latest": {"2.44.0--pl5321r44he5774e6_1": "sha256:ed23dd2e88e49e3a1f91242eee18a8a06505bac2987aaba67f81d4957cecea23"}, "tags": {"2.4.1--0": "sha256:293a404803d64aeb2f19c6cdb42180dbed1d309297f194fd173d3fc97be2109c", "2.36.0--pl5321r42hc247a5b_0": "sha256:b43d169275b96fb421720db6df4eb23b2d8a2dff2a6ecf32df27b8328792b241", "2.32.0--pl5321r41hc247a5b_2": "sha256:b5a4be957da898c81e59dc2e25fc250f0404a86184fa4140d24da985ee1b33f6", "2.30.0--pl5320r41h399db7b_0": "sha256:435d2a51195d1a8aea995dce730880fb90f25eb7ddca60090eb5e477e0601364", "2.28.0--pl530r40h5f743cb_0": "sha256:5befbbd68404051fcc782a292337f3a6efc00750f994b23e47a881ddd9d352ba", "2.26.0--pl526r40h5f743cb_0": "sha256:7f02ff017850501c9c456cffa539a7472c94898e33fcd0bd0bc66756a2a1cf4b", "2.38.0--pl5321r43hf17093f_0": "sha256:bd524a5d7103a191d70f6b71ffcd23fca5d2161e0c3ee3ce4a052c716ac143ff", "2.40.0--pl5321r43hf17093f_0": "sha256:1a3a3840ef322fc08abb3ad01db61fe3c87c6b687daa73da2384d4ee24842084", "2.44.0--pl5321r44he5774e6_0": "sha256:f745fed93e690ab491391e8045e7a5256c21b181085aeb3f9913749571aebc1f", "2.44.0--pl5321r44he5774e6_1": "sha256:ed23dd2e88e49e3a1f91242eee18a8a06505bac2987aaba67f81d4957cecea23"}, "docker": "quay.io/biocontainers/bioconductor-mosaics", "aliases": {"perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "pngcp": "/usr/local/bin/pngcp", "bmp2tiff": "/usr/local/bin/bmp2tiff", "gif2tiff": "/usr/local/bin/gif2tiff", "ras2tiff": "/usr/local/bin/ras2tiff", "rgb2ycbcr": "/usr/local/bin/rgb2ycbcr", "thumbnail": "/usr/local/bin/thumbnail", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mosaics.
shpc-registry automated BioContainers addition for bioconductor-mosaics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mosaics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mosaics:2.44.0--pl5321r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mosaics/2.44.0--pl5321r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-mosaics/2.44.0--pl5321r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mosaics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mosaics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mosaics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mosaics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mosaics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mosaics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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