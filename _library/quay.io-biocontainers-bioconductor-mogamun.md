---
layout: container
name:  "quay.io/biocontainers/bioconductor-mogamun"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mogamun/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mogamun/container.yaml"
updated_at: "2022-10-29 05:59:29.690112"
latest: "1.4.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mogamun"
aliases:
 - "Cytoscape"
 - "aserver"
 - "curve_keygen"
 - "cytoscape.sh"
 - "gen_vmoptions.sh"
 - "gif2rgb"
 - "gifbuild"
 - "gifclrmp"
 - "giffix"
 - "giftext"
versions:
 - "1.4.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mogamun"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mogamun", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mogamun", "latest": {"1.4.0--r41hdfd78af_0": "sha256:75d395718e6c06e52a16967b030e9f7c0dab7553198190950087109cc069c5eb"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:75d395718e6c06e52a16967b030e9f7c0dab7553198190950087109cc069c5eb"}, "docker": "quay.io/biocontainers/bioconductor-mogamun", "aliases": {"Cytoscape": "/usr/local/bin/Cytoscape", "aserver": "/usr/local/bin/aserver", "curve_keygen": "/usr/local/bin/curve_keygen", "cytoscape.sh": "/usr/local/bin/cytoscape.sh", "gen_vmoptions.sh": "/usr/local/bin/gen_vmoptions.sh", "gif2rgb": "/usr/local/bin/gif2rgb", "gifbuild": "/usr/local/bin/gifbuild", "gifclrmp": "/usr/local/bin/gifclrmp", "giffix": "/usr/local/bin/giffix", "giftext": "/usr/local/bin/giftext"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mogamun.
shpc-registry automated BioContainers addition for bioconductor-mogamun
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mogamun
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mogamun:1.4.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mogamun/1.4.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mogamun/1.4.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mogamun-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogamun-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogamun-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mogamun-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mogamun-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mogamun-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Cytoscape

```bash
$ singularity exec <container> /usr/local/bin/Cytoscape
$ podman run --it --rm --entrypoint /usr/local/bin/Cytoscape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Cytoscape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cytoscape.sh

```bash
$ singularity exec <container> /usr/local/bin/cytoscape.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cytoscape.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cytoscape.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gen_vmoptions.sh

```bash
$ singularity exec <container> /usr/local/bin/gen_vmoptions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gen_vmoptions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gen_vmoptions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifbuild

```bash
$ singularity exec <container> /usr/local/bin/gifbuild
$ podman run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifclrmp

```bash
$ singularity exec <container> /usr/local/bin/gifclrmp
$ podman run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffix

```bash
$ singularity exec <container> /usr/local/bin/giffix
$ podman run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftext

```bash
$ singularity exec <container> /usr/local/bin/giftext
$ podman run --it --rm --entrypoint /usr/local/bin/giftext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftext   -v ${PWD} -w ${PWD} <container> -c " $@"
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